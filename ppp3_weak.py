import pygame
from pygame.draw import *

pygame.init()


FPS = 30
screen = pygame.display.set_mode((600, 1000))

rect(screen, (0, 255, 255), (0, 0, 600, 450))
rect(screen, (0, 255, 0), (0, 450, 600, 550))

circle(screen, (255, 222, 84), (550, 200), 120)

rect(screen, (231, 231, 231), (70, 565, 30, 150))
ellipse(screen, (0, 129, 0), (25, 490, 120, 80))
ellipse(screen, (0, 129, 0), (-15, 425, 200, 85))
ellipse(screen, (0, 129, 0), (20, 320, 130, 145))
circle(screen, (255, 205, 171), (10, 468), 13)
circle(screen, (255, 205, 171), (170, 468), 13)
circle(screen, (255, 205, 171), (125, 378), 13)
circle(screen, (255, 205, 171), (133, 542), 13)


ellipse(screen, (255, 255, 255), (270, 600, 200, 100))  # ���� � ����
rect(screen, (255, 255, 255), (290, 680, 20, 90))
rect(screen, (255, 255, 255), (325, 680, 20, 80))
rect(screen, (255, 255, 255), (400, 680, 20, 90))
rect(screen, (255, 255, 255), (430, 680, 20, 80))

ellipse(screen, (255, 255, 255), (400, 510, 70, 165))  # ������
ellipse(screen, (255, 255, 255), (430, 505, 85, 43))
circle(screen, (230, 129, 171), (460, 520), 9)
circle(screen, (0, 0, 0), (458, 518), 4)
polygon(screen, (234, 177, 176), ([425, 513], [435, 405], [445, 513]))

ellipse(screen, (222, 177, 234), (385, 510, 65, 20))  # �����
ellipse(screen, (222, 177, 234), (383, 512, 65, 20))
ellipse(screen, (255, 239, 171), (382, 525, 60, 18))
ellipse(screen, (255, 239, 171), (362, 565, 55, 23))
ellipse(screen, (244, 216, 228), (372, 545, 52, 23))
ellipse(screen, (176, 234, 222), (350, 575, 52, 23))
ellipse(screen, (234, 177, 176), (350, 585, 55, 20))
ellipse(screen, (234, 177, 176), (380, 535, 60, 23))

ellipse(screen, (234, 177, 176), (255, 615, 60, 23))  # �����
ellipse(screen, (214, 177, 176), (245, 620, 55, 20))
ellipse(screen, (255, 239, 171), (200, 670, 63, 30))
ellipse(screen, (222, 177, 234), (235, 650, 65, 20))
ellipse(screen, (255, 239, 171), (240, 660, 60, 18))
ellipse(screen, (255, 239, 171), (235, 627, 55, 23))
ellipse(screen, (244, 216, 228), (210, 640, 62, 33))
ellipse(screen, (176, 234, 222), (235, 670, 32, 23))
ellipse(screen, (200, 177, 176), (240, 680, 60, 23))
ellipse(screen, (176, 234, 222), (245, 670, 55, 23))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()