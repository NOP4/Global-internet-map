import sys
from PIL import Image

picture_width = 256
picture_height = 256

final_width = picture_width * (53-11)
final_height = picture_height * (61-3)

final_im = Image.new('RGB', (final_width, final_height))

print("Create file", end='', flush=True)
for x in range(11, 53):
    for y in range(3, 61):
        filename = "DL/map_" + f'{x:02d}' + "_" + f'{y:02d}' + ".png"
        image = Image.open(filename)
        final_im.paste(image, ((picture_width * (x-11)), (picture_height * (y-3))))
    print(".", end='', flush=True)

print("")
print("Save file", flush=True)

final_im.save('global-internet-map-2021.png')

