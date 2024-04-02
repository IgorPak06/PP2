import pygame

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

THICKNESS = 5
drawing = True
drawing_rect = False
drawing_cirle = False
done = False
LMBPressed = False
RMBPressed = False

screen.fill(WHITE)
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


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
                cur = WHITE
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if LMBPressed:
                    pygame.draw.circle(screen, cur, mouse_pos, THICKNESS)
                if RMBPressed:
                    pygame.draw.circle(screen, cur, mouse_pos, THICKNESS)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                LMBPressed = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                RMBPressed = False
                cur = BLACK
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                pygame.quit()
            elif event.key == pygame.K_F4 and alt_held:
                pygame.quit()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                THICKNESS -= 1
            elif event.key == pygame.K_r:
                cur = RED
            elif event.key == pygame.K_b:
                cur = BLUE
            elif event.key == pygame.K_k:
                cur = BLACK
            elif event.key == pygame.K_g:
                cur = GREEN
            elif event.key == pygame.K_p:
                cur = PINK
            elif event.key == pygame.K_y:
                cur = YELLOW
            elif event.key == pygame.K_a: #Draw rectangle
                drawing_rect = True
                drawing = False
            elif event.key == pygame.K_s: #Draw Circle
                drawing_cirle = True
                drawing = False
            elif event.key == pygame.K_d: #Draw freely
                drawing = True
                drawing_rect = False
                drawing_cirle = False

    for event_rect in pygame.event.get():
        if drawing_rect:
            if event_rect.type == pygame.MOUSEBUTTONDOWN and event_rect.button == 1:
                LMBPressed = True
                prevX = event_rect.pos[0]
                prevY = event_rect.pos[1]
            if event_rect.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if LMBPressed:
                    currX = event_rect.pos[0]
                    currY = event_rect.pos[1]
            if event_rect.type == pygame.MOUSEBUTTONUP and event_rect.button == 1:
                LMBPressed = False
                currX = event_rect.pos[0]
                currY = event_rect.pos[1]
                pygame.draw.rect(screen, cur, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                base_layer.blit(screen, (0, 0))

    for event_circle in pygame.event.get():
        if drawing_cirle:
            if event_circle.type == pygame.MOUSEBUTTONDOWN and event_circle.button == 1:
                LMBPressed = True
                prevX = event_circle.pos
            if event_rect.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event_rect.type == pygame.MOUSEBUTTONUP and event_rect.button == 1:
                LMBPressed = False
                currX = event_rect.pos
                radius = ((currX[0] - prevX[0])**2 + (currX[1] - prevX[1])**2)**0.5
                pygame.draw.circle(screen, cur, prevX, int(radius), THICKNESS)
                base_layer.blit(screen, (0, 0))
        pygame.display.flip()
        clock.tick(60)
