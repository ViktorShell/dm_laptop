import sys
import subprocess as sb
from .utils import *

class Lumen:
    def get_str(self, background):
        c_max = "brightnessctl max"
        c_get = "brightnessctl g"
        output = ""
        try:
            max = float(sb.check_output(c_max, shell=True).decode("utf-8").strip("\n"))
            get = float(sb.check_output(c_get, shell=True).decode("utf-8").strip("\n"))
            current = ((max - get) / 100) * (max / 100)
            current = 100 - int(current)
            output = f" {current}" + "%% "
        except sb.CalledProcessError as error:
            output = "light_module error"

        icon = "  "
        icon = ground_color(icon, "#101010", "F")
        icon = ground_color(icon, background, "B")
        return icon + output
