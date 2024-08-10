#!/bin/bash

# Activate virtual environment if exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Run the Python script
python main.py