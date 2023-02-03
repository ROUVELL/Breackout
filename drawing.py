import pygame as pg

from padle import Padle
from group import Group
from config import BG


class Drawing:
    def __init__(self, clock: pg.time.Clock, padle: Padle, bricks: Group, balls: Group):
        self._sc = pg.display.get_surface()
        self._clock = clock
        #######
        self._padle = padle
        self._bricks = bricks
        self._balls = balls
        #######
        self._font = pg.font.SysFont('calibri', 26)

    def _fps(self):
        fps = f'{self._clock.get_fps(): .1f}'
        text = self._font.render(fps, True, 'grey')
        self._sc.blit(text, (0, 0))

    def all(self):
        self._sc.fill(BG)
        self._bricks.draw(self._sc)
        self._padle.draw(self._sc)
        self._balls.draw(self._sc)
        self._fps()
        self._sc.blit(self._font.render(f'Bricks: {len(self._bricks)}', True, 'grey'), (80, 0))
        pg.display.flip()