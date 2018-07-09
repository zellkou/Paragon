class rePeat:
    def inNoRE():
        print('Input Not Recognized, Try Again')

class menRou:
###########Main Menu Routine
    def maiRou():
        maMeVar = input()
        Main()
        if maMeVar = '1':
            #goto freq routine #menu still needed for this
        elif maMeVar = '2':
            Mode() #goto mode routine
        elif maMeVar = '3':
            Filter() #goto filter routine
        elif maMeVar = '4':
            #goto alpha tag rount #menu still needed
        elif maMeVar = '5':
            AuxDis() #goto auxdis routine
        elif maMeVar = '6':
            VFO() #goto vfo routine
        elif maMeVar = '7':
            Memory() # goto memory routine
        elif maMeVar = '8':
            #goto display radio status #menu still needed
        elif maMeVar = '9':
           AuxFun() #goto auxfun routine
        elif maMeVar = 'C' or 'c':
            del maMeVar
            os.system('clear')
            MaiRou()
        elif maMeVar = 'D':
            #goto mem table display routine #menu still needed
        elif maMeVar = 'E' or 'e':
            MemEdi() #goto memedi routine
        elif maMeVar =  'L' or 'l':
            MemLoa() #goto memloa routine
        elif memMeVar = 'S' or 's':
            MemLoa() #goto memloa routine
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
            MaiRou()
###########Mode routine
    def modRou():
        moMeVar = input()
        Mode()
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
            maiRou()
        else:
            del moMeVar
            inNoRe()
            sleep(5)
            modRou()
###########filter routine
    def filRou():
        filMeVar = input()
        Filter()
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
            MaiRou()
        else:
            del filMeVar
            inNoRE()
            sleep(5)
            filRou()
###########aux display menu routine
    def auxDisRou():
        auxDisVar = input()
        AuxDis()
        if auxDisVar = '1':
            #aux dis time routine
        elif auxDisVar = '2':
            #aux dis alpha tag routine
        elif auxDisVar = '3':
            #aux dis date routine
        elif auxDisVar = 'M' or 'm'
            MaiRou()
        else:
            del auxDisVar
            inNoRe()
            sleep(5)
            auxDisRou()
##########VFO menu routine
    def VfoRou():
        vfoVar = input()
        VFO()
        if vfoVar = '1':
            #change vfo routine
        elif vfoVar = '2':
            #set vfos equal routine
        elif vfoVar = '3':
            #change split mode routine
        elif vfoVar = 'M' or 'm':
            MaiRou()
        else:
            del vfoVar
            inNoRe()
            sleep(5)
            VfoRou()
##########Memory menu routine
    def MemRou():
        memVar = input()
        Memory()
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
            MaiRou()
        else:
            del memVar
            inNoRe()
            sleep(5)
            MemRou()
#########memory lockout routine
    def memLocRou():
        memLocVar = input()
        MemLoc()
        if memLocVar = '1':
            #lock out selected memory channel routine
        elif memLocVar = '2':
            #unlock selected memory channel routine
        elif memLocVar = '3':
            #lock out all memory channels
        elif memLocVar = '4':
            #unlock all memory channels
        elif memLocVar = 'M' or 'm':
            MaiRou()
        else:
            del memLocVar
            inNoRe()
            sleep(5)
            memLocRou()
#########memoyr tune routine
    def memTunRou():
        memTunVar = input()
        MemTun()
        if memTunVar = '\x1b[D': #left arrow - down
            #mem tune down routine
        elif memtunVar = '\x1b[C': #right arrow - up
            #mem tune up routine
        elif memtunVar = 'M' or 'm':
            MaiRou()
        else:
            del memTunVar
            inNoRe()
            sleep(5)
            memTunRou()
#
