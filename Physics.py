import constants as c
from constants import FRICTION, MIN_SPEED_FOR_STOP


class Physics:
    def __init__(self, dt):
        self.dt = dt

    @staticmethod
    def set_ball_velocity(ball, new_xv, new_yv):
        ball.xv = new_xv
        ball.yv = new_yv

    @staticmethod
    def update_ball(ball, dt):
        ball.x += ball.xv * dt
        ball.y += ball.yv * dt

        ball.xv *= FRICTION
        ball.yv *= FRICTION

        if abs(ball.xv) <= MIN_SPEED_FOR_STOP: ball.xv = 0
        if abs(ball.yv) <= MIN_SPEED_FOR_STOP: ball.yv = 0

    @staticmethod
    def check_collision(ball):
        if ball.x < (0 + ball.radius) or ball.x > (c.SCREEN_WIDTH - ball.radius):
            ball.xv = ball.xv * -1
        if ball.y < (0 + ball.radius) or ball.y > (c.SCREEN_HEIGHT - ball.radius):
            ball.yv = ball.yv * -1