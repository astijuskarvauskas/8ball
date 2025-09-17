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
