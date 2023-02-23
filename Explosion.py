# import pygame
# from settings import ExplosionSettings, GameSettings
#
#
# class Explosion:
#     def __init__(self, explosion_x, explosion_y,draw_times):
#         self.explosion_x = explosion_x
#         self.explosion_y = explosion_y
#         self.draw_times = draw_times
#
#     def get_explosion_rect(self):
#         image = pygame.image.load(f"images/burst4.png")
#         image = pygame.transform.scale(image, (20, 20))
#
#         explosion_position = pygame.rect.Rect(self.explosion_x - 31, self.explosion_y - 18,
#                                               image.get_width(), image.get_height())
#         # GameSettings.screen.blit(pygame.image.load(f"images/burst{image_num}.png"), explosion_position)
#         GameSettings.screen.blit(image, explosion_position)

import pygame
from settings import ExplosionSettings, GameSettings


class Explosion:
    def __init__(self, explosion_x, explosion_y,draw_times,size):
        self.explosion_x = explosion_x
        self.explosion_y = explosion_y
        self.draw_times = draw_times
        self.images = []
        self.size = size
        for num in range(1, 6):
            self.image = pygame.image.load(f"images/burst{num}.png")
            if self.size == 1:
                self.image = pygame.transform.scale(self.image,(120,120))
            self.images.append(self.image)
        # self.index = 0
        # self.image = self.images[self.index]

    def get_explosion_rect(self, index):

        explosion_position = pygame.rect.Rect(self.explosion_x - 31, self.explosion_y - 18,
                                              self.images[index+1].get_width(), self.images[index+1].get_height())

        GameSettings.screen.blit(self.images[index+1], explosion_position)