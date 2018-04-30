#!/bin/bash
set -e
pip install -r /project/requirements.txt
cd /project && gunicorn -b 0.0.0.0:8000 api:app
