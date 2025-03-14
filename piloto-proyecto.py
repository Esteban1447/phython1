profesor = ""
estudiante = ""

validacion = input("Estudiante o profesor: ")

if validacion.lower() == "estudiante":
    estudiante = input("Estudiante:"+"\n"
                       +"Digite el nombre ")
    profesor = "profesor 1"
elif validacion.lower() == "profesor":
        profesor = input("Profesor:"+"\n"
                         +"Digite el nombre ")
        estudiantes = "estudiante 1"

print(estudiante+" "+profesor)
