import pygame
from settings import GameSettings


class LostGameButton:
    def __init__(self):
        self.restart_image = pygame.image.load("images/restart_image.png")
        self.restart_image_hovered = pygame.image.load("images/restart_grey_bcg.png")
        self.restart_button_x_cord = 100
        self.restart_button_y_cord = 360

    def restart_button_is_pressed(self):
        restart_image_hitbox = pygame.Rect(self.restart_button_x_cord, self.restart_button_y_cord,
                                           self.restart_image.get_width(), self.restart_image.get_height())

        if restart_image_hitbox.collidepoint(pygame.mouse.get_pos()):
            GameSettings.screen.blit(self.restart_image_hovered, (self.restart_button_x_cord, self.restart_button_y_cord))
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            GameSettings.screen.blit(self.restart_image, (self.restart_button_x_cord, self.restart_button_y_cord))


class MainMenuButton:
    def __init__(self):
        self.start_game_button_x_cord = 100
        self.start_game_button_y_cord = 300
        self.start_game_hitbox = pygame.Rect(self.start_game_button_x_cord,self.start_game_button_y_cord,
                                             GameSettings.start_game_image.get_width(),GameSettings.start_game_image.get_height())

    def menu_button_is_pressed(self):
        if self.start_game_hitbox.collidepoint(pygame.mouse.get_pos()):
            GameSettings.screen.blit(GameSettings.start_game_hovered,
                                     (self.start_game_button_x_cord, self.start_game_button_y_cord))
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            GameSettings.screen.blit(GameSettings.start_game_image,
                                     (self.start_game_button_x_cord, self.start_game_button_y_cord))
