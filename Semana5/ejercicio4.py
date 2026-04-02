"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    pares =  0
    numero = 1 
    while numero <= n: 
        if numero % 2 == 0 : 
            pares = pares + 1
            numero= numero + 1
    return pares


def contar_pares_recursivo(n):
    if n == 1: 
       return 0 
    else: 
        if n % 2 == 0:
            return contar_pares_recursivo(n-1)+1
        else:  
            return contar_pares_recursivo(n-1)