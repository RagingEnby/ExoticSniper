import requests

#def get_name(uuid):
#  mojang_response = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}').json()
#  return mojang_response['name']
RAGINGENBY_HEADERS = {
    "User-Agent": "ExoticSniper",
    "accept": "application/json"
}
cache = {}
def get_name(uuid):
    uuid = uuid.replace('-', '')
    if uuid in cache:
        return cache[uuid]
    try:
        raging_response = requests.get(
            f"https://api.ragingenby.dev/ign/{uuid}",
            headers=RAGINGENBY_HEADERS
        )
        name = raging_response.json()['name']
        cache[uuid] = name
        return name
    except Exception:
        mojang_response = requests.get(
            f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
        )
        if mojang_response.status_code == 200:
            name = mojang_response.json()['name']
            cache[uuid] = name
            return name
        else:
            return uuid
