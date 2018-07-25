###### frequency tuning routines
class freq:
    def tunUpRou():
        ser.write('[')
    def tunDowRou():
        ser.write(']')
    def entfreRou():
        print('Enter Frequency')
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
            break
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
    def 60fil():
        ser.write('R')
    def 24fil():
        ser.write('S')
    def 18fil():
        ser.write('T')
    def 50fil():
        ser.write('U')
    def 25fil():
        ser.write('V')

