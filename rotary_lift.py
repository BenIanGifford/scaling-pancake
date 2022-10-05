def vend_item(pin_num):
    """A basic vend cycle with a mosfet motor""" 
    pin+pin_num.setValue(onionGpio.Value.HIGH)
    print("Vending")
    time.sleep(2)
    pin+pin_num.setValue(onionGpio.Value.LOW)
    print("Motor stopped")
    wait_for_light_gate()
    
def set_output(out_num):
  pin+out_num = onionGpio.OnionGpio(out_num, ignore_busy=True)
  pin+pin_num.setDirection(onionGpio.Direction.OUTPUT_LOW)
  print("Outputs set")

    
set_output(1)
vend_item(1)
  
