#!/usr/bin/env python3
"""
Safety Report Analyzer - Setup Script
Cross-platform installation and setup script
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python():
    """Check if Python is available and has the right version"""
    if sys.version_info < (3, 8):
        print("❌ ERROR: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def create_venv():
    """Create virtual environment"""
    venv_path = Path(".venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    print("📦 Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("✅ Virtual environment created")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        return False

def get_activate_script():
    """Get the correct activation script for the platform"""
    if platform.system() == "Windows":
        return ".venv\\Scripts\\activate.bat"
    else:
        return ".venv/bin/activate"

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    
    # Get the correct pip executable
    if platform.system() == "Windows":
        pip_exe = ".venv\\Scripts\\pip.exe"
        python_exe = ".venv\\Scripts\\python.exe"
    else:
        pip_exe = ".venv/bin/pip"
        python_exe = ".venv/bin/python"
    
    try:
        # Upgrade pip first
        subprocess.run([python_exe, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        
        # Install requirements
        subprocess.run([pip_exe, "install", "-r", "requirements.txt"], check=True)
        
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def create_config():
    """Create config.py from template if it doesn't exist"""
    config_path = Path("config.py")
    example_path = Path("config.example.py")
    
    if config_path.exists():
        print("✅ config.py already exists")
        return True
    
    if example_path.exists():
        print("📝 Creating config.py from template...")
        try:
            with open(example_path, 'r') as src, open(config_path, 'w') as dst:
                dst.write(src.read())
            print("✅ config.py created - please add your OpenAI API key")
            return True
        except Exception as e:
            print(f"❌ Failed to create config.py: {e}")
            return False
    else:
        print("⚠️  config.example.py not found - please create config.py manually")
        return False

def main():
    """Main setup function"""
    print("🛡️ Safety Report Analyzer Setup")
    print("=" * 40)
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Create virtual environment
    if not create_venv():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Create config
    create_config()
    
    print("\n" + "=" * 40)
    print("🎉 Setup completed successfully!")
    print("\nNext steps:")
    print("1. Edit config.py and add your OpenAI API key")
    print("2. Run the application:")
    
    if platform.system() == "Windows":
        print("   - Double-click run.bat, or")
        print("   - Run: .venv\\Scripts\\python.exe gui.py")
    else:
        print("   - Run: source .venv/bin/activate && python gui.py")
    
    print("\nFor web deployment:")
    print("   - Run: python app.py")

if __name__ == "__main__":
    main()
