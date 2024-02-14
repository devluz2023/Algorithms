def pode_colocar_rainha(tabuleiro, linha, coluna, N):
    # Verifica se há uma rainha na mesma coluna
    for i in range(linha):
        if tabuleiro[i][coluna] == 1:
            return False

    # Verifica diagonal superior esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    # Verifica diagonal superior direita
    for i, j in zip(range(linha, -1, -1), range(coluna, N)):
        if tabuleiro[i][j] == 1:
            return False

    return True

def resolver_n_rainhas(tabuleiro, linha, N):
    if linha >= N:
        return True

    for coluna in range(N):
        if pode_colocar_rainha(tabuleiro, linha, coluna, N):
            tabuleiro[linha][coluna] = 1
            if resolver_n_rainhas(tabuleiro, linha + 1, N):
                return True
            tabuleiro[linha][coluna] = 0

    return False

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' '.join(map(str, linha)))

def resolver_problema_n_rainhas(N):
    tabuleiro = [[0] * N for _ in range(N)]
    if resolver_n_rainhas(tabuleiro, 0, N):
        print(f"Solução encontrada para {N} rainhas:")
        imprimir_tabuleiro(tabuleiro)
    else:
        print(f"Não há solução para {N} rainhas.")

# Exemplo de uso
resolver_problema_n_rainhas(8)  # Resolver o problema das 8 rainhas
