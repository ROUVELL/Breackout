import pygame as pg

from group import Group
from config import *


class Brick:
    def __init__(self, pos: tuple, size: tuple, color: str, *, group: Group):
        self.group = group
        #########
        self.rect = pg.Rect((0, 0), size)
        self.rect.center = pos
        self.color = color

    def kill(self):
        self.group.remove(self)

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, self.color, self.rect, border_radius=5)