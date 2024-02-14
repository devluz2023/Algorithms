class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        if no_atual is None:
            return No(chave)

        if chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, chave)

        return no_atual

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no_atual, chave):
        if no_atual is None or no_atual.chave == chave:
            return no_atual

        if chave < no_atual.chave:
            return self._buscar_recursivo(no_atual.esquerda, chave)
        return self._buscar_recursivo(no_atual.direita, chave)

    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, no_atual):
        if no_atual is not None:
            self._em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.chave, end=' ')
            self._em_ordem_recursivo(no_atual.direita)


# Exemplo de uso:
arvore = ArvoreBuscaBinaria()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arvore.inserir(valor)

print("Percurso em ordem da árvore de busca binária:")
arvore.em_ordem()

chave_busca = 30
no_encontrado = arvore.buscar(chave_busca)
if no_encontrado:
    print(f"Chave {chave_busca} encontrada na árvore.")
else:
    print(f"Chave {chave_busca} não encontrada na árvore.")
