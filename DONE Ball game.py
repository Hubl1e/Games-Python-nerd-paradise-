import pygame

pygame.init()

screen = pygame.display.set_mode((1900, 1000))

clock = pygame.time.Clock()

x = 100
y = 100
radius = 25
skorost = 20

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if y - radius - skorost >= 0:
            y -= skorost

    if pressed[pygame.K_DOWN]:
        if y + radius + skorost <= 1000:
            y += skorost

    if pressed[pygame.K_RIGHT]:
        if x + radius + skorost  <= 1900:
            x += skorost

    if pressed[pygame.K_LEFT]:
        if x - radius - skorost >= 0:
            x -= skorost

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0 ,0), (x,y), radius)


    pygame.display.flip()
    clock.tick(60)

