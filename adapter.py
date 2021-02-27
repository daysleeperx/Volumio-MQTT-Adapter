import secrets
from datetime import datetime

import paho.mqtt.client as mqtt
import socketio
import yaml

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile)

debug = config.get('app', 'debug')

CLIENT_ID = f'volumio-mqtt-{secrets.token_hex(16)}'
DEVICE = config.get('mqtt', 'device')
MQTT_BROKER = config.get('mqtt', 'broker')
VOLUMIO_HOST = f'{config.get("volumio", "host")}'
MQTT_TOPIC = f'{DEVICE}/#'


def connect_mqtt() -> mqtt.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            log('Connected to MQTT Broker!')
        else:
            log(f'Failed to connect, return code {rc}\n')

        client.subscribe(MQTT_TOPIC)

    mqtt_client = mqtt.Client(CLIENT_ID)
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(MQTT_BROKER)
    return mqtt_client


def subscribe(client: mqtt.Client, socket: socketio.Client):
    @socket.on('connect')
    def on_connect():
        log(f'Connected to Volumio player: {DEVICE}')

    @socket.on('disconnect')
    def disconnect():
        log(f'Connected to Volumio player: {DEVICE}')

    volume_options = {
        'percent': lambda msg: socket.emit('volume', int(msg)),
        'mute': lambda msg:
            socket.emit('volume', 'mute' if msg == 'true' else 'unmute')
    }

    playback_options = {
        'play': lambda _: socket.emit('play'),
        'stop': lambda _: socket.emit('stop'),
        'pause': lambda _: socket.emit('pause')
    }

    options = {
        'playback': lambda cmd, _:
            playback_options.get(cmd, lambda: log(f'No such cmd: {cmd}'))(_),
        'volume': lambda cmd, msg:
            volume_options.get(cmd, lambda: log(f'No such cmd: {cmd}'))(msg)
    }

    def on_message(_, userdata, msg):
        message = msg.payload.decode()
        if debug:
            log(f'Message received from MQTT topic {msg.topic}: {message}')

        (_, action, command) = msg.topic.split('/')
        options.get(action, lambda act: log(f'No such action: {act}'))(command, message)

    client.subscribe(MQTT_TOPIC)
    client.on_message = on_message


def log(message):
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'[{current_time}] {message}')


if __name__ == '__main__':
    log(f'Starting MQTT for device {DEVICE}')

    log(f'Connecting to MQTT broker {MQTT_BROKER}...')
    client = connect_mqtt()

    log(f'Connecting to Volumio Player...')
    sio = socketio.Client(logger=debug)
    sio.connect(VOLUMIO_HOST)

    subscribe(client, sio)
    client.loop_forever()

