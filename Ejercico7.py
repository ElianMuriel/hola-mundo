def celsius_a_fahrenheit (celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit
celsius_temp = float(input("Ingrese la temperatura en grados celsius: "))
fahrenheit_temp = celsius_a_fahrenheit(celsius_temp)
print(f"La temperatura de: {celsius_temp} grados celsius convertida a grados fahrenheit es: {fahrenheit_temp}.")