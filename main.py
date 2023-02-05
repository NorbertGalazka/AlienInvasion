import pygame
import sys
from settings import Settings
import random


class AlienInvasion:
    def __init__(self, settings, ship, bullet,aliens):
        self.aliens = aliens
        self.ship = ship
        self.settings = settings
        self.bullet = bullet
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # Utworzenie okienka gry
        self.spaceship_position = \
            pygame.rect.Rect(265, 680, self.settings.spaceship_img.get_width(), self.settings.spaceship_img.get_height())

    def run_game(self):
        pygame.init()  # Inicjalizacja gry
        pygame.display.set_caption("Inwazja obcych")
        bullets = []
        x = 50
        y = 50
        aliens = self.aliens.create_aliens()
        while True:
            pygame.time.Clock().tick(60)  # Maksymalne FPS
            spaceship_rect = self.ship.get_ship_rect()
            # alien_rect = self.aliens.get_alien_rect(aliens)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Wyłączanie gry, jeśli klikniemy X
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(Bullet(self.ship.rect_start_x_position + 36, self.ship.rect_start_y_position,
                                              self.settings))

            self.screen.blit(self.settings.bg, (0, 0))  # rysowanie tła
            self.screen.blit(self.settings.spaceship_img, spaceship_rect)  # wstawianie obrazka (obrazek,pozycja)

            self.bullet.get_bullet_rect(bullets)  # robienie i rysowanie pocisku
            self.bullet.change_bullet_position(bullets)

            self.aliens.get_alien_rect(aliens)
            self.aliens.alien_movement()

            pygame.display.update()  # Wyswietlenie ostatnio zmodyfikowanego ekranu

# class


class Aliens():
    def __init__(self, alien_x_position, alien_y_position, settings):
        self.image = pygame.image.load("images/alien" + str(random.randint(1, 2)) + ".png")
        self.image_width = self.image.get_width()
        self.image_height = self.image.get_height()
        self.alien_x_position = alien_x_position
        self.alien_y_position = alien_y_position
        self.settings = settings
        self.row = 2
        self.cols = 3
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.aliens = []
        self.move_direction = 1

    def create_aliens(self):
        self.aliens = []
        for row in range(self.row):
            for item in range(self.cols):
                alien = Aliens(100 + item * 150, 50 + row * 150, self.settings)
                self.aliens.append(alien)
        return self.aliens

    def get_alien_rect(self,aliens):
        for alien in aliens:
            alien_position = pygame.rect.Rect(alien.alien_x_position, alien.alien_y_position,
                                                   self.image_width, self.image_height)
            self.screen.blit(self.image, alien_position)

    def alien_movement(self):
        for alien in self.aliens:
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


class Bullet:
    def __init__(self, bullet_x_start_position, bullet_y_start_position, settings):
        self.bullet_x_start_position = bullet_x_start_position
        self.bullet_y_start_position = bullet_y_start_position
        self.settings = settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

    def get_bullet_rect(self, bullets):
        for bullet in bullets:
            bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                               self.settings.bullet_width,
                                               self.settings.bullet_height)
            pygame.draw.rect(self.screen, self.settings.bullet_color, bullet_position)

    def change_bullet_position(self,bullets):
        for bullet in bullets:
            bullet.bullet_y_start_position -= 7
            if bullet.bullet_y_start_position <= 0:
                bullets.pop(bullets.index(bullet))


def main():
    game = AlienInvasion(settings=Settings(), ship=Ship(Settings()),bullet=Bullet(0, 0, Settings()),aliens=Aliens(0,0,Settings()))
    game.run_game()


if __name__ == "__main__":
    main()




