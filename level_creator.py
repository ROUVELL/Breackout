import pygame as pg
from random import choice

from brick import Brick
from ball import Ball
from group import Group
from config import *


class LevelCreator:
    def __init__(self, bricks: Group, balls: Group):
        self._bricks = bricks
        self._balls = balls

    def new(self, *positions):
        def get_pos(ix, iy):  # з двох індексів отримуємо (х,у), по-моєму тупа реалізація
            x, y = (ix * (BRICK_WIDTH + DX)) + SIDE_OFFSET, (iy * (BRICK_HEIGHT + DY)) + YOFFSET
            return x, y

        # якщо нічого не передали - заповнюємо левел повністью
        if not positions:
            positions = [(i, j) for i in range(MAX_COLS) for j in range(MAX_ROWS)]

        self._bricks.add(*[Brick(pos=get_pos(ix, iy), group=self._bricks)
                           for ix, iy in positions])

        self._balls.add(Ball((choice([-3, -2, 2, 3]), choice([-2, -3])), group=self._balls))
        # self._padle.rect.centralize

    def add_ball(self):
        direction = (choice([-3, -2, 2, 3]), choice([-3, -2, 2, 3]))
        pos = self._balls.last.rect.center
        self._balls.add(Ball(direction, pos, group=self._balls))