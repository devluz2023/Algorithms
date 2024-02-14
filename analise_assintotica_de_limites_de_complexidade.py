# O(log n) - Complexidade Logarítmica:
def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


# O(n^2) - Complexidade Quadrática:
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# O(n) - Complexidade Linear:
def soma_lista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

# O(1) - Complexidade Constante:
def retorna_primeiro_elemento(lista):
    return lista[0]



# O(log n) - Binary Search
def test_busca_binaria():
    lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert busca_binaria(lista, 5) == 2
    assert busca_binaria(lista, 13) == 5
    assert busca_binaria(lista, 29) == 9
    assert busca_binaria(lista, 6) == -1
    assert busca_binaria(lista, 30) == -1

# O(n^2) - Bubble Sort
def test_bubble_sort():
    lista = [64, 25, 12, 22, 11]
    assert bubble_sort(lista) == [11, 12, 22, 25, 64]

# O(n) - Linear Complexity
def test_soma_lista():
    lista = [1, 2, 3, 4, 5]
    assert soma_lista(lista) == 15

# O(1) - Constant Complexity
def test_retorna_primeiro_elemento():
    lista = [42, 56, 78, 93]
    assert retorna_primeiro_elemento(lista) == 42

# Run tests
test_busca_binaria()
test_bubble_sort()
test_soma_lista()
test_retorna_primeiro_elemento()

print("All tests passed successfully!")
