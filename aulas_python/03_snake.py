import pygame, sys, random
from pygame.math import Vector2

class COBRA:
    def __init__(self):
        self.corpo = [Vector2(5,10), Vector2(4,10), (3,10)]
        self.direcao = Vector2(1,0)
        self.novo_bloco = False 


    def desenhar_cobra(self):
        for bloco in self.corpo:
            pos_x = int(bloco[0] * tamanho_celula) 
            pos_y = int(bloco[1] * tamanho_celula)
            cobra_rect = pygame.Rect(pos_x, pos_y, tamanho_celula, tamanho_celula)
            pygame.draw.rect(tela,(183,111,122), cobra_rect)
    

    def movimentar_cobra(self):
        if self.novo_bloco == True:
            copia_corpo = self.corpo[:]
            self.novo_bloco = False
        else:
            copia_corpo = self.corpo[:-1]
            
        copia_corpo.insert(0,copia_corpo[0] + self.direcao)
        self.corpo = copia_corpo[:]
            

    def add_bloco(self):
        self.novo_bloco = True

class FRUTA:
    def __init__(self):
        self.randomize()
    
    def desenhar_fruta(self):
        fruta_rect = pygame.Rect(int(self.pos.x * tamanho_celula), int(self.pos.y * tamanho_celula), tamanho_celula, valor_celula)
        pygame.draw.rect(tela, (126,166,114), fruta_rect)
    
    def randomize(self):
        self.y = random.randint(0, valor_celula - 1)
        self.x = random.randint(0, valor_celula - 1) 
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.cobra = COBRA()
        self.fruta = FRUTA()
    
    def update(self):
        self.cobra.movimentar_cobra()
        self.ver_colisao()
        self.ver_falha()
    
    def desenhar_elementos(self):
        self.fruta.desenhar_fruta()
        self.cobra.desenhar_cobra()

    def ver_colisao(self):
        if self.fruta.pos == self.cobra.corpo[0]:
             self.fruta.randomize()
             self.cobra.add_bloco()
    
    def ver_falha(self):
        cabeca_x = self.cobra.corpo[0].x
        cabeca_y = self.cobra.corpo[0].y
        if not 0 <= cabeca_x < valor_celula or not 0 <= cabeca_y < valor_celula:
            self.game_over()

        for block in self.cobra.corpo[1:]:
            if block == self.cobra.corpo[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()    
    
pygame.init()
tamanho_celula = 30
valor_celula = 30
tela = pygame.display.set_mode((tamanho_celula * valor_celula,tamanho_celula * valor_celula))
relogio = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.cobra.direcao.y != 1:
                     main_game.cobra.direcao = Vector2(0,-1)
            if event.key == pygame.K_DOWN and main_game.cobra.direcao.y != -1:
                main_game.cobra.direcao = Vector2(0,1)
            if event.key == pygame.K_LEFT and main_game.cobra.direcao.x != 1:
                main_game.cobra.direcao = Vector2(-1,0)
            if event.key == pygame.K_RIGHT and main_game.cobra.direcao.x != -1:
                main_game.cobra.direcao = Vector2(1,0)

    tela.fill((175,215,70))
    main_game.desenhar_elementos()
    pygame.display.update()
    relogio.tick(60)