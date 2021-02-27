#!/bin/bash

docker build --tag volumio-mqtt-docker .
docker tag volumio-mqtt-docker:latest volumio-mqtt-docker:v1.0.0
docker run -d --network host --restart unless-stopped volumio-mqtt-docker