# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

tabuleiro_player_2 = [[2, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 2, 2]]

tabuleiro_player_1 = [[2, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 2, 2]]

ROW_HEIGHT = 115
COL_WIDTH = 105
MARGIN = 6

tipo_de_letra = pygame.font.Font(None, 25)  

pontos_player_2:int = 0
pontos_player_1:int = 0

total_pedras_p1, total_pedras_p2 = sum(map(sum,tabuleiro_player_1)), sum(map(sum,tabuleiro_player_2))

quem_joga = 1
vencedor = None


class TABULEIRO:
    def __init__(self) -> None:
        
        self.tabuleiro_vazio = pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/tabuleiro_vazio.png')
        self.cova_pontos = pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/covas_pontos.png')
        
        self.valores_pedras = {0: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_00.png'),
                               1: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_01.png'),
                               2: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_02.png'),
                               3: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_03.png'),
                               
                               4: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_04.png'),
                               5: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_05.png'),
                               6: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_06.png'),
                               7: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_07.png'),
                               
                               8: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_08.png'),
                               9: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_09.png'),
                               10: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_10.png'),
                               11: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_11.png'),
                               
                               12: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_12.png'),
                               13: pygame.image.load('aulas_python/resources/02_ntchuva/tabuleiro/cova_12+.png')}

    def desenhar_tabuleiro(self):
        self.rect_cova_pontos = self.cova_pontos.get_rect()
        rect_cova_pontos = 52, 196
        screen.blit(self.cova_pontos, rect_cova_pontos)

        rect_cova_pontos = 1003, 196
        screen.blit(tabuleiro.cova_pontos, rect_cova_pontos)

        self.desenhar_numero_de_pedras(tabuleiro_player_2, 319, 223)
        self.desenhar_numero_de_pedras(tabuleiro_player_1, 319, 493)

    def desenhar_numero_de_pedras(self, tabuleiro, x_offset, y_offset):
        for row in range(len(tabuleiro)):
            for col in range(len(tabuleiro[row])):
                x = x_offset + COL_WIDTH * col + MARGIN
                y = y_offset + ROW_HEIGHT * row + MARGIN

                # TEXTO DE NUMERO DE PEDRAS
                numero_de_pedras = tabuleiro[row][col]
                camada_pedras_numeros = tipo_de_letra.render(str(numero_de_pedras), True, ("black"))

                numero_render = camada_pedras_numeros.get_rect(center=(x, y))
                screen.blit(camada_pedras_numeros, numero_render)

                # IMAGEM DE NUMERO DE PEDRAS

                y_pedras = (y_offset + ROW_HEIGHT * row + MARGIN) - 58
                img_pedras_surface = numero_de_pedras
                if img_pedras_surface > 12:
                    img_pedras_surface = 13
                
                img_pedras = self.valores_pedras.get(img_pedras_surface)

                pedras_render = img_pedras.get_rect(center=(x, y_pedras))
                screen.blit(img_pedras, pedras_render)
    
    def display_update(self):
        screen.fill((217, 217, 217))
        rect_bg = bg_img.get_rect()
        rect_bg.center = 588, 379
        screen.blit(bg_img, rect_bg)
        tabuleiro.desenhar_tabuleiro()
        pygame.display.flip()

class JOGADAS:
    def __init__(self):
        self.move_executed = False

    def mover_peca(self, x: int, y: int, tabuleiro:list):
        tab = TABULEIRO()
        if self.move_executed:
            return
        casas_a_percorrer = tabuleiro[x][y] # define o numero de casas que irá percorrer
        casas_percorridas = 0 # helper
        global pontos_player_1, pontos_player_2 # número actual de pontos dos jogadores.


        while casas_a_percorrer > casas_percorridas:
            for _ in range(casas_a_percorrer + 1): # +1 para adicionar mais um movimento, pois inicia a contagem a partir da remoção da pedra.
                valor = tabuleiro[x][y] # helper
                pygame.time.wait(250)
                # Verifica a posição e e diz ao programa que posição é a proxima a mover

                if x == 0 and y == 0:
                    next_x = 1
                    next_y = 0
                elif x == 1 and y == 0:
                    next_x = 1
                    next_y = 1
                elif x == 1 and y == 1:
                    next_x = 1
                    next_y = 2
                elif x == 1 and y == 2:
                    next_x = 1
                    next_y = 3
                elif x == 1 and y == 3:
                    next_x = 1
                    next_y = 4
                elif x == 1 and y == 4:
                    next_x = 1
                    next_y = 5
                elif x == 1 and y == 5:
                    next_x = 0
                    next_y = 5        
                elif x == 0 and y == 5:
                    next_x = 0
                    next_y = 4
                elif x == 0 and y == 4:
                    next_x = 0
                    next_y = 3
                elif x == 0 and y == 3:
                    next_x = 0
                    next_y = 2
                elif x == 0 and y == 2:
                    next_x = 0
                    next_y = 1
                elif x == 0 and y == 1:
                    next_x = 0
                    next_y = 0
                
                # Movimento da primeira casa, que remove as pedras da casa e inicia a distribuição na proxima casa no sentido anti-horário.
                if casas_percorridas == 0:
                    tab.display_update()
                    print(pygame.time.get_ticks())
                    casas_percorridas += 1
                    tabuleiro[x][y] = 0
                    print(f"\n{casas_percorridas}. pos(x={x}, y={y}), {valor} -> {tabuleiro[x][y]}")
                    

                else:
                    # Caso não seja a primeira casa continua a distribuição no sentido anti-horário.
                    tab.display_update()
                    print(pygame.time.get_ticks())
                    casas_percorridas += 1
                    tabuleiro[x][y] += 1
                    print(f"{casas_percorridas}. pos(x={x}, y={y}), {valor} -> {tabuleiro[x][y]}")
                    
                     # Imprime o relatório da posição actual, pedras existentes anteriorimente e novo número de pedras.
                    if (casas_percorridas-1 == casas_a_percorrer): # Verifica se está no ultimo movimento
                        if tabuleiro[x][y] > 1: # se a casa onde foi feito o ultimo movimento número de peças for maior que 1
                            print(f"\nPeças a mover: {tabuleiro[x][y]}") # Informa o número de peças que irá mover
                            self.mover_peca(x, y, tabuleiro) # Aplica novamente a função usando os parametros da posição actual.
                        
                        elif tabuleiro[x][y] == 1: # CAPTURA DE PEÇA
                            if tabuleiro == tabuleiro_player_1 and x == 0: # verifica se está na posição interna
                                if tabuleiro_player_2[x+1][y] > 0: # verifica se o numero de pedras do adversário na linha imediatamente a seguir do jogador 1 tem ou não peças
                                    pedras_externas = 0 # helper
                                    pedras_internas = tabuleiro_player_2[x+1][y] # helper
                                    
                                    tabuleiro_player_2[x+1][y] = 0 # recolhe as pedras internas do adversário
                                    pontos_player_1 = pontos_player_1 + pedras_internas # converte o número de pedras removidas do jogador 2 em pontos
                                    
                                    if tabuleiro_player_2[x][y] > 0: # verfica se a coluna externa tem ou não pedras
                                        pedras_externas = tabuleiro_player_2[x][y] # helper
                                        tabuleiro_player_2[x][y] = 0 # recolhe as pedras externas
                                        pontos_player_1 = pontos_player_1 + pedras_externas # converte o número de pedras removidas do jogador 2 em pontos
                                
                                    print(f"\nCapuradas {pedras_internas + pedras_externas} peças do Jogador 2") # informa aos jogadores quantas peças foram removidas
                            
                            elif tabuleiro == tabuleiro_player_2 and x == 1:
                                if tabuleiro_player_1[x-1][y] > 0:
                                    pedras_externas = 0
                                    pedras_internas = tabuleiro_player_1[x-1][y]

                                    tabuleiro_player_1[x-1][y] = 0
                                    pontos_player_2 = pontos_player_2 + pedras_internas

                                    if tabuleiro_player_1[x][y] > 0:
                                        pedras_externas = tabuleiro_player_1[x][y]
                                        tabuleiro_player_1[x][y] = 0
                                        pontos_player_2 = pontos_player_2 + pedras_internas
                                    
                                    print(f"\nCapuradas {pedras_internas + pedras_externas} peças do Jogador 1")
                        else:
                            break
                x = next_x
                y = next_y 
        
        self.move_executed = True

tabuleiro = TABULEIRO()
jogada = JOGADAS()
screen = pygame.display.set_mode([1176, 758])

bg_img = tabuleiro.tabuleiro_vazio
relogio = pygame.time.Clock()

def main():
    # Run until the user asks to quit
    
    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((217, 217, 217))
        rect_bg = bg_img.get_rect()

        rect_bg.center = 588, 379
        screen.blit(bg_img, rect_bg)
        
        tabuleiro.desenhar_tabuleiro()
        jogada.mover_peca(0, 0, tabuleiro_player_1)
       
        # Flip the display
        pygame.display.flip()
        relogio.tick(24)

    # Done! Time to quit.
    pygame.quit()

main()

