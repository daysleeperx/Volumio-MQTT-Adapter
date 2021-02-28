#!/bin/bash

docker build --tag volumio-mqtt-docker .
docker tag volumio-mqtt-docker:latest volumio-mqtt-docker:v1.0.0
docker stop volumio_mqtt || true && docker rm volumio_mqtt || true
docker run -d --network host --name volumio_mqtt --restart unless-stopped volumio-mqtt-docker --env DEBUG=$CI_DEBUG --env VOLUMIO_HOST=$CI_VOLUMIO_HOST --env MQTT_HOST=$CI_MQTT_HOST --env DEVICE=CI_DEVICE