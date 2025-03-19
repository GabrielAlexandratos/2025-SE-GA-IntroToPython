# Example starter code
def rgb_to_hex(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


if __name__ == "__main__":
    # Test with some popular colors
    red = rgb_to_hex(255, 0, 0)
    sky_blue = rgb_to_hex(135, 206, 235)
    print(f"Red: {red}")
    print(f"Sky Blue: {sky_blue}")
