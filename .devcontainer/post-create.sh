#!/bin/bash
# Post-create command: Runs once after container is created

set -e

echo "Running post-create setup..."

# Install Claude Code CLI
curl -fsSL https://claude.ai/install.sh | bash

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"

# Ensure we're in the workspace
cd /workspace

# Place venv in the repository for simplicity
poetry config virtualenvs.in-project true

# Pin Poetry to the conda Python from the pytorch base image
poetry env use "$(which python3)"

poetry install --with dev

# Venv is now in-project as .venv
VENV_REAL="/workspace/.venv"
VENV_ACTIVATE=$VENV_REAL/bin/activate

# Persist ~/.local/bin on PATH and auto-activate the venv in every new terminal session
for RC in "$HOME/.bashrc" "$HOME/.zshrc"; do
    if [ -f "$RC" ]; then
        if ! grep -q 'HOME/.local/bin' "$RC"; then
            {
                echo ""
                echo "# Add user-local binaries (Poetry, CLI tools) to PATH"
                echo 'export PATH="$HOME/.local/bin:$PATH"'
            } >> "$RC"
        fi
        if ! grep -q "source $VENV_ACTIVATE" "$RC"; then
            {
                echo ""
                echo "# Auto-activate Poetry venv"
                echo "[ -f $VENV_ACTIVATE ] && source $VENV_ACTIVATE"
            } >> "$RC"
        fi
    fi
done

# Install pre-commit hooks if .pre-commit-config.yaml exists
if [ -f ".pre-commit-config.yaml" ]; then
    echo ""
    echo "Installing pre-commit hooks..."
    poetry run pre-commit install || echo "Warning: Failed to install pre-commit hooks (continuing anyway)"
fi

# Install developer tools from GitHub releases (best-effort — failures are non-fatal)
LOCAL_BIN="$HOME/.local/bin"
mkdir -p "$LOCAL_BIN"


echo ""
echo "Post-create setup complete!"
echo "Venv   : /workspace/.venv -> $VENV_REAL"
echo "Python : $($VENV_REAL/bin/python --version)"
