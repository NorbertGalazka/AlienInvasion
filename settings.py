import pygame
from dataclasses import dataclass


@dataclass
class GameSettings:
    bg = pygame.image.load("images\space.png")
    screen_width = 589
    screen_height = 793
    screen = pygame.display.set_mode((screen_width, screen_height))
    left_edge_of_the_screen = 0


@dataclass
class ShipBulletSettings:
    bullet_speed = 9
    bullet_width = 5
    bullet_height = 15
    bullet_color = (255, 128, 0)
    bullet_start_x = 300
    bullet_start_y = 750


@dataclass
class AlienBulletSettings:
    bullet_speed = 10
    bullet_width = 7
    bullet_height = 7
    bullet_color = (255, 255, 100)
    bullet_start_x = 300
    bullet_start_y = 750


@dataclass
class AlienSettings:
    alien_columns = 3
    alien_rows = 2
    alien_cooldown = 500


@dataclass
class ShipSettings:
    spaceship_img = pygame.image.load("images\spaceship-removebg-preview.png")
    rect_width = spaceship_img.get_width()
    rect_height = spaceship_img.get_height()
    speed = 5
