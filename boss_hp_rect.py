import pygame
from settings import GameSettings


class BossHp:
    def __init__(self):
        self.image1 = pygame.image.load("images/life_bar1.png")
        self.image2 = pygame.image.load("images/life_bar2.png")
        self.image3 = pygame.image.load("images/life_bar3.png")
        self.image4 = pygame.image.load("images/life_bar4.png")
        self.image5 = pygame.image.load("images/life_bar5.png")
        self.rect_width = self.image1.get_width()
        self.rect_height = self.image1.get_height()

    def get_hp_bar_rect(self,boss_x_position, boss_y_position, boss_hp):
        image = pygame.image.load("images/life_bar1.png")
        if boss_hp > 16:
            image = self.image1
        if 12 > boss_hp <= 16:
            image = self.image2
        if 8 < boss_hp <= 12:
            image = self.image3
        if 4 < boss_hp <= 8:
            image = self.image4
        if boss_hp <= 4:
            image = self.image5
        hp_bar_position = pygame.rect.Rect(boss_x_position, boss_y_position, self.rect_width, self.rect_height)
        GameSettings.screen.blit(image, hp_bar_position)

