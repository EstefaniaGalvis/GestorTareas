# Importamos la librería datetime para manejar fechas.
from datetime import datetime

# Definimos la estructura de datos para almacenar las tareas.
tareas = []

# Función para agregar una nueva tarea.
def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_limite = input("Ingrese la fecha límite (formato YYYY-MM-DD): ")
    tarea = {
        "descripcion": descripcion,
        "fecha_limite": datetime.strptime(fecha_limite, "%Y-%m-%d"),
        "estado": "pendiente",
    }
    tareas.append(tarea)

# Función para listar todas las tareas.
def listar_tareas():
    for tarea in tareas:
        print(f"ID: {tareas.index(tarea)}")
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')}")
        print(f"Estado: {tarea['estado']}")
        print("---")

# Función para completar una tarea.
def completar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
    tareas[id_tarea]["estado"] = "completada"

# Función para eliminar una tarea.
def eliminar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
    del tareas[id_tarea]

# Función para editar una tarea.
def editar_tarea():
    id_tarea = int(input("Ingrese el ID de la tarea a editar: "))
    tarea = tareas[id_tarea]
    print(f"Tarea actual: {tarea['descripcion']} - Fecha límite: {tarea['fecha_limite'].strftime('%Y-%m-%d')} - Estado: {tarea['estado']}")
    nueva_descripcion = input("Ingrese la nueva descripción de la tarea (deje en blanco para mantener la actual): ")
    nueva_fecha_limite = input("Ingrese la nueva fecha límite (formato YYYY-MM-DD) (deje en blanco para mantener la actual): ")
    nuevo_estado = input("Ingrese el nuevo estado (pendiente/completada) (deje en blanco para mantener el actual): ")

    if nueva_descripcion:
        tarea['descripcion'] = nueva_descripcion
    if nueva_fecha_limite:
        tarea['fecha_limite'] = datetime.strptime(nueva_fecha_limite, "%Y-%m-%d")
    if nuevo_estado:
        tarea['estado'] = nuevo_estado

# Menú principal
while True:
    print("**Sistema de gestión de tareas**")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Editar tarea")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        listar_tareas()
    elif opcion == 3:
        completar_tarea()
    elif opcion == 4:
        eliminar_tarea()
    elif opcion == 5:
        editar_tarea()
    elif opcion == 6:
        break
    else:
        print("Opción no válida.")

print("¡Hasta luego!")



