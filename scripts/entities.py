import pygame as pg

class PhysicsEntity:
    def __init__(self, game, eType, pos, size):
        self.game = game
        self.type = eType
        self.pos = list(pos)
        self.size = size
        self.vel = [0, 0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

    def rect(self):
        return pg.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

        frameMovement = (movement[0] + self.vel[0], movement[1] + self.vel[1])

        self.pos[0] += frameMovement[0]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[0] > 0:
                    entityRect.right = rect.left
                    self.collisions['right'] = True
                if frameMovement[0] < 0:
                    entityRect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entityRect.x

        self.pos[1] += frameMovement[1]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[1] > 0:
                    entityRect.bottom = rect.top
                    self.collisions['down'] = True
                if frameMovement[1] < 0:
                    entityRect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entityRect.y

        self.vel[1] = min(7, self.vel[1] + 0.1)  # Terinal velocity

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)