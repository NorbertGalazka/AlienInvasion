import pygame
from settings import GameSettings


class Explosion:
    def __init__(self, explosion_x, explosion_y,size):
        self.explosion_x = explosion_x
        self.explosion_y = explosion_y
        self.images = []
        self.size = size
        for num in range(0, 5):
            self.image = pygame.image.load(f"images/burst{num}.png")
            if self.size == 1:
                self.image = pygame.transform.scale(self.image, (120, 120))
                self.correct_pos_x = 31
                self.correct_pos_y = 18
            if self.size == 2:
                self.image = pygame.transform.scale(self.image, (35, 35))
                self.correct_pos_x = 8
                self.correct_pos_y = 0
            if self.size == 3:
                self.image = pygame.transform.scale(self.image, (200, 200))
                self.correct_pos_x = 60
                self.correct_pos_y = 40
            if self.size == 4:
                self.image = pygame.transform.scale(self.image, (300, 300))
                self.correct_pos_x = 100
                self.correct_pos_y = 100

            self.images.append(self.image)

    def get_explosion_rect(self, index):
        explosion_position = pygame.rect.Rect(self.explosion_x - self.correct_pos_x, self.explosion_y - self.correct_pos_y,
                                              self.images[index].get_width(), self.images[index].get_height())

        GameSettings.screen.blit(self.images[index], explosion_position)