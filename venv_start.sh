#!/bin/bash

sudo pip3 install virtualenv
python3 -m venv volumio-mqtt-env
source volumio-mqtt-env/bin/activate
pip3 install -r requirements.txt
python3 adapter.py