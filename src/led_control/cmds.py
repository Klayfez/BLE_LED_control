def power(is_on: bool):
    # 7e 00 04 is_on 00 00 00 00 ef
    is_on = "01" if is_on else "00"

    return f"7e 00 04 {is_on} 00 00 00 00 ef".lower()

def brightness(brightness: int):
    # 7e 00 01 brightness 00 00 00 00 ef
    brightness = format(brightness, '02X')

    return f"7e 00 01 {brightness} 00 00 00 00 ef".lower()

def color(r: int, g: int, b: int):
    # 7e 00 05 03 r g b 00 ef
    r = format(r, '02X')
    g = format(g, '02X')
    b = format(b, '02X')

    return f"7e 00 05 03 {r} {g} {b} 00 ef".lower()