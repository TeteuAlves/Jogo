import pygame

pygame.init()
#configuração da tela
tela = pygame.display.set_mode((900, 700))

pygame.display.set_caption("Comilão")


FUNDO = pygame.image.load("Fundo_do_mar.png")
FUNDO = pygame.transform.scale(FUNDO,(900, 700))

clock = pygame.time.Clock()

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(FUNDO, (0,0))

    pygame.display.update()

    #REGULAR O FPS
    clock.tick(60)
