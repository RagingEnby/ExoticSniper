from PIL import Image

def render_armor(piece, hex):
  armor_path = f"modules/armor_image/a/{piece.lower()}.png"
  armor_overlay_path = f"modules/armor_image/a/{piece.lower()}_overlay.png"
  overlay_color = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

  grayscale_image = Image.open(armor_path)
  light_array = grayscale_image.convert('L')
  rgba_array = grayscale_image.convert('RGBA')

  result_image = Image.new('RGBA', rgba_array.size)
  for x in range(light_array.width):
    for y in range(light_array.height):
      light_value = light_array.getpixel((x, y))
      adjusted_color = tuple(int(c * (light_value / 255)) for c in overlay_color)
      alpha = rgba_array.getpixel((x, y))[-1]
      rgba = adjusted_color + (alpha,)
      result_image.putpixel((x, y), rgba)

  overlay_image = Image.open(armor_overlay_path)
  result_image.paste(overlay_image, (0, 0), mask=overlay_image)
  result_image = result_image.resize((128, 128), resample=Image.BOX)
  result_image.save("modules/armor_image/a/output.png")
  return result_image
