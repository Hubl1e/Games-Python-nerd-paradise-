import pygame
import os


pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music programm")


songs = ['everybreathyoutake.mp3', 'malo.mp3', 'ALASKAPUFFER.mp3']
current_index = 0

def load_song(index):
    pygame.mixer.music.load(songs[index])

def play_song():
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs)
    load_song(current_index)
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(songs)
    load_song(current_index)
    play_song()

load_song(current_index)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   #играет
                play_song()
            elif event.key == pygame.K_s:     #остановливпет
                stop_song()
            elif event.key == pygame.K_RIGHT: #следующая песня
                next_song()
            elif event.key == pygame.K_LEFT:  #прошлая пенся
                previous_song()


pygame.quit()
