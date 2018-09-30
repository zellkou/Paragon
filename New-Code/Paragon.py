# Paragon Control Software

#import
import os
from time import sleep
import serial
import mainMenu
import routines
import tuneRoutine

#list serial ports
os.system('ls /dev/tty*S*')

print('Choose Serial Port')

#input saved here
serial_port_variable = input()

#Open Serial Port
ser = serial.Serial(
    port=serial_port_variable,
    baudrate=1200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=30, #need to find correct time for this
    rtscts=False,
    dsrdtr=False,
    write_timeout=2,
    inter_byte_timeout=None,
    exclusive=True,
    encoding=ASCII
)

data0 = 0
data1 = 1

while True:
    data0 = ser.read(30)
    if len(data0) == 60:
        data1 = (data0.decode('hex'))
        print('Paragon active')
        print(data1)
        print('Ready')
    else:
        print('No connection, check cable. Exiting')
        raise SystemExit

#clear screen before logo
os.system('clear')

#call mainmenu Main
routines.main_menu_routine()
