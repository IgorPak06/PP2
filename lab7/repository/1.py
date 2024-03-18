import pygame
from datetime import datetime

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
image = pygame.image.load("main-clock.png")
image_left = pygame.image.load("left-hand.png")
image_right = pygame.image.load("right-hand.png")

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    screen.blit(rotated_image, rotated_image_rect)

def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

rotated_image_right = pygame.transform.rotate(image_right, 90)
rotated_image_left = pygame.transform.rotate(image_left, 90)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    current_time = datetime.now()
    minute = current_time.minute
    second = current_time.second
    
    minute_angle = 360 * (minute / 60)
    second_angle = 360 * (second / 60)

    pos = (330, 125)
    pos2 = (310, 190)

    screen.fill((255, 255, 255))
    screen.blit(pygame.transform.scale(image, (800, 800)), (0, 0))
    blitRotate2(screen, rotated_image_right, pos2, minute_angle)
    blitRotate2(screen, rotated_image_left, pos, second_angle)
    pygame.display.flip()
    clock.tick(60)
