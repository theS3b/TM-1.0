# -*- coding: utf-8 -*-
"""
Created on Mon Jan  27 20:52:19 2020

@author: seb
"""
import time
import os
from clientConnexion import SocketConnexion
from playAgainstAi import playAgainstAi
from ledControl import *
from AIvsAI import AIvsAI
from movePiece import MoveMagnet, set_magnet_off, set_magnet_on

def main():
    # wait for player
    big_light_on()
    wait_for_big_activation()
    big_light_off()

    print("[*] Launching application...")
    magnet = MoveMagnet()

    # try connecting to server
    while True:
        try:
            conn = SocketConnexion()
            break
        except:
            print("[-] Failed to connect.")
            time.sleep(2)
            pass
    
    while True:
        # succeed
        little_light_on()
        time.sleep(0.3)
        little_light_off()

        # choose mode
        little_light_on()
        mode = queen_or_knight()
        little_light_off()

        # manage mode
        if mode == 'q':
            print("[*] Playing human vs AI")
            conn.send_data("HA")  # Human vs Ai
            if playAgainstAi(conn, magnet):
                conn.send_data("ST")
        elif mode == 'k':
            print("[*] Playing AI vs AI")
            conn.send_data("AA")  # Ai vs Ai
            AIvsAI(conn, magnet)

        print("[*] End of game")

        # security
        set_magnet_off()

        #check next action
        big_light_on()
        next_action = check_next_action()
        big_light_off()

        # Shutdown
        if next_action == -1:
            conn.send_data("EN")  # end
            print("[-] Shutting down.")
            os.system("sudo shutdown -h now")

        # New game
        elif next_action == 1:
            print("[+] Playing again.")
            conn.send_data("ST")  # start

if __name__ == "__main__":
    main()


##########  todo shutting down from menu