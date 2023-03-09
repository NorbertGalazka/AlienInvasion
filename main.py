import time
import pygame
import sys
import random
import Sounds
import settings
from settings import GameSettings, ShipBulletSettings,AlienBulletSettings, AlienSettings,\
    ShipSettings, BossSettings
from Ship import Ship, SpaceshipBullet
from Alien import Alien, AlienBullet
from Boss import BossAlien, BossAlienBullet
from Buttons import LostGameButton, MainMenuButton
from Explosion import Explosion
from Sounds import Sounds
from boss_hp_rect import BossHp


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
        self.sound = Sounds()

    def create_aliens(self, aliens):
        for row in range(AlienSettings.alien_rows):
            for amount in range(AlienSettings.alien_columns):
                alien = Alien(100 + amount * 150, 50 + row * 150)
                aliens.append(alien)

    def restart_game_menu(self):
        self.lost_game_button.restart_button_x_cord = 100
        self.lost_game_button.restart_button_y_cord = 360
        self.sound.play_game_over_sound()
        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            GameSettings.screen.blit(GameSettings.background, (0, 0))
            GameSettings.screen.blit(GameSettings.game_over_image, (200, 130))
            if self.lost_game_button.restart_button_is_pressed():
                self.run_game()
            pygame.display.update()

    def alien_shot(self, time_now, aliens, alien_bullets):
        if time_now - self.last_alien_shot > AlienSettings.alien_cooldown and len(aliens) > 0:
            attacking_alien = random.choice(aliens)
            alien_bullet = AlienBullet(attacking_alien.alien_x_position + 34, attacking_alien.alien_y_position + 60)
            alien_bullets.append(alien_bullet)
            self.last_alien_shot = time_now

    def boss_shot(self, time_now, boss_bullets, boss):
        if time_now - self.last_alien_shot > AlienSettings.alien_cooldown:
            attacking_alien = boss
            shot_directions = [7, -7, 0]
            shot_directions_without_zero = [7, -7]
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

    def remove_alien_and_spaceship_bullet_if_collision(self, aliens, bullets):
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
                    self.sound.play_explosion_sound()
                    return True, alien_position

    def alien_bullet_collision_spaceship(self, alien_bullets, spaceship_position):
        for alien_bullet in alien_bullets:
            alien_bullet_position = pygame.rect.Rect(alien_bullet.bullet_x_start_position,
                                                     alien_bullet.bullet_y_start_position,
                                                     AlienBulletSettings.bullet_width,
                                                     AlienBulletSettings.bullet_height)
            if alien_bullet_position.colliderect(spaceship_position):
                alien_bullets.remove(alien_bullet)
                return True

    def draw_explosion(self, list_of_explosion, index_of_image, loop_times):
        for explosion in list_of_explosion:
            explosion.get_explosion_rect(index_of_image)
            loop_times += 1
            if loop_times == 2:
                index_of_image += 1
                loop_times = 0
            if index_of_image == 5:
                index_of_image = 0
                list_of_explosion.remove(explosion)
        return index_of_image, loop_times

    def alien_collision_spaceship(self, aliens, spaceship_position):
        for alien in aliens:
            alien_position = pygame.rect.Rect(alien.alien_x_position, alien.alien_y_position,
                                              alien.image_width, alien.image_height)
            if alien_position.colliderect(spaceship_position):
                aliens.remove(alien)
                return True

    def boss_collision_spaceship(self, boss_position, spaceship_position, boss_explosion):
        if boss_position.colliderect(spaceship_position):
            collision_x_pos = boss_position[0]
            collision_y_pos = boss_position[1]
            explosion = Explosion(collision_x_pos, collision_y_pos, 4)
            boss_explosion.append(explosion)
            self.boss.boss_hp = BossSettings.boss_hp

    def spacebullet_collision_boss_alien(self, bullets, boss_position, list_of_explosion, win_boss_explosion):
        for bullet in bullets:
            bullet_position = pygame.rect.Rect(bullet.bullet_x_start_position,
                                               bullet.bullet_y_start_position,
                                               ShipBulletSettings.bullet_width, ShipBulletSettings.bullet_height)
            if boss_position.colliderect(bullet_position):
                bullets.remove(bullet)
                collision_x_pos = bullet_position[0]
                collision_y_pos = bullet_position[1]
                explosion = Explosion(collision_x_pos, collision_y_pos, 2)
                list_of_explosion.append(explosion)
                self.boss.boss_hp -= 1
                self.sound.play_small_explosion_sound()
            if self.boss.boss_hp <= 0:
                self.sound.play_explosion_sound()
                boss_explosion = Explosion(boss_position[0], boss_position[1], 4)
                win_boss_explosion.append(boss_explosion)
                self.boss.boss_hp = BossSettings.boss_hp
                return True

    def explosion_if_collision(self, collision, list_of_explosion):
        explosion_size = 1
        if collision:
            collision_x_pos = collision[1][0]
            collision_y_pos = collision[1][1]
            explosion = Explosion(collision_x_pos, collision_y_pos, explosion_size)
            list_of_explosion.append(explosion)

    def you_win_menu(self):
        self.lost_game_button.restart_button_x_cord = 100
        self.lost_game_button.restart_button_y_cord = 600
        self.sound.play_win_game_sound()
        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            GameSettings.screen.blit(GameSettings.background, (0, 0))
            GameSettings.screen.blit(GameSettings.you_win_image, (46, 220))
            if self.lost_game_button.restart_button_is_pressed():
                self.run_game()
            pygame.display.update()

    def remove_distant_boss_bullets(self, boss_bullets):
        edge_of_the_screen = 0
        for bullet in boss_bullets:
            bullet.get_boss_alien_bullet_rect(bullet)
            bullet.change_boss_alien_bullet_position()
            if bullet.bullet_y_start_position > settings.GameSettings.screen_height \
                    or bullet.bullet_y_start_position < edge_of_the_screen \
                    or bullet.bullet_x_start_position < edge_of_the_screen \
                    or bullet.bullet_x_start_position > settings.GameSettings.screen_width:
                boss_bullets.remove(bullet)

    def main_menu(self):
        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            GameSettings.screen.blit(GameSettings.background, (0, 0))
            if self.main_menu_button.menu_button_is_pressed():
                self.run_game()
            pygame.display.update()

    def second_round(self):
        bullets = []
        boss_bullets = []
        boss = BossAlien(250, 50)
        list_of_explosion = []
        image_index, image_index_1, image_index_2 = 0, 0, 0
        loop_times, loop_times1, loop_times2 = 0, 0, 0
        self.ship.rect_start_x_position = 265
        self.ship.rect_start_y_position = 680
        boss_explosion_during_coll = []
        win_boss_explosion = []
        hp_bar = BossHp()
        ship_is_alive = True
        ship_explosions = []
        loop_turns = 0

        while True:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(SpaceshipBullet(self.ship.rect_start_x_position + ShipSettings.rect_width / 2.15,
                                                       self.ship.rect_start_y_position))
                        self.sound.play_laser_sound()

            time_now = pygame.time.get_ticks()

            GameSettings.screen.blit(GameSettings.background, (0, 0))

            spaceship_position = self.ship.get_ship_rect(ship_is_alive)
            spaceship_x_position = spaceship_position[0]
            spaceship_y_position = spaceship_position[1]

            boss_position = boss.get_boss_rect(spaceship_x_position, spaceship_y_position)
            hp_bar.get_hp_bar_rect(boss_position[0] - 10, boss_position[1] - 30, self.boss.boss_hp)

            self.bullet.get_bullet_rect(bullets)
            self.bullet.change_bullet_position(bullets)

            self.boss_shot(time_now, boss_bullets, boss)
            self.remove_distant_boss_bullets(boss_bullets)

            self.boss_collision_spaceship(boss_position, spaceship_position, boss_explosion_during_coll)
            self.spacebullet_collision_boss_alien(bullets, boss_position, list_of_explosion, win_boss_explosion)

            image_index, loop_times = self.draw_explosion(list_of_explosion, image_index, loop_times)
            image_index_1, loop_times1 = self.draw_explosion(boss_explosion_during_coll, image_index_1, loop_times1)
            image_index_2, loop_times2 = self.draw_explosion(win_boss_explosion, image_index_2, loop_times2)
            if image_index_1 == 4:
                self.sound.play_explosion_sound()
                self.restart_game_menu()
            if image_index_2 == 4:
                self.you_win_menu()

            boss_bullet_coll_spaceship = self.alien_bullet_collision_spaceship(boss_bullets, spaceship_position)

            if boss_bullet_coll_spaceship is True:
                ship_is_alive = False
                burst_size = 3
                self.sound.play_explosion_sound()
                ship_explosion = Explosion(spaceship_x_position, spaceship_y_position, burst_size)
                ship_explosions.append(ship_explosion)
                loop_turns = 12
            if boss_bullet_coll_spaceship is None:
                pygame.display.update()
            if loop_turns:
                image_index, loop_times = self.draw_explosion(ship_explosions, image_index, loop_times)
                loop_turns -= 1
            if loop_turns == 1:
                self.restart_game_menu()

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Inwazja obcych")
        bullets = []
        aliens = []
        alien_bullets = []
        alien_explosions = []
        ship_explosions = []
        self.create_aliens(aliens)
        loop_turns = 0
        image_index = 0
        loop_times = 0
        loop_rotation_after_last_explosion = 0
        self.ship.rect_start_x_position = 265
        self.ship.rect_start_y_position = 680
        ship_is_alive = True

        while True:
            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and len(bullets) < 5:
                    if event.key == pygame.K_SPACE:
                        bullets.append(SpaceshipBullet(self.ship.rect_start_x_position + ShipSettings.rect_width / 2.15,
                                                       self.ship.rect_start_y_position))
                        self.sound.play_laser_sound()

            time_now = pygame.time.get_ticks()

            GameSettings.screen.blit(GameSettings.background, (0, 0))

            spaceship_position = self.ship.get_ship_rect(ship_is_alive)
            spaceship_x_pos = spaceship_position[0]
            spaceship_y_pos = spaceship_position[1]

            self.bullet.get_bullet_rect(bullets)
            self.bullet.change_bullet_position(bullets)

            self.alien.get_alien_rect(aliens)
            if self.alien.alien_movement(aliens):
                self.restart_game_menu()

            self.alien_bullet.get_alien_bullet_rect(alien_bullets)
            self.alien_shot(time_now, aliens, alien_bullets)
            self.alien_bullet.change_alien_bullet_position(alien_bullets)

            alien_and_spaceship_bullet_coll = self.remove_alien_and_spaceship_bullet_if_collision(aliens, bullets)
            self.explosion_if_collision(alien_and_spaceship_bullet_coll, alien_explosions)
            image_index, loop_times = self.draw_explosion(alien_explosions, image_index, loop_times)

            alien_bullet_coll_spaceship = self.alien_bullet_collision_spaceship(alien_bullets, spaceship_position)
            alien_coll_spaceship = self.alien_collision_spaceship(aliens, spaceship_position)

            if alien_bullet_coll_spaceship or alien_coll_spaceship is True:
                ship_is_alive = False
                burst_size = 3
                if alien_coll_spaceship is True:
                    burst_size = 4
                self.sound.play_explosion_sound()
                ship_explosion = Explosion(spaceship_x_pos, spaceship_y_pos, burst_size)
                ship_explosions.append(ship_explosion)
                loop_turns = 12
            if loop_turns:
                image_index, loop_times = self.draw_explosion(ship_explosions, image_index, loop_times)
                loop_turns -= 1
            if loop_turns == 1:
                self.restart_game_menu()
            if alien_bullet_coll_spaceship is None:
                pygame.display.update()
            if len(aliens) == 0:
                loop_rotation_after_last_explosion += 1
            if loop_rotation_after_last_explosion == 30:
                time.sleep(0.3)
                self.second_round()


def main():
    game = AlienInvasion(alien=Alien(0, 0))
    game.main_menu()


if __name__ == "__main__":
    main()




