import sys
import psutil
from .utils import *

class Battery:
    def get_str(self, background): 
        battery = psutil.sensors_battery()   
        icon = ""
        if battery.power_plugged:
            icon = "  "
        else:
            icon = "  "
        output = f" {int(battery.percent)}" + "%% "
        output = ground_color(output, "#e8e8d3", "F")
        icon = ground_color(icon, "#101010", "F")
        icon = ground_color(icon, background, "B")
        output = icon + output
        return output

