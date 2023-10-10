import json

from modules.color import decimal_to_hex, rgb_to_hex
from modules.items import process_item_data
import config

default_colors, item_types = process_item_data()

with open('cache/exotic_types.json', 'r') as file:
  colors = json.load(file)

def isLeatherArmor(item_id):
  return item_id in item_types and item_types[item_id].startswith('LEATHER_')
  
def getExoticType(item_data):
  item_id = item_data['ExtraAttributes']['id']
  if 'color' in item_data['display']: color = hex = decimal_to_hex(item_data['display']['color'])
  elif 'color' in item_data['ExtraAttributes']: hex = rgb_to_hex(item_data['ExtraAttributes']['color'].replace(':', ','))
  else: hex = 'A06540'
  
  if 'dye_item' in item_data['ExtraAttributes']: return None, hex


  if default_colors[item_id] == hex: return None, hex
  if item_id in config.great_spook_armor:
    print('great spook found')
    if hex in colors['great_spook']:
      return None, hex
    else:
      print(f'{hex} great spook armor not in great spook colors')

  armor_type = item_types[item_id]
  armor_type = armor_type.lower().replace('leather_', '')

  if isVariant(item_id, hex): return None, hex

  if isGlitched(item_id, hex): return 'glitched', hex

  if isOgFairy(item_id, armor_type, hex): return 'og_fairy', hex

  if isFairy(item_id, hex): return 'fairy', hex

  if isCrystal(item_id, hex): return 'crystal', hex
  
  if isBleached(hex): return 'bleached', hex

  
  return 'exotic', hex
  

def isOgFairy(item_id, armor_type, hex):
  if item_id in config.fairy_armor: return False
  if hex in colors['og_fairy']: return True
  if hex in colors['og_fairy_' + armor_type]: return True
  return False

def isFairy(item_id, hex):
  if item_id in config.fairy_armor: return False
  return hex in colors['fairy']

def isCrystal(item_id, hex):
  if item_id in config.crystal_armor: return False
  return hex in colors['crystal']

def isBleached(hex):
  return hex == colors['bleached']

def isVariant(item_id, hex):
  if item_id in config.never_exotic: return True
    
  # Color changing stuff
  if item_id in config.fairy_armor and hex in colors['fairy']: return True
  if item_id in config.crystal_armor and hex in colors['crystal']: return True
  if item_id in config.great_spook_armor and hex in colors['great_spook']: return True

  if item_id == config.ghostly_boots: return True

  if item_id in colors['variants'] and hex in colors['variants'][item_id]: return True

def isGlitched(item_id, hex):
  return item_id in colors['glitched'] and colors['glitched'][item_id] == hex