class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave)
            else:
                self._inserir_recursivo(no_atual.esquerda, chave)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(chave)
            else:
                self._inserir_recursivo(no_atual.direita, chave)

    def busca(self, chave):
        return self._busca_recursiva(self.raiz, chave)

    def _busca_recursiva(self, no_atual, chave):
        if no_atual is None or no_atual.chave == chave:
            return no_atual
        if chave < no_atual.chave:
            return self._busca_recursiva(no_atual.esquerda, chave)
        return self._busca_recursiva(no_atual.direita, chave)

    def em_ordem(self):
        return self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, no_atual):
        if no_atual is not None:
            self._em_ordem_recursivo(no_atual.esquerda)
            print(no_atual.chave, end=' ')
            self._em_ordem_recursivo(no_atual.direita)


# Exemplo de uso:
arvore = ArvoreBinaria()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arvore.inserir(valor)

print("Percurso em ordem da árvore binária:")
arvore.em_ordem()
