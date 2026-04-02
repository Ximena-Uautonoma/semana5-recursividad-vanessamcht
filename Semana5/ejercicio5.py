"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1 
    contador = 0 
    while contador < exponente:
        resultado = base * exponente 
        contador = contador + 1
        return resultado


def potencia_recursiva(base, exponente):
    if exponente == 0: 
        return 1
    else: 
        return base * potencia_recursiva(base, exponente - 1)
    
    pass 
