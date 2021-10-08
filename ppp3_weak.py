import pygame
from pygame.draw import *

# Useful colors
red = (255, 0, 0)
green = (0, 255, 0)
light_green = (0, 129, 0)
black = (0, 0, 0)
blue = (50, 255, 255)
white = (255, 255, 255)
grey = (230, 230, 230)
yellow = (255, 222, 84)
pink1 = (234, 177, 176)
pink2 = (222, 177, 234)
pink3 = (255, 239, 171)
pink4 = (244, 216, 228)
pink5 = (176, 234, 222)
pink6 = (214, 177, 176)
eye = (230, 129, 171)
fruity = (255, 205, 171)

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 1000))


def end():
    """
    End of drawing
    :return: None
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()


def draw_bg(scale=1.):
    """
    Drawing of the background
    :param scale: resize param
    :return: None
    """
    h = scale * 450
    rect(screen, blue, (0, 0, 600, h))
    rect(screen, green, (0, h, 600, 1000 - h))


def draw_sun(coords=(0, 0), scale=1.):
    """
    Drawing the sun
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    circle(screen, yellow, (x0 + scale * 550, y0 + scale * 200), 120 * scale)


def draw_tree(coords=(0, 0), scale=1.):
    """
    Drawing the tree
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    rect(screen, grey, (x0 + scale * 70, y0 + scale * 565, 30 * scale, 150 * scale))
    ellipse(screen, light_green, (x0 + scale * 25, y0 + scale * 490, 120 * scale, 80 * scale))
    ellipse(screen, light_green, (x0 + scale * -15, y0 + scale * 425, 200 * scale, 85 * scale))
    ellipse(screen, light_green, (x0 + scale * 20, y0 + scale * 320, 130 * scale, 145 * scale))
    circle(screen, fruity, (x0 + scale * 10, y0 + scale * 468), 13 * scale)
    circle(screen, fruity, (x0 + scale * 170, y0 + scale * 468), 13 * scale)
    circle(screen, fruity, (x0 + scale * 125, y0 + scale * 378), 13 * scale)
    circle(screen, fruity, (x0 + scale * 133, y0 + scale * 542), 13 * scale)


def draw_unicorn_body(coords=(0, 0), scale=1.):
    """
    Drawing body
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    ellipse(screen, white, (x0 + scale * 270, y0 + scale * 600, scale * 200, scale * 100))
    rect(screen, white, (x0 + scale * 290, y0 + scale * 680, scale * 20, scale * 90))
    rect(screen, white, (x0 + scale * 325, y0 + scale * 680, scale * 20, scale * 80))
    rect(screen, white, (x0 + scale * 400, y0 + scale * 680, scale * 20, scale * 90))
    rect(screen, white, (x0 + scale * 430, y0 + scale * 680, scale * 20, scale * 80))


def draw_unicorn_head(coords=(0, 0), scale=1.):
    """
    Drawing head
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    ellipse(screen, white, (x0 + scale * 400, y0 + scale * 510, scale * 70, scale * 165))
    ellipse(screen, white, (x0 + scale * 430, y0 + scale * 505, scale * 85, scale * 43))
    circle(screen, eye, (x0 + scale * 460, y0 + scale * 520), scale * 9)
    circle(screen, black, (x0 + scale * 458, y0 + scale * 518), scale * 4)
    polygon(screen, pink1, (
    [x0 + scale * 425, y0 + scale * 513], [x0 + scale * 435, y0 + scale * 405], [x0 + scale * 445, y0 + scale * 513]))


def draw_unicorn_hair(coords=(0, 0), scale=1.):
    """
        Drawing hair
        :param coords: position of the top left corner of the pic
        :param scale: resize param
        :return: None
        """
    x0, y0 = coords
    ellipse(screen, pink2, (x0 + scale * 385, y0 + scale * 510, scale * 65, scale * 20))
    ellipse(screen, pink2, (x0 + scale * 383, y0 + scale * 512, scale * 65, scale * 20))
    ellipse(screen, pink3, (x0 + scale * 382, y0 + scale * 525, scale * 60, scale * 18))
    ellipse(screen, pink3, (x0 + scale * 362, y0 + scale * 565, scale * 55, scale * 23))
    ellipse(screen, pink4, (x0 + scale * 372, y0 + scale * 545, scale * 52, scale * 23))
    ellipse(screen, pink5, (x0 + scale * 350, y0 + scale * 575, scale * 52, scale * 23))
    ellipse(screen, pink1, (x0 + scale * 350, y0 + scale * 585, scale * 55, scale * 20))
    ellipse(screen, pink1, (x0 + scale * 380, y0 + scale * 535, scale * 60, scale * 23))


def draw_unicorn_tail(coords=(0, 0), scale=1.):
    """
    Drawing tail
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    x0, y0 = coords
    ellipse(screen, pink1, (x0 + scale * 255, y0 + scale * 615, scale * 60, scale * 23))
    ellipse(screen, pink6, (x0 + scale * 245, y0 + scale * 620, scale * 55, scale * 20))
    ellipse(screen, pink3, (x0 + scale * 200, y0 + scale * 670, scale * 63, scale * 30))
    ellipse(screen, pink2, (x0 + scale * 235, y0 + scale * 650, scale * 65, scale * 20))
    ellipse(screen, pink3, (x0 + scale * 240, y0 + scale * 660, scale * 60, scale * 18))
    ellipse(screen, pink3, (x0 + scale * 235, y0 + scale * 627, scale * 55, scale * 23))
    ellipse(screen, pink4, (x0 + scale * 210, y0 + scale * 640, scale * 62, scale * 33))
    ellipse(screen, pink5, (x0 + scale * 235, y0 + scale * 670, scale * 32, scale * 23))
    ellipse(screen, pink6, (x0 + scale * 240, y0 + scale * 680, scale * 60, scale * 23))
    ellipse(screen, pink5, (x0 + scale * 245, y0 + scale * 670, scale * 55, scale * 23))


def draw_unicorn(coords=(0, 0), scale=1.):
    """
    Drawing the f*king unicorn waifu
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    draw_unicorn_body(coords=coords, scale=scale)
    draw_unicorn_head(coords=coords, scale=scale)
    draw_unicorn_hair(coords=coords, scale=scale)
    draw_unicorn_tail(coords=coords, scale=scale)


def draw_pic(coords=(0, 0), scale=1.):
    """
    Drawing the picture
    :param coords: position of the top left corner of the pic
    :param scale: resize param
    :return: None
    """
    draw_bg(scale=scale)
    draw_sun(coords=coords, scale=scale)
    draw_tree(coords=coords, scale=scale)
    draw_unicorn(coords=coords, scale=scale)
    end()


draw_pic()