#!/usr/bin/python3

from time import sleep
import onionGpio
import paho.mqtt.client as mqtt 
import random

machine_blocked = False

broker = 'broker.emqx.io'
debug_topic = "vending debug"
port = 1883
topic = "vending"
failure = "Vend failed" 
sucess = "Vend sucess" 
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

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
        client.publish(debug_topic, failure)
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
            client.publish(debug_topic, failure)
            break
        elif machine_blocked == False:
            check_for_block(port_num)
            print("Checking")
        elif machine_blocked == True:
            print("Item vended")
            client.publish(debug_topic, sucess)
            break

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)
    
def on_message(client, userdata, msg):
    vend_item(int(msg.payload))

client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
#def wait_for_vend():
#    while True:
#        item_to_vend = input("Which item would you like to vend?\n 1, 2, 3,\n>>> ")
#        try:
#            vend_item(int(item_to_vend))
#        except ValueError:
#            print("Must be an intiger")
