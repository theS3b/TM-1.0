# -*- coding: utf-8 -*-
"""
Created on Mon Jan  27 21:52:59 2020

@author: seb
"""
from clientConnexion import SocketConnexion
from makeAiMove import makeAiMove
from movePiece import set_magnet_off
from ledControl import big_light_off, big_light_on, wait_for_big_activation
from detectPieces import get_board_map

def AIvsAI(conn, magnet):
    try :
        
        haswon = False

        while get_board_map() != 0xFFFF00000000FFFF:
            time.sleep(1)

        # when player is ready
        big_light_on()
        wait_for_big_activation()
        big_light_off()

        print("[+] Beginning to play")

        # Sending ready to receive
        print("[*] Sending ready to receive")
        conn.send_data("RE")

        # playing until someone wins
        while not haswon:
            # Receiving move from AI
            ai_move = conn.recv_data()
            print("[+] Received :", ai_move)

            # Check if win or lost
            if ai_move == "WW":
                print("[+] White player wins.")
                saying_win()                        ############## todo
                break
            if ai_move == "BW":
                print("[+] Black player wins.")
                saying_win()                       #########
                break
            elif ai_move[:2] == "PR":
                print("[*] Promotion from player.")
                ai_move = ai_move[:2]

            haswon = makeAiMove(ai_move, magnet)
            conn.send_data("RE")

    except:
        set_magnet_off()
        exit()