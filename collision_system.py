import pygame as pg

from config import WIDTH, HEIGHT


class CollisionSystem:
    def __init__(self, padle, ball, bricks):
        self.padle = padle
        self.ball = ball
        self.bricks = bricks

    def _ball_with_bricks(self) -> pg.Vector2:
        colliders = self.bricks.copy()
        dx, dy = self.ball.direction

        # vertical and horizontal collision
        x_indexes = self.ball.rect.move(dx, 0).collidelistall(colliders)
        y_indexes = self.ball.rect.move(0, dy).collidelistall(colliders)

        if x_indexes:
            self.ball.change_direction(x=True)
        if y_indexes:
            self.ball.change_direction(y=True)

        # delete brick(s)
        [colliders[i].kill() for i in {*x_indexes, *y_indexes}]


    def _ball_with_padle(self):
        # TODO: Зміна напряму м'яча в залежності від дистанції до центру дошки

        is_collide = lambda dx, dy: self.ball.rect.move(dx, dy).colliderect(self.padle)

        dx, dy = self.ball.direction
        if is_collide(dx, 0):
            self.ball.change_direction(x=True)
        if is_collide(0, dy):
            self.ball.change_direction(y=True)

    def _ball_with_screen(self):
        if self.ball.rect.top < 0:
            self.ball.direction.y = -self.ball.direction.y
        if self.ball.rect.left < 0 or self.ball.rect.right > WIDTH:
            self.ball.direction.x = -self.ball.direction.x

    def ball_with_bottom(self) -> bool:
        if self.ball.rect.top > HEIGHT:
            return True
        return False

    def ball_with_all(self):
        self._ball_with_bricks()
        self._ball_with_screen()
        self._ball_with_padle()