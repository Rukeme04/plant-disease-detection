#!/usr/bin/env python3
"""
Setup script for Plant Disease Detection System deployment
This script helps prepare your project for deployment to Streamlit Cloud
"""

import os
import subprocess
import sys

def check_git_installed():
    """Check if Git is installed"""
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        print("✅ Git is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed. Please install Git first.")
        return False

def check_git_lfs_installed():
    """Check if Git LFS is installed"""
    try:
        subprocess.run(['git', 'lfs', 'version'], check=True, capture_output=True)
        print("✅ Git LFS is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git LFS is not installed. Please install Git LFS for large model files.")
        return False

def check_files_exist():
    """Check if required files exist"""
    required_files = ['main.py', 'requirements.txt', 'README.md', '.gitignore']
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_model_files():
    """Check if model files exist"""
    model_files = ['trained_model.h5', 'trained_model.keras']
    existing_models = []
    
    for file in model_files:
        if os.path.exists(file):
            size_mb = os.path.getsize(file) / (1024 * 1024)
            print(f"✅ {file} exists ({size_mb:.1f} MB)")
            existing_models.append(file)
        else:
            print(f"❌ {file} is missing")
    
    return existing_models

def initialize_git_repo():
    """Initialize Git repository if not already done"""
    if not os.path.exists('.git'):
        print("📁 Initializing Git repository...")
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
    else:
        print("✅ Git repository already exists")

def setup_git_lfs():
    """Setup Git LFS for large model files"""
    if check_git_lfs_installed():
        print("🔧 Setting up Git LFS...")
        subprocess.run(['git', 'lfs', 'install'], check=True)
        subprocess.run(['git', 'lfs', 'track', '*.h5'], check=True)
        subprocess.run(['git', 'lfs', 'track', '*.keras'], check=True)
        print("✅ Git LFS configured")

def create_initial_commit():
    """Create initial commit"""
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit: Plant Disease Detection System'], check=True)
        print("✅ Initial commit created")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create initial commit")
        return False

def main():
    """Main setup function"""
    print("🚀 Plant Disease Detection System - Deployment Setup")
    print("=" * 50)
    
    # Check prerequisites
    print("\n📋 Checking prerequisites...")
    if not check_git_installed():
        print("\nPlease install Git first:")
        print("- Windows: https://git-scm.com/download/win")
        print("- macOS: brew install git")
        print("- Linux: sudo apt-get install git")
        return
    
    check_git_lfs_installed()
    
    # Check project files
    print("\n📁 Checking project files...")
    if not check_files_exist():
        print("\n❌ Some required files are missing. Please ensure all files are present.")
        return
    
    # Check model files
    print("\n🤖 Checking model files...")
    model_files = check_model_files()
    if not model_files:
        print("\n❌ No model files found. Please ensure trained_model.h5 or trained_model.keras exists.")
        return
    
    # Setup Git
    print("\n🔧 Setting up Git...")
    initialize_git_repo()
    setup_git_lfs()
    
    # Create initial commit
    print("\n💾 Creating initial commit...")
    if create_initial_commit():
        print("\n✅ Setup completed successfully!")
        print("\n📝 Next steps:")
        print("1. Create a GitHub repository at https://github.com/new")
        print("2. Make it PUBLIC (required for free Streamlit Cloud)")
        print("3. Run these commands:")
        print("   git remote add origin https://github.com/YOUR_USERNAME/plant-disease-detection.git")
        print("   git branch -M main")
        print("   git push -u origin main")
        print("4. Deploy to Streamlit Cloud at https://share.streamlit.io")
    else:
        print("\n❌ Setup failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 