import pygame

def setup():
    screen = pygame.display.set_mode((800, 600))
    return screen


def draw(screen: pygame.Surface):
    pass

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    screen = setup()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw(screen)

        pygame.display.flip()
        clock.tick(60)
