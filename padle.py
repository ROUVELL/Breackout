import pygame as pg

from config import *


class Padle:
    def __init__(self):
        self.rect = pg.Rect((0, 0), PADLE_SIZE)
        self.rect.center = PADLE_POS
        self.color = 'white'

    def kill(self):
        # TODO: Костиль!!!ф
        pass

    def update(self):
        dx = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_a]: dx -= 4
        if keys[pg.K_d]: dx += 4

        self.rect.move_ip(dx, 0)

        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(WIDTH, self.rect.right)


    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, self.color, self.rect, border_radius=5)