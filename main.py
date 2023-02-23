import time
import pygame
import sys
import random
from settings import GameSettings, ShipBulletSettings,AlienBulletSettings, AlienSettings,\
    ShipSettings, BossSettings, ExplosionSettings
from Ship import Ship, SpaceshipBullet
from Alien import Alien, AlienBullet
from Boss import BossAlien, BossAlienBullet
from Buttons import LostGameButton, MainMenuButton
from Explosion import Explosion


class AlienInvasion:
    def __init__(self, alien):
        self.alien = alien
        self.ship = Ship()
        self.boss = BossAlien(0, 0)
        self.bullet = SpaceshipBullet(0, 0)
        self.alien_bullet = AlienBullet(0, 0)
        self.lost_game_button = LostGameButton()
        self.main_menu_button = MainMenuButton()
        self.last_alien_shot = pygame.time.get_ticks()
        self.explosion = Explosion(0,0,0,1)
        self.draw_times = 0
        self.x = 0
        self.y = 0

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

    def boss_shot(self, time_now, boss_bullets,boss):
        if time_now - self.last_alien_shot > AlienSettings.alien_cooldown:

            attacking_alien = boss
            shot_directions = [7, -7, 0]
            shot_directions_without_zero = [7, 7]
            first_direction = random.choice(shot_directions)
            if first_direction == 0:
                second_direction = random.choice(shot_directions_without_zero)
            else:
                second_direction = random.choice(shot_directions)
            boss_bullet = BossAlienBullet(attacking_alien.boss_start_x_position + 34,
                                          attacking_alien.boss_start_y_position + 60,
                                          first_direction, second_direction)
            boss_bullets.append(boss_bullet)
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
                    return True, alien_position

    def alien_bullet_collision_spaceship(self, alien_bullets, spaceship_position):
        for alien_bullet in alien_bullets:
            alien_bullet_position = pygame.rect.Rect(alien_bullet.bullet_x_start_position,
                                                     alien_bullet.bullet_y_start_position,
                                                     AlienBulletSettings.bullet_width,
                                                     AlienBulletSettings.bullet_height)

            if alien_bullet_position.colliderect(spaceship_position):
                alien_bullets.remove(alien_bullet)

                # explosion = Explosion(spaceship_position[0],spaceship_position[1],0,1)

                return False

    def spacebullet_collision_boss_alien(self, bullets, boss_position):
        for bullet in bullets:
            bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position,
                                               bullet.bullet_y_start_position,
                                               ShipBulletSettings.bullet_width, ShipBulletSettings.bullet_height)
            if boss_position.colliderect(bullet_position):
                bullets.remove(bullet)
                self.boss.boss_hp -= 1
            if self.boss.boss_hp <= 0:
                self.boss.boss_hp = BossSettings.boss_hp
                return True

    def you_win_menu(self):
        self.lost_game_button.restart_button_x_cord = 100
        self.lost_game_button.restart_button_y_cord = 600
        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            GameSettings.screen.blit(GameSettings.bg, (0, 0))
            GameSettings.screen.blit(GameSettings.you_win_image, (46, 220))
            if self.lost_game_button.restart_button_is_pressed():
                self.run_game()
            pygame.display.update()

    def restart_game_menu(self):
        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            GameSettings.screen.blit(GameSettings.bg, (0, 0))
            GameSettings.screen.blit(GameSettings.game_over_image, (200, 130))
            if self.lost_game_button.restart_button_is_pressed():
                self.run_game()
            pygame.display.update()

    def second_round(self):
        bullets = []
        boss_bullets = []
        boss = BossAlien(250, 50)

        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(SpaceshipBullet(self.ship.rect_start_x_position + ShipSettings.rect_width / 2.15,
                                                       self.ship.rect_start_y_position))

            time_now = pygame.time.get_ticks()

            GameSettings.screen.blit(GameSettings.bg, (0, 0))

            spaceship_position = self.ship.get_ship_rect()
            spaceship_x_position = spaceship_position[0]
            spaceship_y_position = spaceship_position[1]

            boss_position = boss.get_boss_rect(spaceship_x_position, spaceship_y_position)

            self.bullet.get_bullet_rect(bullets)
            self.bullet.change_bullet_position(bullets)

            self.boss_shot(time_now, boss_bullets, boss)

            for bullet in boss_bullets:
                bullet.get_boss_alien_bullet_rect(bullet)
                bullet.change_boss_alien_bullet_position()
                if bullet.bullet_y_start_position > 1000 or bullet.bullet_y_start_position < 0 \
                        or bullet.bullet_x_start_position < 0 or bullet.bullet_x_start_position > 700:
                    boss_bullets.remove(bullet)

            if boss_position.colliderect(spaceship_position):
                self.restart_game_menu()

            if self.spacebullet_collision_boss_alien(bullets, boss_position):
                self.you_win_menu()

            is_game_started = self.alien_bullet_collision_spaceship(boss_bullets, spaceship_position)

            if is_game_started is None:
                pygame.display.update()
            else:
                self.restart_game_menu()

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Inwazja obcych")

        bullets = []
        aliens = []
        alien_bullets = []

        list_of_explosion = []

        self.create_aliens(aliens)
        index = 0
        loop_times = 0
        while True:
            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(SpaceshipBullet(self.ship.rect_start_x_position + ShipSettings.rect_width / 2.15,
                                                       self.ship.rect_start_y_position))

            time_now = pygame.time.get_ticks()

            GameSettings.screen.blit(GameSettings.bg, (0, 0))
            spaceship_position = self.ship.get_ship_rect()

            self.bullet.get_bullet_rect(bullets)
            self.bullet.change_bullet_position(bullets)

            self.alien.get_alien_rect(aliens)
            self.alien.alien_movement(aliens)

            self.alien_bullet.get_alien_bullet_rect(alien_bullets)
            self.alien_shot(time_now, aliens, alien_bullets)
            self.alien_bullet.change_alien_bullet_position(alien_bullets)

            colision = self.remove_alien_spaceship_bullet_if_collision(aliens, bullets)
            # print(colision)

            if colision:
                self.x = colision[1][0]
                self.y = colision[1][1]
                burst = Explosion(self.x, self.y, 15, 1)
                list_of_explosion.append(burst)

            for explosion in list_of_explosion:
                explosion.get_explosion_rect(index)
                loop_times += 1
                if loop_times == 4:
                    index += 1
                    loop_times = 0
            if index == 4:
                index = 0
                list_of_explosion.remove(explosion)
            print(list_of_explosion)

            is_game_started = self.alien_bullet_collision_spaceship(alien_bullets, spaceship_position)

            if is_game_started is None:
                pygame.display.update()
            else:
                self.restart_game_menu()
            if len(aliens) == 0:
                time.sleep(0.3)
                self.second_round()

    def main_menu(self):
        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            GameSettings.screen.blit(GameSettings.bg, (0, 0))
            if self.main_menu_button.menu_button_is_pressed():
                self.run_game()
            pygame.display.update()


def main():
    game = AlienInvasion(alien=Alien(0, 0))

    game.main_menu()


if __name__ == "__main__":
    main()




