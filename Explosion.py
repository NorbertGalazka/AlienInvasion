import pygame
from settings import ExplosionSettings, GameSettings


class Explosion:
    def __init__(self, explosion_x, explosion_y):
        self.explosion_image = pygame.image.load("images/exp1.png")
        self.expl_img_width = self.explosion_image.get_width()
        self.expl_img_height = self.explosion_image.get_height()
        self.explosion_x = explosion_x
        self.explosion_y = explosion_y

    def get_explosion_rect(self):
        explosion_position = pygame.rect.Rect(self.explosion_x - 31, self.explosion_y - 18, self.expl_img_width,
                                              self.expl_img_height)
        GameSettings.screen.blit(ExplosionSettings.image, explosion_position)
