# Paragon Control Software
import serial
from time import sleep

#Open Serial Port
with serial.Serial() as ser:
    ser.port = '/dev/ttyS0'
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
    open()
    
while True:
    data = ser.read(9999)
    if len(data) > 0:
        print 'Paragon active', data

    sleep(1)
    print 'Ready'

# logo

print "TEN-TEC Paragon Serial Interface Control Program"
print "Copyright 1988"
print "By"
print "TEN-TEC, Inc."
print "Ported to Python"
print "By"
print "The Hillbilly Hacker"
print "Python 3 Version" #add date when finished

