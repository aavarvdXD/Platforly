class Tilemap():
    def __init__(self, game, tileSize=16):
        self.game = game
        self.tileSize = tileSize
        self.tileMap = {}
        self.offgridTiles = []

        for i in range(10):
            self.tileMap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tileMap['10;' + str(i + 5)] = {'type': 'grass', 'variant': 1, 'pos': (10, i + 5)}

    def render(self, surf):
        for tile in self.offgridTiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tileMap:
            tile = self.tileMap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tileSize, tile['pos'][1] * self.tileSize))