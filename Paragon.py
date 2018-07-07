# Paragon Control Software

#Imports

#import serial
import serial

#import
from time import sleep
import os

#list serial ports
os.system('ls /dev/tty*S*')

#input saved here
serVar = input()

#Open Serial Port
ser = serial.Serial(
    port=serVar,
    baudrate=1200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=30, #need to find correct time for this
    rtscts=False,
    dsrdtr=False,
    write_timeout=2,
    inter_byte_timeout=None,
    exclusive=True
)

while True:
    data = ser.read(9999)
    if len(data) > 0:
        print('Paragon active', data)
        sleep(1)
        print('Ready')
    else:
        print('No connection, check cable. Exiting')
        raise SystemExit

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



