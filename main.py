# Example file showing a basic pygame "game loop"
import pygame

from Renderer import Renderer
from Ball import Ball
from Physics import Physics

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

renderer = Renderer(screen)
physics = Physics(dt)

ball = Ball(screen.get_width() / 2, screen.get_height() / 2, 0, 0)
physics.set_ball_velocity(ball, 100, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    renderer.draw_ball(ball)
    physics.update_ball(ball, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for fps independent physics
    dt = clock.tick(60) / 1000



pygame.quit()