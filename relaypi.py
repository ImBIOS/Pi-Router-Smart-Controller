# Ensure postive leads are hooked up to NO and C terminals
import sys
import os
import RPi.GPIO as GPIO
from time import sleep

ip_address = "192.168.102.1"
channel = 21
relay_mode = 1
restart_ops = 0

GPIO.setmode(GPIO.BCM) # GPIO setup
GPIO.setup(channel, GPIO.OUT)

def relay_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn relay on
    relay_mode = 1

def relay_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn relay off
    relay_mode = 0


while True: #Loop in here forever
 
    response = os.system ("ping -c 1 " + ip_address) #Ping the define IP address
 
    if response == 0: #Healthy repsonse is 0
        print ip_address, 'is up'
        if relay_mode == 0:
            relay_on(channel)
 
    else:
        print ip_address, 'is down'
        if restart_ops <= 5:
            print "restart executed"
            relay_off(channel)
            sleep(30)
            relay_on(channel)
            restart_ops += 1
            print "done restarting for" + restart_ops + "times"
 
    GPIO.cleanup()
    sleep(5) #Wait a time period then do again

