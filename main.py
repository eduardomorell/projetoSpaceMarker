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

    # Escrever (F10, F11, F12)
    f10 = fonte.render('F10 para salvar os Arquivos', True, branco) 
    f11 = fonte.render('F11 para carregar os Arquivos', True, branco)
    f12 = fonte.render('F12 para deletar os Arquivos', True, branco)

    tela.blit(f10, (10, 10))
    tela.blit(f11, (10, 30))
    tela.blit(f12, (10, 50))


    # Desenhar todos os pontos das estrelas e seus nomes
    for name, pos in estrelas:
        pygame.draw.circle(tela, (255, 255, 255), pos, 2)
        text_surface = fonte.render(name, True, (255, 255, 255))
        tela.blit(text_surface, (pos[0] + 10, pos[1] - 10))

    # Desenhar linhas entre os pontos
    if len(estrelas) > 1:
        for i in range(1, len(estrelas)):
            pos_atual = estrelas[i][1]
            pos_anterior = estrelas[i - 1][1]
            pygame.draw.line(tela, (255, 255, 255), pos_anterior, pos_atual, 2)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
