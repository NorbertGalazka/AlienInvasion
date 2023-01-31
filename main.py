import pygame
import sys
from settings import Settings


class AlienInvasion:
    def __init__(self, settings, ship, bullet):
        self.ship = ship
        self.settings = settings
        self.bullet = bullet
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # Utworzenie okienka gry
        self.spaceship_position = \
            pygame.rect.Rect(265, 680, self.settings.image.get_width(), self.settings.image.get_height())

    def run_game(self):
        pygame.init()  # Inicjalizacja gry
        pygame.display.set_caption("Inwazja obcych")
        bullets = []
        while True:
            pygame.time.Clock().tick(60)  # Maksymalne FPS
            spaceship_rect = self.ship.get_ship_rect()
            # (2 pierwsze zmienne to jego położenie),
            # (2 pozostałe to rozmiar)

            self.screen.blit(self.settings.image, spaceship_rect)  # wstawianie obrazka (obrazek,pozycja)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Wyłączanie gry, jeśli klikniemy X
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(Bullet(self.ship.rect_start_x_position + 36, self.ship.rect_start_y_position,
                                              self.settings))

            self.screen.blit(self.settings.bg, (0, 0))  # rysowanie tła
            self.screen.blit(self.settings.image, spaceship_rect)  # wstawianie obrazka (obrazek,pozycja)

            self.bullet.get_bullet_rect(bullets)  # robienie i rysowanie pocisku
            self.bullet.change_bullet_position(bullets)

            pygame.display.update()  # Wyswietlenie ostatnio zmodyfikowanego ekranu


class Ship:
    def __init__(self, settings):
        self.settings = settings
        self.speed = 5
        self.rect_start_x_position = 265
        self.rect_start_y_position = 680
        self.rect_width = self.settings.image.get_width()
        self.rect_height = self.settings.image.get_height()
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
        self.screen = self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

    def get_bullet_rect(self,bullets):
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
    game = AlienInvasion(settings=Settings(), ship=Ship(Settings()),bullet=Bullet(0, 0, Settings()))
    game.run_game()


if __name__ == "__main__":
    main()




