import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pygame Docker Example")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(200, 200, 200, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
