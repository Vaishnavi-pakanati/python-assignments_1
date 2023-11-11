COLOR_CODES = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

TOLERANCES = {"grey": "±0.05%",
             "violet": "±0.1%",
             "blue": "±0.25%",
             "green": "±0.5%",
             "brown": "±1%",
             "red": "±2%",
             "gold": "±5%",
             "silver": "±10%"}

def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black": return "0 ohms"

    if len(colors) == 4: colors.insert(0, "black")
    
    resistance = (COLOR_CODES.index(colors[0]) * 100 + COLOR_CODES.index(colors[1]) * 10 + COLOR_CODES.index(colors[2])) * 10**COLOR_CODES.index(colors[3])

    prefixes = ("", "kilo", "mega", "giga")
    idx = 0

    if resistance >= 1000:
        while resistance % 1000 == 0:
            resistance //= 1000
            idx += 1
        
        if resistance % 10 == 0:
            resistance /= 1000
            idx += 1
    
    tolerance = TOLERANCES[colors[4]]

    return f"{resistance} {prefixes[idx]}ohms {tolerance}"
