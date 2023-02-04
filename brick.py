import pygame as pg
from random import choice, random

from group import Group
from config import BRICK_SIZE, BRICK_COLORS


class Brick:
    def __init__(self, pos: tuple, *, group: Group):
        self.group = group
        #########
        self.rect = pg.Rect(pos, BRICK_SIZE)
        self.color = choice(BRICK_COLORS)
        self.score_value = 3 if random() >= .91 else 2 if random() >= .85 else 1

    def kill(self):
        self.group.remove(self)
        return self.score_value

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, self.color, self.rect, border_radius=5)
