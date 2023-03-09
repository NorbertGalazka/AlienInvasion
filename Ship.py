import pygame
from settings import ShipSettings
from settings import GameSettings
from settings import ShipBulletSettings


class Ship:
    def __init__(self):
        self.rect_start_x_position = 265
        self.rect_start_y_position = 680

    def get_spaceship_position(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect_start_x_position -= ShipSettings.speed
            if self.rect_start_x_position < - ShipSettings.rect_width:
                self.rect_start_x_position = GameSettings.screen_width

        if keys[pygame.K_RIGHT]:
            self.rect_start_x_position += ShipSettings.speed
            if self.rect_start_x_position > GameSettings.screen_width:
                self.rect_start_x_position = GameSettings.left_edge_of_the_screen

        if keys[pygame.K_UP]:
            self.rect_start_y_position -= ShipSettings.speed
            if self.rect_start_y_position < - ShipSettings.rect_height:
                self.rect_start_y_position = GameSettings.screen_height

        if keys[pygame.K_DOWN]:
            self.rect_start_y_position += ShipSettings.speed
            if self.rect_start_y_position > GameSettings.screen_height:
                self.rect_start_y_position = GameSettings.left_edge_of_the_screen

        return self.rect_start_x_position, self.rect_start_y_position

    def get_ship_rect(self, ship_is_alive):
        spaceship_x_position, spaceship_y_position = self.get_spaceship_position()
        spaceship_position = pygame.rect.Rect(spaceship_x_position, spaceship_y_position, ShipSettings.rect_width,
                                              ShipSettings.rect_height)
        if ship_is_alive is True:
            GameSettings.screen.blit(ShipSettings.spaceship_img, spaceship_position)
        return spaceship_position


class SpaceshipBullet:
    def __init__(self, bullet_x_start_position, bullet_y_start_position):
        self.bullet_x_start_position = bullet_x_start_position
        self.bullet_y_start_position = bullet_y_start_position
        self.bullet_position = pygame.Rect(self.bullet_x_start_position, self.bullet_y_start_position,
                                           ShipBulletSettings.bullet_width, ShipBulletSettings.bullet_height)

    def get_bullet_rect(self, bullets):
        for bullet in bullets:
            self.bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                    ShipBulletSettings.bullet_width,
                                                    ShipBulletSettings.bullet_height)
            pygame.draw.rect(GameSettings.screen, ShipBulletSettings.bullet_color, self.bullet_position)

    def change_bullet_position(self, bullets):
        for bullet in bullets:
            bullet.bullet_y_start_position -= 7
            if bullet.bullet_y_start_position <= 0:
                bullets.pop(bullets.index(bullet))