cantidad = 0

while cantidad <= 0:
    try:
        cantidad = int(input("¿Cuántas notas deseas guardar? "))
        if cantidad <= 0:
            print("Debes ingresar una cantidad mayor que cero.")
    except ValueError:
        print("Ingresa una cantidad usando un número entero.")

notas = []

while len(notas) < cantidad:
    try:
        nota = float(input(f"Ingresa la nota {len(notas) + 1}: "))
        notas.append(nota)
    except ValueError:
        print("Ingresa una nota usando un número.")

respuesta = input("¿Deseas guardar todas las notas en el archivo? (s/n): ").strip().lower()

while respuesta != "s" and respuesta != "n":
    respuesta = input("Responde con 's' para sí o 'n' para no: ").strip().lower()

if respuesta == "s":
    with open("notas.txt", "w", encoding="utf-8") as archivo:
        for nota in notas:
            archivo.write(f"{nota}\n")

    with open("notas.txt", "r", encoding="utf-8") as archivo:
        notas = [float(linea.strip()) for linea in archivo]
    print("Las notas se guardaron en notas.txt.")
else:
    print("Las notas no se guardaron en el archivo.")

promedio = sum(notas) / len(notas)
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print(f"Notas ingresadas: {notas}")
print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")
