import sys
import subprocess as sb

if __name__ == "__main__":
    value = sys.argv[1]
    try:
        max = float(sb.check_output("brightnessctl max", shell=True).decode("utf-8").strip("\n"))
        current = float(sb.check_output("brightnessctl g", shell=True).decode("utf-8").strip("\n"))
        inc = (max / 100.0) * 5

        if value == "inc":
            current = int(current + inc)
            if current > max:
                current = max
            sb.check_output(f"brightnessctl s {current}", shell=True)
        if value == "dec":
            current = int(current - inc)
            if current <= 0:
                current = 1
            sb.check_output(f"brightnessctl s {current}", shell=True)
    except bs.CallProcessError as error:
        print("Error")
