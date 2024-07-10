print("Area del circulo")
radio = float(input("Ingrese el radio del circulo: "))
def area_circulo ():
  pi = 3.14
  area = pi * radio ** 2
  return area

resultado = area_circulo()
print(f"el area del circulo es: {resultado}.")