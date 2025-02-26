import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Plane')


#Define Game Variables
ground_scroll = 0
scroll_speed = 4

#Load images
bg = pygame.image.load('Assets/bg.png')
ground = pygame.image.load('Assets/ground.png')

run = True
while run:
    
    clock.tick(fps)
    
#Background
    screen.blit(bg, (0, 0))

#Ground Scrolling
    screen.blit(ground,(ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()        
pygame.quit()
