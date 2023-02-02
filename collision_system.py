import pygame as pg

from config import WIDTH, HEIGHT


class CollisionSystem:
    def __init__(self, padle, balls, bricks):
        self.padle = padle
        self.balls = balls
        self.bricks = bricks

    def _ball_with_bricks(self, ball) -> pg.Vector2:
        colliders = self.bricks.copy()

        dx, dy = ball.direction

        # vertical and horizontal collision
        x_indexes = ball.rect.move(dx, 0).collidelistall(colliders)
        y_indexes = ball.rect.move(0, dy).collidelistall(colliders)

        if x_indexes:
            ball.change_direction(x=True)
        if y_indexes:
            ball.change_direction(y=True)

        # delete brick(s)
        [colliders[i].kill() for i in {*x_indexes, *y_indexes}]

    def _ball_with_padle(self, ball):
        # TODO: Зміна напряму м'яча в залежності від дистанції до центру дошки

        is_collide = lambda dx, dy: ball.rect.move(dx, dy).colliderect(self.padle)

        dx, dy = ball.direction
        if is_collide(dx, 0):
            ball.change_direction(x=True)
        if is_collide(0, dy):
            ball.change_direction(y=True)

    def _ball_with_screen(self, ball):
        if ball.rect.top < 0:
            ball.change_direction(y=True)
        if ball.rect.left < 0 or ball.rect.right > WIDTH:
            ball.change_direction(x=True)
        if ball.rect.top > HEIGHT:
            ball.kill()

    def balls_with_all(self):
        for ball in self.balls.copy():
            self._ball_with_bricks(ball)
            self._ball_with_padle(ball)
            self._ball_with_screen(ball)