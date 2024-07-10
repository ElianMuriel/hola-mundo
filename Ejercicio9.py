def tabla_de_multiplicar (num):
  print(f"Tabla del {num}")
  for numero in range (1, 12 +1):
    resultado = num * numero
    print(f"{num} x {numero} = {resultado}")

ingreso_usuario = int(input("Ingrese un número para ver su tabla: "))
tabla_de_multiplicar(ingreso_usuario)