def texto_palindromo (texto):
  texto = texto.lower()
  return texto == texto[::-1]

texto_usuario = input("Ingrese una palabra para comprobar si es palindromo: ")
if texto_palindromo(texto_usuario):
  print(f"La palabra {texto_usuario} es palindromo.")
else:
  print(f"La palabra {texto_usuario} no es palindromo.")