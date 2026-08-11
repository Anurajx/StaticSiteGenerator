#!/bin/bash

# python3 src/main.py

# python3 src/main.py
# cd public && python3 -m http.server 8888

python3 src/main.py "/StaticSiteGenerator/"
cd docs && python3 -m http.server 8888

#go to http://localhost:8888/ to view site