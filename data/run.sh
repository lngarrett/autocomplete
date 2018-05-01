#!/bin/bash
set -e
pip install -r /project/requirements.txt
cd /project && python loader.py
