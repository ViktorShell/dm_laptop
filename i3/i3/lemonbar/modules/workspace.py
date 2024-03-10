import sys
import i3ipc
from .utils import *

class Workspace:
    def __init__(self):
        self.ipc = i3ipc.Connection()

    def get_str(
        self,
        foc_color_bg,
        foc_color_fg,
        unfoc_color_bg,
        unfoc_color_fg,
        normal_color_bg,
        normal_color_fg):

        output = ""
        workspace = self.ipc.get_workspaces()
        active = {}
        for ws in workspace:
            active[ws.num] = ws

        for index in range(1,7):
            if index in active:
                ws = active[index]
                if ws.focused:
                    line = ground_color(f" {ws.num} ", foc_color_bg, "B")
                    line = ground_color(line, foc_color_fg, "F")
                    output += line
                else:
                    line = ground_color(f" {ws.num} ", unfoc_color_bg, "B")
                    line = ground_color(line, unfoc_color_fg, "F")
                    output += line
            else:
                output += f" {index} "
        return output
