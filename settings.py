import pygame

"""Klasa przeznaczona do przechowywania wszystkich ustawień gry"""
class Settings:
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        #Ustawienia ekranu
        self.rectangle_color = ((0,230,0))
        self.screen_width = 589
        self.screen_height = 793
        self.bg_color = (230,0,0)
        self.window_with_size = pygame.display.set_mode((589, 793))

