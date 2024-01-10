import pygame

class Piece:
    def __init__(self, window, texturePath, pos):
        self.window = window
        self.pos = pos
        self.texture = pygame.transform.scale(pygame.image.load(texturePath).convert_alpha(), (80, 80))
        self.x = 0
        self.y = 0
        self.arrayPosToCoordinates(pos)
        
    def render(self):
        self.window.blit(self.texture, (self.x, self.y))
        
    def arrayPosToCoordinates(self, pos):
        self.x = ((pos % 8) * 100) + 10
        self.y = ((pos // 8) * 100) + 10
        