#!/bin/bash
set -e
flake8 . --exclude=migrations,apps.py,settings,init.py,.venv --ignore=E501,E722
