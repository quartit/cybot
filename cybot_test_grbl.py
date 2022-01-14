#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()
    ser.write(b"x20\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
     
