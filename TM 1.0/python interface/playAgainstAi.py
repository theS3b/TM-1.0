# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:15:19 2019

@author: seb
"""
import time
import os
from detectPieces import get_move, get_board_map
from clientConnexion import SocketConnexion
from movePiece import set_magnet_on, set_magnet_off 
from ledControl import *
from talking import saying_win, saying_lost
from makeAiMove import makeAiMove

def playAgainstAi(conn, magnet):
    try :
        haswon = False
        first = True
        while not haswon:
            
            while get_board_map() != 0xFFFF00000000FFFF:
                time.sleep(1)

            big_light_on()
            wait_for_big_activation()
            big_light_off()

            print("[+] Beginning to play")
            # blinking led to start

            while True:
                move = get_move(not first)
                time.sleep(1)  # leave time in case of roque

                if first:
                    first = False

                if move == "MENU":
                    conn.send_data("ME")
                    return False

                # Sending move
                print("[*] Sending move :", move)
                conn.send_data(move)

                # Receiving move from AI
                ai_move = conn.recv_data()

                if ai_move == "BADMOVE":
                    print("[*] Bad move played.")
                    big_light_on()
                    wait_for_big_activation()
                    big_light_off()
                    continue

                print("[+] Received :", ai_move)

                if ai_move == "WI":
                    print("[++] You won !")
                    saying_win()
                    break
                elif ai_move[:2] == "PR":
                    print("[*] Promotion from the black player.")
                    ai_move = ai_move[:2]
                
                haswon = makeAiMove(ai_move, magnet)
                if haswon:
                    saying_lost()
                    break

            set_magnet_off()  # security

    except:
        set_magnet_off()
        return False
    
    return True