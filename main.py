import pygame as pg
import sys, os

from scripts.utils import loadImg, loadImgs
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

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
            'decor': loadImgs('tiles/decor'),
            'grass': loadImgs('tiles/grass'),
            'large_decor': loadImgs('tiles/large_decor'),
            'stone': loadImgs('tiles/stone'),
            'player': loadImg('player/png/idle/idle-0.png'),
            'backgrounds': pg.transform.scale(loadImg('background/1.png'), self.display.get_size()),
            'clouds': loadImgs('background/clouds'),
        }

        self.clouds = Clouds(self.assets['clouds'], self.display.get_size())

        self.player = PhysicsEntity(self, 'player', (50, 50), (16, 40))
        self.speed = 1.5

        self.tilemap = Tilemap(self, tileSize=16)

        self.scroll = [0,0]

    def run(self):
        while True:
            self.display.blit(self.assets['backgrounds'], (0, 0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            renderScroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset=renderScroll)

            self.tilemap.render(self.display, offset=renderScroll)

            self.player.update(self.tilemap, (self.movement[1] * self.speed - self.movement[0] * self.speed, 0))
            self.player.render(self.display, offset=renderScroll)

            for event in pg.event.get():
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.movement[0] = True
                    if event.key == pg.K_d:
                        self.movement[1] = True
                    if event.key == pg.K_SPACE:
                        self.player.vel[1] = -5
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