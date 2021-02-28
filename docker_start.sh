#!/bin/bash

docker build --tag volumio-mqtt-docker .
docker tag volumio-mqtt-docker:latest volumio-mqtt-docker:v1.0.0
# shellcheck disable=SC2086
docker run -d --network host --name volumio_mqtt --restart unless-stopped volumio-mqtt-docker --rm -e DEBUG=$CI_DEBUG -e VOLUMIO_HOST=$CI_VOLUMIO_HOST -e MQTT_HOST=$CI_MQTT_HOST -e DEVICE=CI_DEVICE