import pygame as pg
from random import choice

from brick import Brick
from padle import Padle
from ball import Ball
from group import Group
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

    def create_level(self, cols=MAX_COLUMNS, rows=MAX_ROWS, ox=5, oy=30, dx=5, dy=5):
        """Створення списка плиток по заданим параметрам к-сті стовпчиків і рядків"""
        # не виходимо за границю максьмальних значень ширини та висоти

        # TODO: Розмір плитки має вичислятись в залежності від переданих аргументів
        cols = min(MAX_COLUMNS, cols)
        rows = min(MAX_ROWS, rows)

        colors = ['orange', 'lightgreen', 'lightgrey', 'azure', 'skyblue', 'pink', 'brown', 'yellow']

        for y in range(oy + BRICK_HIGHT // 2, BRICK_HIGHT * rows, BRICK_HIGHT + dy):
            for x in range(ox + BRICK_WIDTH // 2, BRICK_WIDTH * cols, BRICK_WIDTH + dx):
                self.bricks.add(Brick((x, y), group=self.bricks, color=choice(colors)))

    def start(self):
        self.bricks = Group()
        self.padle = Padle()
        direct = (choice([-3, -2, -1, 1, 2, 3]), -3)
        self.ball = Ball(direct)
        ###########
        self.create_level()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.on_exit()
                # elif event.key == pg.K_q:
                #     self.ball.change_speed(sx=1)
                # elif event.key == pg.K_e:
                #     self.ball.change_speed(sy=1)

    def collide_ball_with_bricks(self):
        ball = self.ball
        colliders = [*self.bricks.copy(), self.padle]
        direction = ball.direction
        dx, dy = ball.direction

        # check game over
        if ball.rect.move(0, dy).top > HEIGHT:
            self.on_game_over()

        # vertical and horizontal collision
        x_indexes = ball.rect.move(dx, 0).collidelistall(colliders)
        y_indexes = ball.rect.move(0, dy).collidelistall(colliders)

        if x_indexes:
            direction.x = -direction.x
        if y_indexes:
            direction.y = -direction.y

        # delete brick(s)
        [colliders[i].kill() for i in {*x_indexes, *y_indexes}]

        return direction

    def update(self):
        self.check_events()
        self.bricks.update()
        self.padle.update()
        self.ball.update(direction=self.collide_ball_with_bricks())
        self.collide_ball_with_bricks()

    def draw(self):
        self.sc.fill((10, 10, 10))
        self.bricks.draw(self.sc)
        self.padle.draw(self.sc)
        self.ball.draw(self.sc)
        self.sc.blit(self._fps_font.render(f'{self.game.clock.get_fps(): .1f}', True, 'grey'), (0, 0))
        self.sc.blit(self._fps_font.render(f'Bricks: {len(self.bricks)}', True, 'grey'), (80, 0))
        pg.display.flip()