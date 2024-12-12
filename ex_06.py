""""
Escreva quatro funções que calculem, respectivamente, a soma 
dos quadrados, a média, a variância e o desvio padrão de uma 
lista de dados.
"""

def soma_quadrados(lista):
    """
    retorna a soma dos quadrados dos elementos da lista
    """
    return sum(x ** 2 for x in lista)


def media(lista):
    """
    retorna a média dos elementos da lista
    """
    return sum(lista)/len(lista)


def variancia(lista):
    """
    retorna a variância dos elementos da lista
    """
    m = media(lista)
    return soma_quadrados([x - m for x in lista]) / len(lista)


def desvio_padrao(lista):
    """
    retorna o desvio padrão dos elementos da lista
    """
    return variancia(lista) ** 0.5
