# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:15:19 2019

@author: seb
"""
from IOPi import IOPi
import math
import time

busAB = IOPi(0x21)
busDC = IOPi(0x20)
busEF = IOPi(0x24)
busGH = IOPi(0x25)

# A
A = 0
busAB.set_port_pullups(A, 0xFF)
busAB.set_port_direction(A, 0xFF)
busAB.invert_port(A, 0xFF)

# B
B = 1
busAB.set_port_pullups(B, 0xFF)
busAB.set_port_direction(B, 0xFF)
busAB.invert_port(B, 0xFF)

# C
C = 1
busDC.set_port_pullups(C, 0xFF)
busDC.set_port_direction(C, 0xFF)
busDC.invert_port(C, 0xFF)

# D
D = 0
busDC.set_port_pullups(D, 0xFF)
busDC.set_port_direction(D, 0xFF)
busDC.invert_port(D, 0xFF)

# E
E = 0
busEF.set_port_pullups(E, 0xFF)
busEF.set_port_direction(E, 0xFF)
busEF.invert_port(E, 0xFF)

# F
F = 1
busEF.set_port_pullups(F, 0xFF)
busEF.set_port_direction(F, 0xFF)
busEF.invert_port(F, 0xFF)

# G
G = 0
busGH.set_port_pullups(G, 0xFF)
busGH.set_port_direction(G, 0xFF)
busGH.invert_port(G, 0xFF)

# H
H = 1
busGH.set_port_pullups(H, 0xFF)
busGH.set_port_direction(H, 0xFF)
busGH.invert_port(H, 0xFF)

def transform_CD(nbr):
    b = 0
    if nbr & 64 != 0:
        b |= 1
    if nbr & 128 != 0:
        b |= 2
    if nbr & 16 != 0:
        b |= 4
    if nbr & 32 != 0:
        b |= 8
    if nbr & 4 != 0:
        b |= 16
    if nbr & 8 != 0:
        b |= 32
    if nbr & 1 != 0:
        b |= 64
    if nbr & 2 != 0:
        b |= 128
    return b

def insert_zero(pieces, col):
    sp = bin(pieces)[2:]
    sp = sp[::-1]
    sret = col* "0"
    for c in sp:
        sret = "0000000" + c + sret

    return int(sret, 2)

def get_board_map():
    board = insert_zero(busAB.read_port(A), 7) | insert_zero(busAB.read_port(B), 6) | insert_zero(transform_CD(busDC.read_port(C)), 5) | insert_zero(transform_CD(busDC.read_port(D)), 4) | insert_zero(busEF.read_port(E), 3) | insert_zero(busEF.read_port(F), 2) | insert_zero(busGH.read_port(G), 1) | insert_zero(busGH.read_port(H), 0)
    return board

def get_nbr_pieces(board_map):
    return bin(board_map)[2:].count('1')

def case_index_to_coo(index):
    n = int(index / 8) + 1
    char = 'hgfedcba'
    let = char[int(index % 8)]
    return let + str(n)

def get_move():
    piece_removed = False
    capturing_piece = False

    before = get_board_map()
    nbr_pieces_before = get_nbr_pieces(before)
    case_piecer = 0
    boardr = 0
    after = 0
    case_after = 0
    
    while True:
        bmap = get_board_map()
        nbr_pieces = get_nbr_pieces(bmap)
        
        if bmap != before and not piece_removed:
            piece_removed = True
            case_piecer = bmap ^ before
            boardr = bmap

        elif (piece_removed and nbr_pieces == nbr_pieces_before) or (capturing_piece and nbr_pieces == (nbr_pieces_before -1)):
            after = bmap
            case_after = boardr ^ after
            break

        elif piece_removed and nbr_pieces == (nbr_pieces_before - 2):
            case_piecer = bmap ^ boardr
            boardr = bmap
            capturing_piece = True
            time.sleep(2)  # so there's less probability of catching the place moving

        time.sleep(0.5)
    return case_index_to_coo(math.log2(case_piecer)) + case_index_to_coo(math.log2(case_after))
