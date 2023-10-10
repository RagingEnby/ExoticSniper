def rgb_to_hex(rgb_string):
  r, g, b = map(int, rgb_string.split(','))
  hex_code = "{:02X}{:02X}{:02X}".format(r, g, b)
  return hex_code

def decimal_to_hex(decimal):
  hex_color = hex(decimal)[2:]
  hex_color = hex_color.zfill(6).upper()
  return hex_color