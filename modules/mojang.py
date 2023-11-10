import requests

#def get_name(uuid):
#  mojang_response = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
#  return mojang_response['name']
  
def get_name(uuid):
    try:
        raging_response = requests.get(
            f"https://api.ragingenby.dev/ign/{uuid}"
        )
        return raging_response.json()['name']
    except Exception:
        mojang_response = requests.get(
            f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
        )
        if mojang_response.status_code == 200:
            return mojang_response.json()['name']
        else:
            return uuid
