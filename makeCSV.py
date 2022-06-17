#!/usr/bin/python
# coding:utf-8

from datetime import datetime
import re
import serial

## Serial setting
portN = "COM3"
bps = 9600
timeOut = 5

dataFileName = "output.csv"
ser = serial.Serial(portN, bps, timeout=timeOut)

print(ser.name)
print("[+] Write to %s" %(dataFileName))

while True:
    try:
        str_data = ser.readline().strip().decode()
        print(str_data)
        with open(dataFileName, 'a') as f:
            f.writelines(str_data)
            f.writelines('\n')
        f.close()
    except Exception as e:
        print("[-] Error: ", e)