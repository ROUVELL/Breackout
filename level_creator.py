import pygame as pg
from random import choice

from brick import Brick
from ball import Ball
from group import Group
from config import WIDTH, HEIGHT, PADLE_HEIGHT, BRICK_COLORS


class LevelCreator:
    def __init__(self, bricks: Group, balls: Group):
        self._bricks = bricks
        self._balls = balls

    def _get_level_size(self, brick_size, ox, oy, dx, dy):
        w, h = brick_size
        w += dx
        h += dy  # 25
        size = ((WIDTH - ox) // w, ((HEIGHT - PADLE_HEIGHT - 20 - oy) // h))
        return size

    def _get_brick_size(self, level_size, ox, oy, dx, dy):
        cols, rows = level_size
        w, h = (WIDTH - ox) // cols, (HEIGHT - PADLE_HEIGHT - 20 - oy) // rows
        return (w - dx, h - dy)

    def new(self, brick_size=None, level_size=None, ox=5, oy=30, dx=5, dy=5):
        # TODO: Вичисляти розмір плитки від розміру левела якщо він не переданий і навпаки

        assert (brick_size or level_size), 'Відсутній один із важливих параметрів'

        w, h = brick_size if brick_size else self._get_brick_size(level_size, ox, oy, dx, dy)
        cols, rows = level_size if level_size else self._get_level_size(brick_size, ox, oy, dx, dy)

        print(cols, rows)
        end_x, step_x = ((w + dx) * cols) + ox, w + dx
        end_y, step_y = ((h + dy) * rows) + oy, h + dy

        self._bricks.add(*[Brick(pos=(x, y), size=(w, h), group=self._bricks, color=choice(BRICK_COLORS))
                           for x in range(ox, end_x, step_x)
                           for y in range(oy, end_y, step_y)])

        self._balls.add(Ball((choice([-3, -2, 2, 3]), choice([-2, -3])), group=self._balls))
        # self._padle.rect.centralize

    def add_ball(self):
        direction = (choice([-3, -2, 2, 3]), choice([-3, -2, 2, 3]))
        pos = self._balls.last.rect.center
        self._balls.add(Ball(direction, pos, group=self._balls))