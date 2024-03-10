import sys
import subprocess as sb
from .utils import *

class Audio:
    def get_str(self, background):
        command = "pactl get-sink-volume \"$(pactl get-default-sink)\" | awk '{print $5}'" 
        muted = "pacmd list-sinks | awk '/muted/ {print $2}'"

        try:
            mute = sb.check_output(muted, shell=True).decode("utf-8").strip("\n")
            if mute == "no":
                output = sb.check_output(command, shell=True).decode("utf-8").strip("\n").replace("%", "%%")
                output = " " + output + " "
                icon = "  "
            else:
                icon = "  "
                output = " muted "
        except sb.CalledProcessError as error:
            output = " muted ERR "
            icon = "  "
        icon = ground_color(icon, "#101010", "F")
        icon = ground_color(icon, background, "B")
        return icon + output
