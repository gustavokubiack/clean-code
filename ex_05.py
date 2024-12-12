"""
Escreva um programa que armazene as oito notas e os nomes 
dos estudantes da disciplina de POO II. Calcule a média 
da turma e imprima os nomes e as notas daqueles ficaram acima da média.
"""

def area_circulo(raio: int) :
    """
    Calcula a área de um círculo dado o raio
    """
    return 3.14159 * (raio ** 2)


def volume_esfera(raio: int):
    """
    Calcula o volume de uma esfera dado o raio
    """
    return (4 / 3) * 3.14159 * (raio ** 3) 


print(area_circulo(5))
print(volume_esfera(raio=5))
