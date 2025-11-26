# ------------------------------------------
# DATOS DEL RESORT ARENA AZUL
# ------------------------------------------

servicios = {
    "sencilla":    (7, 10, 15, 1),
    "doble":       (10, 15, 20, 2),
    "familiar":    (24, 35, 48, 4),
    "turismo":     (10, 15, 20, 1),
    "alimentacion":(2,  3,  4,  1),
    "mascotas":    (8,  8, 15, 1)
}

# Lista para guardar los resultados del día
resultados = []


# ----------------------------------------------------
# FUNCIÓN PARA CALCULAR COSTO, VENTA Y GANANCIA
# ----------------------------------------------------
def calcular_servicio(nombre_servicio, cantidad, tipo_alistamiento):
    valores = servicios[nombre_servicio]
    costo_general = valores[0]
    costo_extra = valores[1]
    precio_venta = valores[2]

    if tipo_alistamiento == "general":
        costo = costo_general * cantidad
    else:
        costo = costo_extra * cantidad

    venta = precio_venta * cantidad
    ganancia = venta - costo

    return {
        "servicio": nombre_servicio,
        "cantidad": cantidad,
        "costo": costo,
        "venta": venta,
        "ganancia": ganancia
    }


# ----------------------------------------------------
# MÓDULO PRINCIPAL DE SERVICIOS
# ----------------------------------------------------
print("=== CÁLCULO DE COSTOS, VENTAS Y GANANCIAS ===\n")

continuar_general = "si"

while continuar_general == "si":

    print("\nServicios disponibles:")
    print(list(servicios.keys()))

    # Servicio principal
    servicio = input("\nIngrese el servicio principal: ").lower()
    cantidad = int(input("Cantidad a registrar: "))
    tipo = input("Tipo de alistamiento (general / extraordinario): ").lower()

    resultado = calcular_servicio(servicio, cantidad, tipo)
    resultados.append(resultado)

    print("\nServicio principal registrado correctamente.\n")

    # ----------------------------------------------------
    # CICLO PARA AGREGAR SERVICIOS ADICIONALES
    # ----------------------------------------------------
    agregar_mas = input("¿Desea agregar servicios adicionales? (si/no): ").lower()

    while agregar_mas == "si":
        print("\nServicios adicionales disponibles:")
        print(list(servicios.keys()))

        serv_extra = input("\nIngrese el servicio adicional: ").lower()
        cant_extra = int(input("Cantidad: "))
        tipo_extra = input("Tipo de alistamiento (general / extraordinario): ").lower()

        resultado_extra = calcular_servicio(serv_extra, cant_extra, tipo_extra)
        resultados.append(resultado_extra)

        print("\nServicio adicional registrado.\n")

        agregar_mas = input("¿Agregar otro servicio adicional? (si/no): ").lower()

    continuar_general = input("\n¿Desea registrar otro cliente/servicio? (si/no): ").lower()


# ----------------------------------------------------
# RESUMEN FINAL DEL DÍA
# ----------------------------------------------------
total_costos = sum(r["costo"] for r in resultados)
total_ventas = sum(r["venta"] for r in resultados)
total_ganancias = sum(r["ganancia"] for r in resultados)

print("\n=========== RESUMEN DEL DÍA ===========")
print(f"{'Servicio':15} {'Cantidad':10} {'Costo':10} {'Venta':10} {'Ganancia':10}")

for r in resultados:
    print(f"{r['servicio']:15} {r['cantidad']:10} {r['costo']:10} {r['venta']:10} {r['ganancia']:10}")

print("---------------------------------------")
print(f"{'TOTALES':15} {'':10} {total_costos:10} {total_ventas:10} {total_ganancias:10}")
print("=======================================")
