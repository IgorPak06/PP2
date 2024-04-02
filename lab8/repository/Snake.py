#Import 
import pygame
import random, time
import sys

pygame.init()

#Constants
width = 600
height = 600
border = 20
block = 20
speed = 10

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

#Setting up font
font = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

#Screen size and caption of screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

#Setting up by speed
clock = pygame.time.Clock()

#Classes
#Snake:
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width / 2), (height / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = green

    def head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
        
    def move(self):
        current = self.head_position()
        x, y = self.direction
        new = (((current[0] + (x * block)) % width), (current[1] + (y * block)) % height)
        #if len(self.positions) > 2 and new in self.positions[2:]:
            #self.reset()
        #else:
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    #def reset(self):
        #self.length = 1
        #self.positions = [((width / 2), (height / 2))]
        #self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw (self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (block, block))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, white, r, 1)

    def controller_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.turn(UP)
        elif keys[pygame.K_DOWN]:
            self.turn(DOWN)
        elif keys[pygame.K_LEFT]:
            self.turn(LEFT)
        elif keys[pygame.K_RIGHT]:
            self.turn(RIGHT)
#Food
class Food:
    def __init__(self):
        self.position = (0,0)
        self.color = red
        self.randomizer()

    def randomizer(self):
        while True:
            x = random.randint(border, width - border - block)
            y = random.randint(border, height - border - block)
            if (x % block == 0) and (y % block == 0):
                self.position = (x, y)
                break

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (block, block))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, white, r, 1)

def draw_border(surface):
    border_rect = pygame.Rect(0, 0, width, border)
    pygame.draw.rect(surface, white, border_rect)
    border_rect = pygame.Rect(0, 0, border, height)
    pygame.draw.rect(surface, white, border_rect)
    border_rect = pygame.Rect(0, height - border, width, border)
    pygame.draw.rect(surface, white, border_rect)
    border_rect = pygame.Rect(width - border, 0, border, height)
    pygame.draw.rect(surface, white, border_rect)

def game_over(score_renewable, level):
    text = font.render("Game Over!", True, white)
    text_rect = screen.blit(text, (160, height // 2 - 100))
    text_1 = font.render("Score: " + str(score_renewable), True, white)
    text_rect = screen.blit(text_1, (200, height // 2 - 50))
    text_2 = font.render("Level:  " + str(level), True, white)
    text_rect = screen.blit(text_2, (200, height // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()
#Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

#Initialization of classes
S1 = Snake()
F1 = Food()

score_renewable = 0
score = 0
level = 1

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    S1.controller_keys()
    S1.move()

    if S1.head_position() == F1.position:
        S1.length += 1
        score += 1
        score_renewable += 1
        F1.randomizer()

    if S1.head_position() in S1.positions[1:] or S1.head_position()[0] < border or S1.head_position()[0] >= width - border or S1.head_position()[1] < border or S1.head_position()[1] >= height - border:
        game_over(score_renewable, level)  

    screen.fill(black)
    draw_border(screen)
    text_score = font_small.render("Score: ", True, white)
    scores = font_small.render(str(score_renewable), True, white)
    screen.blit(text_score, (30,30))
    screen.blit(scores, (100,30))
    S1.draw(screen)
    F1.draw(screen)
    if score > 0 and score % 10 == 0:
        score = 0
        level += 1
        speed += 2
        pygame.display.set_caption("Snake Game - Level " + str(level))

    pygame.display.update()
    clock.tick(speed)
