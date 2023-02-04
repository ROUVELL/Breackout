import pygame as pg

from padle import Padle
from ball import Ball
from group import Group
from config import WIDTH, HEIGHT


class CollisionSystem:
    def __init__(self, breackout, padle: Padle, balls: Group, bricks: Group):
        self._breckout = breackout
        self._padle = padle
        self._balls = balls
        self._bricks = bricks

    def _padle_with_screen(self):
        # Не даємо дошці вийти за межі екрана
        self._padle.rect.left = max(0, self._padle.rect.left)
        self._padle.rect.right = min(WIDTH, self._padle.rect.right)

    def _ball_with_bricks(self, ball: Ball, dt: float) -> pg.Vector2:
        bricks = self._bricks.copy()

        dx, dy = ball.direction * dt

        # отримуємо індекси плиток з якими зіткнувся м'яч
        x_indexes = ball.rect.move(dx, 0).collidelistall(bricks)
        y_indexes = ball.rect.move(0, dy).collidelistall(bricks)

        # міняємо напрям в залежності від зіткнення
        if x_indexes: ball.change_direction(x=True)
        if y_indexes: ball.change_direction(y=True)

        # TODO: Деякі плитки можуть мати "здоровя" і видалятися не зразу
        # видаляємо плитки з якими зіткнулися
        [self._breckout.add_score(bricks[i].kill()) for i in {*x_indexes, *y_indexes}]

    def _ball_with_padle(self, ball: Ball, dt: float):
        # TODO: Зміна напряму м'яча в залежності від дистанції до центру дошки

        # true якщо є зіткнення, інакше false
        is_collide = lambda dx, dy: ball.rect.move(dx, dy).colliderect(self._padle)

        dx, dy = ball.direction * dt
        if is_collide(dx, 0): ball.change_direction(x=True)
        if is_collide(0, dy): ball.change_direction(y=True)

    def _ball_with_screen(self, ball: Ball):
        rect = ball.rect
        if rect.top < 0:
            ball.change_direction(y=True)
        if rect.left < 0 or rect.right > WIDTH:
            ball.change_direction(x=True)
        if rect.top > HEIGHT:
            self._breckout.add_score(-1)
            ball.kill()

    def update(self, dt: float):
        self._padle_with_screen()
        for ball in self._balls.copy():
            self._ball_with_bricks(ball, dt)
            self._ball_with_padle(ball, dt)
            self._ball_with_screen(ball)