'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3'''

#importar pygame
import pygame
#iniciar mixer
pygame.mixer.init()
#iniciar pygame
pygame.init()
#carregar música
pygame.mixer.music.load('primeiros testes/PrimeiroMUNDO/musica.mp3')
#play na música
pygame.mixer.music.play()
#aguardar a música acabar
pygame.event.wait()
