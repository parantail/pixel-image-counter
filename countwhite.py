filepath = "worldmap.bmp"

from PIL import Image
#img = input("File name: ")
img = Image.open(filepath);

count = 0
for y in range(img.height):
  for x in range(img.width):
    pixel = img.getpixel((x, y))
    if pixel[0] > 0:
      count = count + 1

print(count, "pixels")
