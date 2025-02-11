#!/bin/bash

echo "Setting up development environment..."

# Install system dependencies
echo "Installing system dependencies..."
sudo apt update && sudo apt install -y \
    build-essential \
    libssl-dev \
    libreadline-dev \
    libsqlite3-dev \
    libbz2-dev \
    libncursesw5-dev \
    libgdbm-dev \
    liblzma-dev \
    zlib1g-dev \
    libffi-dev \
    curl \
    wget \
    dotnet-sdk-7.0 \
    libxkbcommon-x11-0 libxcb-cursor0 libegl1-mesa libgl1-mesa-glx \
    x11-utils x11-xserver-utils x11-apps

# Download and install Python 3.12.8
PYTHON_VERSION=3.12.8
PYTHON_SRC="Python-$PYTHON_VERSION"
PYTHON_TAR="$PYTHON_SRC.tgz"

echo "Downloading Python $PYTHON_VERSION..."
wget "https://www.python.org/ftp/python/$PYTHON_VERSION/$PYTHON_TAR"

echo "Extracting Python source..."
tar -xvf $PYTHON_TAR
cd $PYTHON_SRC

echo "Building Python from source..."
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall

# Go back to the project root
cd ..
rm -rf $PYTHON_SRC $PYTHON_TAR

# Verify Python installation
PYTHON_INSTALLED_VERSION=$(python3.12 --version 2>/dev/null)
if [[ $PYTHON_INSTALLED_VERSION == "Python 3.12.8" ]]; then
    echo "Python 3.12.8 successfully installed!"
else
    echo "Error: Python 3.12.8 installation failed."
    exit 1
fi

# Set Python 3.12 as the default
echo "Setting Python 3.12.8 as default..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.12 1
sudo update-alternatives --config python3

# Set up Python virtual environment
echo "Creating Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r ../resource/requirements.txt

# Check if .NET is installed
if ! command -v dotnet &> /dev/null; then
    echo "Error: .NET SDK not found. Please install .NET manually."
    exit 1
fi

# Set environment variables
echo "Setting environment variables..."
export QT_QPA_PLATFORM=xcb
export DISPLAY=:0

echo "Development environment setup complete!"
echo "To activate the Python virtual environment, run: source .venv/bin/activate"

