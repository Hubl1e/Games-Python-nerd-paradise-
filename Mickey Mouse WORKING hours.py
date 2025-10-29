import pygame
import os
import datetime

_image_library = {}


def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


pygame.init()
screen = pygame.display.set_mode((1900,1000))
clock = pygame.time.Clock()

base_mickey = pygame.image.load(r"C:\Users\Tarlan Vinogradov\Desktop\ебаный пайтон\labki igri\картинка\base_micky.jpg")
right_minute_hand = pygame.image.load(r"C:\Users\Tarlan Vinogradov\Desktop\ебаный пайтон\labki igri\картинка\minute.png")
left_second_hand = pygame.image.load(r"C:\Users\Tarlan Vinogradov\Desktop\ебаный пайтон\labki igri\картинка\second.png")

center = (950, 500)

minute_pivot = (right_minute_hand.get_width() // 2, right_minute_hand.get_height() // 2)
second_pivot = (left_second_hand.get_width() // 2, left_second_hand.get_height() // 2)


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255)) #белый фон

    now = datetime.datetime.now()
    minute_angle = -6 * now.minute   #эта минута -6 градусов за один тик типо
    second_angle = -6 * now.second  # секунда тоже -6 градусов за тик

    screen.blit(base_mickey, (center[0] - base_mickey.get_width() // 2,
                              center[1] - base_mickey.get_height() // 2))



    blitRotate(screen, get_image('minute.png'), center, minute_pivot, minute_angle)
    blitRotate(screen, get_image('second.png'), center, second_pivot, second_angle)



    pygame.display.flip()
    clock.tick(60)

    