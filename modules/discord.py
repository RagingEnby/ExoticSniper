import aiohttp
import disnake

import config
from modules.mojang import get_name
from modules.formatters import pretty_exotic_type, numerize, string_to_hex
from modules.armor_image.armor_image import render_armor
def make_webhook(item_data, auction, exotic_type, hex, item_type):
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
  return '', embed



async def send_webhook(webhook, content, embed):
  await webhook.send(content=content,
               embed=embed,
               username=config.bot_name,
               avatar_url=config.bot_avatar
              )