#-*- coding:utf8 -*-
import pygame, sys, time
import numpy as np
from pygame.locals import *

# height and width of interface
HEIGHT = 60
WIDTH = 120

pygame.clock_start = 0

# keep track of status of mouse and keyboard
pygame.button_down = False

# array to record game world
pygame.world=np.zeros((HEIGHT,WIDTH))

class Cell(pygame.sprite.Sprite):

    # size of each cell
    size = 8

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill((255,255,255))

        # Create a rectangle with top left corner at position and has the
        #   same size as cell
        self.rect = self.image.get_rect()
        self.rect.topleft = position

# we redraw the world every step
def draw():
    screen.fill((0,0,0))
    for col in range(pygame.world.shape[1]):
        for row in range(pygame.world.shape[0]):
            if pygame.world[int(row)][int(row)]:
                cell_create = Cell((col * Cell.size,row * Cell.size))
                screen.blit(cell_create.image,cell_create.rect)

def next_frame():
    count = sum(np.roll(np.roll(pygame.world, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))

    pygame.world = (count == 3) | ((pygame.world == 1) & (count == 2)).astype('int')

# initialize the world
def init():
    pygame.world.fill(0)
    draw()
    return 'Stop'

# in pause state
def stop():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RETURN:
            return 'Move'

        if event.type == KEYDOWN and event.key == K_r:
            return 'Reset'

        if event.type == MOUSEBUTTONDOWN:
            pygame.button_down = True
            pygame.button_type = event.button

        if event.type == MOUSEBUTTONUP:
            pygame.button_down = False

        if pygame.button_down:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = mouse_x / Cell.size;
            row = mouse_y / Cell.size;

            if pygame.button_type == 1: # left mouse
                pygame.world[int(row)][int(col)] = 1
            elif pygame.button_type == 3: # right mouse
                pygame.world[int(row)][int(col)] = 0
            draw()

    return 'Stop'
