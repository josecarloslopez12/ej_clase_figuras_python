try:
    ancho_maximo = int(input("Introduce el ancho de la figura: "))
except ValueError:
    print("Error: Por favor, introduce un número entero válido.")
    exit()

if ancho_maximo <= 0:
    print("Error: El ancho máximo debe ser un número positivo.")
    exit()

altura_total = (ancho_maximo * 2) - 1

for i in range(1, altura_total + 1):

    if i <= ancho_maximo:
        indice_linea = i
    else:
        indice_linea = ancho_maximo - (i - ancho_maximo)
    columna_borde_derecho = ancho_maximo - 1
    columna_borde_izquierdo = ancho_maximo - indice_linea
    linea = ""
    for j in range(ancho_maximo):
        if j == columna_borde_izquierdo:
            linea += "*"
        elif j == columna_borde_derecho:
            linea += "*"
        else:
            linea += " "
    print(linea)
