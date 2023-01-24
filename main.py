
import pygame
import sys

from settings import Settings
# from ship import Ship


class AlienInvasion:
    def __init__(self,settings):
        """Przypisanie ustawień z klasy Settings do zmiennej"""
        self.settings = settings

        """Utworzenie zmiennej, oraz utworzenie okienka gry"""
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))


    def run_game(self):
        """Inicjalizacja gry"""
        pygame.init()

        """Nagłówek"""
        pygame.display.set_caption("Inwazja obcych")

        x = 265
        y = 680

        # spaceship_postion = pygame.rect.Rect(x, y, 60, 60)
        while True:
            for event in pygame.event.get():
                """Wyłączanie gry, jeśli klikniemy X"""
                if event.type == pygame.QUIT:
                    sys.exit()


            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x -= 1
            if keys[pygame.K_RIGHT]:
                x += 1
            spaceship_postion = pygame.rect.Rect(x, y, 60, 60)

            # Ship().movement()

            """Rysowanie tła"""
            self.screen.fill((230,0,0))

            """Rysowanie prostokąta (wybrany ekran, kolor prostokąta, wybrany prostokąt i jego położenie)"""
            pygame.draw.rect(self.screen,(0,230,0),spaceship_postion)


            """Wyswietlenie ostatnio zmodyfikowanego ekranu"""
            pygame.display.update()
#
# class Ship(AlienInvasion):
#     def __init__(self):
#         """Położenie prostokąta (dwie piersze liczby), rozmiar prostokąta (dwie ostatnie)"""
#         x = 265
#         y = 680
#         self.spaceship_postion = pygame.rect.Rect(x, y, 60, 60)
#
#
#     def movement(self):
#         x = 265
#         y = 680
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             x -= 5
#         if keys[pygame.K_RIGHT]:
#             x += 5
#
#         self.spaceship_postion = pygame.rect.Rect(x, y, 60, 60)
#         pygame.draw.rect(self.screen,(0, 230, 0), self.spaceship_postion)


game = AlienInvasion(Settings())
game.run_game()




