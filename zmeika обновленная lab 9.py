import pygame, sys, random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("змея зилёная")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#значения змеи
snake_pos = [[100, 100]]  #башка змеи
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10
score = 0
level = 1

#еда появляется рандомно с цветом и весом
def generate_food():
    while True:
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        if [x, y] not in snake_pos:
            color = random.choice([RED, (255, 255, 0), GREEN])  # красный, желтый, зеленый
            if color == RED:
                weight = 1
            elif color == (255, 255, 0):
                weight = 2
            else:
                weight = 3
            return [x, y], color, weight

food_pos, food_color, food_weight = generate_food()
food_spawn_time = pygame.time.get_ticks()
FOOD_LIFETIME = 8000 #8 тыщ миллисекунд типо 8 секунд



font = pygame.font.SysFont("Verdana", 20)

#цикл работы кода и движенья
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    snake_direction = change_to

    #движение змеи
    head_x, head_y = snake_pos[0]
    if snake_direction == "UP":
        head_y -= BLOCK_SIZE
    elif snake_direction == "DOWN":
        head_y += BLOCK_SIZE
    elif snake_direction == "LEFT":
        head_x -= BLOCK_SIZE
    elif snake_direction == "RIGHT":
        head_x += BLOCK_SIZE

    snake_pos.insert(0, [head_x, head_y])

#чекает съел ли еду
    if snake_pos[0] == food_pos:
        score += food_weight
        if score % 3 == 0:
            level += 1
            speed += 2
        #создает новые фрукты с цветом
        food_pos, food_color, food_weight = generate_food()
        food_spawn_time = pygame.time.get_ticks()

    else:
        snake_pos.pop() #удаляет хвост если не съел


        #проверка таймера еды
        current_time = pygame.time.get_ticks()
        if current_time - food_spawn_time >= FOOD_LIFETIME:
            food_pos, food_color, food_weight = generate_food()
            food_spawn_time = pygame.time.get_ticks()

    #чекает косается край экрана или себя
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        break
    if snake_pos[0] in snake_pos[1:]:
        break

    screen.fill(BLACK)
    for block in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, food_color, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))


    #показывает счет и уровень
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - 100, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()
