import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("пеинт который убил мои нервы")
clock = pygame.time.Clock()

canvas = pygame.Surface((800, 600))
canvas.fill((0, 0, 0))  #фон черный

tool = "draw"
color = (255, 255, 255)
radius = 10
drawing = False
start_pos = (0, 0)

temp_canvas = None  #типо временно рисует фигуры


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
            elif event.key == pygame.K_5:
                tool = "right_triangle"  #это прямоугольный треугольник
            elif event.key == pygame.K_6:
                tool = "equilateral_triangle"  #равностороний треугольник
            elif event.key == pygame.K_7:
                tool = "rhombus"  #ромб
            elif event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_w:
                color = (255, 255, 255)

        #рисование началось
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos
            if tool in ["draw", "eraser"]:
                pygame.draw.circle(canvas, color if tool=="draw" else (0,0,0), event.pos, radius)
        #конец рисования типо отпускаем кнопку
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            end_pos = event.pos
            x0, y0 = start_pos
            x1, y1 = end_pos

            if tool == "rect":
                pygame.draw.rect(canvas, color, (x0, y0, x1 - x0, y1 - y0), 0)
            elif tool == "circle":
                dx = x1 - x0
                dy = y1 - y0
                r = int((dx * dx + dy * dy) ** 0.5)
                pygame.draw.circle(canvas, color, start_pos, r, 0)
            elif tool == "right_triangle":
                points = [(x0, y0), (x0, y1), (x1, y1)]
                pygame.draw.polygon(canvas, color, points)
            elif tool == "equilateral_triangle":
                width = x1 - x0
                height = width * (3 ** 0.5) / 2
                points = [(x0, y1), (x1, y1), ((x0 + x1) / 2, y1 - height)]
                pygame.draw.polygon(canvas, color, points)
            elif tool == "rhombus":
                points = [(x0, (y0 + y1) / 2), ((x0 + x1) / 2, y0), (x1, (y0 + y1) / 2), ((x0 + x1) / 2, y1)]
                pygame.draw.polygon(canvas, color, points)  #типо фиксирует фигуру на основной канве ну холсте

            temp_canvas = None  #чистим холст

        #рисует когда мышкой двигать
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool in ["draw", "eraser"]:
                pygame.draw.circle(canvas, color if tool == "draw" else (0, 0, 0), event.pos, radius)
            elif tool in ["rect", "circle", "right_triangle", "equilateral_triangle", "rhombus"]:
                temp_canvas = canvas.copy()
                x0, y0 = start_pos
                x1, y1 = event.pos

                if tool == "rect":
                    pygame.draw.rect(temp_canvas, color, (x0, y0, x1 - x0, y1 - y0), 0)
                elif tool == "circle":
                    dx = x1 - x0
                    dy = y1 - y0
                    r = int((dx * dx + dy * dy) ** 0.5)
                    pygame.draw.circle(temp_canvas, color, start_pos, r, 0)
                elif tool == "right_triangle":
                    points = [(x0, y0), (x0, y1), (x1, y1)]
                    pygame.draw.polygon(temp_canvas, color, points)
                elif tool == "equilateral_triangle":
                    width = x1 - x0
                    height = width * (3 ** 0.5) / 2
                    points = [(x0, y1), (x1, y1), ((x0 + x1) / 2, y1 - height)]
                    pygame.draw.polygon(temp_canvas, color, points)
                elif tool == "rhombus":
                    points = [(x0, (y0 + y1) / 2), ((x0 + x1) / 2, y0), (x1, (y0 + y1) / 2), ((x0 + x1) / 2, y1)]
                    pygame.draw.polygon(temp_canvas, color, points)

    #типо когда фигуру зажал чтобы видно было што я ее растягиваю
    if temp_canvas:
        screen.blit(temp_canvas, (0, 0))
    else:
        screen.blit(canvas, (0, 0))

    pygame.display.flip()
    clock.tick(60)
