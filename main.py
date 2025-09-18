# Example file showing a basic pygame "game loop"
import pygame

import constants as c

from inputHandler import InputHandler
from renderer import Renderer
from ball import Ball
from physicsHandler import Physics
from action import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

renderer = Renderer(screen)
physics = Physics()
inputHandler = InputHandler()

ball = Ball(screen.get_width() / 2, screen.get_height() / 2, 0, 0)
physics.set_ball_velocity(ball, 0, 1000)

while c.RUNNING:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        action = inputHandler.handle_input(event)

        if action and action.type == ActionType.SHOOT:
            # TODO: Implement shoot ball mechanic
            m_x = action.payload[0]
            m_y = action.payload[1]


            pass

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    renderer.draw_ball(ball)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for fps independent physics
    dt = clock.tick(60) / 1000
    physics.update_ball(ball, dt)
    physics.check_collision(ball)

pygame.quit()