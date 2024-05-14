import pygame
from personagem import Jogador
from obstaculos_bons import Obstaculo
from obstaculos_ruins import Buff

pygame.init()
#configuração da tela
tela = pygame.display.set_mode((900, 700))

pygame.display.set_caption("Comilão")


FUNDO = pygame.image.load("Imagens/Fundo_do_mar.png")
FUNDO = pygame.transform.scale(FUNDO,(900, 700))

#Adicionando jogador
jogador1 = Jogador("Imagens/peixe.png",100,100,400,600 )

lista_objeto_bonus = [Obstaculo("imagens/salsicha.png",75,75,0),
                    Obstaculo("imagens/Ração.png",75,75,0),
                    Obstaculo("imagens/salsicha.png",75,75,0),
                    Obstaculo("imagens/Ração.png",75,75,0)]

lista_objeto_ruins = [Buff("imagens/anzol.png",75,75,0),
                        Buff("imagens/anzol.png",75,75,0),
                        Buff("imagens/anzol.png",75,75,0)]

fonte = pygame.font.SysFont("Arial", 50)
perder = pygame.font.SysFont("Arial", 50)
ganhar = pygame.font.SysFont("Arial", 50)
#pontuação
pontuação_personagem = 0

pontuação_vida = 3


#configurar FPS
clock = pygame.time.Clock()

#rodar jogo para sempre
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO, (0,0))

#movimentando e aparecendo jogador
    jogador1.movimenta_via_controle(pygame.K_LEFT, pygame.K_RIGHT)
    jogador1.apareca(tela)

#movimentando objeto
    for obstaculos in lista_objeto_bonus:
        obstaculos.movimenta()
        obstaculos.apareca(tela)
        if jogador1.mascara.overlap(obstaculos.mascara,(obstaculos.pos_x - jogador1.pos_x, obstaculos.pos_y - jogador1.pos_y )):
            pontuação_personagem = pontuação_personagem + 1
            obstaculos.pos_y = 700
            if pontuação_personagem == 0:
                ganhar = fonte.render(f"PARABÉNSS!!", False,(255,0,0))
                tela.blit(perder,(300,300))
                pygame.display.update()
                pygame.time.wait(2000)
                rodando = False

    for ruim in lista_objeto_ruins:
        ruim.movimenta()
        ruim.apareca(tela)
        if jogador1.mascara.overlap(ruim.mascara,(ruim.pos_x - jogador1.pos_x, ruim.pos_y - jogador1.pos_y )):
            pontuação_vida = pontuação_vida - 1
            ruim.pos_y = 700
            if pontuação_vida == 0:
                perder = fonte.render(f"VOCÊ PERDEU!!", False,(255,0,0))
                tela.blit(perder,(300,300))
                pygame.display.update()
                pygame.time.wait(2000)
                rodando = False

#contagem
    texto_pontos = fonte.render(f"Pontuação:{pontuação_personagem} ", False,(255,0,0))

    texto_vidas = fonte.render(f"Vidas:{pontuação_vida} ", False,(255,0,0))

    tela.blit(texto_pontos,(600,0))
    tela.blit(texto_vidas,(100,0))
#atualizar a tela
    pygame.display.update()

    #REGULAR O FPS
    clock.tick(60)

