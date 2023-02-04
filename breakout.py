import pygame as pg

from brick import Brick
from padle import Padle
from ball import Ball
from group import Group
from drawing import Drawing
from timer import Timer, TimerGroup
from level_creator import LevelCreator
from collision_system import CollisionSystem
from config import *


class Breackout:
    def __init__(self, clock: pg.time.Clock):
        self.bricks = Group()
        self.balls = Group()  # TODO: kill() по таймеру якщо в групі більше одного м'яча
        self.padle = Padle()
        ###########
        self.timers = TimerGroup(restart_timer=Timer(6000, self.start))
        self.drawer = Drawing(self, clock, self.padle, self.bricks, self.balls, self.timers)
        self.level_creator = LevelCreator(self.bricks, self.balls)
        self.collision_system = CollisionSystem(self.padle, self.balls, self.bricks)
        ###########
        self.start()

    @property
    def is_win(self): return self.bricks.is_empty

    @property
    def is_loss(self): return self.balls.is_empty

    def start(self):
        self.timers.deactivate('restart_timer')
        ###########
        self.bricks.clear()
        self.balls.clear()
        ###########
        self.level_creator.new(brick_size=(100, 50))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    exit()
                if event.key == pg.K_SPACE and not self.balls.is_empty:
                    self.level_creator.add_ball()

    def check_game_over(self):
        if self.is_win or self.is_loss:
            self.timers.activate('restart_timer')

    def update(self, dt: float):
        self.check_events()
        self.timers.update()
        self.padle.update(dt)
        self.balls.update(dt)
        self.collision_system.update(dt)
        self.check_game_over()

    def draw(self):
        self.drawer.all()