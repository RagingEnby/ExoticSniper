from base64 import decode
import disnake
import json
import disnake
import requests
import json
from tqdm import tqdm
import time
import aiohttp
import asyncio

from modules.ah_utils import get_nbt_data, get_auction_data, until_refresh
from modules.items import get_item_data, process_item_data
from modules.exotic_type import getExoticType, isLeatherArmor
from modules.color import decimal_to_hex
from modules.discord import make_webhook, send_webhook
from modules.filters import should_send_webhook
import config

item_data = get_item_data()
colors, item_types = process_item_data(item_data)

lastlastUpdated = get_auction_data()['lastUpdated']

#while True:
async def scanner(webhook):
  print('Starting scan...')
  auction_data = get_auction_data()
  lastlastUpdated = auction_data['lastUpdated']
  for auction in auction_data['auctions']:
    if auction['claimed']: return
    if auction['start'] < lastlastUpdated:
      if auction["auctioneer"] == 'f1f46b624a9e4fedbc347dc0f06c2996':
        print(f'Skiping auction by {auction["auctioneer"]} ({auction["uuid"]}) for {auction["item_name"]} due to being old')
      continue
    
    item_data = get_nbt_data(auction['item_bytes'])
    if item_data == {}: continue
    item_id = item_data['ExtraAttributes']['id']
    if not isLeatherArmor(item_id): continue
    exotic_type, hex = getExoticType(item_data)
    if exotic_type is None: continue

    print('\n\n')
    print(hex)
    print(auction['uuid'])
    print(str(item_data).replace("'", '"'))
    print(exotic_type)
    print('\n\n')
    if should_send_webhook(item_id, exotic_type):
      content, embed = make_webhook(item_data, auction, exotic_type, hex, item_types[item_id])
      await send_webhook(webhook, content, embed)
  lastlastUpdated = auction_data['lastUpdated']

  print('Finished scan!')

  sleep_time = until_refresh(auction_data['lastUpdated'])
  print(f'Sleeping for {sleep_time}\n')
  time.sleep(sleep_time)

async def main():
  async with aiohttp.ClientSession() as session:
    webhook = disnake.Webhook.from_url(config.WEBHOOK_URL, session=session)
    while True:
      await scanner(webhook)

asyncio.run(main())