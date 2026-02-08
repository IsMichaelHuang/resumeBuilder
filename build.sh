#!/bin/bash

# Available resume versions and where they live
VERSIONS="ai-ml fullstack backend general-swe"
VERSIONS_DIR="versions"

# Build a single tailored resume version
# Takes the version name (e.g. "ai-ml") as an argument
build_version() {
    local version="$1"
    local dir="$VERSIONS_DIR/$version"

    # Check that the version directory exists
    if [ ! -d "$dir" ]; then
        echo "Error: version '$version' not found at $dir"
        return 1
    fi

    echo "Building $version..."

    # cd into the version directory so relative paths (../../preamble.tex) resolve correctly
    # Run in a subshell (...) so the cd doesn't affect the rest of the script
    # -interaction=nonstopmode: don't pause on errors, just keep going
    # > /dev/null 2>&1: suppress the verbose LaTeX output
    (cd "$dir" && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1)

    # Check if pdflatex succeeded (exit code 0 = success)
    if [ $? -eq 0 ]; then
        echo "  Done: $dir/main.pdf"
    else
        echo "  Failed. Run manually for details: cd $dir && pdflatex main.tex"
        return 1
    fi
}

# Build the monster (multi-page master) resume
build_monster() {
    echo "Building monster..."

    # cd into monster dir so relative paths (../preamble.tex, ../sections/) resolve correctly
    (cd "monster" && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1)

    if [ $? -eq 0 ]; then
        echo "  Done: monster/main.pdf"
    else
        echo "  Failed. Run manually for details: cd monster && pdflatex main.tex"
        return 1
    fi
}

# --- Main script ---

# Show usage if no argument provided
if [ -z "$1" ]; then
    echo "Usage: ./build.sh <version|all|monster>"
    echo "Versions: $VERSIONS"
    exit 1
fi

# Route to the right build function based on the argument
if [ "$1" = "all" ]; then
    # Build every tailored version
    for v in $VERSIONS; do
        build_version "$v"
    done
elif [ "$1" = "monster" ]; then
    # Build the master document
    build_monster
else
    # Build a specific version (e.g. ./build.sh ai-ml)
    build_version "$1"
fi
