#!/usr/bin/env python3
"""
Safety Report Analyzer - Web Server Starter
Starts the Flask web application for local development
"""

import os
import sys
from pathlib import Path

def check_venv():
    """Check if virtual environment exists and activate it"""
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("❌ Virtual environment not found!")
        print("Please run setup.py first: python setup.py")
        return False
    
    # Add venv to Python path
    if sys.platform == "win32":
        venv_lib = venv_path / "Lib" / "site-packages"
    else:
        venv_lib = venv_path / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    
    if venv_lib.exists():
        sys.path.insert(0, str(venv_lib))
    
    return True

def check_config():
    """Check if config.py exists and has API key"""
    config_path = Path("config.py")
    if not config_path.exists():
        print("❌ config.py not found!")
        print("Please copy config.example.py to config.py and add your API key")
        return False
    
    try:
        with open(config_path, 'r') as f:
            content = f.read()
            if "your-openai-api-key-here" in content:
                print("⚠️  Please update config.py with your actual OpenAI API key")
                return False
    except Exception as e:
        print(f"❌ Error reading config.py: {e}")
        return False
    
    return True

def main():
    """Start the web application"""
    print("🌐 Starting Safety Report Analyzer Web Server...")
    print("=" * 50)
    
    # Check virtual environment
    if not check_venv():
        sys.exit(1)
    
    # Check configuration
    if not check_config():
        sys.exit(1)
    
    # Import and run Flask app
    try:
        from app import app
        print("✅ Flask app loaded successfully")
        print("🚀 Starting web server...")
        print("📱 Open your browser and go to: http://localhost:5000")
        print("⏹️  Press Ctrl+C to stop the server")
        print("=" * 50)
        
        app.run(host='0.0.0.0', port=5000, debug=True)
        
    except ImportError as e:
        print(f"❌ Failed to import Flask app: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting web server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
