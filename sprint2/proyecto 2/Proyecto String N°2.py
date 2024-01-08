#Proyecto String N°2  Nombre: Matias Ismael Cansignia Burbano
"""Crear un sistema interactivo que permita agregar, buscar, eliminar y exportar estudiantes"""

#Agregar estudiantes
import csv
import re

def validar_nombre(nombre):
    patron = r'^[a-zA-Z\s]+$'
    return bool(re.match(patron, nombre))

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del nuevo estudiante (solo letras y espacios): ")
    if not validar_nombre(nombre):
        print("Nombre inválido, vuelva a intentarlo.Debe cumplir con las condiciones: solo letras y espacios.")
        return

    edad = input("Ingrese la edad del estudiante: ")
    curso = input("Ingrese el código del curso del estudiante: ")
    estudiantes.append({'Nombre': nombre, 'Edad': edad, 'Curso': curso})
    print("Estudiante agregado con exito.")

#Buscar el nombre del estudiante: 
def buscar_estudiante(estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
    resultados = [estudiante for estudiante in estudiantes if estudiante['Nombre'].lower() == nombre_buscar.lower()]
    if resultados:
        print("Resultados de su búsqueda:")
        for estudiante in resultados:
            print(f"Nombre: {estudiante['Nombre']}, Edad: {estudiante['Edad']}, Curso: {estudiante['Curso']}")
    else:
        print("Estudiante no registrado.")

#Eliminar estudiante:
def eliminar_estudiante(estudiantes):
    nombre_eliminar = input("Ingrese el nombre del estudiante a expulsar: ")
    for estudiante in estudiantes:
        if estudiante['Nombre'].lower() == nombre_eliminar.lower():
            estudiantes.remove(estudiante)
            print(f"{nombre_eliminar} ya no se encuentra registrado.")
            return
    print("Estudiante no encontrado.")

#Exportar a CSV: 
def exportar_a_csv(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['Nombre'])
    nombre_archivo = input("Ingrese el nombre del archivo CSV para exportar (sin extensión): ")
    nombre_archivo += '.csv'

    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Nombre', 'Edad', 'Curso'])
        writer.writeheader()
        writer.writerows(estudiantes_ordenados)
    print(f"Estudiantes exportados a '{nombre_archivo}' correctamente.")


lista_estudiantes = []

while True:
    print("\nBienvenido al sistema de estudiantes")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Exportar a formato CSV")
    print("5. Muchas gracias por su visita")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante(lista_estudiantes)

    elif opcion == "2":
        buscar_estudiante(lista_estudiantes)

    elif opcion == "3":
        eliminar_estudiante(lista_estudiantes)

    elif opcion == "4":
        exportar_a_csv(lista_estudiantes)

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
