import os

def saying_win():
    os.system("./speak.sh /home/pi/win.wav")

def saying_lost():
    os.system("./speak.sh /home/pi/lost.wav")
