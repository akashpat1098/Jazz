import os
import subprocess as sp
import random
import socket
import utils

# play music randomly from given file directory
def playMusic():
    music_dir = utils.paths["Music"]
    songs = os.listdir(music_dir)   #need to change the directory
    randSong = random.choice(songs)
    print("Playing Music")
    print(f"Name:{randSong}")
    os.startfile(os.path.join(music_dir, randSong))

def open_notepad():
    os.startfile(utils.paths["Notepad"])

def open_calculator():
    sp.Popen(utils.paths["Calculator"])

# def open_camera():
#     sp.run("startmicrosft.windows.camera:",shell=True)

def open_cmd():
    os.system("start cmd")

# get ip
# it is offline function
def find_my_ip():
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    return ip_address

