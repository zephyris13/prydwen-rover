#!/bin/sh

opkg update
opkg install python-light pyPwmExp
opkg install python-pip pyRelayExp
pip install --upgrade setuptools

pip install paho-mqtt

cp etc/init.d/actuator /etc/init.d/actuator
chmod +x /etc/init.d/actuator

/etc/init.d/actuator enable
/etc/init.d/actuator restart