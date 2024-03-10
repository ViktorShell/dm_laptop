import subprocess as sb
from .utils import *

class Network:
    def get_str(self, background):
        command = "nmcli dev status | awk 'NR > 1 {print $3, $4}' | sed -n 1p"
        out = "disconnected"
        try:
            out = sb.check_output(command, shell=True)
            out = out.decode("utf-8").strip("\n").split()
        except sb.CalledProcessError as err:
            pass
      
        print(out)
        if out[0] == "disconnected" or out[1] == "(externally)":
            output = f" disconnected "
            icon = "  "
        else:
            icon = "  "
            output = f" {out[1]} "
        icon = ground_color(icon, "#101010", "F") 
        icon = ground_color(icon, background, "B")
        return icon + output 

if __name__ == "__main__":
    net = Network()
    print(net.get_str("#AAA"))
