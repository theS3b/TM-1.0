from movePiece import *
import time

try:

    mg = MoveMagnet()
    mg.go_to_coo((1,1), SLOW)
    set_magnet_on()

    time.sleep(1)
    mg.go_to_coo((14,1), SLOW)


finally:
    set_magnet_off()


'''
def new(mg, tick, dir, sspeed):
    speed = int(sspeed)
    delta = 0
    busMot.write_pin(dirlet, dir)
    if dir == home_dir:
        while mg.let != 0 and delta != tick:
            busMot.write_pin(steplet,1)
            time.sleep(speed/1000000)
            busMot.write_pin(steplet,0)
            time.sleep(speed/1000000)
            delta += 1
            mg.let -= 1
        print("[+] Magnet set to", mg.let, "let.")
    
    elif dir == ext_dir:
        while mg.let < MAXLET and delta < tick:
            busMot.write_pin(steplet,1)
            time.sleep(speed/1000000)
            busMot.write_pin(steplet,0)
            time.sleep(speed/1000000)
            delta += 1
            mg.let += 1

        print("[+] Magnet set to", mg.let, "let.")

try:
    mg = MoveMagnet()
    mg.go_to_A1_from_home()
    mg.go_to_A1_from_home()

    set_magnet_on()

    busMot.write_pin(MSnb, 0)
    busMot.write_pin(MSlet, 0)

    time.sleep(2)
    new(mg, 200, 1, 100)
    time.sleep(1)
    new(mg, 200, 1, 800)
    time.sleep(1)
    new(mg, 200, 0, 300)

    set_magnet_off()

    busMot.write_pin(MSnb, 1)
    busMot.write_pin(MSlet, 1)

    mg.home_nb()
    mg.home_let()
finally:
    busMot.write_pin(MSnb, 1)
    busMot.write_pin(MSlet, 1)
    set_magnet_off()
'''