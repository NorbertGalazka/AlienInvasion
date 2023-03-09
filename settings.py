import pygame
from dataclasses import dataclass


@dataclass
class GameSettings:
    background = pygame.image.load("images\space.png")
    screen_width = 589
    screen_height = 793
    screen = pygame.display.set_mode((screen_width, screen_height))
    left_edge_of_the_screen = 0
    game_over_image = pygame.image.load("images/game_over.png")
    restart_image = pygame.image.load("images/restart_image.png")
    restart_image_hovered = pygame.image.load("images/restart_grey_bcg.png")
    start_game_image = pygame.image.load("images/start_game.png")
    start_game_hovered =pygame.image.load("images/start_game_bcg.png")
    you_win_image = pygame.image.load("images/you_win_r_bg.png")


@dataclass
class AlienSettings:
    alien_columns = 3
    alien_rows = 2
    alien_cooldown = 500


@dataclass
class ShipSettings:
    spaceship_img = pygame.image.load("images\spaceship-removebg-preview.png")
    rect_width = spaceship_img.get_width()
    rect_height = spaceship_img.get_height()
    speed = 5


@dataclass
class ShipBulletSettings:
    bullet_speed = 9
    bullet_width = 5
    bullet_height = 15
    bullet_color = (255, 128, 0)
    bullet_start_x = 300
    bullet_start_y = 750


@dataclass
class AlienBulletSettings:
    bullet_speed = 10
    bullet_width = 7
    bullet_height = 7
    bullet_color = (255, 255, 100)
    bullet_start_x = 300
    bullet_start_y = 750


@dataclass
class BossSettings:
    boss_img = pygame.image.load("images\\little_boss.png")
    rect_width = boss_img.get_width()
    rect_height = boss_img.get_height()
    boss_speed = 0.5
    boss_hp = 20


@dataclass
class ExplosionSettings:
    image = pygame.image.load("images/burst2.png")
    image_height = image.get_height()
    image_width = image.get_width()


@dataclass
class SoundsSettings:
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    explosion_fx = pygame.mixer.Sound("sounds/explosion1.wav")
    explosion_fx.set_volume(0.15)
    laser_sound = pygame.mixer.Sound("sounds/laser.wav")
    laser_sound.set_volume(0.15)
    small_explosion_sound = pygame.mixer.Sound("sounds/explosion2.wav")
    small_explosion_sound.set_volume(0.2)
    game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")
    game_over_sound.set_volume(0.15)
    win_game_sound = pygame.mixer.Sound("sounds/you_win.wav")
    win_game_sound.set_volume(0.15)
