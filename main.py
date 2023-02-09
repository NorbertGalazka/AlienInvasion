import pygame
import sys
import random
from settings import GameSettings
from settings import ShipBulletSettings
from settings import AlienBulletSettings
from settings import AlienSettings
from settings import ShipSettings


class AlienInvasion:
    def __init__(self, alien):
        self.alien = alien
        self.ship = Ship()
        self.bullet = SpaceshipBullet(0, 0)
        self.alien_bullet = AlienBullet(0, 0)
        self.last_alien_shot = pygame.time.get_ticks()

    def create_aliens(self, aliens):
        for row in range(AlienSettings.alien_rows):  # Utworzenie obcych
            for amount in range(AlienSettings.alien_columns):
                alien = Alien(100 + amount * 150, 50 + row * 150)  # Alien(x_pos,y_pos,sett)
                aliens.append(alien)

    def alien_shot(self, time_now, aliens, alien_bullets):
        if time_now - self.last_alien_shot > AlienSettings.alien_cooldown and len(aliens) > 0:
            attacking_alien = random.choice(aliens)
            alien_bullet = AlienBullet(attacking_alien.alien_x_position + 34, attacking_alien.alien_y_position + 60)
            alien_bullets.append(alien_bullet)
            self.last_alien_shot = time_now

    def remove_alien_spaceship_bullet_if_collision(self, aliens, bullets):
        for alien in aliens:
            for bullet in bullets:
                alien_position = pygame.rect.Rect(alien.alien_x_position, alien.alien_y_position,
                                                  self.alien.image_width,
                                                  self.alien.image_height)
                bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position, bullet.bullet_y_start_position,
                                                   ShipBulletSettings.bullet_width,
                                                   ShipBulletSettings.bullet_height)
                if bullet_position.colliderect(alien_position):
                    aliens.remove(alien)
                    bullets.remove(bullet)

    def alien_bullet_collision_spaceship(self, alien_bullets, spaceship_position):
        for alien_bullet in alien_bullets:
            alien_bullet_position = pygame.rect.Rect(alien_bullet.bullet_x_start_position,
                                                     alien_bullet.bullet_y_start_position,
                                                     AlienBulletSettings.bullet_width,
                                                     AlienBulletSettings.bullet_height)

            if alien_bullet_position.colliderect(spaceship_position):
                alien_bullets.remove(alien_bullet)
                return False

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Inwazja obcych")

        bullets = []
        aliens = []
        alien_bullets = []

        self.create_aliens(aliens)

        while True:
            pygame.time.Clock().tick(60)  # Maksymalne FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Wyłączanie gry, jeśli klikniemy X
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(SpaceshipBullet(self.ship.rect_start_x_position + ShipSettings.rect_width / 2.15,
                                                       self.ship.rect_start_y_position))

            time_now = pygame.time.get_ticks()

            GameSettings.screen.blit(GameSettings.bg, (0, 0))  # rysowanie tła
            spaceship_position = self.ship.get_ship_rect()

            self.bullet.get_bullet_rect(bullets)  # robienie i rysowanie pocisku
            self.bullet.change_bullet_position(bullets)

            self.alien.get_alien_rect(aliens)
            self.alien.alien_movement(aliens)

            self.alien_bullet.get_alien_bullet_rect(alien_bullets)
            self.alien_shot(time_now, aliens, alien_bullets)
            self.alien_bullet.change_alien_bullet_position(alien_bullets)

            self.remove_alien_spaceship_bullet_if_collision(aliens, bullets)

            is_game_started = self.alien_bullet_collision_spaceship(alien_bullets, spaceship_position)

            if is_game_started is None:
                pygame.display.update()  # Wyświetlenie ostatnio zmodyfikowanego ekranu
            else:
                break


class Alien:
    def __init__(self, alien_x_position, alien_y_position):
        self.image = pygame.image.load("images/alien" + str(random.randint(1, 2)) + ".png")
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

    def get_ship_rect(self):
        spaceship_x_position, spaceship_y_position = self.get_spaceship_position()
        spaceship_position = pygame.rect.Rect(spaceship_x_position, spaceship_y_position, ShipSettings.rect_width,
                                              ShipSettings.rect_height)
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


def main():
    game = AlienInvasion(alien=Alien(0, 0))

    game.run_game()


if __name__ == "__main__":
    main()




