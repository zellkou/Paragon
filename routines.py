import mainMenu
import os
import time

class rePeat:
    def inNoRE():
        print('Input Not Recognized, Try Again')

class menRou:
###########Main Menu Routine
    def maiRou():
        Main()
        maMeVar = input()
        if maMeVar = '1':
            #goto freq routine #menu still needed for this
        elif maMeVar = '2':
            ModRou() #goto mode routine
        elif maMeVar = '3':
            FilRou() #goto filter routine
        elif maMeVar = '4':
            #goto alpha tag rount #menu still needed
        elif maMeVar = '5':
            AuxDisRou() #goto auxdis routine
        elif maMeVar = '6':
            vfoRou() #goto vfo routine
        elif maMeVar = '7':
            MemRou() # goto memory routine
        elif maMeVar = '8':
            #goto display radio status #menu still needed
        elif maMeVar = '9':
           AuxFunRou() #goto auxfun routine
        elif maMeVar = 'C' or 'c':
            del maMeVar
            os.system('clear')
            MaiRou()
        elif maMeVar = 'D':
            #goto mem table display routine #menu still needed
        elif maMeVar = 'E' or 'e':
            MemEdiRou() #goto memedi routine
        elif maMeVar =  'L' or 'l':
            MemLoaRou() #goto memloa routine
        elif memMeVar = 'S' or 's':
            MemLoaRou() #goto memloa routine
        elif meMeVar = 'X' or 'x':
           raise SystemExit
        elif meMeVar = '\x1b[D': #left arrow - down
            #goto tune freq routine #menu still needed
        elif meMeVar = '\x1b[C': #right arrow - up
            #goto tune freq routine #menu still needed
        else:
            del meMeVar
            inNoRe()
            sleep(5)
            maiRou()
###########Mode routine
    def modRou():
        Mode()
        moMeVar = input()
        if moMeVar = '1':
            #tune routine #menu still needed
        elif moMeVar = '2'
            #mod set cw routine
        elif moMeVar = '3':
            #mod set usb routine
        elif moMeVar = '4':
            #mod set lsb routine
        elif moMeVar = '5':
            #mod set am routine
        elif moMeVar = '6':
            #mod set fm routine
        elif moMeVar = '7':
            #mod set rtty routine
        elif moMeVar = 'M' or 'm':
            del moMeVar
            maiRou()
        else:
            del moMeVar
            inNoRe()
            sleep(5)
            modRou()
###########filter routine
    def filRou():
        Filter()
        filMeVar = input()
        if filMeVar = '1':
            #fil set 6.0 routine
        elif filMeVar = '2':
            #fil set 2.4 routine
        elif filMeVar = '3':
            #fil set 1.8 routine
        elif filMeVar = '4':
            #fil set .50 routine
        elif filMeVar = '5':
            #fil set .25 routine
        elif filMeVar = 'M' or 'm':
            del filMeVar
            maiRou()
        else:
            del filMeVar
            inNoRE()
            sleep(5)
            filRou()
###########aux display menu routine
    def auxDisRou():
        AuxDis()
        auxDisVar = input()
        if auxDisVar = '1':
            #aux dis time routine
        elif auxDisVar = '2':
            #aux dis alpha tag routine
        elif auxDisVar = '3':
            #aux dis date routine
        elif auxDisVar = 'M' or 'm'
            del auxDisVar
            maiRou()
        else:
            del auxDisVar
            inNoRe()
            sleep(5)
            auxDisRou()
##########VFO menu routine
    def VfoRou():
        VFO()
        vfoVar = input()
        if vfoVar = '1':
            #change vfo routine
        elif vfoVar = '2':
            #set vfos equal routine
        elif vfoVar = '3':
            #change split mode routine
        elif vfoVar = 'M' or 'm':
            del vfoVar
            maiRou()
        else:
            del vfoVar
            inNoRe()
            sleep(5)
            VfoRou()
##########Memory menu routine
    def MemRou():
        Memory()
        memVar = input()
        if memVar = '1':
            #mem store routine
        elif memVar = '2':
            #mem recall routine
        elif memVar = '3':
            memLocRou()
        elif memVar = '4':
            #mem clear routine
        elif memVar = '5':
            #mem tune routine
        elif memVar = 'M' or 'm':
            del memVar
            maiRou()
        else:
            del memVar
            inNoRe()
            sleep(5)
            MemRou()
#########memory lockout routine
    def memLocRou():
        MemLoc()
        memLocVar = input()
        if memLocVar = '1':
            #lock out selected memory channel routine
        elif memLocVar = '2':
            #unlock selected memory channel routine
        elif memLocVar = '3':
            #lock out all memory channels
        elif memLocVar = '4':
            #unlock all memory channels
        elif memLocVar = 'M' or 'm':
            maiRou()
        else:
            del memLocVar
            inNoRe()
            sleep(5)
            memLocRou()
#########memoyr tune routine
    def memTunRou():
        MemTun()
        memTunVar = input()
        if memTunVar = '\x1b[D': #left arrow - down
            #mem tune down routine
        elif memtunVar = '\x1b[C': #right arrow - up
            #mem tune up routine
        elif memtunVar = 'M' or 'm':
            del memtunVar
            maiRou()
        else:
            del memTunVar
            inNoRe()
            sleep(5)
            memTunRou()
#######aux function routine
    def auxFunRou():
        AuxFun()
        auxFunVar = input()
        #curRxoffVar = ?
        #curTxoffVar = ?
        #curFastunVar = ? #should be 0/1
        if auxFunVar = '1':
            print(curRxoffVar) #need to get this var
            del curRxoffVar
            #need routine for setting this var
        elif auxFunVar = '2':
            print(curTxoffVarr) #need to get this var
            del curTxoffVar
            #need routine for setting this var
        elif auxFunVar = '3':
            print(CurFastunVar)
            del CurFastunVar
            #need routine for setting this var
        elif auxFunVar = '4':
            #unsure what this is for the menu says 'voice'
        elif auxFunVar = '5':
            #band down need routine
        elif auxFunVar = '6':
            #band up need routine
        elif auxFunVar = '7':
            #set date need routine
        elif auxFunVar = '8':
            #set time need routine
        elif auxFunVar = '\x1b[D':
            #unkVar0 down # not real sure whats going on here
        elif auxFunVar = '\x1b[C':
            #unkVar0 up # ditto
        elif auxFunVar = 'M' or 'm':
            del auxFunVar
            maiRou()
        else:
            del auxFunVar
            inNoRe()
            sleep(5)
            auxFunRou()
#########Mem load/save
    def memLoaRou():
        MemLoa()
        memLoaVar = input()
        if memLoaVar = '1':
            file = (foo.bar, r)
            print file.read()
        elif memLoaVar = '2':
            #edit mem table routine
        elif memLoaVar = '3':
            file = open(memFilVar, r+) # need way of choosing file and not 100% on opening it this way
            print file.read()
            #need way to push this to the radioo
        elif memLoaVar = '4':
            print('Choose Memory File')
            os.system('ls ~/Documents/Paragon/')
            memFilVar = '~/Documents/Paragon/' + input() # unsure about this
            file = open(memFilVar, r+)
            print file.read()
        elif memLoaVar = '5':
            file.close()
        elif memLoaVar = 'M' or 'm':
            del memLoaVar
            maiRou()
        else:
            del memLoaVar
            inNoRe()
            sleep(5)
            memLoaRou()
##########mem edit routine
    def memEdiRou():
        MemEdi()
        memEdiVar = input()
        if memEdiVar = '1':
            #edit mem freq routine
        elif memEdiVar = '2':
            #edit alpha tag routine
        elif memEdiVar = '3':
            #edit mode routine
        elif memEdiVar = '4':
            #edit filter routine
        elif memEdiVar = 'N' or 'n':
            #next memory routine
        elif memEdiVar = 'P' or 'p':
            del memEdiVar
            memLoaRou()
        elif memEdiVar = 'M' or 'm':
            del memEdiVar
            maiRou()
        else:
            del memEdiVar
            inNoRe()
            sleep(5)
            memEdiRou()