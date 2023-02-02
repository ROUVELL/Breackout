import pygame as pg

from config import PADLE_SIZE, PADLE_POS, PADLE_SPEED


class Padle:
    def __init__(self):
        self.rect = pg.Rect((0, 0), PADLE_SIZE)
        self.rect.center = PADLE_POS
        self.color = 'white'
        self.speed = PADLE_SPEED

    def update(self, dt: float):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]: self.rect.move_ip(-self.speed * dt, 0)
        if keys[pg.K_d]: self.rect.move_ip(self.speed * dt, 0)

    def draw(self, sc: pg.Surface):
        pg.draw.rect(sc, self.color, self.rect, border_radius=5)