"""Tests for the resume build script.

Covers environment loading, template injection, snippet reading,
project assembly, full document assembly, version config integrity,
and section order handling.

Run with::

    python3 -m pytest tests/ -v
"""

import importlib
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Import the build module (it's a file named "build" with no .py extension)
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
BUILD_PATH = ROOT / "build"

# The build script has no .py extension, so we need to use a file loader directly.
loader = importlib.machinery.SourceFileLoader("build", str(BUILD_PATH))
spec = importlib.util.spec_from_loader("build", loader)
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


# ===========================================================================
# Fixtures
# ===========================================================================


@pytest.fixture
def tmp_env(tmp_path):
    """Create a temporary .env file and return its path."""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "# Comment line\n"
        "FULL_NAME=Jane Doe\n"
        "FULL_NAME_UNDERSCORE=Jane_Doe\n"
        "\n"
        "EMAIL=jane@example.com\n"
        "PHONE=(555) 123-4567\n"
    )
    return env_file


@pytest.fixture
def sample_env():
    """Return a sample env dict for injection tests."""
    return {
        "FULL_NAME": "Jane Doe",
        "EMAIL": "jane@example.com",
        "PHONE": "(555) 123-4567",
    }


@pytest.fixture
def tmp_version(tmp_path):
    """Create a minimal version directory with a summary.tex."""
    version_dir = tmp_path / "versions" / "test"
    version_dir.mkdir(parents=True)
    (version_dir / "summary.tex").write_text("Test summary content.\n")
    return version_dir


@pytest.fixture
def tmp_sections(tmp_path, monkeypatch):
    """Create temporary section files and patch build module paths."""
    sections = tmp_path / "sections"
    sections.mkdir()
    (sections / "heading.tex").write_text("Heading: {{FULL_NAME}}\n")
    (sections / "education.tex").write_text("Education content.\n")
    (sections / "experience.tex").write_text("Experience content.\n")
    (sections / "skills.tex").write_text("Skills content.\n")

    projects = sections / "projects"
    projects.mkdir()
    (projects / "project_a.tex").write_text("        Project A content.\n")
    (projects / "project_b.tex").write_text("        Project B content.\n")

    monkeypatch.setattr(build, "SECTIONS", sections)
    return sections


# ===========================================================================
# load_env
# ===========================================================================


class TestLoadEnv:
    """Tests for the .env file parser."""

    def test_parses_key_value_pairs(self, tmp_env):
        env = build.load_env(tmp_env)
        assert env["FULL_NAME"] == "Jane Doe"
        assert env["EMAIL"] == "jane@example.com"
        assert env["PHONE"] == "(555) 123-4567"

    def test_skips_comments(self, tmp_env):
        env = build.load_env(tmp_env)
        # Comments should not produce keys
        for key in env:
            assert not key.startswith("#")

    def test_skips_blank_lines(self, tmp_env):
        env = build.load_env(tmp_env)
        assert "" not in env

    def test_missing_file_exits(self, tmp_path):
        missing = tmp_path / "nonexistent.env"
        with pytest.raises(SystemExit):
            build.load_env(missing)

    def test_empty_file(self, tmp_path):
        env_file = tmp_path / ".env"
        env_file.write_text("")
        env = build.load_env(env_file)
        assert env == {}

    def test_value_with_equals_sign(self, tmp_path):
        """Values containing = should be preserved (only split on first =)."""
        env_file = tmp_path / ".env"
        env_file.write_text("URL=https://example.com?foo=bar\n")
        env = build.load_env(env_file)
        assert env["URL"] == "https://example.com?foo=bar"


# ===========================================================================
# inject_env
# ===========================================================================


class TestInjectEnv:
    """Tests for placeholder injection."""

    def test_replaces_placeholders(self, sample_env):
        text = "Hello {{FULL_NAME}}, email: {{EMAIL}}"
        result = build.inject_env(text, sample_env)
        assert result == "Hello Jane Doe, email: jane@example.com"

    def test_no_placeholders_unchanged(self, sample_env):
        text = "No placeholders here."
        result = build.inject_env(text, sample_env)
        assert result == text

    def test_unknown_placeholder_preserved(self):
        text = "Hello {{UNKNOWN}}"
        result = build.inject_env(text, {"FULL_NAME": "Jane"})
        assert "{{UNKNOWN}}" in result

    def test_multiple_occurrences(self):
        text = "{{NAME}} and {{NAME}} again"
        result = build.inject_env(text, {"NAME": "X"})
        assert result == "X and X again"

    def test_empty_env(self):
        text = "Hello {{FULL_NAME}}"
        result = build.inject_env(text, {})
        assert result == text


# ===========================================================================
# read_section / read_project
# ===========================================================================


class TestSnippetReading:
    """Tests for reading .tex snippet files from disk."""

    def test_read_section(self, tmp_sections):
        content = build.read_section("education")
        assert "Education content." in content

    def test_read_section_missing_raises(self, tmp_sections):
        with pytest.raises(FileNotFoundError):
            build.read_section("nonexistent")

    def test_read_project(self, tmp_sections):
        content = build.read_project("project_a")
        assert "Project A content." in content

    def test_read_project_missing_raises(self, tmp_sections):
        with pytest.raises(FileNotFoundError):
            build.read_project("nonexistent")


# ===========================================================================
# assemble_projects
# ===========================================================================


class TestAssembleProjects:
    """Tests for project section assembly."""

    def test_empty_list_returns_empty(self):
        result = build.assemble_projects([])
        assert result == ""

    def test_wraps_in_section_boilerplate(self, tmp_sections):
        result = build.assemble_projects(["project_a"])
        assert "\\section{Projects}" in result
        assert "\\resumeSubHeadingListStart" in result
        assert "\\resumeSubHeadingListEnd" in result
        assert "Project A content." in result

    def test_multiple_projects_concatenated(self, tmp_sections):
        result = build.assemble_projects(["project_a", "project_b"])
        assert "Project A content." in result
        assert "Project B content." in result

    def test_project_order_preserved(self, tmp_sections):
        result = build.assemble_projects(["project_b", "project_a"])
        pos_b = result.index("Project B")
        pos_a = result.index("Project A")
        assert pos_b < pos_a


# ===========================================================================
# assemble_main
# ===========================================================================


class TestAssembleMain:
    """Tests for full document assembly."""

    def test_contains_document_structure(self, tmp_sections, tmp_version, monkeypatch):
        monkeypatch.setattr(build, "ENV", {"FULL_NAME": "Jane Doe"})
        monkeypatch.setattr(build, "SECTION_ORDER", ["heading", "summary", "skills"])
        config = {"projects": []}
        result = build.assemble_main(tmp_version, config)

        assert "\\documentclass[letterpaper,11pt]{article}" in result
        assert "\\begin{document}" in result
        assert "\\end{document}" in result
        assert "\\input{../../preamble}" in result

    def test_injects_env_values(self, tmp_sections, tmp_version, monkeypatch):
        monkeypatch.setattr(build, "ENV", {"FULL_NAME": "Jane Doe"})
        monkeypatch.setattr(build, "SECTION_ORDER", ["heading"])
        config = {"projects": []}
        result = build.assemble_main(tmp_version, config)

        assert "Jane Doe" in result
        assert "{{FULL_NAME}}" not in result

    def test_includes_summary_from_version_dir(self, tmp_sections, tmp_version, monkeypatch):
        monkeypatch.setattr(build, "ENV", {})
        monkeypatch.setattr(build, "SECTION_ORDER", ["summary"])
        config = {"projects": []}
        result = build.assemble_main(tmp_version, config)

        assert "Test summary content." in result

    def test_includes_projects_when_configured(self, tmp_sections, tmp_version, monkeypatch):
        monkeypatch.setattr(build, "ENV", {})
        monkeypatch.setattr(build, "SECTION_ORDER", ["projects"])
        config = {"projects": ["project_a"]}
        result = build.assemble_main(tmp_version, config)

        assert "Project A content." in result

    def test_omits_projects_when_empty(self, tmp_sections, tmp_version, monkeypatch):
        monkeypatch.setattr(build, "ENV", {})
        monkeypatch.setattr(build, "SECTION_ORDER", ["projects"])
        config = {"projects": []}
        result = build.assemble_main(tmp_version, config)

        assert "\\section{Projects}" not in result

    def test_section_order_respected(self, tmp_sections, tmp_version, monkeypatch):
        monkeypatch.setattr(build, "ENV", {})
        monkeypatch.setattr(build, "SECTION_ORDER", ["skills", "education"])
        config = {"projects": []}
        result = build.assemble_main(tmp_version, config)

        pos_skills = result.index("Skills content.")
        pos_edu = result.index("Education content.")
        assert pos_skills < pos_edu


# ===========================================================================
# Config integrity
# ===========================================================================


class TestConfigIntegrity:
    """Tests that the build configuration is consistent with files on disk."""

    def test_all_version_dirs_exist(self):
        for version in build.VERSIONS:
            version_dir = build.VERSIONS_DIR / version
            assert version_dir.is_dir(), f"Version directory missing: {version_dir}"

    def test_all_versions_have_summary(self):
        for version in build.VERSIONS:
            summary = build.VERSIONS_DIR / version / "summary.tex"
            assert summary.is_file(), f"Summary missing: {summary}"

    def test_all_configured_projects_exist(self):
        for version, config in build.VERSIONS.items():
            for project in config["projects"]:
                path = build.SECTIONS / "projects" / f"{project}.tex"
                assert path.is_file(), (
                    f"Project snippet '{project}' configured for "
                    f"'{version}' but file missing: {path}"
                )

    def test_all_shared_sections_exist(self):
        for section in build.SECTION_ORDER:
            if section in ("summary", "projects"):
                continue
            path = build.SECTIONS / f"{section}.tex"
            assert path.is_file(), f"Shared section missing: {path}"

    def test_versions_have_required_keys(self):
        for version, config in build.VERSIONS.items():
            assert "label" in config, f"'{version}' missing 'label' key"
            assert "projects" in config, f"'{version}' missing 'projects' key"

    def test_env_example_exists(self):
        assert (build.ROOT / ".env.example").is_file(), ".env.example missing"

    def test_preamble_exists(self):
        assert (build.SRC / "preamble.tex").is_file(), "preamble.tex missing"


# ===========================================================================
# Heading template
# ===========================================================================


class TestHeadingTemplate:
    """Tests that heading.tex uses placeholders instead of hardcoded values."""

    def test_no_hardcoded_personal_info(self):
        heading = (build.SECTIONS / "heading.tex").read_text()
        assert "{{FULL_NAME}}" in heading, "heading.tex should use {{FULL_NAME}} placeholder"
        assert "{{EMAIL}}" in heading, "heading.tex should use {{EMAIL}} placeholder"
        assert "{{PHONE}}" in heading, "heading.tex should use {{PHONE}} placeholder"
        assert "{{LOCATION}}" in heading, "heading.tex should use {{LOCATION}} placeholder"
