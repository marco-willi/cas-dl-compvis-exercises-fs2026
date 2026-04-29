#!/bin/bash
# Post-start command: Runs every time the container starts

set -e

echo "Running post-start tasks..."

# Ensure Poetry is on PATH (installed during post-create)
export PATH="$HOME/.local/bin:$PATH"

# Re-create .venv symlink if missing (survives container rebuilds)
VENV_REAL=$(poetry env info --path 2>/dev/null || true)
if [ -n "$VENV_REAL" ] && [ ! -L /workspace/.venv ]; then
    rm -rf /workspace/.venv
    ln -s "$VENV_REAL" /workspace/.venv
    echo "Re-linked .venv -> $VENV_REAL"
fi


# Install CLI tools
bash "$(dirname "$0")/cli-tools.sh"

echo ""
echo "Python : $(which python3) ($(python3 --version 2>&1))"
echo "Poetry : $(poetry --version)"
echo "Venv   : /workspace/.venv -> $(readlink -f /workspace/.venv 2>/dev/null || echo 'not linked')"

echo ""
echo "Container ready!"
