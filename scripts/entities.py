import pygame as pg

class PhysicsEntity:
    def __init__(self, game, eType, pos, size):
        self.game = game
        self.type = eType
        self.pos = list(pos)
        self.size = size
        self.vel = [0, 0]

    def update(self, movement=(0, 0)):
        frameMovement = (movement[0] + self.vel[0], movement[1] + self.vel[1])

        self.pos[0] += frameMovement[0]
        self.pos[1] += frameMovement[1]

        self.vel[1] = min(7, self.vel[1] + 0.1)  # Terinal velocity

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)