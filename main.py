import pygame as pg

from config import *


class Game:
    def __init__(self):
        pg.init()
        self.sc = pg.display.set_mode(SCREEN, pg.NOFRAME)
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)
            [exit() for e in pg.event.get() if e.type == pg.KEYUP and e.key == pg.K_ESCAPE]
            self.sc.fill((10, 10, 10))
            # update
            # draw
            pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()