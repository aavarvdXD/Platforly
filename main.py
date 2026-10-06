import pygame as pg
import sys, os

from scripts.utils import loadImg
from scripts.entities import PhysicsEntity

class Game():
    def __init__(self):
        pg.init()

        pg.display.set_caption("Platforly")
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

        screenWidth, screenHeight = self.screen.get_size()
        self.display = pg.Surface((screenWidth // 2, screenHeight // 2))

        self.clock = pg.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': loadImg('player/png/idle/idle-0.png')
        }


        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            self.display.fill((0, 0, 15))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.movement[0] = True
                    if event.key == pg.K_d:
                        self.movement[1] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.movement[0] = False
                    if event.key == pg.K_d:
                        self.movement[1] = False

            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))

            pg.display.update()
            self.clock.tick(60)

game = Game()
game.run()