import sys
import time
from .utils import *

class Clock:
    def __init__(self):
        self.output = ""

    def get_str(self, text_color):
        self.output = time.strftime("%H:%M")
        self.output = ground_color(self.output, text_color, "F")
        return self.output
