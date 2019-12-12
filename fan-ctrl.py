#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

# Configuration
PWM_PIN = 16            # BCM pin used to drive transistor
WAIT_TIME = 3           # [s] Time to wait between each refresh
PWM_FREQ = 25           # [Hz] 

# Configurable temperature and fan duty cycle limits
bottomTemp = 60   # [°C] below this temperature, fan does not run
topTemp = 75      # [°C] above this temperature, fan runs max speed 
bottomDC = 50     # [%] minimum safe duty cycle to run fan
topDC = 100       # [%] maximum duty cycle to run fan

# Fan speed will change only of the difference of temperature is higher than hysteresis
hyst = 1

# Setup GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT, initial=GPIO.LOW)
fan=GPIO.PWM(PWM_PIN,PWM_FREQ)
fan.start(0);

#initialize the working variables
cpuTempOld=0
DC=0

try:
    while (1):
        # Read CPU temperature
        cpuTempFile=open("/sys/class/thermal/thermal_zone0/temp","r")
        cpuTemp=float(cpuTempFile.read())/1000
        cpuTempFile.close()

        # Calculate desired fan speed
        if(abs(cpuTemp-cpuTempOld) > hyst):
            
            # Below bottomTemp fan does not run
            if(cpuTemp <= bottomTemp):
              DC = 0

           # Above topTemp, fan runs at max speed
            elif(cpuTemp >= topTemp):
              DC = topDC

            # Between topTemp and bottomTemp, use linear interpolation
            else:       
              DC = (cpuTemp-bottomTemp)/(topTemp-bottomTemp) * (topDC - bottomDC) + bottomDC
 
            fan.ChangeDutyCycle(DC)
            cpuTempOld = cpuTemp

        # Wait until next refresh
        time.sleep(WAIT_TIME)


# If a keyboard interrupt occurs (ctrl + c), the GPIO is set to 0 and the program exits.
except(KeyboardInterrupt):
    print("Fan ctrl interrupted by keyboard")
    GPIO.cleanup()
    sys.exit()


