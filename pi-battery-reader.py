#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
*** RED REACTOR - Copyright (c) 2022
*** Author: Pascal Herczog

*** This code is designed for the RED REACTOR Raspberry Pi Battery Power Supply
*** Example code provided without warranty
*** Provides Voltage and Current readings to Battery Icon

*** Filename: pi-battery-reader.py
*** PythonVn: 3.8, 32-bit
*** Date: January 2022
"""
import os


def trim(data):
      data=data[11:-1]
      return(float(data))
try:
	# Include busnum=1 for Bullseye
    voltage=trim(os.popen('echo "get battery_v" | sudo nc -U -W 1 /tmp/pisugar-server.sock').read())
    current=trim(os.popen('echo "get battery_i" | sudo nc -U -W 1 /tmp/pisugar-server.sock').read())

except RuntimeError as e:
	#  to access I2C bus but there is power
	voltage = 0.0
	current = 0.0

finally:
    # Read by sscanf(buffer, "%f|%f",&vv, &current);
    print("{:.3f}|{:.2f}".format(voltage, current))
