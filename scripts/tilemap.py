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

    def tilesAround(self, pos, size=(16, 16)):
        tiles = []
        tileLoc = (int(pos[0] // self.tileSize), int(pos[1] // self.tileSize))
        
        # Calculate how many tiles the entity spans
        width_in_tiles = int((pos[0] + size[0]) // self.tileSize) - tileLoc[0] + 1
        height_in_tiles = int((pos[1] + size[1]) // self.tileSize) - tileLoc[1] + 1

        for x in range(-1, width_in_tiles + 1):
            for y in range(-1, height_in_tiles + 1):
                checkLoc = str(tileLoc[0] + x) + ";" + str(tileLoc[1] + y)
                if checkLoc in self.tileMap:
                    tiles.append(self.tileMap[checkLoc])
        return tiles

    def physicsRectsAround(self, pos, size=(16, 16)):
        rects = []
        for tile in self.tilesAround(pos, size):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pg.Rect(tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize, self.tileSize, self.tileSize))
        return rects

    def render(self, surf, offset=(0, 0)):
        for tile in self.offgridTiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tileSize - offset[0], tile['pos'][1] * self.tileSize - offset[1]))