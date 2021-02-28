#!/bin/bash

docker build --tag volumio-mqtt-docker .
docker tag volumio-mqtt-docker:latest volumio-mqtt-docker:v1.0.0
docker stop volumio_mqtt || true && docker rm volumio_mqtt || true
docker run -d --network host --name volumio_mqtt --restart unless-stopped volumio-mqtt-docker -e DEBUG=$CI_DEBUG -e VOLUMIO_HOST=$CI_VOLUMIO_HOST -e MQTT_HOST=$CI_MQTT_HOST -e DEVICE=CI_DEVICE