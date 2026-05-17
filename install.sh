#!/bin/bash
set -e

echo "📦 Creating an isolated environment..."
python3 -m venv .venv

echo "📥 Installing dependencies safely..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

echo "🚀 Setting up executable paths..."
chmod +x bin/explain
chmod +x src/main.py

REPO_PATH=$(pwd)

echo "🔒 Creating global command (requires sudo)..."
sudo ln -sf "$REPO_PATH/bin/explain" /usr/local/bin/explain

echo "✅ Setup complete! Run: explain <command>"
