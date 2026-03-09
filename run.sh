#!/usr/bin/env bash
set -e

# ---------------------------------------------------------------------------
# run.sh — start Chocolate locally (venv) or with Docker
# ---------------------------------------------------------------------------

# Check for .env and copy from .env.example if missing
if [[ ! -f .env ]]; then
  if [[ ! -f .env.example ]]; then
    echo "ERROR: .env.example not found. Cannot create .env."
    exit 1
  fi
  cp .env.example .env
  echo ""
  echo "  .env file was not found."
  echo "  A new .env has been created from .env.example."
  echo ""
  echo "  Please open .env and fill in your values before running again:"
  echo "    DISCORD_TOKEN   — your Discord bot token"
  echo "    API_UID         — your 42 Intra app UID"
  echo "    API_SECRET      — your 42 Intra app secret"
  echo ""
  exit 0
fi

# Ask the user how to run
echo ""
echo "How do you want to run Chocolate?"
echo "  1) Local (venv)"
echo "  2) Docker"
echo ""
read -rp "Enter 1 or 2: " choice

case "$choice" in
  1)
    if ! command -v uv &>/dev/null; then
      echo "ERROR: uv is not installed. Install it from https://docs.astral.sh/uv/"
      exit 1
    fi
    echo ""
    echo "Installing dependencies..."
    uv sync
    echo "Starting Chocolate locally..."
    uv run python -m chocolate
    ;;
  2)
    if ! command -v docker &>/dev/null; then
      echo "ERROR: docker is not installed or not in PATH."
      exit 1
    fi
    echo ""
    echo "Starting Chocolate with Docker..."
    docker compose up --build
    ;;
  *)
    echo "Invalid choice. Please enter 1 or 2."
    exit 1
    ;;
esac
