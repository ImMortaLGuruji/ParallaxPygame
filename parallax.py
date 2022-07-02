import pygame
from config import *


class ParallaxBackground():
    def __init__(self):
        self.layers = []

        for num in range(2, 6):
            layer = pygame.image.load(f'img/{num}.png').convert_alpha()
            self.layers.append(layer)

        self.layerWidth = 768
        self.x = 0

    def update(self):
        x2 = self.x % self.layerWidth

        for layer in self.layers:
            screen.blit(layer, (x2 - self.layerWidth, 0))

        for layer in self.layers:
            if x2 <= self.layerWidth:
                screen.blit(layer, (x2, 0))


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Parallax')

clock = pygame.time.Clock()

bg = pygame.image.load('img/1.png').convert_alpha()

parallaxBackground = ParallaxBackground()

running = True
while running:
    screen.blit(bg, (0, 0))

    parallaxBackground.update()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        parallaxBackground.x += 5
    if key[pygame.K_RIGHT]:
        parallaxBackground.x -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
