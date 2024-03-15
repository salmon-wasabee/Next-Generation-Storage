#!/bin/bash

# Define the URL of the GitHub repository
REPO_URL="https://github.com/salmon-wasabee/Next-Generation-Storage.git"

# Define the directory where the repository will be cloned
CLONE_DIR="$HOME/Desktop/Next-Generation-Storage"

# Check if the directory already exists
if [ ! -d "$CLONE_DIR" ]; then
    # Create the directory
    mkdir -p "$CLONE_DIR"
fi

# Use the git command to clone the repository
git clone "$REPO_URL" "$CLONE_DIR"

echo "The repository $REPO_URL was successfully cloned to $CLONE_DIR."

