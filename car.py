import pygame


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/SportsRacingCar_0.png')
        self.width = 100
        self.height = 100
        self.scaled_image = (pygame.transform.scale
                             (self.image, (self.width, self.height)).convert_alpha())
        self.move_vel = 15

    def move(self, wind_width):
        if pygame.key.get_pressed():
            if pygame.key.get_pressed()[pygame.K_LEFT] and self.x > 0:
                self.x -= self.move_vel
            if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x < wind_width - self.width:
                self.x += self.move_vel

    def check_collision_with_rect(self, rect):
        car_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        rect_rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height)
        if car_rect.colliderect(rect_rect):
            return True
