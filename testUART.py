#!/usr/bin/env python

# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial,time


if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyS0", 115200, timeout=1) as stm32:
        time.sleep(2) #wait for serial to open
        if stm32.isOpen():
            print("{} connected!".format(stm32.port))
            stm32.write("W".encode('utf-8'))
           
