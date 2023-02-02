import pygame as pg

from breakout import Breackout
from config import *


class Game:
    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode(SCREEN, pg.NOFRAME)
        self.clock = pg.time.Clock()
        self.breackout = Breackout(self)

    def run(self):
        while True:
            dt = float(f'{self.clock.tick(60) / 16.66 : .1f}')
            self.breackout.update(dt)
            self.breackout.draw()
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()