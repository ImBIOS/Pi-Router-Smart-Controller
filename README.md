# Pi Router Smart Controller
## By Imamuzzaki Abu Salam

relaypi.py is the main python file.
README.md is this file you reading on.
launcher.sh is the shell script to run this command.
logs folder is folder to store error logs.

I use this tutorial to run this script in startup:
https://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/

sudo crontab -e
Now, enter the line:
@reboot sh /home/pi/bbt/launcher.sh >/home/pi/logs/cronlog 2>&1
