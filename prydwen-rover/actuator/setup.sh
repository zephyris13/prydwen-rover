#!/bin/sh
apt-get install libwebsockets-openssl mosquitto-ssl mosquitto-client-ssl
apt-get install mosquitto mosquitto-clients

pip install --upgrade setuptools

pip install paho-mqtt
pip install PyLidar2

cp etc/init.d/actuator /etc/init.d/actuator
chmod +x /etc/init.d/actuator

/etc/init.d/actuator enable
/etc/init.d/actuator restart