import pygame as pg

from group import Group
from config import *


class Ball:
    def __init__(self, direction: tuple, pos: tuple = BALL_START_POS, *, group: Group):
        self.group = group
        ##########
        self.rect = pg.Rect(pos, (BALL_DIAMETR, BALL_DIAMETR))
        self.direction = pg.Vector2(direction)

    def kill(self):
        self.group.remove(self)

    def change_direction(self, *, x=None, y=None):
        if x: self.direction.x = -self.direction.x
        if y: self.direction.y = -self.direction.y

    def update(self, dt: float):
        self.rect.move_ip(self.direction * dt)

    def draw(self, sc: pg.Surface):
        pg.draw.circle(sc, 'red', self.rect.center, BALL_DIAMETR // 2)