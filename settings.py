import pygame
from dataclasses import dataclass


@dataclass
class GameSettings:

    bg = pygame.image.load("images\space.png")
    spaceship_img = pygame.image.load("images\spaceship-removebg-preview.png")
        # self.rectangle_color = (0, 230, 0)
    screen_width = 589
    screen_height = 793
        # self.bg_color = (230, 0, 0)
        # self.window_with_size = pygame.display.set_mode((589, 793))
        # self.spaceship_start_x_position = 265
    screen = pygame.display.set_mode((screen_width, screen_height))


class ShipBulletSettings:
    def __init__(self):
        self.bullet_speed = 9
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 128, 0)
        self.bullet_start_x = 300
        self.bullet_start_y = 750


class AlienBulletSettings:
    def __init__(self):
        self.bullet_speed = 10
        self.bullet_width = 7
        self.bullet_height = 7
        self.bullet_color = (255, 255, 100)
        self.bullet_start_x = 300
        self.bullet_start_y = 750
