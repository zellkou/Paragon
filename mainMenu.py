#Menu Class

class Menu:
    maMe = "M -- Return To Main Menu"
    seDe = "Select Desired Function"

    def Main():
        print('Main Menu')
        print('1 -- Enter Frequency')
        print('2 -- Change Mode')
        print('3 -- Change Crystal Filter')
        print('4 -- Enter Alpha Tag')
        print('5 -- Change Aux. Display')
        print('6 -- VFO Functions')
        print('7 -- Memory Functions')
        print('8 -- Display Radio Status')
        print('9 -- Aux. Functions')
        print('C -- Clear Command')
        print('D -- Display Paragon Memory Table')
        print('E -- Edit Memory Table')
        print('L -- Load All Paragon Memories From Disk')
        print('S -- Save All Paragon Memories To Disk')
        print('X -- Exit')
        print('Left Cursor -- Frequency Tune Down')
        print('Right Cursor -- Frequency Tune Up')
        print(SeDe)
    def Mode():  #Main Menu 2
        print('Mode Select Menu')
        print('Current Mode = curModvar') #need variable here
        print('1 -- Tune')
        print('2 -- CW')
        print('3 -- USB')
        print('4 -- LSB')
        print('5 -- AM')
        print('6 -- FM')
        print('7 -- RTTY')
        print(M)
        print('Select Desired Mode')
    def Filter():  #Main Menu 3
        print('Crystal Filter Select Menu')
        print('Current Filter = curFilvar') #need variable here
        print('1 -- 6.0 Khz')
        print('2 -- 2.4 Khz')
        print('3 -- 1.8 Khz')
        print('4 -- 0.50 Khz')
        print('5 -- 0.25 Khz')
        print('M -- Return to Main Menu')
        print('Select Desired Filter')
    def AuxDis():  #Main Menu 5
        print('Aux. Display Menu')
        print('Current Aux. Display = curAuxdisVar') #need Variable here
        print('1 -- Time')
        print('2 -- Alpha Tag')
        print('3 -- Date')
        print('M -- Return To Main Menu')
        print('Select Desired Aux. Display')
    def VF0(): #Main Menu 6
        print('VFO Control Functions')
        print('1 -- Change VFOs')
        print('2 -- Set VFOs Equal')
        print('3 -- Change Split Mode')
        print('M -- Return To Main Menu')
        print('Select Desired Function')
    def Memory(): #Main Menu 7
        print('Memory Functions Menu')
        print('1 -- Memory Store')
        print('2 -- Memory Recall')
        print('3 -- Memory Lockout')
        print('4 -- Memory Clear')
        print('5 -- Memory Tune')
        print('M -- Return To Main Menu')
        print('Select Desired Function')
    def MemLoc(): #Main Menu 7 #Memory Menu  3
        print('Memory Lock/Unlock Menu')
        print('1 -- Lock Out Selected Memory Channel')
        print('2 -- Unlock Selected Memory Channel')
        print('3 -- Lock Out All Memory Channels')
        print('4 -- Unlock All Memory Channels')
        print('M -- Return to Main Menu')
        print('Select Desired Function')
    def MemTun(): # Main Menu 7 #Memory Menu 5
        print('Memory Tune Menu')
        print('Left Cursor -- Memory Tune Down')
        print('Right Cursor -- Memory Tune Up')
        print('M -- Return To Main Menu')
        print('Select Desired Function')
    def AuxFun(): # Main Menu 9
        print('Aux. Functions Select Menu')
        print('1 -- RX Offset curRxoffVar') #need variable here
        print('2 -- TX Offset curTxoffVar') #need variable here
        print('3 -- Fast Tuning CurFastunVar') #need variable here
        print('4 -- Voice')
        print('5 -- Ham Band Down')
        print('6 -- Ham Band Up')
        print('7 -- Set Date curDatvar') #not really a variable just need to pull it from the system
        print('8 -- Set Time curTimvar') #ditto
        print('9 -- Display Radio Status')
        print('Left Cursor -- unkVar0 Down') #unknown variable 0 I believe it's tuning size 100khz or 1mhz
        print('Right Cursor -- unkVar0 Up') #ditto
        print('M -- Return To Main Menu')
        print('Select Desired Function')
    def MemLoa(): # Main Menu L/S
        print('Memory Load/Save Menu')
        print('1 -- Display Memory Table')
        print('2 -- Edit Memory Table')
        print('3 -- Load Paragon Memories')
        print('4 -- Get New Disk File')
        print('5 -- Save Memory Table To Disk')
        print('M -- Return To Main Menu')
        print('Select Desired Function')
    def MemEdi(): #Main Menu L/S #MemLoa 2
        print('Memory Edit Menu')
        print('1 -- Frequency')
        print('2 -- Alpha Tag')
        print('3 -- Mode')
        print('4 -- Crystal Filter')
        print('N -- Next Memory To Edit')
        print('P -- Go To Memory Load/Save Menu')
        print('M -- Return to Main Menu')
        print('Select Item To Edit')
