import pygame
from car import Car
from rect import Rect
import random

pygame.init()

WIDTH = 500
HEIGHT = 650

BACKGROUND_COLOR = (41, 49, 51)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Dodger')

FONT_GAME = pygame.font.Font(None, 36)
FONT_MENU = pygame.font.Font(None, 72)

FPS = 60

car = Car(WIDTH / 2 - 50, HEIGHT - 100)
rect = Rect()


def draw_game(window):
    window.fill(BACKGROUND_COLOR)
    window.blit(car.scaled_image, (car.x, car.y))
    car.move(WIDTH)
    if rect.y > HEIGHT:
        rect.y = 0
        rect.x = None
        rect.dodged += 1
        rect.move_vel += 0.5
        rect.width = random.randint(30, 90)
        rect.height = random.randint(30, 90)
    if not rect.x:
        rect.x = random.randint(0, WIDTH - rect.width)
    rect.draw(WINDOW)
    rect.move()
    dodged_text = FONT_GAME.render(f'Dodged: {rect.dodged}', True, (0, 255, 0))
    window.blit(dodged_text, (10, 10))
    pygame.display.flip()


def draw_menu(window):
    window.fill(BACKGROUND_COLOR)
    game_end_text = FONT_MENU.render(f'YOU LOST!', True, (180, 0, 0))
    window.blit(game_end_text, (WIDTH / 2 - game_end_text.get_width() / 2,
                                HEIGHT / 2 - 80 - game_end_text.get_height() / 2))
    dodged_text = FONT_MENU.render(f' Dodged: {rect.dodged}', True, (0, 180, 0))
    window.blit(dodged_text, (WIDTH / 2 - dodged_text.get_width() / 2,
                              HEIGHT / 2 - 10 - dodged_text.get_height() / 2))
    restart_text = FONT_MENU.render('Type "R" to restart', True, (0, 0, 0))
    window.blit(restart_text, (WIDTH / 2 - restart_text.get_width() / 2,
                               HEIGHT / 2 + 80 - restart_text.get_height() / 2))
    pygame.display.flip()


def restart_game():
    rect.x = None
    rect.y = 0
    rect.move_vel = 10
    rect.dodged = 0


def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_game(WINDOW)

        if car.check_collision_with_rect(rect):
            running = False
            running_menu = True
            while running_menu:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_menu = False

                draw_menu(WINDOW)

                if pygame.key.get_pressed()[pygame.K_r]:
                    running_menu = False
                    running = True
                    restart_game()

        pygame.time.Clock().tick(FPS)


run()
