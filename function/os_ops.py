from ipaddress import ip_address
import ipaddress
import os
import subprocess as sp
import random
import socket

paths = {
    "Chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "Music": "H:\\87 HONEY SINGH DJ MIX",
    "Notepad":"C:\\Windows\\system32\\notepad.exe",
    "Calculator":"C:\\Windows\\System32\\calc.exe"
}

def playMusic():
    music_dir = paths["Music"]
    songs = os.listdir(music_dir)
    randSong = random.choice(songs)
    print("Playing Music")
    print(f"Name:{randSong}")
    os.startfile(os.path.join(music_dir, randSong))

def open_notepad():
    os.startfile(paths["Notepad"])

def open_calculator():
    sp.Popen(paths["Calculator"])

def open_camera():
    sp.run("startmicrosft.windows.camera:",shell=True)

def open_cmd():
    os.system("start cmd")

def find_my_ip():
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    return ip_address