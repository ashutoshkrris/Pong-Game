import pygame

#Paddle class here
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,75])
        self.rect = self.image.get_rect()
        self.score = 0