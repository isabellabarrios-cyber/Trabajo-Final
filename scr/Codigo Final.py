# ============================================================
# SISTEMA INTEGRADO – RESORT ARENA AZUL
# Incluye:
# - Planeación
# - Registro
# - Finanzas
# - Reportes
# - CSV
# - Login Administrativo (INTEGRADO)
# ============================================================

import csv
from datetime import datetime

# -----------------------------
# LOGIN ADMINISTRATIVO (INTEGRADO)
# -----------------------------

def linea():
    print("-" * 60)

def titulo(texto):
    linea()
    print(texto.center(60))
    linea()

def login_admin():
    """
    Valida usuario y contraseña del administrador
    (integrado al sistema grande)
    """
    credenciales = {
        "admin": "1234",
        "gerente": "5678",
        "supervisor": "9999"
    }

    titulo("ACCESO ADMINISTRATIVO")

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in credenciales and credenciales[usuario] == contraseña:
        print("\n✔ Acceso concedido.\n")
        return True
    else:
        print("\n✘ ACCESO DENEGADO.\n")
        return False


# -----------------------------
# ESTADO GLOBAL DEL SISTEMA
# -----------------------------
plan_dia = []               # Alistamientos del día
resultados = []            # Servicios vendidos / costos / ganancias
clientes_registrados = []  # Personas registradas en el día


# -----------------------------
# DATOS BASE DEL HOTEL
# -----------------------------
alistamientos = {
    "sencilla":     (7, 10),
    "doble":        (10, 15),
    "familiar":     (24, 35),
    "turismo":      (10, 15),
    "alimentacion": (2,  3),
    "mascotas":     (8,  8)
}

servicios = {
    "sencilla":    (7, 10, 15, 1),
    "doble":       (10, 15, 20, 2),
    "familiar":    (24, 35, 48, 4),
    "turismo":     (10, 15, 20, 1),
    "alimentacion":(2,  3,  4,  1),
    "mascotas":    (8,  8, 15, 1)
}

# ---------------------------------------------------
# MÓDULO 1: PLANEACIÓN DE LA DEMANDA
# ---------------------------------------------------
def calcular_alistamiento(servicio, cantidad, tipo):
    datos = alistamientos[servicio]
    costo_unitario = datos[0] if tipo == "general" else datos[1]
    costo_total = costo_unitario * cantidad
    return {
        "servicio": servicio,
        "cantidad": cantidad,
        "tipo": tipo,
        "costo_unitario": costo_unitario,
        "costo_total": costo_total
    }

def modulo_planeacion():
    print("=== PLANEACIÓN DE LA DEMANDA ===")
    continuar = "si"
    while continuar == "si":
        print("\nServicios disponibles:")
        print(list(alistamientos.keys()))

        servicio = input("Servicio a alistar: ").lower()
        if servicio not in alistamientos:
            print("Servicio inválido.")
            continue

        try:
            cantidad = int(input("Cantidad a alistar: "))
        except:
            print("Cantidad inválida.")
            continue

        tipo = input("Tipo (general/extraordinario): ").lower()
        if tipo not in ("general", "extraordinario"):
            print("Tipo inválido.")
            continue

        resultado = calcular_alistamiento(servicio, cantidad, tipo)
        plan_dia.append(resultado)

        print("\n✔ Alistamiento registrado")
        continuar = input("¿Registrar otro? (si/no): ").lower()

    print("\n=== RESUMEN DE ALISTAMIENTO ===")
    total = 0
    for r in plan_dia:
        print(r)
        total += r["costo_total"]
    print(f"COSTO TOTAL DEL DÍA: ${total}\n")

# ---------------------------------------------------
# MÓDULO 2: REGISTRO DE LLEGADA DE CLIENTES
# ---------------------------------------------------
def separador():
    print("\n" + "-" * 40 + "\n")

def validar_nombre(nombre):
    return len(nombre) >= 3 and nombre.isalpha()

def validar_apellido(apellido):
    return len(apellido) >= 3 and apellido.isalpha()

def validar_documento(doc):
    return doc.isdigit() and 3 <= len(doc) <= 15

def registrar_persona():
    separador()
    print("REGISTRO DE PERSONA")
    separador()

    while True:
        nombre = input("Nombre: ").strip()
        if validar_nombre(nombre):
            break
        print("Error: mínimo 3 letras.")

    while True:
        apellido = input("Apellido: ").strip()
        if validar_apellido(apellido):
            break
        print("Error: mínimo 3 letras.")

    while True:
        documento = input("Documento: ").strip()
        if validar_documento(documento):
            break
        print("Documento inválido.")

    return {"nombre": nombre, "apellido": apellido, "documento": documento}

def registrar_llegada():
    print("\n=== REGISTRO DE LLEGADA ===")
    print("1. Individual (1)")
    print("2. Pareja (2)")
    print("3. Familia (4)")

    while True:
        opcion = input("Seleccione (1-3): ")
        if opcion == "1": tipo = "Individual"; cantidad = 1; break
        elif opcion == "2": tipo = "Pareja"; cantidad = 2; break
        elif opcion == "3": tipo = "Familia"; cantidad = 4; break
        else:
            print("Opción inválida.")

    grupo = []
    for i in range(cantidad):
        print(f"\nPersona {i+1}:")
        p = registrar_persona()
        p["grupo_tipo"] = tipo
        clientes_registrados.append(p)
        grupo.append(p)

    print("\n✔ Registro completado.\n")
    return grupo

# ---------------------------------------------------
# MÓDULO 3: FINANZAS
# ---------------------------------------------------
def calcular_servicio(nombre_servicio, cantidad, tipo_alistamiento):

    valores = servicios[nombre_servicio]
    costo_general = valores[0]
    costo_extra   = valores[1]
    precio_venta  = valores[2]

    costo = (costo_general if tipo_alistamiento == "general" else costo_extra) * cantidad
    venta = precio_venta * cantidad
    ganancia = venta - costo

    return {
        "servicio": nombre_servicio,
        "cantidad": cantidad,
        "costo": costo,
        "venta": venta,
        "ganancia": ganancia
    }

def modulo_finanzas():
    print("\n=== REGISTRO DE SERVICIOS (COSTOS/VENTAS) ===")

    continuar_general = "si"

    while continuar_general == "si":

        print("\nServicios disponibles:")
        print(list(servicios.keys()))

        servicio = input("\nServicio principal: ").lower()
        if servicio not in servicios:
            print("Servicio inválido.")
            continue

        try:
            cantidad = int(input("Cantidad: "))
        except:
            print("Inválido.")
            continue

        tipo = input("Tipo (general/extraordinario): ").lower()
        if tipo not in ("general", "extraordinario"):
            print("Tipo inválido.")
            continue

        # Registrar servicio principal
        resultado = calcular_servicio(servicio, cantidad, tipo)
        resultados.append(resultado)

        print("\n✔ Servicio principal registrado.")

        # Servicios adicionales
        agregar = input("¿Agregar servicios adicionales? (si/no): ").lower()

        while agregar == "si":
            print("\nServicios disponibles:")
            print(list(servicios.keys()))

            serv_extra = input("\nServicio adicional: ").lower()
            if serv_extra not in servicios:
                print("Servicio inválido.")
                continue

            try:
                cant_extra = int(input("Cantidad: "))
            except:
                print("Inválido.")
                continue

            tipo_extra = input("Tipo (general/extraordinario): ").lower()
            if tipo_extra not in ("general", "extraordinario"):
                print("Tipo inválido.")
                continue

            resultado_extra = calcular_servicio(serv_extra, cant_extra, tipo_extra)
            resultados.append(resultado_extra)

            print("\n✔ Servicio adicional registrado.")
            agregar = input("¿Agregar otro? (si/no): ").lower()

        continuar_general = input("\n¿Registrar otro cliente/servicio? (si/no): ").lower()

# ---------------------------------------------------
# MÓDULO 4: ADMINISTRADOR (CON LOGIN INTEGRADO)
# ---------------------------------------------------
def calcular_disponibilidades():
    dispo = { "sencilla": 0, "doble": 0, "familiar": 0, "alimentacion": 0, "turismo": 0 }
    for a in plan_dia:
        s = a["servicio"]
        if s in dispo:
            dispo[s] += a["cantidad"]
    return dispo

def total_clientes_por_tipo():
    total = {"Individual":0, "Pareja":0, "Familia":0}
    for c in clientes_registrados:
        total[c["grupo_tipo"]] += 1
    return total

def contar_mascotas():
    return sum(r["cantidad"] for r in resultados if r["servicio"] == "mascotas")

def mostrar_reportes_admin():

    if not login_admin():
        return  # NO accede si falla el login

    dispo = calcular_disponibilidades()
    fin = {
        "costos": sum(r["costo"] for r in resultados),
        "ventas": sum(r["venta"] for r in resultados),
        "ganancias": sum(r["ganancia"] for r in resultados)
    }

    print("\n================= REPORTE GENERAL =================\n")
    print(f"Clientes registrados: {len(clientes_registrados)}")
    print("Clientes por tipo:", total_clientes_por_tipo())
    print(f"Mascotas atendidas: {contar_mascotas()}")
    print("\nDisponibilidades:", dispo)
    print("\nFinanzas:", fin)
    print(f"\nReporte generado el: {datetime.now()}")
    print("\n===================================================\n")

    return {"dispo": dispo, "finanzas": fin}


# ---------------------------------------------------
# MÓDULO 5: EXPORTACIÓN CSV Y SALIDA
# ---------------------------------------------------
def exportar_csv(clientes, finanzas, disponibilidades):
    archivo = "reporte_final_del_dia.csv"
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)

        w.writerow(["CLIENTES REGISTRADOS"])
        w.writerow(["Nombre", "Apellido", "Documento", "Grupo"])
        for c in clientes:
            w.writerow([c["nombre"], c["apellido"], c["documento"], c["grupo_tipo"]])
        w.writerow([])

        w.writerow(["DISPONIBILIDAD"])
        w.writerow(["Servicio", "Cantidad"])
        for s, v in disponibilidades.items():
            w.writerow([s, v])
        w.writerow([])

        w.writerow(["FINANZAS"])
        w.writerow(["Costos", "Ventas", "Ganancias"])
        w.writerow([finanzas["costos"], finanzas["ventas"], finanzas["ganancias"]])

    print(f"\n✔ Archivo exportado como: {archivo}")

def salir_sistema():
    print("\n=== FIN DEL DÍA ===")

    # Acceso protegido
    if not login_admin():
        print("\nNo se pueden generar reportes sin acceso administrativo.\n")
        return

    reporte = mostrar_reportes_admin()

    opc = input("\n¿Exportar reporte CSV? (si/no): ").lower()
    if opc == "si":
        exportar_csv(clientes_registrados, reporte["finanzas"], reporte["dispo"])

    print("\nSistema cerrado. ¡Hasta mañana!\n")

# ---------------------------------------------------
# MENÚ PRINCIPAL
# ---------------------------------------------------
def menu_principal():
    while True:
        print("\n===== SISTEMA RESORT ARENA AZUL =====")
        print("1. Planeación de demanda")
        print("2. Registro de clientes")
        print("3. Servicios (ventas/costos)")
        print("4. Administrador (reportes)  🔐")
        print("5. Salir del sistema")
        op = input("Seleccione una opción: ")

        if op == "1":
            modulo_planeacion()
        elif op == "2":
            registrar_llegada()
        elif op == "3":
            modulo_finanzas()
        elif op == "4":
            mostrar_reportes_admin()
        elif op == "5":
            salir_sistema()
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
