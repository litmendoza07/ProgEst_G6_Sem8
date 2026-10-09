estudiantes = []

cantidad = int(input("Ingrese la cantidad de estudiantes: "))

while cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
    cantidad = int(input("Ingrese la cantidad de estudiantes: "))

for numero in range(cantidad):
    print(f"\nEstudiante {numero + 1}")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    nota = float(input("Nota: "))

    estudiante = {
        "nombres": nombres,
        "apellidos": apellidos,
        "nota": nota
    }
    estudiantes.append(estudiante)

total_notas = 0
estudiante_mayor = estudiantes[0]
estudiante_menor = estudiantes[0]

for estudiante in estudiantes:
    total_notas += estudiante["nota"]

    if estudiante["nota"] > estudiante_mayor["nota"]:
        estudiante_mayor = estudiante

    if estudiante["nota"] < estudiante_menor["nota"]:
        estudiante_menor = estudiante

promedio = total_notas / cantidad

mejores_estudiantes = []
indices_seleccionados = []

for posicion in range(3):
    mejor_estudiante = None
    mejor_indice = -1

    for indice in range(cantidad):
        if indice not in indices_seleccionados:
            if mejor_estudiante is None or estudiantes[indice]["nota"] > mejor_estudiante["nota"]:
                mejor_estudiante = estudiantes[indice]
                mejor_indice = indice

    if mejor_estudiante is not None:
        mejores_estudiantes.append(mejor_estudiante)
        indices_seleccionados.append(mejor_indice)

print(f"\nPromedio de notas: {promedio:.2f}")
print(
    f"Nota más alta: {estudiante_mayor['nota']} - "
    f"{estudiante_mayor['nombres']} {estudiante_mayor['apellidos']}"
)
print(
    f"Nota más baja: {estudiante_menor['nota']} - "
    f"{estudiante_menor['nombres']} {estudiante_menor['apellidos']}"
)

print("\nLos 3 estudiantes con mayor nota:")
for posicion in range(len(mejores_estudiantes)):
    estudiante = mejores_estudiantes[posicion]
    print(
        f"{posicion + 1}. {estudiante['nombres']} {estudiante['apellidos']} "
        f"- Nota: {estudiante['nota']}"
    )
