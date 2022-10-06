import onionGpio
from time import sleep
output_pins = {1:1}
#this is used to keep track of the items and which pin is used to vend them
#item number maps to a gpio pin number
    
def set_output(out_num=int(input("Item number "))):
  output_pins[out_num] = onionGpio.OnionGpio(out_num, ignore_busy=True)
  output_pins[out_num].setDirection(onionGpio.Direction.OUTPUT_LOW)
  print("Outputs set")

def vend_item(item_num=int(input("Item number "))):
    output_pins[item_num].setValue(onionGpio.Value.HIGH)
    sleep(2)
    output_pins[item_num].setValue(onionGpio.Value.LOW)
    
set_output(1)
vend_item(1)
  
