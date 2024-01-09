import random

tabuleiro_player_2 = [[0, 0, 0, 0],
                      [0, 1, 0, 0]]

tabuleiro_player_1 = [[4, 0, 1, 4],
                      [4, 4, 4, 4]]


coordenadas_P2 = {"A1": (0,0), "A2": (0,1), "A3": (0,2), "A4": (0,3),
                  "B1": (1,0), "B2": (1,1), "B3": (1,2), "B4": (1,3)}

coordenadas_P1 = {"C1": (0,0), "C2": (0,1), "C3": (0,2), "C4": (0,3),
                  "D1": (1,0), "D2": (1,1), "D3": (1,2), "D4": (1,3)}

pontos_player_2:int = 0
pontos_player_1:int = 31

quem_joga = 1
vencedor = None


def ver_tabuleiro():
    p2_letras = ["   ", "1", "2", "3", "4", "   "]
    p1_letras = ["   ", "1", "2", "3", "4", "   "]
    index_letra = ["A", "B", "C", "D"]
    
    for p2_letra in p2_letras:
        print(p2_letra, end=" ")
    print("\n   ---------  ")
    for index, linha in enumerate(tabuleiro_player_2):
        print(index_letra[index], end=" | ")
        for index_col, coluna in enumerate(linha):
            print(coluna, end=" ")
            if index_col == 3:
                print(f"| {index_letra[index]}", end="")
        print("")
    print("   --------- ")
    for index, linha in enumerate(tabuleiro_player_1):
        print(index_letra[index+2], end=" | ")
        for index_col, coluna in enumerate(linha):
            print(coluna, end=" ")
            if index_col == 3:
                print(f"| {index_letra[index+2]}", end="")
        print("")
    print("   --------- ")
    for p1_letra in p1_letras:
        print(p1_letra, end=" ")
    print(f"\n\nP1 = {pontos_player_1}    P2 = {pontos_player_2}\nPedras Capuradas")


def obter_coordenadas(coordenada:str, tabuleiro:dict):
    if coordenada in tabuleiro:
        return tabuleiro.get(coordenada)
    else:
        return "Posição desconhecida."

def mover_peca(x: int, y: int, tabuleiro:list):
  casas_a_percorrer = tabuleiro[x][y]
  casas_percorridas = 0
  global pontos_player_1, pontos_player_2


  while casas_a_percorrer > casas_percorridas:
        for _ in range(casas_a_percorrer + 1):
          valor = tabuleiro[x][y]
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
          
          if casas_percorridas == 0:
            casas_percorridas += 1
            tabuleiro[x][y] = 0
            print(f"\n{casas_percorridas}. pos(x={x}, y={y}), {valor} -> {tabuleiro[x][y]}")
          else:
              casas_percorridas += 1
              tabuleiro[x][y] += 1
              print(f"{casas_percorridas}. pos(x={x}, y={y}), {valor} -> {tabuleiro[x][y]}")
              if (casas_percorridas-1 == casas_a_percorrer):
                    if tabuleiro[x][y] > 1:
                        print(f"\nPeças a mover: {tabuleiro[x][y]}")
                        mover_peca(x, y, tabuleiro)
                    elif tabuleiro[x][y] == 1: # CAPTURA DE PEÇA
                        if tabuleiro == tabuleiro_player_1 and x == 0:
                            if tabuleiro_player_2[x+1][y] > 0:
                                pontos_player_1 = pontos_player_1 + tabuleiro_player_2[x+1][y]
                                print(f"\nCapuradas {tabuleiro_player_2[x+1][y]} peças do Jogador 2")
                                tabuleiro_player_2[x+1][y] = 0
                                
                        elif tabuleiro == tabuleiro_player_2 and x == 1:
                            if tabuleiro_player_1[x-1][y] > 0:
                                pontos_player_2 = pontos_player_2 + tabuleiro_player_1[x-1][y]
                                print(f"\nCapuradas {tabuleiro_player_1[x-1][y]} peças do Jogador 1")
                                tabuleiro_player_1[x-1][y] = 0
          x = next_x
          y = next_y    
          

def jogar(tabuleiro_jogador):
    while True:
        if tabuleiro_jogador == tabuleiro_player_1:
            texto = input("Digite a coordenada: ").capitalize()
            coordenada = coordenadas_P1
        
        elif tabuleiro_jogador == tabuleiro_player_2:
            texto = random.choice(list(coordenadas_P2.keys()))
            coordenada = coordenadas_P2
            print(f"Jogador 2 escolheu: {texto}")
            
        coordenada = obter_coordenadas(texto, coordenada)
        if coordenada != "Posição desconhecida.":
            x, y = coordenada[0], coordenada[1]
            if tabuleiro_jogador[x][y] > 0:
                mover_peca(coordenada[0], coordenada[1], tabuleiro_jogador)
                print()
                ver_tabuleiro()
                break
            else:
                print("Nenhuma peça nesta posição. Tente novamente.")
        else:
            print("Coordenada desconhecida. Tente novamente.")

def main():
    global quem_joga, vencedor, pontos_player_1, pontos_player_2
    ver_tabuleiro()
    while vencedor is None:
        if quem_joga == 1:
            print("\nJogador 1")
            jogar(tabuleiro_player_1)
            if pontos_player_1 > 31:
                vencedor = pontos_player_1
                print("GAME OVER")
            else:
                quem_joga = 2
        else:
            print("\nJogador 2")
            jogar(tabuleiro_player_2)
            if pontos_player_2 >= 31:
                vencedor = pontos_player_2
                print("GAME OVER")
            else:
                quem_joga = 1

if __name__ == "__main__":
    main()
