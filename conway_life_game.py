#-*- coding:utf8 -*-
import pygame, sys, time
import numpy as np
from pygame.locals import *

# height and width of interface
HEIGHT = 60
WIDTH = 120

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
