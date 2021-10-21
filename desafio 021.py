import pygame

input('para tocar uma musiquinha aperte enter :)')
pygame.mixer.init()
pygame.mixer.music.load('sleep_away.mp3')
pygame.mixer.music.play()
input('se quiser encerrar o programa aperte enter novamente')
