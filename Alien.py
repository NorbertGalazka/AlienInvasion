import pygame
import random
from settings import GameSettings
from settings import AlienBulletSettings


class Alien:
    def __init__(self, alien_x_position, alien_y_position):
        self.image = pygame.image.load("images/alien" + str(random.randint(1, 5)) + ".png")
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.alien_x_position = alien_x_position
        self.alien_y_position = alien_y_position
        self.move_direction = 1

    def get_alien_rect(self, aliens):
        for alien in aliens:
            aliens_position = pygame.rect.Rect(alien.alien_x_position, alien.alien_y_position,
                                               alien.image_width, alien.image_height)
            GameSettings.screen.blit(alien.image, aliens_position)

    def alien_movement(self, aliens):
        for alien in aliens:
            alien.alien_y_position += 0.1
            alien.alien_x_position += self.move_direction
            if alien.alien_x_position < 0:
                self.move_direction *= -1
            elif alien.alien_x_position > 500:
                self.move_direction *= -1
            if alien.alien_y_position > 793:
                return True


class AlienBullet:
    def __init__(self, bullet_x_start_position, bullet_y_start_position):
        self.bullet_x_start_position = bullet_x_start_position
        self.bullet_y_start_position = bullet_y_start_position
        self.bullet_position = pygame.Rect(self.bullet_x_start_position, self.bullet_y_start_position,
                                           AlienBulletSettings.bullet_width,
                                           AlienBulletSettings.bullet_height)

    def get_alien_bullet_rect(self, bullets):
        for bullet in bullets:
            self.bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                    AlienBulletSettings.bullet_width, AlienBulletSettings.bullet_height)
            pygame.draw.rect(GameSettings.screen, AlienBulletSettings.bullet_color, self.bullet_position)

    def change_alien_bullet_position(self, bullets):
        for bullet in bullets:
            bullet.bullet_y_start_position += 7
            if bullet.bullet_y_start_position >= 1000:
                bullets.pop(bullets.index(bullet))