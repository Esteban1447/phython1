# Lista de materias
materias = ['Matemáticas', 'Historia', 'Ciencias']


# Lista de estudiantes disponibles para elegir
estudiantes_disponibles = ['Estudiante 1', 'Estudiante 2', 'Estudiante 3']

# Diccionario para almacenar las notas de cada estudiante (inicialmente en 0)
notas_estudiantes = {estudiante: {materia: 0 for materia in materias} for estudiante in estudiantes_disponibles}

# Validación para saber si es estudiante o profesor
validacion = input("¿Eres estudiante o profesor?: ").lower()

if validacion == "estudiante":
    estudiante = input("Digite su nombre: ")

    # Si el estudiante no ingresa un nombre, asignamos uno por defecto
    if estudiante == "":
        estudiante = "Estudiante 1"

    
    # Mostrar las notas del estudiante
    print(f"\nNotas de {estudiante}:")
    for materia, nota in notas_estudiantes[estudiante].items():
        print(f'{materia}: {nota:.2f}')

elif validacion == "profesor":
    profesor = input("Digite su nombre: ")

    # Si el profesor no ingresa un nombre, asignamos uno por defecto
    if profesor == "":
        profesor = "Profesor 1"

    while True:
        # Mostrar lista de estudiantes disponibles para que el profesor elija
        print("\nEstudiantes disponibles:")
        for i, est in enumerate(estudiantes_disponibles, 1):
            print(f"{i}. {est}")

        # El profesor elige un estudiante
        eleccion = int(input("\nSeleccione el número del estudiante (o 0 para salir): "))

        if eleccion == 0:
            break

        estudiante_elegido = estudiantes_disponibles[eleccion - 1]

        # Mostrar las notas actuales del estudiante
        print(f"\nNotas actuales de {estudiante_elegido}:")
        for materia, nota in notas_estudiantes[estudiante_elegido].items():
            print(f'{materia}: {nota:.2f}')

        # El profesor puede asignar nuevas notas manualmente
        print("\nIngrese las nuevas notas para las materias del estudiante:")
        for materia in materias:
            while True:
                try:
                    nueva_nota = float(input(f"Nota para {materia}: "))
                    if 0 <= nueva_nota <= 10:  # Validamos que la nota esté entre 0 y 10
                        notas_estudiantes[estudiante_elegido][materia] = nueva_nota
                        break
                    else:
                        print("Por favor, ingrese una nota válida entre 0 y 10.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        # Mostrar las nuevas notas asignadas
        print(f"\nNuevas notas de {estudiante_elegido}:")
        for materia, nota in notas_estudiantes[estudiante_elegido].items():
            print(f'{materia}: {nota:.2f}')

else:
    print("Opción no válida. Por favor, ingrese 'estudiante' o 'profesor'.")
