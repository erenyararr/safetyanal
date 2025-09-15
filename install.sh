#!/bin/bash
# Safety Report Analyzer - Installation Script for Linux/Mac

echo "Installing Safety Report Analyzer..."
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 from https://python.org"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create virtual environment"
    exit 1
fi

# Activate virtual environment and install dependencies
echo "Installing dependencies..."
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo
echo "✅ Installation completed successfully!"
echo
echo "Next steps:"
echo "1. Copy config.example.py to config.py"
echo "2. Edit config.py and add your OpenAI API key"
echo "3. Run: python gui.py"
echo
