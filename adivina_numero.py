"""
Crea un juego simple en el que la computadora selecciona aleatoriamente un número y le pide al usuario que lo adivine. 
El programa debe proporcionar pistas al usuario si el número que ingresó es demasiado alto o demasiado bajo. 
El juego continuará hasta que el usuario adivine correctamente el número.
"""
import random


def dame_numero(inicio_n: int, fin_n: int)-> int:
    return random.randint(inicio_n, fin_n)

def adivinar_numero():

    star_n = input('Ingrese numero inicial: ')
    while not star_n.isdigit():
        star_n = input('Debe ingresar un numero entero: ')
    star_n = int(star_n)

    end_n = input('Ingrese numero final: ')
    while not end_n.isdigit():
        end_n = input('Debe ingresar un numero entero: ')
    end_n = int(end_n)


    n_para_adivinar = dame_numero(star_n, end_n)

    n_ingresado = int(input('Adivine el numero que yo tengo: \n'))

    while n_ingresado != n_para_adivinar:

        if n_ingresado < n_para_adivinar:
            print(f'Tiene que ser mayor a {n_ingresado}')
        
        elif n_ingresado > n_para_adivinar:
            print(f'Tiene que ser menor a {n_ingresado}')
        
        n_ingresado = int(input('intentelo de nuevo: \n'))
    
    print(f'Enhorabuena! {n_ingresado} es el numero correcto!')


adivinar_numero()
