import pygame
import sys
from settings import Settings


class AlienInvasion:
    def __init__(self,settings):
        self.settings = settings   # Przypisanie ustawień z klasy Settings do zmiennej

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) # Utworzenie zmiennej, oraz utworzenie okienka gry


    def run_game(self):
        pygame.init()   # Inicjalizacja gry

        pygame.display.set_caption("Inwazja obcych")   # Nagłówek

        ship = Ship(Settings())

        while True:
            pygame.time.Clock().tick(60) # Maksymalne FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Wyłączanie gry, jeśli klikniemy X
                    sys.exit()

            self.screen.fill((230, 0, 0))  # Rysowanie tła

            spaceship_position = ship.movement() # Przypisanie pozycji i rozmiaru prostokąta do zmiennej

            pygame.draw.rect(self.screen,(0,230,0),spaceship_position)    # Rysowanie prostokąta (wybrany ekran,
                                                                # kolor prostokąta, wybrany prostokąt i jego położenie)

            pygame.display.update()  # Wyswietlenie ostatnio zmodyfikowanego ekranu


class Ship(AlienInvasion):
    def __init__(self,settings):
        super().__init__(settings)
        self.speed = 10
        self.rect_x_position = 265
        self.rect_y_position = 680
        self.rect_width = 60
        self.rect_heigth = 60


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect_x_position -= self.speed
            if self.rect_x_position < -self.rect_width:  # jeśli pozycja jest mniejsza kwadrat przenosi się na:
                self.rect_x_position = 589  # prawą krawędź okna

        if keys[pygame.K_RIGHT]:
            self.rect_x_position += self.speed
            if self.rect_x_position > 589:    # jeśli pozycja x kwadratu przekracza szerokość okna (589) to zmień ją na:
                self.rect_x_position = 0    # lewą krawędź okna (x = 0)

        if keys[pygame.K_UP]:
            self.rect_y_position -= self.speed
            if self.rect_y_position < - self.rect_heigth:
                self.rect_y_position = 793

        if keys[pygame.K_DOWN]:
            self.rect_y_position += self.speed
            if self.rect_y_position > 793:
                self.rect_y_position = 0

        return pygame.rect.Rect(self.rect_x_position, self.rect_y_position, self.rect_width, self.rect_heigth)   # tworzenie prostokąta (2 pierwsze zmienne to jego położenie),
                                                                                    # (2 pozostałe to rozmiar)



game = AlienInvasion(Settings())
game.run_game()




