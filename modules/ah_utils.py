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
    return {}


def get_auction_data(page=0):
  page = str(page)
  try:
    response = requests.get(f'https://api.hypixel.net/v2/skyblock/auctions?page={page}', timeout=15).json()
    return response
  except requests.Timeout:
    print("Request timed out (15 seconds). Returning None.")
    return None


def until_refresh(lastUpdated):
  lastUpdated_sec = round(lastUpdated / 1000)
  current_time = round(time.time())
  
  nextUpdate = lastUpdated_sec + 60
  untilNextUpdate = nextUpdate - current_time
  if untilNextUpdate <= 0: return 0
  return untilNextUpdate



