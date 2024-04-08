import pygame
import math
pygame.init()

Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height))
base_layer = pygame.Surface((Width, Height))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

cur = BLACK
eraser = WHITE

currX = 0
currY = 0

prevX = 0
prevY = 0

THICKNESS = 5
drawing = True
drawing_rect = False
drawing_circle = False
drawing_right_triangle = False
drawing_equilateral_triangle = False
drawing_rhombus = False


done = False
LMBPressed = False
RMBPressed = False

screen.fill(WHITE)
def manual():
    print("Colors:")
    print("'Red' - key R")
    print("'Blue' - key B")
    print("'Black' - key K")
    print("'Green' - key G")
    print("'Yellow' - key Y")
    print("Clean canvas - key BACKSPACE")
    print("Increase thickness - key '+'")
    print("Decrease thickness - key '-'")
    print("-----------------------------")
    print("Modes:")
    print("Normal - key 1")
    print("Rectangle, square - key 2")
    print("Circle - key 3")
    print("Right triangle - key 4")
    print("Equilateral triangle - key 5")
    print("Rhombus - key 6")
    print("Reprint manual - key H")
#Grid
def grid():
    grid_size = 20
    for x in range(0 , Width, grid_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, Height))
    for y in range(0, Height, grid_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (Width, y))

#Calculation of drawing figures
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def right_triangle(x1, y1, x2, y2):
    pygame.draw.polygon(screen, cur, [(x1, y1), (x1,y2), (x2, y2)], THICKNESS)

def equilateral_triangle(x1, y1, x2, y2):
    pygame.draw.polygon(screen, cur, [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)], THICKNESS)

def rhombus(x1, y1, x2, y2):
    pygame.draw.polygon(screen, cur, [(x1, (y1 + y2) // 2), ((x1 + x2) // 2, y1), (x2, (y1 + y2) // 2), ((x1 + x2) // 2, y2)], THICKNESS)

manual()
while not done:

    pressed = pygame.key.get_pressed()

    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if drawing:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LMBPressed = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                RMBPressed = True
                eraser = WHITE
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if LMBPressed:
                    pygame.draw.circle(screen, cur, mouse_pos, THICKNESS)
                if RMBPressed:
                    pygame.draw.circle(screen, eraser, mouse_pos, THICKNESS)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBPressed = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                RMBPressed = False
        if drawing_rect:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBPressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if LMBPressed:
                    currX = event.pos[0]
                    currY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBPressed = False
                currX = event.pos[0]
                currY = event.pos[1]
                pygame.draw.rect(screen, cur, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))
        if drawing_circle:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                LMBPressed = True
                prevX = event.pos
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBPressed = False
                currX = event.pos
                radius = ((currX[0] - prevX[0]) ** 2 + (currX[1] - prevX[1]) ** 2) ** 0.5
                pygame.draw.circle(screen, cur, prevX, int(radius), THICKNESS)
                base_layer.blit(screen, (0, 0))
        if drawing_right_triangle:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBPressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBPressed = False
                currX = event.pos[0]
                currY = event.pos[1]
                right_triangle(prevX, prevY, currX, currY)
                base_layer.blit(screen, (0, 0))
        if drawing_equilateral_triangle:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBPressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBPressed = False
                currX = event.pos[0]
                currY = event.pos[1]
                equilateral_triangle(prevX, prevY, currX, currY)
                base_layer.blit(screen, (0, 0))             
        if drawing_rhombus:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBPressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBPressed = False
                currX = event.pos[0]
                currY = event.pos[1]
                rhombus(prevX, prevY, currX, currY)
                base_layer.blit(screen, (0, 0))  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                pygame.quit()
            elif event.key == pygame.K_F4 and alt_held:
                pygame.quit()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_EQUALS:
                print("Thickness", THICKNESS)
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                print("Thickness", THICKNESS)
                THICKNESS -= 1
            elif event.key == pygame.K_r:
                print("Red")
                cur = RED
            elif event.key == pygame.K_b:
                print("Blue")
                cur = BLUE
            elif event.key == pygame.K_k:
                print("Black")
                cur = BLACK
            elif event.key == pygame.K_g:
                print("Green")
                cur = GREEN
            elif event.key == pygame.K_y:
                print("Yellow")
                cur = YELLOW
            elif event.key == pygame.K_BACKSPACE:
                print("Canvas is cleared!")
                screen.fill(WHITE)
            elif event.key == pygame.K_1:  # Draw freely
                print("Normal mode is on")
                drawing = True
                drawing_rect = False
                drawing_circle = False
                drawing_right_triangle = False
                drawing_equilateral_triangle = False
                drawing_rhombus = False
            elif event.key == pygame.K_2:  # Draw rectangle
                print("Rectangle mode is on")
                drawing_rect = True
                drawing = False
                drawing_circle = False
                drawing_right_triangle = False
                drawing_equilateral_triangle = False
                drawing_rhombus = False
            elif event.key == pygame.K_3:  # Draw Circle
                print("Circle mode is on")
                drawing_circle = True
                drawing = False
                drawing_rect = False
                drawing_right_triangle = False
                drawing_equilateral_triangle = False
                drawing_rhombus = False
            elif event.key == pygame.K_4:  # Draw Right triangle
                print("Right triangle mode is on")
                drawing_circle = False
                drawing = False
                drawing_rect = False
                drawing_right_triangle = True
                drawing_equilateral_triangle = False
                drawing_rhombus = False
            elif event.key == pygame.K_5:  # Draw Equilateral triangle
                print("Equilateral triangle mode is on")
                drawing_circle = False
                drawing = False
                drawing_rect = False
                drawing_right_triangle = False
                drawing_equilateral_triangle = True
                drawing_rhombus = False
            elif event.key == pygame.K_6:  # Draw Rhombus
                print("Rhombus mode is on")
                drawing_circle = False
                drawing = False
                drawing_rect = False
                drawing_right_triangle = False
                drawing_equilateral_triangle = False
                drawing_rhombus = True
            elif event.key == pygame.K_h:
                manual()
        grid()
        pygame.display.flip()
        clock.tick(60)
