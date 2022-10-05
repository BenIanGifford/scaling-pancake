#!/usr/bin/python3

import time
import onionGpio
machine_blocked = False

"""Set input pins"""
pin2 = onionGpio.OnionGpio(2, ignore_busy=True)
pin2.setDirection(onionGpio.Direction.INPUT)
print("Inputs set")

"""Set output pins (motors)"""
pin1 = onionGpio.OnionGpio(1, ignore_busy=True)
pin1.setDirection(onionGpio.Direction.OUTPUT_LOW)
print("Outputs set")

""" Just defining these things to make the logic easier to understand and help with scalibilty later on"""

def check_for_block():
    """check if its blocked"""
    global machine_blocked
    if pin2.getValue().name == 'HIGH':
        machine_blocked = True
        print(machine_blocked)
    else:
        machine_blocked = False
        
def vend_item():
    """A basic vend cycle with a mosfet motor""" 
    global machine_blocked
    check_for_block()
    if machine_blocked == True:
        print("Blocked")
        exit()
    else:
        pin1.setValue(onionGpio.Value.HIGH)
        print("Vending")
        time.sleep(2)
        pin1.setValue(onionGpio.Value.LOW)
        print("Motor stopped")
        wait_for_light_gate()

def wait_for_light_gate():    
    global machine_blocked
    time.sleep(1.5)
    check_for_block()
    if machine_blocked == False:
        print("Nothing came out")
        exit()
        #raise Exception("Vend failed")
    else:
        print("Item vended")
        exit()
        
def wait_for_vend():
    confirmation = input("Vend? \nYes or No? \n>>> ")

    if  confirmation == "Yes":
        vend_item()
    elif confirmation == "No":
        print("Vend declined")
    else:
        print("Bad input. Please say 'Yes' or 'No'")

wait_for_vend()
