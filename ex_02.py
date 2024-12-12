"""
Escreva uma função que verifique se um número é par ou ímpar. 
Remova os comentários desnecessários do código.
"""

def isPar(numero):
    # Verifica se o número é par
    if numero % 2 == 0: # Usa o operador módulo para obter o resto da divisão por 2
        return True # Retorna verdadeiro se o resto for zero
    else:
        return False # Retorna falso se o resto for diferente de zero


def is_even(number: int) -> bool:
    """
    Return if the number is even or odd
    """
    return number % 2 == 0
