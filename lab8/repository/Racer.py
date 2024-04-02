#Imports
import pygame
from pygame.locals import *
import random, time

#Initialize
pygame.init()

Width = 400
Height = 600

#Setting up FPS
FPS = 60
clock = pygame.time.Clock()

score = 0
speed = 5

#Setting up colors
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

#Setting up font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

crash_sound = "/Users/frl404/Documents/Codes/PP2/lab8/repository/resources/crash.wav"
bg = pygame.image.load("./resources/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((Width, Height))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Game")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < Width:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Width - 40), 0)

    def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, Width - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("./resources/coin.png")
        self.image = pygame.transform.scale(self.original_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, Width - 40), 0)
        self.collected = False
    def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, Width - 40), 0)
            self.collected = False
#Setting up sprites 
p1 = Player()
e1 = Enemy()
c1 = Coin()

#Creating sprites groups
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1, e1, c1)
coins = pygame.sprite.Group()
coins.add(c1)

#Creating a new user event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game loop
done = False

while not done:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        
    DISPLAYSURF.blit(bg, (0, 0))
    scores = font_small.render(str(score), True, black)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image,entity.rect)

    for coin in coins:
        if pygame.sprite.collide_rect(p1, coin) and not coin.collected:
            coin.collected = True
            score += 1
    
    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound(crash_sound).play()
        time.sleep(1)

        DISPLAYSURF.fill(red)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
    
    for coin in coins:
        if pygame.sprite.spritecollideany(coin, enemies):
            coin.rect.center = (random.randint(40, Width - 40), 0)

    pygame.display.update()
    clock.tick(FPS)