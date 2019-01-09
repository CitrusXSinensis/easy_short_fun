#-*- coding:utf8 -*-
import pygame, sys, time
import numpy as np
from pygame.locals import *

# height and width of interface
HEIGHT = 60
WIDTH = 120

# keep track of status of mouse and keyboard
pygame.button_down = False

# 
pygame.world=np.zeros((HEIGHT,WIDTH))

