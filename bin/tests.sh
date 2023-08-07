#!/bin/bash

# TODO: Rewrite all binaries to Makefile
# Set the PYTHONPATH to the relative path of the factory_analyzer directory
cd ..
PYTHONPATH=$(dirname "$PWD")

# Run the Python test using the relative path to the virtual environment's Python interpreter
sudo -E venv/bin/python -m pytest -v -s