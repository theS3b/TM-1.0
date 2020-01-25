# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:15:19 2019

@author: seb
"""
import time
import os
from detectPieces import get_board_map
from detectPieces import get_nbr_pieces
from detectPieces import get_move
from clientConnexion import *
from movePiece import MoveMagnet
from movePiece import set_magnet_on
from movePiece import set_magnet_off
from movePath import generate_graph
from movePath import get_path
from movePath import print_path
from movePath import print_graph
from movePath import transform_coo_to_index
from movePath import Astar
from ledControl import *
from talking import saying_win
from talking import saying_lost

try :
    print("[*] Launching application...")
    conn = SocketConnexion()

    while True:
        magnet = MoveMagnet()
        haswon = False

        while get_board_map() != 0xFFFF00000000FFFF:
            time.sleep(1)

        big_light_on()
        wait_for_big_activation()
        big_light_off()

        print("[+] Beginning to play")
        # blinking led to start

        while True:
            move = get_move()
            time.sleep(1)  # leave time in case of roque

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

            
            # Get paths
            moves = ai_move.split('#')
            move_path = []

            for move in moves:
                if move == "LO":
                    print("[--] You lost !")
                    saying_lost()
                    haswon = True
                    break

                # Generating graph
                graph = generate_graph(get_board_map(), magnet.n_captured_piece)
                
                # Transform coo to index
                begin, end, magnet.n_captured_piece = transform_coo_to_index(move, magnet.n_captured_piece)

                # Find best path with A*
                print_graph(graph)
                print(begin, " : ", end)
                path = get_path(graph, Astar(graph, begin, end))
                print_path(graph, path, begin)
                path.append(begin)

                path = path[::-1]  # path is inverted so we correct it


                # Execute AI move(s)
                
                print("[*] First case is :", path[0])
                # Move magnet to first case
                magnet.go_to_coo(path[0])

                # Move magnet to end case following the good path
                set_magnet_on()

                for step in path[1:]:
                    magnet.go_to_coo(step)

                # Make sure the piece has moved to the end
                set_magnet_off()
                time.sleep(0.3)
                set_magnet_on()
                time.sleep(0.5)
                set_magnet_off()

            if haswon:
                break
            print("[*] Piece moved.")

        set_magnet_off()  # security

        next_action = check_next_action()

        # Shutdown
        if next_action == -1:
            conn.send_data("EN")  # end
            os.system("sudo shutdown -h now")

        # New game
        elif next_action == 1:
            conn.send_data("ST")  # start

        else:
            print("[-] There was a problem checking user action.")


except KeyboardInterrupt:
    set_magnet_off()
    exit()