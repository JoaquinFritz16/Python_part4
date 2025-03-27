def agregar_tarea(tareas, tarea, fecha_limite, prioridad):
    nueva_tarea = {"Tarea": tarea, "Fecha limite": fecha_limite, "Prioridad": prioridad, "Completada": False}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def mostrar_tareas(tareas, completadas=None):
    tareas_filtradas = []

    if completadas is None:
        tareas_filtradas = tareas
    else:
        tareas_filtradas = [t for t in tareas if t["Completada"] == completadas]

    if not tareas_filtradas:
        print("No hay tareas en esta categoría.")
    else:
        for i, tarea in enumerate(tareas_filtradas, 1):
            estado = "✅" if tarea["Completada"] else "❌"
            print(f"\nTarea {i} ({estado}):")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")

def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
        return

    print("\nTareas:")
    for i, tarea in enumerate(tareas, 1):
        estado = "✅" if tarea["Completada"] else "❌"
        print(f"{i}. {tarea['Tarea']} - Estado: {estado}")

    try:
        num_tarea = int(input("Ingrese el número de tarea completada: "))
        if 1 <= num_tarea <= len(tareas):
            tareas[num_tarea - 1]["Completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada no válida. Ingrese un número.")

if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Mostrar tareas completadas")
        print("4. Mostrar tareas no completadas")
        print("5. Marcar tarea como completada")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)
        elif opcion == "2":
            mostrar_tareas(lista_tareas)
        elif opcion == "3":
            mostrar_tareas(lista_tareas, completadas=True)
        elif opcion == "4":
            mostrar_tareas(lista_tareas, completadas=False)
        elif opcion == "5":
            marcar_completada(lista_tareas)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")