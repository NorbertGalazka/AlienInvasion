import random

import pygame

from random import randint

pygame.init()
window = pygame.display.set_mode((800,600))

class Player():
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("images/spaceship-removebg-preview.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 6
        self.hitbox = pygame.rect.Rect(self.x_cord, self.y_cord,self.width,self.height)


    def tick(self,keys):
        if keys[pygame.K_RIGHT]:
            self.x_cord += self.speed
            if self.x_cord > 800:
                self.x_cord = -40
        if keys[pygame.K_LEFT]:
            self.x_cord -= self.speed
            if self.x_cord < -40:
                self.x_cord = 800
        if keys[pygame.K_DOWN]:
            self.y_cord += self.speed
        if keys[pygame.K_UP]:
            self.y_cord -= self.speed

        self.hitbox = pygame.rect.Rect(self.x_cord, self.y_cord, self.width, self.height)


    def draw(self):
        window.blit(self.image,(self.x_cord,self.y_cord))


class Cash():
    def __init__(self):
        self.x_cord = random.randint(0,800)
        self.y_cord = random.randint(0,600)
        self.image = pygame.image.load("images/spaceship.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.rect.Rect(self.x_cord, self.y_cord, self.width, self.height)


    def tick(self):
        self.hitbox = pygame.rect.Rect(self.x_cord, self.y_cord, self.width, self.height)


    def draw(self):
        window.blit(self.image,(self.x_cord,self.y_cord))



def main():
    player = Player()
    clock = 0
    banknotes = []

    run = True
    while run:
        clock += pygame.time.Clock().tick(60) / 1000 #max fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if clock >=3:
            clock = 0
            banknotes.append(Cash())
        player.tick(keys)
        for banknote in banknotes:
            banknote.tick()

        for banknote in banknotes:
            if player.hitbox.colliderect(banknote.hitbox):
                banknotes.remove(banknote)
        window.fill((0,200,200)) #rysowanie tła
        player.draw()
        for banknote in banknotes:
            banknote.draw()
        pygame.display.update() #odświeżanie ekranu

if __name__ == "__main__":
    main()