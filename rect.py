import pygame


class Rect:
    def __init__(self):
        self.x = None
        self.y = 0
        self.dx = 1
        self.width = 30
        self.height = 30
        self.color = (0, 0, 255)
        self.move_vel = 10
        self.dodged = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, ((self.x, self.y),
                                              (self.width, self.height)))

    def move(self):
        self.y += self.move_vel
