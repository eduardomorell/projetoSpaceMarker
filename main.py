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


        if keys[pygame.K_F10]:
            try:
                arquivo = open('bd.atitus', 'w')
                for estrela in estrelas:
                    arquivo.write("{0}\n".format(estrela))
                arquivo.close()
            except:
                print('Erro ao Carregar os Arquivos!')


        if keys[pygame.K_F11]:
            try:
                arquivo = open('bd.atitus', 'r')
                for estrela in arquivo.readlines():
                    tupla = eval(estrela)
                    estrelas.append((tupla))
                arquivo.close()
            except:
                print('Erro ao Carregar os Arquivos!')


        if keys[pygame.K_F12]:
            try:
                arquivo = open('bd.atitus', 'w')
                arquivo.close()
            except:
                print('Erro ao Carregar os Arquivos!')


        if keys[pygame.K_ESCAPE]:
            running = False


    tela.blit(fundo, (0, 0))