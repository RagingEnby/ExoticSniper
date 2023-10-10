import base64
import requests
#from nbt import nbt
from io import BytesIO
import json
import zlib
from nbtlib import nbt
import python_nbt.nbt as nbt
import time

import config

def get_nbt_data(item_bytes):
  try:
    nbt_data = nbt.read_from_nbt_file(file=BytesIO(base64.b64decode(item_bytes)))
    nbt_data = nbt_data.json_obj(full_json=False)
    nbt_data = nbt_data['i'][0]['tag']
    return nbt_data
  except Exception as e:
    print(e)
    print(item_bytes)
    return {}


def get_auction_data(page=0):
  page = str(page)
  response = requests.get(f'https://api.hypixel.net/skyblock/auctions?page={page}').json()
  #with open('cache/auctions.json', 'w') as file:
  #  json.dump(response, file, indent=2)
  #with open('cache/auctions.json', 'r') as file:
  #  response = json.load(file)
  return response


def until_refresh(lastUpdated):
  lastUpdated_sec = round(lastUpdated / 1000)
  current_time = round(time.time())
  
  nextUpdate = lastUpdated_sec + 70
  untilNextUpdate = nextUpdate - current_time
  return untilNextUpdate



