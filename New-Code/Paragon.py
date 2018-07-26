# Paragon Control Software

#Imports

#import serial
import serial

#import
from time import sleep
import os
import mainMenu
import routines

#list serial ports
#os.system('ls /dev/tty*S*') #remove this line if the next line works
serial.tools.list_ports() # if this works it will make it system agnostic


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
    data0 = ser.read(30)
    if len(data0) = 30:
        data1 =  bytes.fromhex(data0).decode('utf-8')
        print('Paragon active', data1)
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
