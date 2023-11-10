import config

def should_send_webhook(item_id, exotic_type):
  if item_id in config.shadow_assassin and exotic_type == 'bleached':
    return False
  if item_id in config.reaper_armor:
    return False

  return True