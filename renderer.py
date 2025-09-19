import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def draw_ball(self, ball):
        pygame.draw.circle(self.screen,
                           "white",
                           (int(ball.x), int(ball.y)),
                           ball.radius)
