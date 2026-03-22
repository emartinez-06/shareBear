#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run collectstatic
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear
