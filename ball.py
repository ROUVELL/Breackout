import pygame as pg

from config import *


class Ball:
    def __init__(self, direction):
        self.rect = pg.Rect((0, 0), (BALL_DIAMETR, BALL_DIAMETR))
        self.rect.center = BALL_START_POS
        self.color = 'red'
        self.direction = pg.Vector2(direction)

    def update(self, direction: pg.Vector2):
        self.direction = direction
        self.rect.move_ip(self.direction)

        # screen collision
        if self.rect.top < 0:
            self.direction.y = -self.direction.y
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction.x = -self.direction.x

    def draw(self, sc: pg.Surface):
        pg.draw.circle(sc, self.color, self.rect.center, BALL_DIAMETR // 2)