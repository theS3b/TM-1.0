# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:15:19 2019

@author: seb
"""

from IOPi import IOPi
import time

# nb -> coo[0], let -> coo[1]

steplet = 2
dirlet = 1
stepnb = 4
dirnb = 3
MSlet = 5
MSnb = 7
intnb = 1
intlet = 2
home_dir = 1
ext_dir = 0
mag = 16

A1_LET = 200
A1_NB = 600
H1_LET = 4100
H1_NB = 570

COO_NB = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # unused
[570, 570, 570, 570, 570, 570, 570, 570, 570, 570, 570, 570, 570, 570, 570],
[845, 845, 845, 845, 845, 845, 845, 845, 845, 845, 845, 845, 845, 845, 845],
[1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120, 1120],
[1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395, 1395],
[1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670, 1670],
[1945, 1945, 1945, 1945, 1945, 1945, 1945, 1946, 1947, 1948, 1950, 1951, 1952, 1954, 1955],
[2220, 2220, 2220, 2220, 2220, 2220, 2220, 2223, 2225, 2227, 2230, 2233, 2235, 2238, 2240],
[2502, 2502, 2502, 2502, 2502, 2502, 2502, 2504, 2505, 2507, 2510, 2513, 2515, 2517, 2520],
[2785, 2785, 2785, 2785, 2785, 2785, 2785, 2785, 2785, 2788, 2790, 2793, 2795, 2797, 2800],
[3070, 3070, 3070, 3070, 3070, 3070, 3070, 3070, 3070, 3073, 3075, 3078, 3080, 3082, 3085],
[3355, 3355, 3355, 3355, 3355, 3355, 3355, 3355, 3355, 3358, 3360, 3363, 3365, 3368, 3370],
[3627, 3629, 3631, 3633, 3636, 3640, 3640, 3640, 3640, 3642, 3645, 3648, 3650, 3652, 3655],
[3900, 3904, 3908, 3912, 3918, 3925, 3925, 3925, 3925, 3927, 3930, 3933, 3935, 3937, 3940],
[4185, 4189, 4193, 4197, 4203, 4207, 4210, 4210, 4210, 4212, 4215, 4218, 4220, 4222, 4225],
[4470, 4474, 4478, 4482, 4488, 4490, 4495, 4495, 4495, 4498, 4500, 4503, 4505, 4508, 4510],
[5095, 5095, 5100, 5100, 5105, 5105, 5105, 5105, 5105, 5105, 5105, 5105, 5105, 5110, 5110]]

COO_LET = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # unused
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4110, 3840, 3570, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4115, 3845, 3575, 3285, 3000, 2723, 2445, 2163, 1880, 1605, 1330, 1050, 770, 490, 210],
[4120, 3850, 3575, 3285, 3000, 2720, 2440, 2160, 1880, 1600, 1320, 1040, 760, 483, 205],
[4120, 3850, 3575, 3285, 3000, 2720, 2440, 2160, 1880, 1600, 1320, 1040, 760, 483, 205]]

MAXLET = 4300
MAXNB = 5120
CAPTURED_NB = 5105

busMot = IOPi(0x22)
busMot.set_port_direction(0, 0)
busMot.write_pin(MSnb, 1)
busMot.write_pin(MSlet, 1)

busInt = IOPi(0x23)

# interupter 1
busInt.set_pin_direction(intnb,1)
busInt.set_pin_pullup(intnb,1)
busInt.invert_pin(intnb,1)
# interupter 2
busInt.set_pin_direction(intlet,1)
busInt.set_pin_pullup(intlet,1)
busInt.invert_pin(intlet,1)
# magnet
busInt.set_pin_direction(mag, 0)

def set_magnet_on():
    busInt.write_pin(16, 1)
    print("[+] Magnet set to 1.")
    return

def set_magnet_off():
    busInt.write_pin(16, 0)
    print("[+] Magnet set to 0.")
    return

class MoveMagnet(object):
    def __init__(self):
        self.nb = 0
        self.let = 0
        self.n_captured_piece = 0
        self.home_let()
        self.home_nb()
    
    def home_nb(self):
        if busInt.read_pin(intnb) == 1:
            print("[*] NB already home.")
            return
        
        busMot.write_pin(dirnb, home_dir)
        while busInt.read_pin(intnb) == 0:
            busMot.write_pin(stepnb,1)
            time.sleep(500/1000000)
            busMot.write_pin(stepnb,0)
            time.sleep(500/1000000)
        
        busMot.write_pin(dirnb, ext_dir)
        for i in range(20):
            busMot.write_pin(stepnb,1)
            time.sleep(500/1000000)
            busMot.write_pin(stepnb,0)
            time.sleep(500/1000000)
        
        self.nb = 0
        print("[+] NB home.")
        return

    def home_let(self):
        if busInt.read_pin(intlet) == 1:
            print("[*] LET already home.")
            return

        busMot.write_pin(dirlet, home_dir)
        while busInt.read_pin(intlet) == 0:
            busMot.write_pin(steplet,1)
            time.sleep(500/1000000)
            busMot.write_pin(steplet,0)
            time.sleep(500/1000000)

        busMot.write_pin(dirlet, ext_dir)
        for i in range(20):
            busMot.write_pin(steplet,1)
            time.sleep(500/1000000)
            busMot.write_pin(steplet,0)
            time.sleep(500/1000000)

        self.let = 0
        print("[+] LET home.")
        return

    def move_let_magnet(self, tick, dir):
        delta = 0
        busMot.write_pin(dirlet, dir)
        if dir == home_dir:
            while self.let != 0 and delta != tick:
                busMot.write_pin(steplet,1)
                time.sleep(500/1000000)
                busMot.write_pin(steplet,0)
                time.sleep(500/1000000)
                delta += 1
                self.let -= 1
            print("[+] Magnet set to", self.let, "let.")
        
        elif dir == ext_dir:
            while self.let < MAXLET and delta < tick:
                busMot.write_pin(steplet,1)
                time.sleep(500/1000000)
                busMot.write_pin(steplet,0)
                time.sleep(500/1000000)
                delta += 1
                self.let += 1
    
            print("[+] Magnet set to", self.let, "let.")

    def move_nb_magnet(self, tick, dir):
        delta = 0
        busMot.write_pin(dirnb, dir)
        if dir == home_dir:
            while self.nb != 0 and delta != tick:
                busMot.write_pin(stepnb,1)
                time.sleep(500/1000000)
                busMot.write_pin(stepnb,0)
                time.sleep(500/1000000)
                delta += 1
                self.nb -= 1
            print("[+] Magnet set to", self.nb, "nb.")
        
        elif dir == ext_dir:
            while self.nb < MAXNB and delta < tick:
                busMot.write_pin(stepnb,1)
                time.sleep(500/1000000)
                busMot.write_pin(stepnb,0)
                time.sleep(500/1000000)
                delta += 1
                self.nb += 1
    
            print("[+] Magnet set to", self.nb, "nb.")

    def go_to_A1_from_home(self):
        self.move_let_magnet(A1_LET, ext_dir)
        self.move_nb_magnet(A1_NB, ext_dir)

    def go_to_coo(self, coo):
        nb = COO_NB[coo[1]][coo[0]]
        let = COO_LET[coo[1]][coo[0]]
        
        dir = 0

        # nb
        if nb < self.nb:
            dir = home_dir
        elif nb > self.nb:
            dir = ext_dir
        
        self.move_nb_magnet(abs(self.nb - nb), dir)

        # let
        if let < self.let:
            dir = home_dir
        elif let > self.let:
            dir = ext_dir
        
        self.move_let_magnet(abs(self.let - let), dir)

