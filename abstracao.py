def encontrar_maior_numero(lista):
    """
    Função para encontrar o maior número em uma lista.
    
    Argumentos:
    lista -- A lista de números.
    
    Retorna:
    O maior número na lista.
    """
    maior = lista[0]  # Suponha que o primeiro número é o maior inicialmente
    
    # Percorre a lista para encontrar o maior número
    for num in lista:
        if num > maior:
            maior = num
    
    return maior

# Exemplo de uso
numeros = [10, 5, 8, 20, 15]
resultado = encontrar_maior_numero(numeros)
print("O maior número na lista é:", resultado)
 