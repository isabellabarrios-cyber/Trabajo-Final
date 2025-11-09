# ===========================================
# Módulo: Planeación de la Demanda
# Proyecto: Resort Arena Azul
# ===========================================

def planeacion_demanda():
    print("\n=== PLANEACIÓN DE LA DEMANDA ===")

    # Solicitar el número total de habitaciones
    habitaciones = int(input("Ingrese el número total de habitaciones: "))

    # Solicitar los cupos disponibles para alimentación y turismo
    alimentacion = int(input("Ingrese los cupos disponibles en alimentación: "))
    turismo = int(input("Ingrese los cupos disponibles en turismo: "))

    # Pedir cuántas habitaciones hay por tipo
    print("\nIngrese la cantidad de habitaciones por tipo:")
    sencillas = int(input("  Sencillas: "))
    dobles = int(input("  Dobles: "))
    familiares = int(input("  Familiares: "))

    # Crear un resumen (almacenado en un diccionario)
    planeacion = {
        "habitaciones_totales": habitaciones,
        "sencillas": sencillas,
        "dobles": dobles,
        "familiares": familiares,
        "cupos_alimentacion": alimentacion,
        "cupos_turismo": turismo
    }

    # Mostrar los datos ingresados
    print("\n--- RESUMEN DE ALISTAMIENTO ---")
    print(f"Habitaciones totales: {habitaciones}")
    print(f" - Sencillas: {sencillas}")
    print(f" - Dobles: {dobles}")
    print(f" - Familiares: {familiares}")
    print(f"Cupos de alimentación: {alimentacion}")
    print(f"Cupos de turismo: {turismo}")

    print("\n Alistamiento completado.")
    return planeacion


# --- Prueba del módulo ---
if __name__ == "__main__":
    datos = planeacion_demanda()
    print("\nDatos guardados:", datos)
