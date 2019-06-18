#!/bin/sh

## script to install mosquitto mqtt and configure a websocket

opkg update
opkg install libwebsockets-openssl mosquitto-ssl mosquitto-client-ssl


echo "
bind_address 0.0.0.0
port 1883
protocol mqtt

listener 9001
protocol websockets

log_type information
log_type websockets
websockets_log_level 0

" > /etc/mosquitto/mosquitto.conf


/etc/init.d/mosquitto enable
/etc/init.d/mosquitto restart
