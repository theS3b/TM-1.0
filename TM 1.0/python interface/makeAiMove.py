# -*- coding: utf-8 -*-
"""
Created on Mon Jan  27 21:32:19 2020

@author: seb
"""

import time
from talking import saying_win, saying_lost
from movePath import *
from movePiece import FAST, SLOW, set_magnet_off, set_magnet_on
from detectPieces import get_board_map

def makeAiMove(ai_move, magnet):
    # Get paths
    moves = ai_move.split('#')

    for move in moves:
        if move == "LO":
            print("[--] You lost !")
            return True

        # Generating graph
        graph = generate_graph(get_board_map(), magnet.n_captured_piece, B_ARR)
        
        # Transform coo to index
        begin, end, magnet.n_captured_piece = transform_coo_to_index(move, magnet.n_captured_piece, B_ARR)

        # Find best path with A*
        print_graph(graph)
        print(begin, " : ", end)
        path = get_path(graph, Astar(graph, begin, end))
        print_path(graph, path, begin)
        path.append(begin)

        # path is inverted so we correct it
        path = path[::-1] 


        # Execute AI move(s)
        print("[*] First case is :", path[0])

        # Move magnet to first case
        magnet.go_to_coo(path[0], FAST)

        # Move magnet to end case following the good path
        set_magnet_on()

        for step in path[1:]:
            magnet.go_to_coo(step, SLOW)

        # Make sure the piece has moved to the end
        set_magnet_off()
        time.sleep(0.3)
        set_magnet_on()
        time.sleep(0.5)
        set_magnet_off()

    print("[*] Piece moved.")
    return False
