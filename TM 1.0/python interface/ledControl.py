from movePiece import busInt
import time

# leds
busInt.set_pin_direction(15, 0)
busInt.set_pin_direction(12, 0)
# buttons
busInt.set_pin_direction(11, 1)
busInt.set_pin_pullup(11,1)
busInt.invert_pin(11, 1)

busInt.set_pin_direction(10, 1)
busInt.set_pin_pullup(10,1)
busInt.invert_pin(10, 1)

busInt.set_pin_direction(9, 1)
busInt.set_pin_pullup(9,1)
busInt.invert_pin(9, 1)

def big_light_on():
    busInt.write_pin(15, 1)

def little_light_on():
    busInt.write_pin(12, 1)

def big_light_off():
    busInt.write_pin(15, 0)

def little_light_off():
    busInt.write_pin(12, 0)

def wait_for_big_activation():
    while busInt.read_pin(11) == 0:
        time.sleep(0.1)

def queen_or_knight():
    while True:
        if busInt.read_pin(9) == 1:
            return "q"
        elif busInt.read_pin(10) == 1:
            return "k"
        time.sleep(0.1)

def check_next_action():
    while busInt.read_pin(11) == 0:
        time.sleep(0.2)
    if busInt.read_pin(11) == 1:
        big_light_on()
        time.sleep(5)  # turn it off is longer
        big_light_off()
        if busInt.read_pin(11) == 1:
            for z in range(3):
                big_light_on()
                little_light_on()
                time.sleep(0.3)
                big_light_off()
                little_light_off()
                time.sleep(0.3)
            return -1  # turn off
        return 1  # new game
    return 0  # not possible
