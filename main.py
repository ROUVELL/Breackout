import pygame as pg

from breakout import Breackout
from config import *


class Game:
    """Клас в якому ініціалізуєить pygame, контролюється fps та запускається основний цикл"""

    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode(SCREEN, pg.NOFRAME)
        self.clock = pg.time.Clock()
        self.breackout = Breackout(self)

    def run(self):
        while True:
            self.clock.tick(60)
            self.breackout.update()
            self.breackout.draw()
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()