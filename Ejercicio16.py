import random

def numeros_aleatorios():
    print("Se muestra 5 numeros aleatorios entre 1 y 100:")
    for num in range(5):
        numero_aleatorio = random.randint(1, 100)
        print(numero_aleatorio)

numeros_aleatorios()