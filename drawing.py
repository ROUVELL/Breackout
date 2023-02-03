import pygame as pg

from padle import Padle
from group import Group
from timer import TimerGroup
from config import BG, CENTER


class Drawing:
    def __init__(self, clock: pg.time.Clock, padle: Padle, bricks: Group, balls: Group, timers: TimerGroup):
        self._sc = pg.display.get_surface()
        self._clock = clock
        #######
        self._padle = padle
        self._bricks = bricks
        self._balls = balls
        self._timers = timers
        #######
        self._font = pg.font.SysFont('calibri', 26)
        self._font2 = pg.font.SysFont('calibri', 36)

    def _time_to_restart(self):
        if self._timers.is_active('restart_timer'):
            time = f"{self._timers.get_remaining_time('restart_timer') / 1000 : .2f}"
            render = self._font2.render(f'Time to restart: {time}', True, 'white')
            self._sc.blit(render, render.get_rect(center=CENTER))

    def _bricks_count(self):
        render = self._font.render(f'Bricks: {len(self._bricks)}', True, 'grey')
        self._sc.blit(render, (80, 0))

    def _fps(self):
        fps = f'{self._clock.get_fps(): .1f}'
        text = self._font.render(fps, True, 'grey')
        self._sc.blit(text, (0, 0))

    def all(self):
        self._sc.fill(BG)
        self._bricks.draw(self._sc)
        self._padle.draw(self._sc)
        self._balls.draw(self._sc)
        self._time_to_restart()
        self._bricks_count()
        self._fps()
        pg.display.flip()