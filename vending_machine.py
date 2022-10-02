#!/usr/bin/python3

import time
import onionGpio
machine_blocked = False

"""Set input pins"""
pin2 = onionGpio.OnionGpio(2, ignore_busy=True)
pin2.setDirection(onionGpio.Direction.INPUT)
print("Outputs set")

"""Set output pins (motors)"""
pin1 = onionGpio.OnionGpio(1, ignore_busy=True)
pin1.setDirection(onionGpio.Direction.OUTPUT_LOW)
print("Outputs set")


"""If the machine thinks it's blocked it wont dispense and the program will stop.
    this is unideal for production but for now it's fine"""

while machine_blocked == False:

    """There will be extra logic here later for mqtt inputs.
    For now its just automatically dispensing"""

    pin1.setValue(onionGpio.Value.HIGH)
    print("Vending")
    time.sleep(2)
    pin1.setValue(onionGpio.Value.LOW)
    print("Motor stopped")
    
    """A basic vend cycle with a mosfet motor""" 

    """This stuff below is the special part that watches for the light gate to be tripped
    It waits .25 seconds then if the gate is open, it syas it's not jammed and prints that it's open
    If the gate is closed, it says there is an object and waits 5 seconds for you to remove it.
    If the object is not removed it sets machine blocked to True whic stops the program.
    If the object is removed it says vend sucessful and continues dispensing"""

    for i in range(20):
        time.sleep(.25)

        if pin2.getValue().name == 'LOW':
            print("Machine open")
            machine_blocked = False

        elif pin2.getValue().name == "HIGH":
            print("Item vended")
            time.sleep(5)

            if pin2.getValue().name == "HIGH": 
                machine_blocked = True
                print("Machine blocked")
                break
            else:
                print("Vend sucessful")
