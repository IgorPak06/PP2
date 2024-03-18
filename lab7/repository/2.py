import pygame
import os

pygame.init()

screen = pygame.display.set_mode((1000, 100))

font = pygame.font.Font(None, 36)

music_dir = "/Users/frl404/Documents/Codes/PP2/lab7/repository/music/"
songs = os.listdir(music_dir)
current_song_index = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))

playing = False

done = False
while not done:
    screen.fill((255, 255, 255))

    txt = font.render(songs[current_song_index], True, (0, 0, 0))
    screen.blit(txt, (50, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not playing:
                    pygame.mixer.music.play()
                    playing = True
            elif event.key == pygame.K_DOWN:
                if playing:
                    pygame.mixer.music.stop()
                    playing = False
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
                if playing:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
                if playing:
                    pygame.mixer.music.play()
    
    pygame.display.flip()