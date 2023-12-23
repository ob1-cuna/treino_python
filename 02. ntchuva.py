import random

tabuleiro_player_1 = [[4, 4, 4, 4],[4, 4, 4, 4]]
tabuleiro_player_2 = [[4, 4, 4, 4],[4, 4, 4, 4]]

coord = {"A1": [0,0],"B1": [0,1],"C1": [0,2],"D1": [0,3],
               "A2": [1,0],"B2": [1,1],"C2": [1,2],"D2": [1,3]}
coordenadas_p1 = coord
coordenadas_p2 = coord

quem_joga = 1
vencedor = None 

def ver_tabuleiro():
    for linha in tabuleiro_player_1:
        for coluna in linha:
            print(coluna, end=" ")
        print("")
    print("-------")
    for linha in tabuleiro_player_2:
        for coluna in linha:
            print(coluna, end=" ")
        print("")

def obter_coordenadas(coordenada:str, tabuleiro:dict):
    if coordenada in tabuleiro:
        return tabuleiro.get(coordenada)
    else:
        return "Posição desconhecida."

def mover_peca(x: int, y: int, tabuleiro:list):
    casas_a_percorrer = tabuleiro[x][y]

    if casas_a_percorrer == 0:
        print("Nada para mover, tenta outra vez.")
        return

    quantidade_de_pedras = sum(len(row) for row in tabuleiro)
    posicao_cova = x * len(tabuleiro[0]) + y
    casas_percorridas = 0

    while casas_percorridas < casas_a_percorrer:
        for i in range(posicao_cova, quantidade_de_pedras):
            linha = i // len(tabuleiro[0])
            coluna = i % len(tabuleiro[0])
            valor = tabuleiro[linha][coluna]
            if casas_percorridas == 0:
                casas_percorridas += 1
                tabuleiro[x][y] = 0
                print(f"{casas_percorridas}. pos(x={linha}, y={coluna}), {valor} -> {tabuleiro[linha][coluna]}")
                #ver_tabuleiro()
            else:
                casas_percorridas += 1
                tabuleiro[linha][coluna] += 1
                print(f"{casas_percorridas}. pos(x={linha}, y={coluna}), {valor} -> {tabuleiro[linha][coluna]}")
                if casas_percorridas-1 >= casas_a_percorrer:
                    if tabuleiro[linha][coluna] > 1:
                        #ver_tabuleiro()
                        mover_peca(linha, coluna, tabuleiro)
                    return
        posicao_cova = 0
        casas_percorridas %= quantidade_de_pedras


def jogar(tabu):
    while True:
        texto = input("Digite a coordenada: ").capitalize()
        cord = obter_coordenadas(texto, coord)
        if cord != "Posição desconhecida.":
            ver_tabuleiro()
            print()
            mover_peca(cord[0], cord[1], tabu)
            print()
            ver_tabuleiro()
            break
        else:
            print("Coordenada desconhecida. Coordenadas válidas:")


def main():
    global quem_joga
    ver_tabuleiro()
    print()
    while vencedor is None:
        if quem_joga == 1:
            print("Jogador 1")
            jogar(tabuleiro_player_1)
            quem_joga = 2
        else:
            print("Jogador 2")
            jogar(tabuleiro_player_2)
            quem_joga = 1

if __name__ == "__main__":
    main()
