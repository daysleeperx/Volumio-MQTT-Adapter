# Volumio MQTT Adapter :headphones:
Volumio MQTT adapter written in Python.

Enables Volumio player control using MQTT messages. Example message, that plays a specific playlist 
```bash
mosquitto_pub -d -t volumio/playback/playPlaylist -m "My Playlist"
```
## Configuration
Settings can be configured in `config.ini` file.  
Example configuration can be found in `config.ini.sample`.

## Installation
Start with docker
```bash
chmod +x docker_start.sh
./docker_start.sh
```

Alternatively, start with `venv`
```bash
chmod +x venv_start.sh
./venv_start.sh
```
## Topics

| Topic | Payload |
|-------|---------|
|`{device}/playback/play` | |
|`{device}/playback/stop` | |
|`{device}/playback/pause` | |
|`{device}/playback/playPlaylist`| [playlist_name]|
|`{device}/playback/power`| [true or false]|
|`{device}/volume/percent`| [0-100]|
|`{device}/volume/push`| [+ or -]|
|`{device}/volume/up`| |
|`{device}/volume/down`| |
|`{device}/volume/mute`| [true or false]|
|`{device}/state/getState`| |
|`{device}/state/pushState`| [state]|


