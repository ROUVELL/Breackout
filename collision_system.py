import pygame as pg

from padle import Padle
from ball import Ball
from group import Group
from config import WIDTH, HEIGHT


class CollisionSystem:
    def __init__(self, breackout, padle: Padle, balls: Group, bricks: Group):
        self.breckout = breackout
        self.padle = padle
        self.balls = balls
        self.bricks = bricks

    def _padle_with_screen(self):
        self.padle.rect.left = max(0, self.padle.rect.left)
        self.padle.rect.right = min(WIDTH, self.padle.rect.right)

    def _ball_with_bricks(self, ball: Ball, dt: float) -> pg.Vector2:
        bricks = self.bricks.copy()

        dx, dy = ball.direction

        # vertical and horizontal collision
        x_indexes = ball.rect.move(dx * dt, 0).collidelistall(bricks)
        y_indexes = ball.rect.move(0, dy * dt).collidelistall(bricks)

        if x_indexes:
            ball.change_direction(x=True)
        if y_indexes:
            ball.change_direction(y=True)

        # delete brick(s)
        [self.breckout.add_score(bricks[i].kill()) for i in {*x_indexes, *y_indexes}]

    def _ball_with_padle(self, ball: Ball, dt: float):
        # TODO: Зміна напряму м'яча в залежності від дистанції до центру дошки

        is_collide = lambda dx, dy: ball.rect.move(dx * dt, dy * dt).colliderect(self.padle)

        dx, dy = ball.direction
        if is_collide(dx, 0):
            ball.change_direction(x=True)
        if is_collide(0, dy):
            ball.change_direction(y=True)

    def _ball_with_screen(self, ball: Ball):
        if ball.rect.top < 0:
            ball.change_direction(y=True)
        if ball.rect.left < 0 or ball.rect.right > WIDTH:
            ball.change_direction(x=True)
        if ball.rect.top > HEIGHT:
            self.breckout.add_score(-1)
            ball.kill()

    def update(self, dt: float):
        self._padle_with_screen()
        for ball in self.balls.copy():
            self._ball_with_bricks(ball, dt)
            self._ball_with_padle(ball, dt)
            self._ball_with_screen(ball)