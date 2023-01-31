import pygame as pg
from random import choice

from brick import Brick
from padle import Padle
from ball import Ball
from group import Group
from config import *


class Breackout:
    """Основний клас який керує всіма ігровими елементами"""

    def __init__(self, game):
        self.game = game
        self.sc = game.sc
        ########
        self.start()

    def on_exit(self):
        pg.quit()
        exit()

    def on_game_over(self):
        pg.time.wait(1000)  # 1 sec
        self.start()

    def create_level(self, cols=MAX_COLUMNS, rows=MAX_ROWS):
        """Створення списка плиток по заданим параметрам к-сті стовпчиків і рядків"""
        # не виходимо за границю максьмальних значень ширини та висоти
        cols = min(MAX_COLUMNS, cols)
        rows = min(MAX_ROWS, rows)

        ox = WIDTH // cols
        oy = (HEIGHT - 3 * BRICK_HIGHT) // rows
        for y in range(int(1.5 * BRICK_HIGHT), BRICK_HIGHT * MAX_ROWS, oy):
            for x in range(ox // 2, WIDTH, ox):
                self.bricks.add(Brick((x, y), group=self.bricks))

    def start(self):
        self.bricks = Group()
        self.padle = Padle()
        direct = (choice([-3, -2, -1, 1, 2, 3]), -3)
        self.ball = Ball(direct)
        ###########
        self.create_level(cols=18, rows=16)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                self.on_exit()

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
        pg.display.flip()