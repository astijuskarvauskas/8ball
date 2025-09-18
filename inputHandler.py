import math

import pygame
from physicsHandler import Physics
from action import *

import constants as c

physicsHandler = Physics()

class InputHandler:
    def __init__(self):
        self.m_x, self.m_y = None, None

    def handle_input(self, e):
        if e.type == pygame.QUIT:
            c.RUNNING = False

        if e.type == pygame.MOUSEBUTTONUP:
            self.m_x, self.m_y = pygame.mouse.get_pos()
            return ShootAction(self.m_x, self.m_y)

        return None