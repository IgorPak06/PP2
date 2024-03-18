import pygame

pygame.init()

height = 800
width = 800
screen = pygame.display.set_mode((width, height))

red = (255, 0, 0)

x = 400
y = 400

r = 25

speed = 20
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_UP]:
        y -= speed

    ball_x = max(r, min(x, width - r))
    ball_y = max(r, min(y, height - r))
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, red, (ball_x, ball_y), r, 0, False, False, False, False)
    pygame.display.flip()
    clock.tick(60)