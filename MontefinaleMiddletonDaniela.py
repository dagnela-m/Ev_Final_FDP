import random
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = {}

def asignar_sueldos_aleatorios(trabajadores):
    sueldos = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos[trabajador] = sueldo

    for trabajador, sueldo in sueldos.items():
        print(f"{trabajador}: ${sueldo}")
    return sueldos

def clasificar_sueldos(sueldos):
    clasificacion = {"Sueldos menores a $800.000": [], "Sueldos entre $800.000 y $2.000.000": [], "Sueldos mayores a $2.000.000": []}

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            clasificacion["Sueldos menores a $800.000"].append((trabajador, sueldo))
        elif sueldo > 800000 and sueldo < 2000000:
            clasificacion["Sueldos entre $800.000 y $2.000.000"].append((trabajador, sueldo))
        else:
            clasificacion["Sueldos mayores a $2.000.000"].append((trabajador, sueldo))
    
    menores_800000 = len(clasificacion["Sueldos menores a $800.000"])

    entre_800000_2000000 = len(clasificacion["Sueldos entre $800.000 y $2.000.000"])

    mayores_2000000 = len(clasificacion["Sueldos mayores a $2.000.000"])

    print(f"Sueldos menores a $800.000\n Total: {menores_800000}")
    for trabajador, sueldo in clasificacion["Sueldos menores a $800.000"]:
            print(f"{trabajador}: {sueldo:,}")
    
    print(f"Sueldos entre $800.000 y $2.000.000\n Total: {entre_800000_2000000}")
    for trabajador, sueldo in clasificacion["Sueldos entre $800.000 y $2.000.000"]:
            print(f"{trabajador}: {sueldo:,}")

    print(f"Sueldos mayores a $2.000.000\n Total: {mayores_2000000}")
    for trabajador, sueldo in clasificacion["Sueldos mayores a $2.000.000"]:
            print(f"{trabajador}: {sueldo:,}")

    print(f"Total sueldos: ${sum(sueldos.values())}")

def ver_estadisticas(sueldos):
    sueldo_mas_alto = max(sueldos.values())
    print(f"Sueldo más alto: {sueldo_mas_alto}")  

    sueldo_mas_bajo = min(sueldos.values())
    print(f"Sueldo más bajo: {sueldo_mas_bajo}")

    sueldos_prom = (sum(sueldos.values()) / len(sueldos))
    print(f"Promedio sueldos: {sueldos_prom}")

    #medida geométrica
    
def reporte_de_sueldos(sueldos):
    with open("sueldos.csv", "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])

        for trabajador, sueldo in sueldos.items():
            duescuento_salud = (sueldo * 0.07)                 
            descuento_afp = (sueldo * 0.12)
            sueldo_liquido = (sueldo - duescuento_salud - descuento_afp)

            escritor_csv.writerow([trabajador, sueldo, duescuento_salud, descuento_afp, sueldo_liquido])    

while True:
    print("""
        1. Asignar sueldos aleatorios
        2. Clasificar sueldos
        3. Ver estadísticas.
        4. Reporte de sueldos
        5. Salir del programa""")
    opcion_menu = input("Seleccione una opción.\n")

    if opcion_menu == "1":
        sueldos = asignar_sueldos_aleatorios(trabajadores)
    elif opcion_menu == "2":
        if len(sueldos) > 0:
            clasificar_sueldos(sueldos)
        else:
            print("Asignar sueldos primero.")
    elif opcion_menu == "3":
        if len(sueldos) > 0:
            ver_estadisticas(sueldos)
        else:
            print("Asignar sueldos primero.")
    elif opcion_menu == "4":
        if len(sueldos) > 0:
            reporte_de_sueldos(sueldos)
        else:
            print("Asignar sueldos primero.")
    elif opcion_menu == "5":
        print("""
                Saliendo del programa...
                Desarrollado por Daniela Montefinale
                RUT: 18.956.898-3""")
        break
    else:
        print("Ingrese una opción de menú válida.")