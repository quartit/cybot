#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    time.sleep(0.1) #wait for serial to open
    if arduino.isOpen():
        print("{} connected!".format(arduino.port))
    ser.reset_input_buffer()
    ser.write("x30\n".encode('utf-8'))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
     
