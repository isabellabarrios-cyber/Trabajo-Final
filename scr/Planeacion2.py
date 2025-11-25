# DATOS DEL RESORT (alistamientos)
# ---------------------------------------

# Diccionario: servicio → (costo_alistamiento_general, costo_alistamiento_extraordinario)
alistamientos = {
    "sencilla":     (7, 10),
    "doble":        (10, 15),
    "familiar":     (24, 35),
    "turismo":      (10, 15),
    "alimentacion": (2,  3),
    "mascotas":     (8,  8)
}

# Lista donde guardaremos los alistamientos del día
plan_dia = []


# ----------------------------------------------------
# FUNCIÓN PARA CALCULAR EL ALISTAMIENTO POR SERVICIO
# ----------------------------------------------------
def calcular_alistamiento(servicio, cantidad, tipo):
    datos = alistamientos[servicio]

    if tipo == "general":
        costo_unitario = datos[0]
    else:
        costo_unitario = datos[1]

    costo_total = costo_unitario * cantidad

    return {
        "servicio": servicio,
        "cantidad": cantidad,
        "tipo": tipo,
        "costo_unitario": costo_unitario,
        "costo_total": costo_total
    }


# ----------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------
print("=== PLANEACIÓN DE LA DEMANDA - ARENA AZUL ===\n")

continuar = "si"

while continuar == "si":
    print("\nServicios disponibles:")
    print(list(alistamientos.keys()))

    servicio = input("\nIngrese el servicio a alistar: ").lower()
    cantidad = int(input("Cantidad a preparar: "))
    tipo = input("Tipo de alistamiento (general / extraordinario): ").lower()

    resultado = calcular_alistamiento(servicio, cantidad, tipo)
    plan_dia.append(resultado)

    print("\n--- ALISTAMIENTO REGISTRADO ---")
    print(f"{'Servicio':15} {'Cantidad':10} {'Tipo':15} {'C.Unitario':12} {'C.Total':10}")
    print(f"{resultado['servicio']:15} {resultado['cantidad']:10} {resultado['tipo']:15} "
          f"{resultado['costo_unitario']:12} {resultado['costo_total']:10}")

    continuar = input("\n¿Desea agregar otro alistamiento? (si/no): ").lower()


# ----------------------------------------------------
# RESUMEN DEL DÍA EN COLUMNAS
# ----------------------------------------------------
print("\n=========== RESUMEN DEL ALISTAMIENTO INICIAL ===========")

print(f"{'Servicio':15} {'Cantidad':10} {'Tipo':15} {'C.Unitario':12} {'C.Total':10}")

costo_general = 0

for r in plan_dia:
    print(f"{r['servicio']:15} {r['cantidad']:10} {r['tipo']:15} {r['costo_unitario']:12} {r['costo_total']:10}")
    costo_general += r["costo_total"]

print("---------------------------------------------------------")
print(f"{'COSTO TOTAL DEL DÍA':30} $ {costo_general}")
print("=========================================================")