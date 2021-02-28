#!/bin/bash

docker build --tag volumio-mqtt-docker:latest --tag volumio-mqtt-docker:v1.0.0 .
docker stop volumio_mqtt || true && docker rm volumio_mqtt || true
docker run -d --network host --name volumio_mqtt --restart unless-stopped volumio-mqtt-docker