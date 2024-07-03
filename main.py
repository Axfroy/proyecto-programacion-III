import json

def imprimir_totales(sucursal, alumnos_por_sucursal, alumnos_por_curso, alumnos_por_materia, alumnos_por_profesor):
    print("-------------------------------------")
    print(f"Sucursal: {sucursal}")
    print(f"Total de alumnos en la sucursal: {alumnos_por_sucursal[sucursal]}")
    # Totales por curso
    for curso, total in alumnos_por_curso.items():
        print(f'Curso "{curso}" hay {total} alumnos')

    # Totales por materia
    for materia, total in alumnos_por_materia.items():
        print(f'En la materia "{materia}" hay {total} alumnos')

    # Totales por profesor
    for profesor, total in alumnos_por_profesor.items():
        print(f'Con el profesor "{profesor}" hay {total} alumnos')


with open("registros_devueltos_de_la_tabla_maestra.json", "r") as json_file:
    data = json.load(json_file)

sucursalActual = 0
cursoActual = 0
materiaActual = 0
profesorActual = 0
contAlumnos = 0
totalAlumnos = 0
totalProfesores = 0

alumnos_por_curso = {}
alumnos_por_materia = {}
alumnos_por_profesor = {}
alumnos_por_sucursal = {}

for registro in data:
    sucursal = int(registro["SUCURSAL"])
    curso = int(registro["CURSO"])
    materia = int(registro["MATERIA"])
    profesor = int(registro["PROFESOR"])

    if sucursalActual == 0:
        sucursalActual = sucursal

    if sucursalActual != sucursal:
        totalProfesores += len(alumnos_por_profesor)
        imprimir_totales(sucursalActual, alumnos_por_sucursal, alumnos_por_curso, alumnos_por_materia, alumnos_por_profesor)

        # Reseteo las variables 
        sucursalActual = sucursal
        cursoActual = 0
        materiaActual = 0
        profesorActual = 0
        contAlumnos = 0
        alumnos_por_curso = {}
        alumnos_por_materia = {}
        alumnos_por_profesor = {}

    if cursoActual != curso:
        cursoActual = curso
        contAlumnos = 0

    if materiaActual != materia:
        materiaActual = materia
        contAlumnos = 0

    if profesorActual != profesor:
        profesorActual = profesor
        contAlumnos = 0

    contAlumnos += 1
    totalAlumnos += 1

    # Aca guardo el array con el registro de cada valor (Key) actual y le aumento el contador (valor)
    alumnos_por_curso[cursoActual] = alumnos_por_curso.get(cursoActual, 0) + 1
    alumnos_por_materia[materiaActual] = alumnos_por_materia.get(materiaActual, 0) + 1
    alumnos_por_profesor[profesorActual] = alumnos_por_profesor.get(profesorActual, 0) + 1
    alumnos_por_sucursal[sucursalActual] = alumnos_por_sucursal.get(sucursalActual, 0) + 1


# Imprimimos la última sucursal
totalProfesores += len(alumnos_por_profesor)
imprimir_totales(sucursalActual, alumnos_por_sucursal, alumnos_por_curso, alumnos_por_materia, alumnos_por_profesor)

# Imprimimos totales generales
print("-------------------------------------")
print(f"Total de alumnos: {totalAlumnos}")
print(f"Total de profesores: {totalProfesores}")