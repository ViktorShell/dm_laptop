import sys
import subprocess as sb
from .utils import *

class Network:
    def get_str(self, background):
        command = "nmcli device status | awk '{print $3, $4}' | grep \"^connected\""
        try:
            out = sb.check_output(command, shell=True)
        except sb.CalledProcessError as err:
            out = " disconnected "

        if out == "disconnected":
            output = out
            icon = "  "
        else:
            icon = "  "
            output = out.decode("utf-8")
            output = output.splitlines()
            if len(output) > 0:
                output = output[0]
                output = output.split()
                output = " " + output[1] + " "
            else:
                output = " disconnected "
        icon = ground_color(icon, "#101010", "F") 
        icon = ground_color(icon, background, "B")
        return icon + output 
