import subprocess as proc
from .utils import *
import math

class Battery:
    def __init__(self):
        self.battery_pwd = "/sys/class/power_supply/BAT1"
        self.charging = proc.check_output(f"cat {self.battery_pwd}/status", shell=True).decode("utf-8").strip("\n")
        self.energy_full = float(proc.check_output(f"cat {self.battery_pwd}/energy_full", shell=True).decode("utf-8").strip("\n")) / 10000
        self.energy_now = float(proc.check_output(f"cat {self.battery_pwd}/energy_now", shell=True).decode("utf-8").strip("\n")) / 10000

    def current_state(self):
        self.energy_now = float(proc.check_output(f"cat {self.battery_pwd}/energy_now", shell=True).decode("utf-8").strip("\n")) / 10000
        percent = 100.0 / self.energy_full 
        current = self.energy_now * percent
        return math.trunc(current)

    def charging_bool(self):
        if self.charging == "Discharging":
            return False
        else:
            return True

    def get_str(self, background): 
        icon = ""
        if self.charging_bool():
            icon = "  "
        else:
            icon = "  "
        output = f" {self.current_state()}" + "%% "
        output = ground_color(output, "#e8e8d3", "F")
        icon = ground_color(icon, "#101010", "F")
        icon = ground_color(icon, background, "B")
        output = icon + output
        return output
