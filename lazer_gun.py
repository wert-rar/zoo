import math
import random
from typing import Any, Callable

import pygame as pg

pg.init()
# --------set screen---------------
HEIGHT, WIDTH = 1000, 1000
screen = pg.display.set_mode([HEIGHT, WIDTH])  # setup screen
colors = [
    (0, 216, 255),  # light  blue
    (0, 0, 255),  # blue
    (153, 255, 170),  # light green
    (0, 255, 0),  # green
    (254, 254, 0),  # yellow
    (255, 134, 0),  # orange
    (255, 0, 0),  # red
    (235, 0, 209),  # magenta
    (255, 157, 255),  # pink
]


# -----------------------------------
get_y: Callable[[int, int], int] = lambda x, d: round(math.tan(math.radians(d)) * x)


def get_d(n):
    ds = []
    while len(ds) != n:
        d = random.randrange(30, 270)
        if ds.count(d) == 0:
            ds.append(d)

    return ds


class Bar:
    def __init__(self, color, x, y, r):
        self.r = r
        self.y = y
        self.x = x
        self.color = color

    def draw(self):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)


# TODO: draw one line instead of many short lines
class Laser:
    def __init__(self, color, x, y, speed, d=None):
        self.speed = speed
        if d is None:
            self.d = random.randrange(1, 180)
        else:
            self.d = d
        self.y_add = get_y(speed, self.d)
        self.y = y
        self.x = x
        self.color = color

    # check collision with target or block
    def collision(self, b):
        if b.x - b.r <= self.x <= b.x + b.r and b.y - b.r <= self.y <= b.y + b.r:
            return True
        return False

    # check collision with walls
    @staticmethod
    def calculate_coord(c_x, c_y, x, y):
        if c_x < 5 or c_x > WIDTH - 5:  x = -x
        if c_y < 5 or c_y > HEIGHT - 5:  y = -y
        return x, y

    def draw(self):
        self.speed, self.y_add = Laser.calculate_coord(self.x, self.y, self.speed, self.y_add)
        # find second pos
        x_2 = self.x + self.speed
        y_2 = self.y + self.y_add

        pg.draw.line(screen, self.color, (self.x, self.y), (x_2, y_2), 2)  # draw laser
        # save end pos like new start pos
        self.x = x_2
        self.y = y_2


def main():
    # start vars
    running = True
    screen.fill((255, 255, 255))
    x, y = 300, 20  # lasers go from one gun
    # create lasers with different angles
    ds = get_d(len(colors))
    lasers = [Laser(color, x, y, 10, d=d) for color, d in zip(colors, ds)]
    # blocks
    bars = [Bar(colors[0], x + 100, 250, 10)
            ]
    for bar in bars:
        bar.draw()

    # clear mem
    del x, y, ds
    # target
    tar = Bar((0, 255, 0), 300, 300, 10)
    tar.draw()
    # mainloop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        for laser in lasers:
            l = laser
            for bar in bars:
                if l.collision(bar):
                    lasers.remove(l)
            l.draw()
        pg.display.flip()
    pg.quit()


main()
