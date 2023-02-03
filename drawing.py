import pygame as pg

from padle import Padle
from group import Group
from timer import TimerGroup
from config import BG, CENTER, HALF_WIDTH, HALF_HEIGHT


class Drawing:
    def __init__(self, breakout, clock: pg.time.Clock, padle: Padle, bricks: Group, balls: Group, timers: TimerGroup):
        self._sc = pg.display.get_surface()
        self._breakout = breakout
        self._clock = clock
        #######
        self._padle = padle
        self._bricks = bricks
        self._balls = balls
        self._timers = timers
        #######
        self._font = pg.font.SysFont('calibri', 26)
        self._font2 = pg.font.SysFont('calibri', 36)

    def _text(self, text: str, pos: tuple | pg.Rect, font: pg.font.FontType, *, centralize=False):
        render = font.render(text, True, 'white')
        if centralize:
            self._sc.blit(render, render.get_rect(center=pos))
            return
        self._sc.blit(render, pos)

    def _time_to_restart(self):
        if self._timers.is_active('restart_timer'):
            if self._breakout.is_win:
                self._text('VICTORY!', CENTER, self._font2, centralize=True)
            if self._breakout.is_loss:
                self._text('DEFEAT!', CENTER, self._font2, centralize=True)
            time = f"{self._timers.get_remaining_time('restart_timer') / 1000 : .2f}"
            self._text(f'Time to restart: {time}', (HALF_WIDTH, HALF_HEIGHT + 26), self._font, centralize=True)

    def _bricks_count(self):
        self._text(f'Bricks: {len(self._bricks)}', (80, 0), self._font)

    def _fps(self):
        fps = f'{self._clock.get_fps(): .1f}'
        self._text(fps, (0, 0), self._font)

    def all(self):
        self._sc.fill(BG)
        self._bricks.draw(self._sc)
        self._padle.draw(self._sc)
        self._balls.draw(self._sc)
        self._time_to_restart()
        self._bricks_count()
        self._fps()
        pg.display.flip()