#!/bin/bash

echo "Checking environment..."

if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    sudo apt update && sudo apt install -y python3
fi

if ! command -v pip3 &> /dev/null; then
    echo "Installing pip3..."
    sudo apt install -y python3-pip
fi

echo "Installing requirements from requirements.txt..."
pip3 install -r requirements.txt --break-system-packages

echo "Starting Deepnut..."
python3 main.py
