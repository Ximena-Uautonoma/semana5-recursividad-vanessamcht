"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    resultado = 1 
    contador = 1 
    while contador <= n: 
        resultado = resultado * contador
        contador = contador + 1
    return resultado
   


def factorial_recursivo(n):
    if n == 1: 
        return 1
    else: 
        return n * factorial_recursivo(n-1)