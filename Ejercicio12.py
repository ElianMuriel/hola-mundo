def invertir_cadena_texto(cadena):
    return cadena[::-1]

ingreso_usuario_cadena = input("Introduce una cadena de texto para invertirla: ")
cadena_invertida = invertir_cadena_texto(ingreso_usuario_cadena)
print("Cadena invertida:", cadena_invertida)