import pygame

pygame.init()

window = pygame.display.set_mode((750,500))

pygame.display.set_caption('PongPongPong')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()