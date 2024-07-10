def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

ingreso_numero_usuario = int(input("Introduce un número para calcular su factorial: "))

if ingreso_numero_usuario < 0:
    print("El factorial no se define por números negativos.")
else:
    resultado = factorial(ingreso_numero_usuario)
    print(f"El factorial de {ingreso_numero_usuario} es: {resultado}")