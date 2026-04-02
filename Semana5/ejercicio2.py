"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    #retorna la suma de los primeros n numeros usando un ciclo 
    suma = 0 
    for i in range (1, n + 1 ):
        suma = suma + i 
        return suma

def suma_recursiva(n):
    #retorna la suma de los primeros n números usando recursividad 
    if n == 1: 
        return 1
    else: 
        return suma_recursiva(n-1)+n