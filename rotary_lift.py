import onionGpio
import time
output_pins = {1:1, 2:3, 3:0}

#this is used to keep track of the items and which pin is used to vend them
#item number maps to a gpio pin number
for key in output_pins:    
  output_pins[key] = onionGpio.OnionGpio(output_pins[key], ignore_busy=True)
  output_pins[key].setDirection(onionGpio.Direction.OUTPUT_LOW)
  print("Outputs set")

def vend_item(item_num=int(input("Item number "))):
    output_pins[item_num].setValue(onionGpio.Value.HIGH)
    time.sleep(2)
    output_pins[item_num].setValue(onionGpio.Value.LOW)
    
vend_item()
