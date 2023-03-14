import pygame
pygame.init()

monitor = pygame.display.set_mode((500, 500 ))
pygame.display.set_caption("TSIS7")
check = True
while check:
    #monitor.fill(177,252,3)
    pygame.draw.circle(monitor, 'White', (50, 50), 25)
    """
    pygame.draw.circle(monitor, 'Red', (100, 50), 25)
    pygame.draw.circle(monitor, 'Blue', (150, 50), 25)
    pygame.draw.circle(monitor, 'Green', (200, 50), 25)
    pygame.draw.circle(monitor, 'Purple', (250, 50), 25)
    pygame.draw.circle(monitor, 'Orange', (300, 50), 25)
    pygame.draw.circle(monitor, 'Black', (0, 50), 25)
    """
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
