print("Calculadora.")
def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplicacion(num1, num2):
  return num1 * num2

def division(num1, num2):
  if num2 == 0:
    return "No se divide para 0"
  else:
    return num1 / num2

print("Seleccione una opcion: ")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

op = input("Ingrese literal de operacion a realizar: ")

num1 = float(input("Ingrese un primer valor: "))
num2 = float(input("Ingrese un segundo valor: "))

if op == "1":
  print("La suma es: ", suma(num1, num2))
elif op == "2":
  print("La resta es: ", resta(num1, num2))
elif op == "3":
  print("La multiplicacion es: ", multiplicacion(num1, num2))
elif op == "4":
  print("La division es: ", division(num1, num2))
else:
  print("Opcion no valida")