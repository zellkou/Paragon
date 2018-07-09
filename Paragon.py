# Paragon Control Software

#Imports

#import serial
import serial

#import
from time import sleep
import os
import mainMenu

#list serial ports
os.system('ls /dev/tty*S*')

print('Choose Serial Port')

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

#call mainmenu MaLo
sleep(10)

#clear sceen before main menu
os.system('clear')

#call mainmenu Main
MaiRou()
