import json

with open('cache/exotic_types.json', 'r') as file:
  data = json.load(file)

with open('cache/exotic_types.json', 'w') as file:
  json.dump(data, file, indent=2)