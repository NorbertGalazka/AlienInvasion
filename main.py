import pygame
import sys
from gamesettings import GameSettings
from gamesettings import ShipBulletSettings , AlienBulletSettings
import random


class AlienInvasion:
    def __init__(self, game_settings, ship, bullet, alien, bullet_settings, alien_bullet_settings,alien_bullet):
        self.alien = alien
        self.ship = ship
        self.alien_bullet_settings = alien_bullet_settings
        self.game_settings = game_settings
        self.bullet_settings = bullet_settings
        self.bullet = bullet
        self.screen = pygame.display.set_mode(
            (self.game_settings.screen_width, self.game_settings.screen_height))  # Utworzenie okienka gry
        self.alien_columns = 3
        self.alien_rows = 2
        self.alien_cooldown = 500
        self.last_aline_shot = pygame.time.get_ticks()
        self.alien_bullet = alien_bullet

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Inwazja obcych")
        bullets = []
        aliens = []
        alien_bullets = []

        for row in range(self.alien_rows):  # Utworzenie obcych
            for amount in range(self.alien_columns):
                alien = Alien(100 + amount * 150, 50 + row * 150, self.game_settings)  # Alien(x_pos,y_pos,sett)
                aliens.append(alien)

        while True:
            pygame.time.Clock().tick(60)  # Maksymalne FPS
            spaceship_rect = self.ship.get_ship_rect()

            time_now = pygame.time.get_ticks()
            if time_now - self.last_aline_shot > self.alien_cooldown and len(aliens) > 0:
                attacking_alien = random.choice(aliens)
                alien_bullet = AlienBullet(attacking_alien.alien_x_position + 34, attacking_alien.alien_y_position + 70,
                                           self.alien_bullet_settings, self.game_settings)
                alien_bullets.append(alien_bullet)
                self.last_aline_shot = time_now

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Wyłączanie gry, jeśli klikniemy X
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(SpaceshipBullet(self.ship.rect_start_x_position + 34.5,
                                                       self.ship.rect_start_y_position,
                                                       self.game_settings, self.bullet_settings))

            self.screen.blit(self.game_settings.bg, (0, 0))  # rysowanie tła
            self.screen.blit(self.game_settings.spaceship_img, spaceship_rect)  # wstawianie obrazka (obrazek,pozycja)

            self.bullet.get_bullet_rect(bullets)  # robienie i rysowanie pocisku
            self.bullet.change_bullet_position(bullets)

            self.alien.get_alien_rect(aliens)
            self.alien.alien_movement(aliens)

            self.alien_bullet.get_alien_bullet_rect(alien_bullets)
            self.alien_bullet.change_alien_bullet_position(alien_bullets)

            for alien in aliens:
                for bullet in bullets:
                    alien_position = pygame.rect.Rect(alien.alien_x_position, alien.alien_y_position,
                                                      self.alien.image_width,
                                                      self.alien.image_height)
                    bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                       self.bullet_settings.bullet_width,
                                                       self.bullet_settings.bullet_height)
                    if bullet_position.colliderect(alien_position):
                        aliens.remove(alien)
                        bullets.remove(bullet)

            pygame.display.update()  # Wyświetlenie ostatnio zmodyfikowanego ekranu


class Alien:
    def __init__(self, alien_x_position, alien_y_position, settings):
        self.image = pygame.image.load("images/alien" + str(random.randint(1, 2)) + ".png")
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.alien_x_position = alien_x_position
        self.alien_y_position = alien_y_position
        self.settings = settings
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.move_direction = 1

    def get_alien_rect(self, aliens):
        for alien in aliens:
            aliens_position = pygame.rect.Rect(alien.alien_x_position, alien.alien_y_position,
                                               alien.image_width, alien.image_height)
            self.screen.blit(alien.image, aliens_position)

    def alien_movement(self, aliens):
        for alien in aliens:
            alien.alien_y_position += 0.1
            alien.alien_x_position += self.move_direction
            if alien.alien_x_position < 0:
                self.move_direction *= -1
            elif alien.alien_x_position > 500:
                self.move_direction *= -1


class Ship:
    def __init__(self, settings):
        self.settings = settings
        self.speed = 5
        self.rect_start_x_position = 265
        self.rect_start_y_position = 680
        self.rect_width = self.settings.spaceship_img.get_width()
        self.rect_height = self.settings.spaceship_img.get_height()
        self.first_pixel = 0

    def get_spaceship_position(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect_start_x_position -= self.speed
            if self.rect_start_x_position < -self.rect_width:
                self.rect_start_x_position = self.settings.screen_width

        if keys[pygame.K_RIGHT]:
            self.rect_start_x_position += self.speed
            if self.rect_start_x_position > self.settings.screen_width:
                self.rect_start_x_position = self.first_pixel

        if keys[pygame.K_UP]:
            self.rect_start_y_position -= self.speed
            if self.rect_start_y_position < - self.rect_height:
                self.rect_start_y_position = self.settings.screen_height

        if keys[pygame.K_DOWN]:
            self.rect_start_y_position += self.speed
            if self.rect_start_y_position > self.settings.screen_height:
                self.rect_start_y_position = self.first_pixel

        return self.rect_start_x_position, self.rect_start_y_position

    def get_ship_rect(self):
        spaceship_x_position, spaceship_y_position = self.get_spaceship_position()
        return pygame.rect.Rect(spaceship_x_position, spaceship_y_position, self.rect_width, self.rect_height)


class SpaceshipBullet:
    def __init__(self, bullet_x_start_position, bullet_y_start_position, game_settings, bullet_settings):
        self.bullet_x_start_position = bullet_x_start_position
        self.bullet_y_start_position = bullet_y_start_position
        self.game_settings = game_settings
        self.bullet_settings = bullet_settings
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = self.game_settings.screen
        self.bullet_position = pygame.Rect(self.bullet_x_start_position, self.bullet_y_start_position,
                                           self.bullet_settings.bullet_width, self.bullet_settings.bullet_height)

    def get_bullet_rect(self, bullets):
        for bullet in bullets:
            self.bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                    self.bullet_settings.bullet_width,
                                                    self.bullet_settings.bullet_height)
            pygame.draw.rect(self.screen, self.bullet_settings.bullet_color, self.bullet_position)

    def change_bullet_position(self, bullets):
        for bullet in bullets:
            bullet.bullet_y_start_position -= 7
            if bullet.bullet_y_start_position <= 0:
                bullets.pop(bullets.index(bullet))


class AlienBullet:
    def __init__(self,bullet_x_start_position,bullet_y_start_position, alien_bullet_settings,game_settings):
        self.bullet_x_start_position = bullet_x_start_position
        self.bullet_y_start_position = bullet_y_start_position
        self.settings = game_settings
        # self.bullet_settings = bullet_settings
        self.alien_bullet_settings = alien_bullet_settings
        self.screen = self.settings.screen
        self.bullet_position = pygame.Rect(self.bullet_x_start_position, self.bullet_y_start_position,
                                           self.alien_bullet_settings.bullet_width,
                                           self.alien_bullet_settings.bullet_height)

    def get_alien_bullet_rect(self, bullets):
        for bullet in bullets:
            self.bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                        self.alien_bullet_settings.bullet_width,
                                                        self.alien_bullet_settings.bullet_height)
            pygame.draw.rect(self.screen, self.alien_bullet_settings.bullet_color, self.bullet_position)

    def change_alien_bullet_position(self, bullets):
        for bullet in bullets:
            bullet.bullet_y_start_position += 7
            if bullet.bullet_y_start_position >= 1000:
                bullets.pop(bullets.index(bullet))


def main():
    game = AlienInvasion(game_settings=GameSettings(), ship=Ship(GameSettings()),
                         bullet=SpaceshipBullet(0, 0, GameSettings(), ShipBulletSettings()),
                         alien=Alien(0, 0, GameSettings()), bullet_settings=ShipBulletSettings(),
                         alien_bullet_settings=AlienBulletSettings(), alien_bullet=AlienBullet(0,0,AlienBulletSettings(),GameSettings()))
    game.run_game()


if __name__ == "__main__":
    main()




