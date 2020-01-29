from movePiece import *
from ledControl import *
import time

mg = MoveMagnet()
f = open("calib.txt", "w")

for nb in range(5, 16):
    for let in range(14,-1, -1):
        set_magnet_on()
        mg.go_to_coo((let, nb), SLOW)
        set_magnet_off()
        time.sleep(0.3)
        set_magnet_on()
        time.sleep(0.7)
        set_magnet_off()
        little_light_on()
        m = queen_or_knight()
        little_light_off()
        if m == 'q':
            continue
        else:
            f.write(str(let) + " " + str(nb) + "\n")
            continue

f.close()
