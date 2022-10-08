#!/usr/bin/python3

from time import sleep
import onionGpio
machine_blocked = False

output_pins = {1:1, 2:3, 3:0}

for key in output_pins:
  output_pins[key] = onionGpio.OnionGpio(output_pins[key], ignore_busy=True)
  output_pins[key].setDirection(onionGpio.Direction.OUTPUT_LOW)
  print("Outputs set")

input_pins = {1:2, 2:2, 3:2}
#I only have one light gate but in practice this would take the form:
#input_pins = {item number:pin for gate}

for key in input_pins:
    input_pins[key] = onionGpio.OnionGpio(input_pins[key], ignore_busy=True)
    input_pins[key].setDirection(onionGpio.Direction.INPUT)


def check_for_block(port_num):
    """check if its blocked"""
    global machine_blocked
    if input_pins[port_num].getValue().name == 'HIGH':
        machine_blocked = True
        print(machine_blocked)
    else:
        machine_blocked = False
        
def vend_item(item_num):
    """A basic vend cycle with a mosfet motor""" 
    global machine_blocked
    check_for_block(item_num)
    if machine_blocked == True:
        print("Blocked")
        exit()
    else:
        output_pins[item_num].setValue(onionGpio.Value.HIGH)
        print("Vending")
        sleep(2)
        output_pins[item_num].setValue(onionGpio.Value.LOW)
        print("Motor stopped")
        wait_for_light_gate(item_num)

def wait_for_light_gate(port_num):    
    global machine_blocked
    for i in range(20):
        sleep(.2)
        if i == 19: 
            print("vend failed")
            exit()
        elif machine_blocked == False:
            check_for_block(port_num)
            print("Checking")
        elif machine_blocked == True:
            print("Item vended")
            exit()

def wait_for_vend():
    while True:
        item_to_vend = input("Which item would you like to vend?\n 1, 2, 3,\n>>> ")
        try:
            vend_item(int(item_to_vend))
        except ValueError:
            print("Must be an intiger")

wait_for_vend()
