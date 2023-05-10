import math
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


fig = plt.figure()
ax_3d = fig.add_subplot(projection='3d')
x = np.arange(-18, 20)
y = np.arange(0, 10)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = np.sin(xgrid * math.pi / 4) * ygrid * 2 * 3
ax_3d.plot_surface(xgrid, ygrid, zgrid, cmap="plasma")

# Сохранение в картинку
# plt.savefig("3d.png")


# PIL
img = Image.open("3d.png").convert("RGBA")
img.load()

# Растянуть
wide_img = img.resize((1200, 480))
wide_img.save("wide_img.png")

# Сжать
compressed_img = img.resize((640, 240))
compressed_img.save("compressed_img.png")

# Повернуть
rotated_img = img.rotate(90)
rotated_img.save("rotated_img.png")

# Перекрасить
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        p = pixels[x, y]
        pixels[x, y] = (0, p[1], p[2], 255)
img.save("deleted_red_img.png")
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        p = pixels[x, y]
        pixels[x, y] = (p[0], 0, p[2], 255)
img.save("deleted_green_img.png")
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        p = pixels[x, y]
        pixels[x, y] = (p[0], p[1], 0, 255)
img.save("deleted_blue_img.png")