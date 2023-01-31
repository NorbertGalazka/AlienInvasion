import pygame

"""Klasa przeznaczona do przechowywania wszystkich ustawień gry"""
class Settings:
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        self.bg = pygame.image.load("images\space.png")
        self.image = pygame.image.load("images\spaceship-removebg-preview.png")
        self.rectangle_color = ((0, 230, 0))
        self.screen_width = 589
        self.screen_height = 793
        self.bg_color = (230,0,0)
        self.window_with_size = pygame.display.set_mode((589, 793))
        # bullet
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (255,128,0)
        self.bullet_start_x = 300
        self.bullet_start_y = 750

