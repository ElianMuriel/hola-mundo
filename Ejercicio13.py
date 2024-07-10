def contar_vocales (texto):
  vocales = "aeiouAEIOU"
  contador = 0
  for letra in texto:
    if letra in vocales:
      contador += 1
  return contador

texto_usuario = input("Ingrese un texto para contar sus vocales: ")
conteo_vocales = contar_vocales(texto_usuario)
print(f"La cantidad de vocales en el texto es: {conteo_vocales}")