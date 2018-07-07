# Paragon Control Software

#Imports

#import serial
import serial

#import time&sleep
from time import sleep

#import OS
import os

#specify serial port
print('Chose a serial port')

#list serial ports
os.system('ls /dev/tty*')

#input saved here
serVar = input()

#Open Serial Port
with serial.Serial() as ser:
   # ser.port = 'serVar'
    ser.baudrate = 1200
    ser.bytesize = EIGHTBITS
    ser.parity = PARITY_NONE
    ser.stopbits = STOPBITS_ONE
    ser.timeout = None
    ser.rtscts = False
    ser.dsrdtr = False
    ser.write_timeout = 2
    ser.inter_byte_timeout = None
    ser.exclusive = True
    ser.port = 'serVar'
    open()
    
while True:
    data = ser.read(9999)
    if len(data) > 0:
        print('Paragon active', data)

    sleep(1)
    print ('Ready')

#clear screen before logo
os.system('clear')

# logo

print("TEN-TEC Paragon Serial Interface Control Program")
print("Copyright 1988")
print("By")
print("TEN-TEC, Inc.")
print("Ported to Python")
print("By")
print("KK4VFU")
print("Python 3 Version") #add date when finished
sleep(10)

#clear sceen before main menu

os.system('clear')

#Main Menu



