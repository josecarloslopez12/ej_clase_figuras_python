try:
    alt = int(input("Introduce la altura de la figura: "))

    if alt <= 0:
        print("Error: La altura debe ser un número entero positivo.")
    else:
        for i in range(1, alt + 1):
            for j in range(1, i + 1):
                if j == 1 or j == i or i == alt:
                    print(" 4", end="")
                else:
                    print("  ", end="")
            print()

except ValueError:
    print(
        f"Error: La entrada '{alt}' no es un numero entero valido.")
