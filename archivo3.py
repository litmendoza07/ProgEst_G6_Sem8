#Leer los nombres, apellidos, edad y carrera de un estudiante 
#guardo en un archivo llamado estudiante.txt
nombre = input("Dime tus nombres: ")
apellido = input("Dime tus apellido: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu carrera: ")

datos = f"Nombre: {nombre.title()}\nApellido: {apellido.title()}\nEdad: {edad}\nCarrera: {carrera.title()}\n"

with open("estudiante.txt", "a+", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo creado satisfactoriamente")

