# text + color + foreground/background
def ground_color(text, color, let):
    return "%{" + let + color + "}" + text + "%{" + let + "-}"

def offset(text, offset):
    return text + "%{O" + f"{offset}" + "}"
