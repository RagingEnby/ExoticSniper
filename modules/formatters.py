def pretty_exotic_type(exotic_type):
  exotic_type = exotic_type.replace('_', ' ')
  exotic_type = exotic_type.capitalize()
  return exotic_type

def numerize(num):
  num = float('{:.3g}'.format(num))
  magnitude = 0
  while abs(num) >= 1000:
    magnitude += 1
    num /= 1000.0
  return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def string_to_hex(hex_string):
  if not hex_string.startswith("0x"): hex_string = "0x" + hex_string
  value = int(hex_string, 16)
  return value