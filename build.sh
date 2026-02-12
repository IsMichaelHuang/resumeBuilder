#!/bin/bash

# Available resume versions and where they live
VERSIONS="ai-ml fullstack backend general-swe"
VERSIONS_DIR="versions"
NAME="Michael_Huang"

# Map version name to a display-friendly suffix for the renamed PDF
version_label() {
    case "$1" in
        ai-ml)       echo "AI_ML" ;;
        fullstack)   echo "Full_Stack" ;;
        backend)     echo "Backend" ;;
        general-swe) echo "General_SWE" ;;
        monster)     echo "Monster" ;;
        *)           echo "$1" ;;
    esac
}

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

# Copy a built PDF to a destination with a descriptive filename
# Usage: rename_version <version> [destination_dir]
rename_version() {
    local version="$1"
    local dest="${2:-$HOME/Desktop}"
    local label
    label=$(version_label "$version")

    # Determine source PDF path
    local src
    if [ "$version" = "monster" ]; then
        src="monster/main.pdf"
    else
        src="$VERSIONS_DIR/$version/main.pdf"
    fi

    if [ ! -f "$src" ]; then
        echo "Error: $src not found. Build it first with: ./build.sh $version"
        return 1
    fi

    # Create destination directory if it doesn't exist
    mkdir -p "$dest"

    local filename="${NAME}_Resume_${label}.pdf"
    cp "$src" "$dest/$filename"
    echo "Copied: $dest/$filename"
}

# --- Main script ---

# Show usage if no argument provided
if [ -z "$1" ]; then
    echo "Usage: ./build.sh <version|all|monster|rename>"
    echo "       ./build.sh rename <version|all> [destination]"
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
elif [ "$1" = "rename" ]; then
    # Rename/copy PDFs: ./build.sh rename <version|all> [destination]
    if [ -z "$2" ]; then
        echo "Usage: ./build.sh rename <version|all> [destination]"
        echo "Versions: $VERSIONS monster"
        echo "Default destination: ~/Desktop"
        exit 1
    fi
    if [ "$2" = "all" ]; then
        for v in $VERSIONS; do
            rename_version "$v" "$3"
        done
    else
        rename_version "$2" "$3"
    fi
else
    # Build a specific version (e.g. ./build.sh ai-ml)
    build_version "$1"
fi
