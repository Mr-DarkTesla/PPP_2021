import numpy as np
import pygame
from random import randint, choice
import copy

FPS = 60
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
GREY = (122, 122, 122)

RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 201, 31)
MAGENTA = (255, 3, 184)

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 204)

WIDTH, HEIGHT = SPACE = 800, 600
NUM_OF_EN = 4


class Game:
    """
    Game class
    """

    def __init__(self, screen):
        """
        Initialises game
        :param screen: screen
        """
        self.screen = screen
        self.shots = []
        self.targets = []
        self.clock = pygame.time.Clock()
        self.gun = Gun()
        self.finished = False
        for i in range(NUM_OF_EN):
            self.create_enemy()
        self.shot = choice(['Beam', 'Bomb'])

    def mainloop(self):
        """
        Main loop lol
        """
        pygame.init()
        while not self.finished:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gun.fire_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.fire()
                    self.gun.fire_end()
                    self.shot = choice(['Beam', 'Bomb'])
                elif event.type == pygame.MOUSEMOTION:
                    self.gun.targeting(pygame.mouse.get_pos())
            self.gun.power_up()

            for shot in self.shots:
                shot.move()
                shot.tick()
                if shot.live <= 0:
                    self.shots.remove(shot)
            for target in self.targets:
                for shot in self.shots:
                    if shot.hit_check(target, self.gun) == 'EOG':
                        self.finished = True
                    elif shot.hit_check(target, self.gun) and target.is_alive:
                        target.is_alive = False
                        self.targets.remove(target)
                        self.create_enemy()
                target.move(times_moved=FPS // 2)
            self.screen.fill(WHITE)
            for target in self.targets:
                target.draw()
            for shot in self.shots:
                shot.draw()
            self.gun.draw(shot=self.shot)
            pygame.display.update()

        pygame.quit()

    def fire(self):
        shot_velocity = {'x': self.gun.power * np.cos(self.gun.angle) / FPS * 20,
                         'y': - self.gun.power * np.sin(self.gun.angle) / FPS * 20}
        if self.shot == 'Beam':
            new_shot = Beam(self.gun.position, shot_velocity)
            self.shots.append(new_shot)
        elif self.shot == 'Bomb':
            shot_velocity['y'] *= -1
            new_shot = Bomb(self.gun.position, shot_velocity)
            self.shots.append(new_shot)

    def create_enemy(self):
        if choice(['Ball', 'Cube']) == 'Ball':
            self.targets.append(Ball())
        else:
            self.targets.append(Cube())


class Gun:
    """
    Actually gun. Stop him he has a gun!
    """
    def __init__(self):
        self.screen = window
        self.power = 0
        self.is_active = False
        self.angle = 0
        self.color = GREY
        self.r = 10
        self.position = {'x': WIDTH / 2, 'y': HEIGHT * 0.9}

    def fire_start(self):
        self.is_active = True
        self.power = 20

    def fire_end(self):
        self.is_active = False
        self.power = 20

    def targeting(self, position):
        """
        Mouse usage for aiming
        :param position: mouse position
        """
        position = {'x': position[0], 'y': position[1]}
        if position['y'] <= self.position['y']:
            if position['x'] - self.position['x'] != 0:
                tan = -(position['y'] - self.position['y']) / (position['x'] - self.position['x'])
                if tan >= 0:
                    self.angle = np.arctan(tan)
                else:
                    self.angle = np.pi + np.arctan(tan)
        elif 30 < position['x'] < WIDTH - 30:
            self.angle = np.pi / 2
            self.position['x'] = position['x']
        if self.is_active:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, shot):
        pygame.draw.circle(self.screen, BLACK, [self.position[i] for i in ['x', 'y']], self.r)
        if shot == 'Bomb':
            pygame.draw.line(self.screen, GREY, [self.position[i] for i in ['x', 'y']],
                             (self.position['x'] + np.cos(self.angle) * (self.power / 2 + 5),
                              self.position['y'] - np.sin(self.angle) * (self.power / 2 + 5)), 5)
        elif shot == 'Beam':
            pygame.draw.line(self.screen, RED, [self.position[i] for i in ['x', 'y']],
                             (self.position['x'] + np.cos(self.angle) * (self.power / 2 + 5),
                              self.position['y'] - np.sin(self.angle) * (self.power / 2 + 5)), 5)

    def power_up(self):
        if self.is_active and self.power < 200:
            self.power += 1


class Shot:
    def __init__(self, position, velocity, live, color=None, r=20):
        """
        All shots are the same...
        :param velocity: shot's velocity
        :param position: shot's position
        :param live: shot's livetime
        :param r: shot's radius
        :param color: ball's color
        """
        if color is None:
            color = (randint(0, 254), randint(0, 254), randint(0, 254))
        self.screen = window
        self.position = copy.copy(position)
        self.r = r
        self.velocity = copy.copy(velocity)
        self.live = live
        self.color = color

    def ricochet(self, reflect):
        """
        Ricochet added
        :param reflect: visual improvement parameter
        """
        touched_wall = self.position['x'] <= (self.r + 1) or self.position['x'] >= (WIDTH - self.r - 1)
        touched_floor = self.position['y'] <= (self.r + 1) or self.position['y'] >= (HEIGHT - self.r - 1)
        if touched_wall or touched_floor:
            if touched_wall:
                self.velocity['x'] = -(self.velocity['x'] * (1 - reflect))
            if self.position['y'] <= (self.r + 1) or self.position['y'] >= (HEIGHT - self.r - 1):
                self.velocity['y'] = -(self.velocity['x'] * (1 - reflect))
            return True
        else:
            return False

    def tick(self):
        """
        Timer for your life.
        """
        if self.live > 0:
            self.live -= 1


class Beam(Shot):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, 20)
        self.velocity = {'x': 0, 'y': 0}
        self.velocity['x'] = 1000 * velocity['x']
        self.velocity['y'] = 1000 * velocity['y']
        self.width = int(np.sqrt(velocity['y'] ** 2 + velocity['x'] ** 2) / 300) + 0.2

    def draw(self):
        pygame.draw.line(self.screen, self.color, [self.position[i] for i in ['x', 'y']],
                         (self.position['x'] + self.velocity['x'], self.position['y'] + self.velocity['y']), int(self.width * self.live))

    def move(self):
        pass

    def hit_check(self, obj, gun):
        """
        The function checks if the shot hits the target
        :param gun: gun
        :param obj: object
        """
        velocity_abs = np.sqrt(self.velocity['x'] ** 2 + self.velocity['y'] ** 2)
        hit_bool = np.abs(obj.position['x'] * self.velocity['y'] + (-self.velocity['x']) * obj.position['y']
                     - (self.velocity['y'] * gun.position['x'] - self.velocity['x'] * gun.position['y']))\
              / velocity_abs <= obj.r
        if hit_bool:
            return True
        else:
            return False


class Bomb(Shot):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, 100)
        self.live = 100
        self.velocity = {'x': 0, 'y': 0}
        self.velocity['x'] = (.7 * velocity['x'])
        self.velocity['y'] = (.7 * velocity['y'])

    def move(self, reflect=0, times_moved=1):
        """
        Shot's moving

        :param reflect: energy loss parameter
        :param times_moved: visible velocity
        """
        if self.live > 5:
            for i in range(times_moved):
                self.velocity['y'] -= 0.5  # gravity
                if self.ricochet(reflect):
                    self.position['x'] += self.velocity['x'] / (1 - 1.1 * reflect)
                    self.position['y'] -= self.velocity['y'] / (1 - 1.1 * reflect)
                else:
                    self.position['x'] += self.velocity['x']
                    self.position['y'] -= self.velocity['y']

    def hit_check(self, obj, gun):
        """
        The function checks whether the shot hits the aim or gun
        :param gun: gun
        :param obj: target
        """
        hit_gun = (self.position['x'] - gun.position['x']) ** 2 + \
                  (self.position['y'] - gun.position['y']) ** 2 <= self.r ** 2
        hit_enemy = (self.position['x'] - obj.position['x']) ** 2 + \
                    (self.position['y'] - obj.position['y']) ** 2 <= (self.r + obj.r) ** 2
        if hit_gun and self.live < 10:
            return 'EOG'
        if hit_enemy:
            if self.live > 10:
                self.live = 10
            return True
        else:
            return False

    def draw(self):
        r = self.r
        if self.live <= 10:
            self.r = r + 2 * (10 - self.live)
            pygame.draw.circle(self.screen, ORANGE, [self.position[i] for i in ['x', 'y']], self.r)
        else:
            pygame.draw.circle(self.screen, BLACK, [self.position[i] for i in ['x', 'y']], self.r - 6)


class Enemy:
    """
    Initializes a target, controls its parameters
    """
    def __init__(self):
        self.r = randint(10, 30)
        self.position = {'x': randint(self.r, WIDTH - self.r), 'y': randint(self.r, HEIGHT * 0.75 - self.r)}
        self.color = RED
        self.is_alive = True
        self.screen = window
        self.velocity = {'x': randint(-10, 10) / FPS, 'y': randint(-10, 10) / FPS}

    def ricochet(self):
        """
        Checks if the target touches the walls and reflect if needed
        """
        touched_wall = self.position['x'] <= (self.r + 1) or self.position['x'] >= (WIDTH - self.r - 1)
        touched_floor = self.position['y'] <= (self.r + 1) or self.position['y'] >= (HEIGHT * 3/4)
        if touched_wall:
            self.velocity['x'] = - self.velocity['x']
        if touched_floor:
            self.velocity['y'] = - self.velocity['y']

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.position[i] for i in ['x', 'y']], self.r)


class Cube(Enemy):
    def __init__(self):
        super().__init__()
        pass

    def draw(self):
        pygame.draw.rect(self.screen, GREEN,
                         (self.position['x'] - self.r, self.position['y'] - self.r, self.r * 2, self.r * 2))

    def move(self, times_moved=30):
        for i in range(times_moved):
            self.ricochet()
            for j in ['x', 'y']:
                self.position[j] -= self.velocity[j]


class Ball(Enemy):
    def __init__(self):
        super().__init__()


    def draw(self):
        pygame.draw.circle(self.screen, YELLOW, [self.position[i] for i in ['x', 'y']], self.r)


    def move(self, reflect=0, times_moved=30):
        """
        Moves the ball according to its velocity and position

        :param reflection_cut: part of velocity value cut by single reflection
        :param times_moved: stands for visible velocity of the ball
        """
        for i in range(times_moved):
            self.velocity['y'] -= (1.2 / times_moved / FPS)
            if self.ricochet():
                self.position['x'] += self.velocity['x'] / (1 - reflect)
                self.position['y'] -= self.velocity['y'] / (1 - reflect)
            else:
                self.position['x'] += self.velocity['x']
                self.position['y'] -= self.velocity['y']


window = pygame.display.set_mode(SPACE)
game = Game(window)
game.mainloop()