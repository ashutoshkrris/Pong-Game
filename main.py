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

    #Title Font here
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('PONG', False, white)
    textRect = text.get_rect()
    textRect.center = (750//2, 25)
    window.blit(text, textRect)

    #Left Paddle Score
    leftPaddle_score = font.render(str(leftPaddle.score), False, red)
    leftPaddle_rect = leftPaddle_score.get_rect()
    leftPaddle_rect.center = (50,50)
    window.blit(leftPaddle_score, leftPaddle_rect)

    #Right Paddle Score
    rightPaddle_score = font.render(str(rightPaddle.score), False, green)
    rightPaddle_rect = rightPaddle_score.get_rect()
    rightPaddle_rect.center = (700,50)
    window.blit(rightPaddle_score, rightPaddle_rect)

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
        #Reset the ball position
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = -1
        leftPaddle.score += 1
    
    #Reverse the direction if ball collides with upper boundary
    if pong.rect.y < 0:
        pong.dy = 1
    
    #Reverse the direction if ball collides with left boundary
    if pong.rect.x < 0:
        #Reset the ball position
        pong.rect.x, pong.rect.y = 375, 250
        pong.dx = 1
        rightPaddle.score += 1

    # Reverse ball direction if it hits left paddle
    if leftPaddle.rect.colliderect(pong.rect):
        pong.dx = 1

    # Reverse ball direction if it hits right paddle
    if rightPaddle.rect.colliderect(pong.rect):
        pong.dx = -1


    redraw()

pygame.quit()