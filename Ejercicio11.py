def suma_infinito (limite):
  suma = 0
  for num in range(1, limite + 1):
    suma += num
  return suma

ingreso_limite_usuario = int(input("Ingrese el limite al que desea sumar los números: "))

resultado = suma_infinito(ingreso_limite_usuario)

print(f"La suma de números naturales hasta {ingreso_limite_usuario} es: {resultado}")