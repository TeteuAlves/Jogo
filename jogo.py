import pygame
from personagem import Jogador

pygame.init()
#configuração da tela
tela = pygame.display.set_mode((900, 700))

pygame.display.set_caption("Comilão")


FUNDO = pygame.image.load("Imagens/Fundo_do_mar.png")
FUNDO = pygame.transform.scale(FUNDO,(900, 700))

jogador1 = Jogador("Imagens/peixe.png",50,50,0,650 )

clock = pygame.time.Clock()

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    tela.blit(FUNDO, (0,0))

    jogador1.movimenta_via_controle(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    jogador1.apareca(tela)

    pygame.display.update()

    #REGULAR O FPS
    clock.tick(60)
