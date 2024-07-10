def indice_masa_corporal(peso, altura):
    # Para calcular el IMC es peso (kg) / altura (m) al cuadrado
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))

imc = indice_masa_corporal(peso, altura)

print("Tu índice de masa corporal (IMC) es:", imc)