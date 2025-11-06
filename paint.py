import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Пеинт")
clock = pygame.time.Clock()

canvas = pygame.Surface((800, 600))
canvas.fill((0, 0, 0))  #фон черный

tool = "draw"  
color = (255, 255, 255)
radius = 10
drawing = False
start_pos = (0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "draw"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_4:
                tool = "eraser"
            elif event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_w:
                color = (255, 255, 255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
                if tool in ["draw", "eraser"]:
                    pygame.draw.circle(canvas, color if tool=="draw" else (0,0,0), event.pos, radius)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                end_pos = event.pos
                if tool == "rect":
                    pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]), radius)
                elif tool == "circle":
                    dx = end_pos[0] - start_pos[0]
                    dy = end_pos[1] - start_pos[1]
                    r = int((dx*dx + dy*dy)**0.5)
                    pygame.draw.circle(canvas, color, start_pos, r, radius)
                drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool in ["draw", "eraser"]:
                pygame.draw.circle(canvas, color if tool=="draw" else (0,0,0), event.pos, radius)

    screen.blit(canvas, (0, 0))
    pygame.display.flip()
    clock.tick(60)

