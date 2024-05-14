import pygame

class Jogador:

    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial ):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.mascara = pygame.mask.from_surface(self.imagem)

    def apareca(self, tela):
        tela.blit(self.imagem, (self.pos_x, self.pos_y))

    def movimenta_via_controle(self,esquerda,direita,poder):
        teclas = pygame.key.get_pressed()
        if teclas[direita]:
            if self.pos_x < 800:
               self.pos_x = self.pos_x + 20

        if teclas[esquerda]:
            if self.pos_x > 0:
              self.pos_x = self.pos_x - 20

        if teclas[poder]:
            self.pos_x = 0
            self.pos_y = 600
            