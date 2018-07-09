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
class band:
    def banUpRou():
        ser.write('Z')
    def banDowRou():
        ser.write('Y')

class fast:
    def fasRou():
        ser.write('G')

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

