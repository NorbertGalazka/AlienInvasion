import pygame
from settings import AlienBulletSettings
from settings import GameSettings
from settings import BossSettings
from settings import ShipSettings


class BossAlienBullet:
    def __init__(self, bullet_x_start_position, bullet_y_start_position, bullet_direction_x, bullet_direction_y):
        self.bullet_x_start_position = bullet_x_start_position
        self.bullet_y_start_position = bullet_y_start_position
        self.bullet_position = pygame.Rect(self.bullet_x_start_position, self.bullet_y_start_position,
                                           AlienBulletSettings.bullet_width,
                                           AlienBulletSettings.bullet_height)
        self.bullet_direction_x = bullet_direction_x
        self.bullet_direction_y = bullet_direction_y

    def get_boss_alien_bullet_rect(self, bullet):
        self.bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                AlienBulletSettings.bullet_width, AlienBulletSettings.bullet_height)
        pygame.draw.rect(GameSettings.screen, AlienBulletSettings.bullet_color, self.bullet_position)

    def change_boss_alien_bullet_position(self):
        self.bullet_y_start_position += self.bullet_direction_x
        self.bullet_x_start_position += self.bullet_direction_y


class BossAlien:
    def __init__(self,boss_start_x_position, boss_start_y_position):
        self.boss_start_x_position = boss_start_x_position
        self.boss_start_y_position = boss_start_y_position
        self.boss_hp = BossSettings.boss_hp

    def get_boss_rect(self, spaceship_x_position, spaceship_y_position):
        if spaceship_x_position > self.boss_start_x_position:
            self.boss_start_x_position += BossSettings.boss_speed
        if spaceship_x_position < self.boss_start_x_position:
            self.boss_start_x_position -= BossSettings.boss_speed
        if spaceship_y_position > self.boss_start_y_position:
            self.boss_start_y_position += BossSettings.boss_speed
        if spaceship_y_position < self.boss_start_y_position:
            self.boss_start_y_position -= BossSettings.boss_speed

        boss_position = pygame.rect.Rect(self.boss_start_x_position, self.boss_start_y_position, ShipSettings.rect_width,
                                         ShipSettings.rect_height)
        GameSettings.screen.blit(BossSettings.boss_img, boss_position)
        return boss_position
