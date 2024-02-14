def troco_minimo(valor, moedas):
    """
    Função para calcular o troco mínimo utilizando o algoritmo guloso.
    
    Argumentos:
    valor -- O valor do troco a ser dado.
    moedas -- Uma lista das denominações das moedas disponíveis.
    
    Retorna:
    Uma lista das moedas necessárias para o troco.
    """
    moedas.sort(reverse=True)  # Ordena as moedas em ordem decrescente
    
    troco = []  # Lista para armazenar as moedas do troco
    
    for moeda in moedas:
        while valor >= moeda:
            troco.append(moeda)
            valor -= moeda
    
    return troco

# Exemplo de uso
valor_troco = 48
denominacoes_moedas = [1, 5, 10, 25]  # Supondo moedas de 1 centavo, 5 centavos, 10 centavos e 25 centavos
troco = troco_minimo(valor_troco, denominacoes_moedas)
print("Troco mínimo:", troco)
