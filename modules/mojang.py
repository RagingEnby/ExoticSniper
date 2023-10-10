import requests

def get_name(uuid):
  mojang_response = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
  return mojang_response['name']