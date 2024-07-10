print("Par o impar.")
def par_o_impar (numero):
  if numero % 2 == 0:
    print(f"el numero: {numero} es par")
  else:
    print(f"el numero {numero} es impar")

numero = int(input("Ingrese un valor: "))
par_o_impar(numero)