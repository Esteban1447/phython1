import random

# Asignar de forma aleatoria el valor de tipoestudiante (True o False)
# Esto para que no siempre le salga todas las notas negativaas a algunos estudiantes
tipoestudiante = random.choice([True, False])


# Lista de materias
materias = ['Matemáticas', 'Historia', 'Ciencias']

# Lista de estudiantes disponibles para elegir
estudiantes_disponibles = ['Estudiante 1', 'Estudiante 2', 'Estudiante 3']

# Diccionario para almacenar las notas de cada estudiante (inicialmente en 0)
notas_estudiantes = {
    estudiante: {materia: 0 for materia in materias} 
    for estudiante in estudiantes_disponibles
}

# Validación para saber si es estudiante o profesor
validacion = input("¿Eres estudiante o profesor?: ").lower()

if validacion == "estudiante":
    # Mostrar menú con los estudiantes disponibles
    print("\nEstudiantes disponibles:")
    for i, est in enumerate(estudiantes_disponibles, 1):
        print(f"{i}. {est}")
        
    # Solicitar al usuario que seleccione un estudiante por su número
    eleccion = int(input("\nSeleccione el número del estudiante: "))
    estudiante = estudiantes_disponibles[eleccion - 1]

    # Asignar notas aleatorias según el valor aleatorio de tipoestudiante
    for materia in materias:
        if tipoestudiante:
            # Si tipoestudiante es True: notas aleatorias de 3 a 5
            notas_estudiantes[estudiante][materia] = random.uniform(3, 5)
        else:
            # Si es False: notas aleatorias de 1 a 5
            notas_estudiantes[estudiante][materia] = random.uniform(1, 5)

    # Mostrar las notas del estudiante elegido
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
                    if 1 <= nueva_nota <= 5:  # Validamos que la nota esté entre 1 y 5
                        notas_estudiantes[estudiante_elegido][materia] = nueva_nota
                        break
                    else:
                        print("Por favor, ingrese una nota válida entre 1 y 5.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        # Mostrar las nuevas notas asignadas
        print(f"\nNuevas notas de {estudiante_elegido}:")
        for materia, nota in notas_estudiantes[estudiante_elegido].items():
            print(f'{materia}: {nota:.2f}')

else:
    print("Opción no válida. Por favor, ingrese 'estudiante' o 'profesor'.")
