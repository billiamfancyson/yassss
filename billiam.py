import pygame

def obstacles(obstacle1, obstacle2, obstacle3, obstacle4, color):
    pygame.draw.rect(gameDisplay, color, [obstacle1, obstacle2, obstacle3, obstacle4]


def  trex(x,y):


x = (display_width * .45)
y = (display_height * .8)
x_change = 0

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        x += x_change
