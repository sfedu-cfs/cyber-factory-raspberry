#!/bin/bash

# Set the PYTHONPATH to the relative path of the factory_analyzer directory
cd ..
PYTHONPATH=$(dirname "$PWD")

# Get the path to the test file from the command-line argument
test_file_path="tests/$1"

# Run the Python test using the relative path to the virtual environment's Python interpreter
sudo -E venv/bin/python -m pytest -v -s "$test_file_path"
