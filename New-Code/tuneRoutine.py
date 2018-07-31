###### frequency tuning routines
class freq:
    def tunUpRou():
        ser.write('[')
    def tunDowRou():
        ser.write(']')
    def entFreRou():
        print('Enter Frequency Including The Decimal')
        userInput = 0
        while True:
            try:
                userInput = int(input("Enter Frequency: "))
            except ValueError:
                print('Numbers Only')
            continue
        else:
            print('Sending To Radio')
            ser.write(userInput)
###### band selection routines
class band:
    def banUpRou():
        ser.write('Z')
    def banDowRou():
        ser.write('Y')
###### fast/slow tuning routhine
class fast:
    def fasRou():
        ser.write('G')
###### transmission mode selection routines
class transMode:
    def fm():
        ser.write('L')
    def am():
        ser.write('M')
    def lsb():
        ser.write('N')
    def usb():
        ser.write('O')
    def cw():
        ser.write('P')
    def tun():
        ser.write('Q')
###### filter selection  routines
class filters:
    def fil60():
        ser.write('R')
    def fil24():
        ser.write('S')
    def fil18():
        ser.write('T')
    def fil50():
        ser.write('U')
    def fil25():
        ser.write('V')

