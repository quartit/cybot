#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
        port='/dev/ttyAMA0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

while 1:
        #ser.write("Write counter: %d \n"%(counter))
        ser.write("W")
        time.sleep(1)
        counter += 1
           
