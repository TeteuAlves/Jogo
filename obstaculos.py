import pygame
import random
class Obstaculo:
    def __init__(self, arquivo_imagem, largura_imagem, altura_imagem, x_inicial, y_inicial ):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))

        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.velocidade = random.randint(10,15)

        self.mascara = pygame.mask.from_surface(self.imagem)
