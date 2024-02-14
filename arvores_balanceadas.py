class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def rotacao_direita(self, no):
        nova_raiz = no.esquerda
        no.esquerda = nova_raiz.direita
        nova_raiz.direita = no

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        nova_raiz.altura = 1 + max(self.altura(nova_raiz.esquerda), self.altura(nova_raiz.direita))

        return nova_raiz

    def rotacao_esquerda(self, no):
        nova_raiz = no.direita
        no.direita = nova_raiz.esquerda
        nova_raiz.esquerda = no

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        nova_raiz.altura = 1 + max(self.altura(nova_raiz.esquerda), self.altura(nova_raiz.direita))

        return nova_raiz

    def fator_balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def inserir(self, no, chave):
        if not no:
            return No(chave)
        elif chave < no.chave:
            no.esquerda = self.inserir(no.esquerda, chave)
        else:
            no.direita = self.inserir(no.direita, chave)

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        balanceamento = self.fator_balanceamento(no)

        # Caso de rotação à direita
        if balanceamento > 1 and chave < no.esquerda.chave:
            return self.rotacao_direita(no)

        # Caso de rotação à esquerda
        if balanceamento < -1 and chave > no.direita.chave:
            return self.rotacao_esquerda(no)

        # Caso de rotação à esquerda-direita
        if balanceamento > 1 and chave > no.esquerda.chave:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # Caso de rotação à direita-esquerda
        if balanceamento < -1 and chave < no.direita.chave:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir_valor(self, raiz, chave):
        return self.inserir(raiz, chave)

    def pre_ordem(self, raiz):
        if raiz:
            print(raiz.chave, end=' ')
            self.pre_ordem(raiz.esquerda)
            self.pre_ordem(raiz.direita)


# Exemplo de uso:
arvore = ArvoreAVL()
raiz = None
valores = [10, 20, 30, 40, 50, 25]

for valor in valores:
    raiz = arvore.inserir_valor(raiz, valor)

print("Pre-ordem da árvore balanceada AVL:")
arvore.pre_ordem(raiz)
