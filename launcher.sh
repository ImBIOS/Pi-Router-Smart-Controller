#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/Desktop/Pi-Router-Smart-Controller/
sudo python relaypi.py
cd /

# make it executable with:
# chmod 755 launcher.sh
# sh launcher.sh