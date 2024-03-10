#!/usr/bin/env python3

from modules import workspace
from modules import clock
from modules import battery
from modules import date
from modules import network
from modules import audio
from modules import lumen
import subprocess as sp
import time
import sys


# Main
if __name__ == "__main__":
    # Init
    #os.environ["FONTCONFIG_PATH"] = "/usr/share/fonts/TTF"
    #command = ["/usr/bin/lemonbar",
    #           "-p",
    #           "-g",
    #           "1920x24+0+0",
    #           "-f", 
    #           "\"JetBrainsMono Nerd Font:bold:size=14\"", 
    #           "-f", 
    #           "\"Iosevka Nerd Font:bold:size=14\""]

    # Launch Lemonbar
    #lemon = sp.Popen(command, stdin=sp.PIPE, env=os.environ) 

    # Modules
    workspace = workspace.Workspace()
    clock = clock.Clock()
    date = date.Date()
    battery = battery.Battery()
    network = network.Network()
    audio = audio.Audio()
    lumen = lumen.Lumen()

    # Main loop
    while True:
        l_mod = workspace.get_str("#ff9da4", "#101010", "#ffd3f3", "#101010", "#2c2c2c", "#e8e8d3")
        c_mod = clock.get_str("#e8e8d3")
        r_mod = battery.get_str("#bbdaff")
        r_mod = date.get_str("#101010") + r_mod 
        r_mod = network.get_str("#e58fe5") + r_mod
        r_mod = audio.get_str("#f0a0c0") + r_mod
        r_mod = lumen.get_str("#f5d595") + r_mod
        
        output = "%{l}" + f"{l_mod}" + "%{c}" + f"{c_mod}" + "%{r}" + f"{r_mod}"
        #lemon.stdin.write(output.encode("utf-8"))
        #lemon.stdin.flush()
        sys.stdout.write(output)
        sys.stdout.flush()
        time.sleep(1)
