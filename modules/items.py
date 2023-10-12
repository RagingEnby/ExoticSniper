import requests
import json

from modules.color import rgb_to_hex
import config

def get_item_data():
  response = requests.get('https://api.hypixel.net/resources/skyblock/items').json()
  with open('cache/items.json', 'w') as file:
    json.dump(response, file, indent=2)
  return response



def process_item_data(item_data=get_item_data()):
  colors = {}
  item_types = {}
  for item in item_data['items']:
    if not item['material'].startswith('LEATHER_'): continue
    if 'color' not in item: item['color'] = '160,124,64'
    colors[item['id']] = rgb_to_hex(item['color'])
    item_types[item['id']] = item['material']
    
  with open('cache/colors.json', 'w') as file:
    json.dump(colors, file, indent=2)

  with open('cache/item_types.json', 'w') as file:
    json.dump(item_types, file, indent=2)
  return colors, item_types