import pygame


class GameSettings:
    def __init__(self):
        self.bg = pygame.image.load("images\space.png")
        self.spaceship_img = pygame.image.load("images\spaceship-removebg-preview.png")
        self.rectangle_color = (0, 230, 0)
        self.screen_width = 589
        self.screen_height = 793
        self.bg_color = (230, 0, 0)
        self.window_with_size = pygame.display.set_mode((589, 793))


class BulletSettings:
    def __init__(self):
        self.bullet_speed = 9
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (255, 128, 0)
        self.bullet_start_x = 300
        self.bullet_start_y = 750



