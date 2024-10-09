def rgb(r, g, b):
    output = ""
    if (r < 0):
        r = 0
    if (r > 255):
        r = 255
    if r // 16 == 0:
        output += f"0{get(r)}"
    else:
        output += f"{get(r//16)}{get(r%16)}"

    if (g < 0):
        g = 0
    if (g > 255):
        g = 255
    if g // 16 == 0:
        output += f"0{get(g)}"
    else:
        output += f"{get(g//16)}{get(g%16)}"

    if (b < 0):
        b = 0
    if (b > 255):
        b = 255
    if b // 16 == 0:
        output += f"0{get(b)}"
    else:
        output += f"{get(b//16)}{get(b%16)}"

    return output


def get(decimal):
    if decimal < 10:
        return decimal
    elif decimal == 10:
        return "A"
    elif decimal == 11:
        return "B"
    elif decimal == 12:
        return "C"
    elif decimal == 13:
        return "D"
    elif decimal == 14:
        return "E"
    elif decimal == 15:
        return "F"


print(rgb(255, 255, 255)) # returns FFFFFF
print(rgb(255, 255, 300)) # returns FFFFFF
print(rgb(0,0,0)) # returns 000000
print(rgb(148, 0, 211)) # returns 9400D3