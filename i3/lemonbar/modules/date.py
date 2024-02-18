import sys
import time
from .utils import *

class Date:
    def get_str(self, background):
        date = time.strftime(" %d.%m.%y ")
        icon = "  "
        icon = ground_color(icon, "#101010", "F")
        icon = ground_color(icon, "#d1f1a9", "B")
        return icon + date
