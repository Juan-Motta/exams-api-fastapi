#!/bin/bash
find . -type d -name '__pycache__' -exec rm -rf {} +

uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload