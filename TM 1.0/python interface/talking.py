import subprocess

def saying_win():
    subprocess.call(["aplay", "/home/pi/win.wav"])

def saying_lost():
    subprocess.call(["aplay", "/home/pi/lost.wav"])
