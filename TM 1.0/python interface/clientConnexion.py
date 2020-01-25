# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:15:19 2019

@author: seb
"""

# communication between raspberry and C++
# Python client and server

import socket

CPPPORT = 62358

class SocketConnexion(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("192.168.10.4", CPPPORT))
    
    def send_data(self, str_data):
        self.sock.sendall(str_data.encode('ascii'))
    
    def recv_data(self):
        return self.sock.recv(1024).decode('ascii')

