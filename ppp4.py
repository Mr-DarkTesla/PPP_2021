import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen_width, screen_height = space = (800, 800)
screen = pygame.display.set_mode(space)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def pif(pos, ball):
    """
    Theorem pif
    :pos: tuple with x and y params
    :ball: ball
    :return: Bool
    """
    return (pos[0] - ball['x']) ** 2 + (pos[1] - ball['y']) ** 2 <= ball['r'] ** 2


def draw_balls():
    """
    Draw balls
    :return: None
    """
    for ball in BALLS:
        circle(screen, ball['c'], (ball['x'], ball['y']), ball['r'])
    for super_ball in SUPER_BALLS:
        for i in range(4):
            circle(screen, super_ball['c'][i], (super_ball['x'], super_ball['y']), super_ball['r'] - i * 20)


def gen_ball():
    """
    Generates parameters of a ball
    :return: parameters of a ball
    """
    ball = {}
    ball['r'] = ball_radius = randint(30, 80)
    ball['x'] = randint(ball_radius, screen_width - ball_radius)
    ball['y'] = randint(ball_radius, screen_height - ball_radius)
    ball['c'] = COLORS[randint(0, len(COLORS) - 1)]
    ball['xv'], ball['yv'] = randint(-100, 100) / 100, randint(-100, 100) / 100
    return ball


def gen_super_ball():
    """
    Generates parameters of a super ball
    :return: parameters for drawing a super ball
    """
    super_ball = {}
    super_ball['r'] = super_ball_radius = randint(80, 100)
    super_ball['x'] = randint(super_ball_radius, screen_width - super_ball_radius)
    super_ball['y'] = randint(super_ball_radius, screen_height - super_ball_radius)
    super_ball['c'] = (RED, BLUE, YELLOW, GREEN)
    super_ball['xv'], super_ball['yv'] = randint(-100, 100) / 100, randint(-100, 100) / 100
    return super_ball


def define_ball(possibility):
    """
    Defines which type of ball is to generate
    :param possibility: possibility (in %) of generating a super ball
    :return:
    """
    var = randint(1, 101)
    if var <= possibility:
        create_super_ball()
    else:
        create_ball()


def create_ball():
    """
    Creates a new ball
    :return:
    """
    BALLS.append(gen_ball())


def create_super_ball():
    """
    Creates a new super ball
    :return:
    """
    SUPER_BALLS.append(gen_super_ball())


def erase_definer(position):
    """
    Checks whether mouse clicked on an object or not.
    If yes, erases the object and adds some scores.
    Otherwise, takes away 10 points from player's scores.
    :param position: Position of the mouse when clicked on the surface
    :return: How many scores should be added
    """
    inner_counter = 0
    mouse_x = position[0]
    mouse_y = position[1]
    for ball in BALLS:
        if pif((mouse_x, mouse_y), ball):
            BALLS.remove(ball)
            inner_counter += (80 - ball['r']) + 1
            define_ball(super_ball_possibility)
    for super_ball in SUPER_BALLS:
        if pif((mouse_x, mouse_y), super_ball):
            SUPER_BALLS.remove(super_ball)
            inner_counter += 200
            define_ball(super_ball_possibility)
    if inner_counter == 0:
        inner_counter -= 20
    return inner_counter


def move_balls(times_moved):
    """
    Moves every ball according their position and velocity
    :param times_moved: indicates the speed of time
    :return:
    """
    for time in range(times_moved):
        for ball in BALLS:
            if ball['x'] <= ball['r'] + 1 or ball['x'] >= screen_width - (ball['r'] + 1):
                ball['xv'] *= -1
            elif ball['y'] <= ball['r'] + 1 or ball['y'] >= screen_height - (ball['r'] + 1):
                ball['yv'] *= -1
            ball['x'] += ball['xv']
            ball['y'] += ball['yv']


def move_super_balls(times_moved):
    """
    Moves a super ball according its position and velocity
    :param times_moved: indicates the speed of time
    :return:
    """
    for super_ball in SUPER_BALLS:
        if super_ball['r'] != 0:
            super_ball['r'] -= 1
        else:
            SUPER_BALLS.remove(super_ball)
            create_ball()
    for time in range(times_moved):
        for ball in SUPER_BALLS:
            if ball['x'] <= ball['r'] + 1 or ball['x'] >= screen_width - (ball['r'] + 1):
                ball['xv'] *= -1
            elif ball['y'] <= ball['r'] + 1 or ball['y'] >= screen_height - (ball['r'] + 1):
                ball['yv'] *= -1
            ball['x'] += ball['xv']
            ball['y'] += ball['yv']


number_of_balls = 4
BALLS = [gen_ball() for i in range(number_of_balls)]
SUPER_BALLS = []
# There was time when i realised that i could use classes to make code shorter and more flexible
# Well yess, but im too laze to improve this code cause it is working...
super_ball_possibility = 20
time_speed = 10
scores = 0
scores_counter_position = (30, 30)
play_time = 30000

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    if pygame.time.get_ticks() >= play_time:
        finished = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            scores += erase_definer(mouse_position)

    move_balls(time_speed)
    move_super_balls(time_speed * 2)

    # View
    screen.fill(BLACK)
    text = pygame.font.Font(None, 36)
    scores_counter = text.render(str(scores), True, WHITE)
    screen.blit(scores_counter, scores_counter_position)
    draw_balls()

    pygame.display.update()

pygame.quit()