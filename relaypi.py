# Ensure postive leads are hooked up to NO and C terminals
import sys
import os
import RPi.GPIO as GPIO
from time import sleep

main_router = "192.168.102.1"
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
 
    response = os.system ("ping -c 1 " + main_router) #Ping the define IP address
 
    if response == 0: #Healthy repsonse is 0
        print main_router, 'is up'
        if relay_mode == 0:
            relay_on(channel)
 
    else:
        print main_router, 'is down'
        if restart_ops <= 5:
            print "restart executed"
            relay_off(channel)
            sleep(30)
            relay_on(channel)
            restart_ops += 1
            print "done restarting for", restart_ops, "times"
        else:
            print "Restart Ops is executed and not solving anything"
 
    GPIO.cleanup()
    sleep(5) #Wait a 5 second then do again

