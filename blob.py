import random

class Blob:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 0, 0)
        self.speed = 5
        self.direction = random.randint(0, 360)
        self.vision_radius = 100
