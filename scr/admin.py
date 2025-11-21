# ===========================================
# Módulo Administrador - Resort Arena Azul
# ===========================================

import getpass
from datetime import datetime


# ---------- PRESENTACIÓN ----------

def linea():
    print("-" * 60)

def titulo(texto):
    linea()
    print(texto.center(60))
    linea()


# ---------- VALIDACIÓN DEL ADMINISTRADOR ----------

def login_admin():
    """
    Valida usuario y contraseña contra la lista interna.
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
        print("\nAcceso concedido.\n")
        return True
    else:
        print("\nACCESO DENEGADO: Usuario o contraseña incorrectos.\n")
        return False



# ---------- DATOS INTERNOS DEL SISTEMA ----------


datos = {
    "total_clientes": 26,
    "individual": 8,
    "pareja": 6,
    "familia": 3,
    "mascotas": 5,

    "hab_disponibles": 12,
    "alim_disponible": 40,
    "tur_disponible": 30,

    "ventas": 850000,
    "costos": 400000,
    "ganancia": 450000
}



# ---------- REPORTE  ----------

def mostrar_reportes():
    """
    Muestra todos los reportes del administrador usando
    los datos internos del sistema.
    """

    titulo("REPORTE GENERAL - RESORT ARENA AZUL")

    # --- Sección 1: Huéspedes ---
    print(">>> CLIENTES REGISTRADOS")
    linea()
    print(f"Total de clientes:                  {datos['total_clientes']}")
    print(f" - Individuales:                    {datos['individual']}")
    print(f" - Parejas:                         {datos['pareja']}")
    print(f" - Familias:                        {datos['familia']}")
    print(f"Total de mascotas:                  {datos['mascotas']}\n")

    # --- Sección 2: Disponibilidad ---
    print(">>> DISPONIBILIDAD DEL RESORT")
    linea()
    print(f"Habitaciones disponibles:           {datos['hab_disponibles']}")
    print(f"Cupos alimentación disponibles:      {datos['alim_disponible']}")
    print(f"Cupos turismo disponibles:           {datos['tur_disponible']}\n")

    # --- Sección 3: Finanzas ---
    print(">>> FINANZAS DEL DÍA")
    linea()
    print(f"Ventas del día:                     ${datos['ventas']}")
    print(f"Costos del día:                     ${datos['costos']}")
    print(f"Ganancia generada:                  ${datos['ganancia']}\n")

    # --- Marca de fecha ---
    linea()
    print(f"Reporte generado el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    linea()
    print()



# ---------- FUNCIÓN PRINCIPAL  ----------

def modulo_administrador():
    """
    Controla todo el proceso:
    1. Validar credenciales
    2. Mostrar reportes
    """

    if login_admin():
        mostrar_reportes()
    else:
        print("No se pudo acceder al módulo administrativo.")



# ---------- EJECUCIÓN DEL MÓDULO ----------
if __name__ == "__main__":
    modulo_administrador()
