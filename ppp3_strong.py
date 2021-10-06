import pygame
from pygame.draw import *

import png
import numpy as np


def load_png(file_path):
    """
    Read from KITTI .png file
    Args:
        file_path string: file path(absolute)
    Returns:
        data (numpy.array): data of image in (Height, Width, 3) layout
    """
    flow_object = png.Reader(filename=file_path)
    flow_direct = flow_object.asDirect()
    flow_data = list(flow_direct[2])
    (w, h) = flow_direct[3]['size']

    flow = np.zeros((h, w, 4), dtype=np.float64)
    for i in range(len(flow_data)):
        flow[i, :, 0] = flow_data[i][0::4]
        flow[i, :, 1] = flow_data[i][1::4]
        flow[i, :, 2] = flow_data[i][2::4]
        flow[i, :, 3] = flow_data[i][2::4]

    #invalid_idx = (flow[:, :, 2] == 0)
    #flow[:, :, 0:2] = (flow[:, :, 0:2] - 2 ** 15) / 64.0
    #flow[invalid_idx, 0] = 0
    #flow[invalid_idx, 1] = 0

    return flow.astype(np.float32)


path = "C:\Root\Downloads\Arts\Stuff\pic_1.png"
img = load_png(path)
print(img.shape)

pygame.init()
FPS = 1
screen = pygame.display.set_mode((800, 1200))


for x in range(len(img)):
    for y in range(len(img[x])):
        color = tuple(img[x][y])
        line(screen, color, (y, x), (y, x))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()