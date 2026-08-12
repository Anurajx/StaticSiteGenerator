#!/bin/bash

# python3 src/main.py

# python3 src/main.py  #USE THIS FOR LOCAL TESTING
# cd docs && python3 -m http.server 8888

python3 src/main.py "/StaticSiteGenerator/" #USE THIS FOR DEPLOYMENT
cd docs && python3 -m http.server 8888

#go to http://localhost:8888/ to view site