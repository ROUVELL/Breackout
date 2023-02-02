import pygame as pg
from random import choice

from brick import Brick
from padle import Padle
from ball import Ball
from group import Group
from collision_system import CollisionSystem
from config import *


class Breackout:
    def __init__(self, game):
        self.game = game
        self.sc = game.sc
        ########
        self._fps_font = pg.font.SysFont('calibri', 26)
        self.start()

    def on_exit(self):
        pg.quit()
        exit()

    def on_game_over(self):
        pg.time.wait(1000)  # 1 sec
        self.start()

    def create_level(self, brick_size, level_size, ox=5, oy=30, dx=5, dy=5):
        # TODO: Вичисляти розмір плитки від розміру левела якщо він не переданий і навпаки

        w, h = brick_size
        cols, rows = level_size

        # Нам не потрібні лишні помилки
        w = min(max(1, w), WIDTH)
        h = min(max(1, h), HEIGHT)

        start_y, end_y, step_y = oy + h // 2, h * rows, h + dy
        start_x, end_x, step_x = ox + w // 2, w * cols, w + dx

        self.bricks.add(*[Brick(pos=(x, y), size=(w, h), group=self.bricks, color=choice(BRICK_COLORS))
                          for x in range(start_x, end_x, step_x)
                          for y in range(start_y, end_y, step_y)])

        # for y in range(start_y, end_y, step_y):
        #     for x in range(start_x, end_x, step_x):
        #         self.bricks.add(Brick(pos=(x, y), size=(w, h), group=self.bricks, color=choice(colors)))

    def start(self):
        self.bricks = Group()
        self.padle = Padle()
        self.ball = Ball((choice([-3, -2, -1, 1, 2, 3]), -3))
        self.collision_system = CollisionSystem(self.padle, self.ball, self.bricks)
        ###########
        self.create_level(brick_size=(100, 50), level_size=(16, 16))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.on_exit()
                # elif event.key == pg.K_q:
                #     self.ball.change_speed(sx=1)
                # elif event.key == pg.K_e:
                #     self.ball.change_speed(sy=1)


    def update(self):
        self.check_events()
        self.bricks.update()
        self.padle.update()
        self.ball.update()
        self.collision_system.ball_with_all()
        if self.collision_system.ball_with_bottom():
            self.start()

    def draw(self):
        self.sc.fill(BG)
        self.bricks.draw(self.sc)
        self.padle.draw(self.sc)
        self.ball.draw(self.sc)
        self.sc.blit(self._fps_font.render(f'{self.game.clock.get_fps(): .1f}', True, 'grey'), (0, 0))
        self.sc.blit(self._fps_font.render(f'Bricks: {len(self.bricks)}', True, 'grey'), (80, 0))
        pg.display.flip()