import random

import pygame
from attractor import Attractor
from mover import Mover

movers = []
attractor = None


def setup():
    global movers, attractor
    screen = pygame.display.set_mode((800, 600))
    width, height = screen.get_width(), screen.get_height()
    for _ in range(20):
        movers.append(
            Mover(
                screen,
                random.random() * width,
                random.random() * height,
                random.random() * 1.9 + 0.1,
            )
        )
    attractor = Attractor(screen)
    return screen


def draw(screen):
    global attractor, movers, mousePressed, running
    screen.fill((255, 255, 255))

    # 여기에 코드 작성


if __name__ == "__main__":
    pygame.init()
    screen = setup()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(screen)

        pygame.display.flip()
        clock.tick(60)
