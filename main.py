#Import libraries here
import pygame
from paddle import *
from ball import *
from constants import *

#Initialise pygame
pygame.init()

#Creating left paddle
leftPaddle = Paddle()
leftPaddle.image.fill(red)
leftPaddle.rect.x = 25
leftPaddle.rect.y = 225

#Creating right paddle
rightPaddle = Paddle()
rightPaddle.image.fill(green)
rightPaddle.rect.x = 715
rightPaddle.rect.y = 225

#Setting paddle speed to move up and down
paddleSpeed = 30

#Creating ball here
pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

#Adding all elements to sprite group
allSprites = pygame.sprite.Group()
allSprites.add(leftPaddle, rightPaddle, pong)

#Displaying the sprites in window
def redraw():
    window.fill(black)
    allSprites.draw(window)
    pygame.display.update()

run = True

#Loop to run the program until quit
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Setting variable to detect key press
    key = pygame.key.get_pressed()

    # W key to move left paddle up
    if key[pygame.K_w]:
        leftPaddle.rect.y += -paddleSpeed
    
    # S key to move left paddle down
    if key[pygame.K_s]:
        leftPaddle.rect.y += paddleSpeed

    # Up arrow key to move right paddle up
    if key[pygame.K_UP]:
        rightPaddle.rect.y += -paddleSpeed

    # Down arrow key to move right paddle up
    if key[pygame.K_DOWN]:
        rightPaddle.rect.y += paddleSpeed

    #Moving the ball
    pong.rect.x += pong.speed * pong.dx
    pong.rect.y += pong.speed * pong.dy

    #Reverse the direction if ball collides with lower boundary
    if pong.rect.y > 490:
        pong.dy = -1

    #Reverse the direction if ball collides with right boundary
    if pong.rect.x > 740:
        pong.dx = -1
    
    #Reverse the direction if ball collides with upper boundary
    if pong.rect.y < 0:
        pong.dy = 1
    
    #Reverse the direction if ball collides with left boundary
    if pong.rect.x < 0:
        pong.dx = 1

    redraw()

pygame.quit()