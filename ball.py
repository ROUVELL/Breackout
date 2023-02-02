import pygame as pg

from config import *


class Ball:
    def __init__(self, direction):
        self.rect = pg.Rect((0, 0), (BALL_DIAMETR, BALL_DIAMETR))
        self.rect.center = BALL_START_POS
        self.color = 'red'
        self.direction = pg.Vector2(direction)

    def change_direction(self, *, x=False, y=False):
        if x: self.direction.x = -self.direction.x
        if y: self.direction.y = -self.direction.y

    def change_speed(self, sx=0, sy=0):
        self.direction += pg.Vector2(sx, sy)

    def update(self):
        self.rect.move_ip(self.direction)

    def draw(self, sc: pg.Surface):
        pg.draw.circle(sc, self.color, self.rect.center, BALL_DIAMETR // 2)