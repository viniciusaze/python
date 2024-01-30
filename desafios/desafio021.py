import pygame
pygame.init() # para iniciar a biblioteca pygame
pygame.mixer.music.load('ex021.mp3') # para selecionar a música
pygame.mixer.music.play() # para dar play na musica
input() # foi preciso colocar para tocar a música
pygame.event.wait() # para esperar a musica acabar para encerrar o programa
