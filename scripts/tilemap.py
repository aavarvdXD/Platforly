import pygame as pg

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap():
    def __init__(self, game, tileSize=16):
        self.game = game
        self.tileSize = tileSize
        self.tileMap = {}
        self.offgridTiles = []

        for i in range(10):
            self.tileMap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tileMap['10;' + str(i + 5)] = {'type': 'grass', 'variant': 1, 'pos': (10, i + 5)}

    def tilesAround(self, pos):
        tiles = []
        tileLoc = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))
        for offset in NEIGHBOR_OFFSETS:
            checkLoc = str(tileLoc[0] + offset[0]) + ";" + str(tileLoc[1] + offset[1])
            if checkLoc in self.tileMap:
                tiles.append(self.tileMap[checkLoc])
        return tiles

    def physicsRectsAround(self, pos):
        rects = []
        for tile in self.tilesAround(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pg.Rect(tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize, self.tileSize, self.tileSize))
        return rects

    def render(self, surf):
        for tile in self.offgridTiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize))