import pygame
from personagem import Jogador
from obstaculos import Obstaculo

pygame.init()
#configuração da tela
tela = pygame.display.set_mode((900, 700))

pygame.display.set_caption("Comilão")


FUNDO = pygame.image.load("Imagens/Fundo_do_mar.png")
FUNDO = pygame.transform.scale(FUNDO,(900, 700))

#Adicionando jogador
jogador1 = Jogador("Imagens/peixe.png",100,100,400,600 )

lista_objeto = [Obstaculo("imagens/anzol.png",75,75,500,10),
                Obstaculo("imagens/salsicha.png",75,75,500,10)]

#configurar FPS
clock = pygame.time.Clock()

#rodar jogo para sempre
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO, (0,0))

    jogador1.movimenta_via_controle(pygame.K_LEFT, pygame.K_RIGHT)
    jogador1.apareca(tela)

    for obstaculos in lista_objeto:
        obstaculos.movimenta()
        obstaculos.apareca(tela)

    pygame.display.update()

    #REGULAR O FPS
    clock.tick(60)
