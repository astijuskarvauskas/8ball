import constants as c
from constants import FRICTION, STOP_SPEED

class Physics:
    def __init__(self):
        pass

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

        if abs(ball.xv) <= STOP_SPEED: ball.xv = 0
        if abs(ball.yv) <= STOP_SPEED: ball.yv = 0

    @staticmethod
    def check_collision(ball):
        if ball.x < (0 + ball.radius) or ball.x > (c.SCREEN_WIDTH - ball.radius):
            ball.xv = ball.xv * -1
        if ball.y < (0 + ball.radius) or ball.y > (c.SCREEN_HEIGHT - ball.radius):
            ball.yv = ball.yv * -1

    @staticmethod
    def strike_ball(ball, m_dx, m_dy):
        # function called on mouse release:
            # dx is displacement from edge of ball to mouse x pos
                # calc horizontal velocity from this
            # dy is displacement from edge of ball to mouse y pos
                # calc vertical velocity from this
            # dxy is total magnitude
                # calc power multiplier for x and y components from this


        x_vel = (ball.x - m_dx) * c.POWER
        y_vel = (ball.y - m_dy) * c.POWER

        Physics.set_ball_velocity(ball, x_vel, y_vel)