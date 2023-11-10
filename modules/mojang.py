import requests

def get_name(uuid):
  try:
    raging_response = requests.get(f'https://api.ragingenby.dev/ign/{uuid}').json()
    return raging_response['name']
  except Exception:
    mojang_response = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
    return mojang_response['name']