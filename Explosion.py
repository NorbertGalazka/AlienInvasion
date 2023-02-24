import pygame
from settings import ExplosionSettings, GameSettings


class Explosion:
    def __init__(self, explosion_x, explosion_y,size):
        self.explosion_x = explosion_x
        self.explosion_y = explosion_y
        self.images = []
        self.size = size
        for num in range(0, 5):
            self.image = pygame.image.load(f"images/burst{num}.png")
            if self.size == 1:
                self.image = pygame.transform.scale(self.image,(120,120))
            self.images.append(self.image)
            # print(self.images)
        # self.index = 0
        # self.image = self.images[self.index]

    def get_explosion_rect(self, index):
        # print(self.images[index + 1])
        explosion_position = pygame.rect.Rect(self.explosion_x - 31, self.explosion_y - 18,
                                              self.images[index].get_width(), self.images[index].get_height())

        GameSettings.screen.blit(self.images[index], explosion_position)