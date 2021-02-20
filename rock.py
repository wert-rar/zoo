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
# scroll of screen
WINDOW_SPEED = 1
PLAYER_SPEED = 10
ROCK_SPEED = PLAYER_SPEED * 8

PLAYER_D = 60
# I use illusion of moving so we get  something like the speed of convergence
# since the player is not moving, this value will be the speed of the ball
ROCK_SPEED = ROCK_SPEED if (ROCK_SPEED - PLAYER_SPEED < 0) else ROCK_SPEED - PLAYER_SPEED
ROCK_SPEED /= 100
PLAYER_SPEED /= 100
# -----------------------------------

get_x: Callable[[int, int], int] = lambda x, d: round(math.tan(math.radians(d)) * x)


class Bar:
    def __init__(self, color, x, y, h, w):
        self.h = h
        self.w = w
        self.y = y
        self.x = x
        self.color = color

    def draw(self):
        self.y -= WINDOW_SPEED
        if self.y < 10:
            self.y = HEIGHT
        rect = pg.Rect(self.x, self.y, self.w, self.h)
        pg.draw.rect(screen, self.color, rect)


class Rock:
    def __init__(self, color, x, y, r, speed):
        self.speed = speed
        self.r = r
        self.y = y
        self.x = x
        self.color = color

    def move(self):
        self.y += self.speed
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def collision(self, player):
        if self.x - self.r <= player.x <= self.x + self.r and self.y - self.r <= player.y <= self.y + self.r:
            return True
        return False


class Player:
    def __init__(self, color, x, y, speed, d=None):
        if d is None:
            self.d = random.randrange(0, 180)
        else:
            self.d = d
        self.x_add = get_x(speed*100, self.d) / 100
        print(self.x_add)
        self.y = y
        self.x = x
        self.color = color

    def draw(self):
        self.x += self.x_add
        rect = pg.Rect(self.x, self.y, 10, 10)
        pg.draw.rect(screen, self.color, rect)  # draw laser


def main():
    # start vars
    running = True
    x, y = 500, 10
    # gives the effect of movement by moving in the opposite direction
    bar = Bar(colors[4], 0, 0, 10, WIDTH)

    player = Player(colors[6], x, y + 500, PLAYER_SPEED,PLAYER_D)
    rock = Rock(colors[0], x, y, 100, ROCK_SPEED)
    del x, y

    # mainloop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # update screen
        screen.fill((0, 255, 0))
        bar.draw()
        player.draw()
        rock.move()
        # check who win
        if rock.collision(player):
            print('Rock WiN')
            running = False
        if player.x > 500+rock.r or player.x < 500 - rock.r:
            print('PLayer WiN')
            running = False

        pg.display.flip()
    pg.quit()


main()
