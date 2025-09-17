BALL_RADIUS = 20

class Ball:
    def __init__(self, x, y, xv, yv, radius=BALL_RADIUS):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.radius = radius

    #def update(self, dt):
        #self.x += self.xv * dt
        #self.y += self.yv * dt

    def collide(self):
        pass

    def collide_with(self, ball):
        pass