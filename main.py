import pygame
import random
from tkinter import simpledialog

pygame.init()

tamanho = (1000, 563)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Space Marker")
branco = (255, 255, 255)

clock = pygame.time.Clock()

icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
fundo = pygame.image.load("bg.jpg")
estrelas = []

pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)

fonte = pygame.font.SysFont("Arial", 15)

running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring('Space', 'Nome da Estrela:')
            if item is None or item == '':
                item = 'Estrela Desconhecida ' + str(pos)
            estrelas.append((item, pos))
            print(estrelas)