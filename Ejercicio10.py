def numero_primo (numero):
  if numero % 2 == 0:
    print(f"el numero {numero} es primo")
  else:
    print(f"el número {numero} no es primo.")
ingreso_usuario = int(input("Ingrese un número para ver si es o no primo: "))
numero_primo(ingreso_usuario)