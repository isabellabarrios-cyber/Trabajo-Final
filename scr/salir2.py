import csv

# Datos temporales para evitar errores
clientes_registrados = []
totales = {"costos": 0, "ventas": 0, "ganancias": 0}

def exportar_csv(clientes, totales):
    nombre_archivo = "reporte_final_del_dia.csv"

    with open(nombre_archivo, mode="w", newline="") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(["CLIENTES REGISTRADOS"])
        escritor.writerow(["Nombre", "Documento", "Habitación"])

        for c in clientes:
            escritor.writerow([c["nombre"], c["documento"], c["habitacion"]])

        escritor.writerow([])  
        escritor.writerow(["RESULTADOS DEL ADMINISTRADOR"])
        escritor.writerow(["Costos", "Ventas", "Ganancias"])
        escritor.writerow([totales["costos"], totales["ventas"], totales["ganancias"]])

    print(f"\nArchivo CSV exportado correctamente como: {nombre_archivo}")


def salir_sistema():
    print("\n=== FIN DEL DÍA ===")
    opcion = input("¿Desea exportar los datos del día en un archivo CSV? (si/no): ").lower()

    if opcion == "si":
        exportar_csv(clientes_registrados, totales)

    print("\nEl sistema se ha cerrado de manera segura. ¡Hasta mañana!")