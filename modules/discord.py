import aiohttp
import disnake

import config
from modules.mojang import get_name
from modules.formatters import pretty_exotic_type, numerize, string_to_hex
from modules.armor_image.armor_image import render_armor
def make_webhook(item_data, auction, exotic_type, hex, item_type, item_id):
  embed = disnake.Embed(
    title=auction['item_name'],
    url=f"https://sky.coflnet.com/auction/{auction['uuid']}",
    color=string_to_hex(hex)
)

  embed.set_author(
    name=get_name(auction['auctioneer']),
    icon_url=f"https://mc-heads.net/head/{auction['auctioneer']}"
  )
  
  embed.add_field(
    name="Price" if auction['bin'] else "Starting Bid",
    value=numerize(auction['starting_bid']),
    inline=True
  )
  embed.add_field(
    name="Exotic Type",
    value=pretty_exotic_type(exotic_type),
    inline=True
  )
  embed.add_field(
    name="Hex",
    value=f"#{hex}",
    inline=True
  )
  
  embed.set_footer(
    text=f"/viewauction {auction['uuid']}"
  )

  render_armor(item_type, hex)
  embed.set_thumbnail(
    file=disnake.File('modules/armor_image/a/output.png')
  )

  content = make_content(item_id, exotic_type, auction)
  return content, embed



async def send_webhook(webhook, content, embed):
  await webhook.send(content=content,
               embed=embed,
               username=config.bot_name,
               avatar_url=config.bot_avatar
              )

def make_content(item_id, exotic_type, auction):
  price = auction['starting_bid']
  # If the armor piece is not lapis or magma armor, price is cheaper than or equal to 100,000,000, and is exotic
  if item_id not in config.lapis_and_magma_armor and price <= 100000000 and exotic_type == 'exotic':
    ping = True

  # If the armor piece is lapis or magma armor, the price is cheaper than or equal to 20,000,000, and is exotic
  elif item_id in config.lapis_and_magma_armor and price <= 20000000 and exotic_type == 'exotic':
    ping = True

  # If the armor piece is wither armor, the price is cheaper than or equal to 50,000,000, and is any non-bleached exotic type
  elif item_id in config.wither_armor and price <= 50000000 and exotic_type != 'bleached':
    ping = True

  # If the armor piece is wither armor, the price is cheaper than or equal to 25,000,000, and it is bleached
  elif item_id in config.wither_armor and price <= 25000000 and exotic_type == 'bleached':
    ping = True

  # If the armor piece is blaze armor, fairy/crystal, and cheaper than or equal to 100,000,000:
  elif item_id in config.blaze_armor and price <= 100000000 and exotic_type in ['crystal', 'fairy', 'og_fairy']:
    ping = True

  # If the price is cheaper than or equal to 5,000,000 and is crystal or fairy
  elif price <= 5000000 and exotic_type in ['crystal', 'fairy', 'og_fairy']:
    ping = True

  # If the price is cheaper than or equal to 1,000,000 and is bleached
  elif price <= 1000000 and exotic_type == 'bleached':
    ping = True

  # If the price is cheaper than or equal to 100,000,000 and is og fairy
  elif price <= 100000000 and exotic_type == 'og_fairy':
    ping = True

  if ping: return config.flip_ping
  return ''