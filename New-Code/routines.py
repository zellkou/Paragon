import os
import time
import serial
import mainMenu
import tuneRoutine
import repeatedPrints


class MenuRoutines:


###########Main Menu Routine
    def main_menu_routine():
        mainMenu.main_menu()
        main_menu_variable = input()
        if main_menu_variable == '1':
            enter_frequency_routine()
        elif main_menu_variable == '2':
            mode_routine()
        elif main_menu_variable == '3':
            filter_routine()
        elif main_menu_variable == '4':
            print('test passed')
            #goto alpha tag rount #menu still needed
        elif main_menu_variable == '5':
            aux_display_routine()
        elif main_menu_variable == '6':
            vfo_routine()
        elif main_menu_variable == '7':
            memory_routine()
        elif main_menu_variable == '8':
            print('test passed')
            #goto display radio status #menu still needed
        elif main_menu_variable == '9':
            aux_function_routine()
        elif main_menu_variable == 'C' or 'c':
            del main_menu_variable
            os.system('clear')
            main_menu_routine()
        elif main_menu_variable == 'D':
            print('test passed')
            #goto mem table display routine #menu still needed
        elif main_menu_variable == 'E' or 'e':
            memory_edit_routine()
        elif main_menu_variable == 'L' or 'l' or 'S' or 's':
            memory_load_routine()
        elif main_menu_variable == 'X' or 'x':
            raise SystemExit
        elif main_menu_variable == '\x1b[D': #left arrow - down
            tuneRoutine.tune_freq_down_routine()
        elif main_menu_variable == '\x1b[C': #right arrow - up
            tuneRoutine.tune_freq_up_routine()
        else:
            del main_menu_variable
            input_not_recognized()
            time.sleep(5)
            main_menu_routine()
###########Mode routine
    def mode_routine():
        mainMenu.mode_menu()
        mode_menu_variable = input()
        if mode_menu_variable == '1':
            tuneRoutine.tune_routine()
        elif mode_menu_variable == '2':
            tuneRoutine.cw_routine()
        elif mode_menu_variable == '3':
            tuneRoutine.usb_routine()
        elif mode_menu_variable == '4':
            tuneRoutine.lsb_routine()
        elif mode_menu_variable == '5':
            tuneRoutine.am_routine()
        elif mode_menu_variable == '6':
            tuneRoutine.fm_routine()
        elif mode_menu_variable == 'M' or 'm':
            del mode_menu_variable
            main_menu_routine()
        else:
            del mode_menu_variable
            repeatedPrints.input_not_recognized()
            time.sleep(5)
            mode_routine()
###########filter routine
    def filter_routine():
        mainMenu.filter_menu()
        filter_menu_variable = input()
        if filter_menu_variable == '1':
            tuneRoutine.filter_6khz()
        elif filter_menu_variable == '2':
            tuneRoutine.filter_24khz
        elif filter_menu_variable == '3':
            tuneRoutine.filter_18khz()
        elif filter_menu_variable == '4':
            tuneRoutine.filter_50khz()
        elif filter_menu_variable == '5':
            tuneRoutine.filter_25khz()
        elif filter_menu_variable == 'M' or 'm':
            del filter_menu_variable
            main_menu_routine()
        else:
            del filter_menu_variable
            input_not_recognized()
            time.sleep(5)
            filter_routine()
###########aux display menu routine
    def aux_display_routine():
        mainMenu.aux_display_menu()
        aux_display_menu_variable = input()
        if aux_display_menu_variable == '1':
            print('test passed')
            #aux dis time routine
        elif aux_display_menu_variable == '2':
            print('test passed')
            #aux dis alpha tag routine
        elif aux_display_menu_variable == '3':
            print('test passed')
            #aux dis date routine
        elif aux_display_menu_variable == 'M' or 'm':
            del aux_display_menu_variable
            main_menu_routine()
        else:
            del aux_display_menu_variable
            input_not_recognized()
            time.sleep(5)
            aux_display_routine()
##########VFO menu routine
    def vfo_routine():
        mainMenu.vfo_menu()
        vfo_menu_variable = input()
        if vfo_menu_variable == '1':
            print('test passed')
            #change vfo A or B routine
        elif vfo_menu_variable == '2':
            print('test passed')
            #set vfos equal a=b routine
        elif vfo_menu_variable == '3':
            print('test passed')
            #change split mode a/=b routine
        elif vfo_menu_variable == 'M' or 'm':
            del vfo_menu_variable
            main_menu_routine()
        else:
            del vfo_menu_variable
            input_not_recognized()
            time.sleep(5)
            vfo_routine()
##########Memory menu routine
    def memory_routine():
        mainMenu.memory_menu()
        memory_menu_varible = input()
        if memory_menu_varible == '1':
            print('test passed')
            #mem store routine
        elif memory_menu_varible == '2':
            print('test passed')
            #mem recall routine
        elif memory_menu_varible == '3':
            memory_lock_routine()
        elif memory_menu_varible == '4':
            print('test passed')
            #mem clear routine
        elif memory_menu_varible == '5':
            print('test passed')
            #mem tune routine
        elif memory_menu_varible == 'M' or 'm':
            del memory_menu_varible
            main_menu_routine()
        else:
            del memory_menu_varible
            input_not_recognized()
            time.sleep(5)
            memory_routine()
#########memory lockout routine
    def memory_lock_routine():
        mainMenu.memory_lock_menu()
        memory_lock_menu_variable = input()
        if memory_lock_menu_variable == '1':
            print('test passed')
            #lock out selected memory channel routine
        elif memory_lock_menu_variable == '2':
            print('test passed')
            #unlock selected memory channel routine
        elif memory_lock_menu_variable == '3':
            print('test passed')
            #lock out all memory channels
        elif memory_lock_menu_variable == '4':
            print('test passed')
            #unlock all memory channels
        elif memory_lock_menu_variable == 'M' or 'm':
            main_menu_routine()
        else:
            del memory_lock_menu_variable
            input_not_recognized()
            time.sleep(5)
            memory_lock_routine()
#########memoyr tune routine
    def memory_tune_routine():
        mainMenu.memory_tune_menu()
        memory_tune_menu_variable = input()
        if memory_tune_menu_variable == '\x1b[D': #left arrow - down
            print('test passed')
            #mem tune down routine
        elif memory_tune_menu_variable == '\x1b[C': #right arrow - up
            print('test passed')
            #mem tune up routine
        elif memory_tune_menu_variable == 'M' or 'm':
            del memory_tune_menu_variable
            main_menu_routine()
        else:
            del memory_tune_menu_variable
            input_not_recognized()
            time.sleep(5)
            memory_tune_routine()
#######aux function routine
    def aux_function_routine():
        mainMenu.aux_function_menu()
        aux_function_menu_variable = input()
        #current_rx_offset_variable = ?
        #current_tx_offset_variable = ?
        #current_fast_tune_variable = ? #should be 0/1
        if aux_function_menu_variable == '1':
            print(current_rx_offset_variable) #need to get this var
            del current_rx_offset_variable
            #need routine for setting this var
        elif aux_function_menu_variable == '2':
            print(current_tx_offset_variabler) #need to get this var
            del current_tx_offset_variable
            #need routine for setting this var
        elif aux_function_menu_variable == '3':
            print(current_fast_tune_variable)
            del current_fast_tune_variable
            #need routine for setting this var
        elif aux_function_menu_variable == '4':
            print('test passed')
            #unsure what this is for the menu says 'voice'
        elif aux_function_menu_variable == '5':
            band_down_routine()
        elif aux_function_menu_variable == '6':
            band_up_routine()
        elif aux_function_menu_variable == '7':
            print('test passed')
            #set date need routine
        elif aux_function_menu_variable == '8':
            print('test passed')
            #set time need routine
        elif aux_function_menu_variable == '\x1b[D':
            print('test passed')
            #unkVar0 down # not real sure whats going on here
        elif aux_function_menu_variable == '\x1b[C':
            print('test passed')
            #unkVar0 up # ditto
        elif aux_function_menu_variable == 'M' or 'm':
            del aux_function_menu_variable
            main_menu_routine()
        else:
            del aux_function_menu_variable
            input_not_recognized()
            time.sleep(5)
            aux_function_routine()
#########Mem load/save
    def memory_load_routine():
        mainMenu.memory_load_menu()
        memory_load_menu_variable = input()
        if memory_load_menu_variable == '1':
            # this is going to need a lot of clean up
            file = (foo.bar, r)
            print(file.read())
        elif memory_load_menu_variable == '2':
            print('test passed')
            #edit mem table routine
        elif memory_load_menu_variable == '3':
            file = open(memory_file_load_variable, r+w)
            # need way of choosing file and not 100% on opening it this way
            print(file.read())
            #need way to push this to the radioo
        elif memory_load_menu_variable == '4':
            print('Choose Memory File')
            os.system('ls ~/Documents/Paragon/')
            memory_file_load_variable = '~/Documents/Paragon/' + input()
            # unsure about this
            file = open(memory_file_load_variable, r+w)
            print(file.read())
        elif memory_load_menu_variable == '5':
            file.close()
        elif memory_load_menu_variable == 'M' or 'm':
            del memory_load_menu_variable
            main_menu_routine()
        else:
            del memory_load_menu_variable
            input_not_recognized()
            time.sleep(5)
            memory_load_routine()
##########mem edit routine
    def memory_edit_routine():
        mainMenu.memory_edit_menu()
        memory_edit_menu_variable = input()
        if memory_edit_menu_variable == '1':
            print('test passed')
            #edit mem freq routine
        elif memory_edit_menu_variable == '2':
            print('test passed')
            #edit alpha tag routine
        elif memory_edit_menu_variable == '3':
            print('test passed')
            #edit mode routine
        elif memory_edit_menu_variable == '4':
            print('test passed')
            #edit filter routine
        elif memory_edit_menu_variable == 'N' or 'n':
            print('test passed')
            #next memory routine
        elif memory_edit_menu_variable == 'P' or 'p':
            del memory_edit_menu_variable
            memory_load_routine()
        elif memory_edit_menu_variable == 'M' or 'm':
            del memory_edit_menu_variable
            main_menu_routine()
        else:
            del memory_edit_menu_variable
            input_not_recognized()
            time.sleep(5)
            memory_edit_routine()
