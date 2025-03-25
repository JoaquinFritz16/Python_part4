def agregar_tarea(tareas, tarea, fecha_limite, prioridad):
    nueva_tarea = {"Tarea": tarea, "Fecha limite": fecha_limite, "Prioridad": prioridad, "Completada":False}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"\nTarea {i}:")
            for clave, valor in tarea.items():
                print(f"{clave}: {valor}")
def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado="🦖"
            if tarea["Completada"]:
                estado="🦖"
                print(f"{i}.{tarea['Tarea']} - Estado = {estado}")
            else:
                estado="👹"
                print(f"{i}.{tarea['Tarea']} - Estado = {estado}")
            print(f"\nTarea {i}:")
    try:
        num_tarea=int(input("Ingrese el numero de tarea completada: "))
        if 1<= num_tarea <= len(tareas):
            tareas[num_tarea - 1]["Completada"] = True
            print("Tarea marcada como completada")
        else:
            print("numero fuera de rango")
    except ValueError:
        print("Entrada no valida de numero")

if __name__ == "__main__":
    lista_tareas = []
    
    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tareas como completadas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha límite (formato: dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)
        elif opcion == "2":
            mostrar_tareas(lista_tareas)
        elif opcion == "3":
            marcar_completada(lista_tareas)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
