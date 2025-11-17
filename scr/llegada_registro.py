# ===========================================
# Módulo: Registro de Clientes
# Proyecto: Resort Arena Azul
# ===========================================

def separador():
    print("\n" + "-" * 40 + "\n")


# -------- VALIDACIONES --------

def validar_nombre(nombre):
    return len(nombre) >= 3 and nombre.isalpha()

def validar_apellido(apellido):
    return len(apellido) >= 3 and apellido.isalpha()

def validar_documento(doc):
    return doc.isdigit() and 3 <= len(doc) <= 15


# -------- REGISTRO DE UNA PERSONA --------

def registrar_persona():
    separador()
    print("REGISTRO DE PERSONA")
    separador()

    # Nombre
    while True:
        nombre = input("Nombre: ").strip()
        if validar_nombre(nombre):
            break
        print("  Error: mínimo 3 letras, solo caracteres alfabéticos.")

    # Apellido
    while True:
        apellido = input("Apellido: ").strip()
        if validar_apellido(apellido):
            break
        print("  Error: mínimo 3 letras, solo caracteres alfabéticos.")

    # Documento
    while True:
        documento = input("Documento: ").strip()
        if validar_documento(documento):
            break
        print("  Error: entre 3 y 15 dígitos, solo números.")

    return {
        "nombre": nombre,
        "apellido": apellido,
        "documento": documento
    }


# -------- REGISTRO DE LLEGADA --------

def registrar_llegada():
    separador()
    print("REGISTRO DE LLEGADA")
    separador()

    print("Tipos de llegada:")
    print("  1. Individual (1 persona)")
    print("  2. Pareja     (2 personas)")
    print("  3. Familia    (4 personas)")

    while True:
        opcion = input("\nSeleccione una opción (1-3): ").strip()

        if opcion == "1":
            tipo = "Individual"
            cantidad = 1
            break
        elif opcion == "2":
            tipo = "Pareja"
            cantidad = 2
            break
        elif opcion == "3":
            tipo = "Familia"
            cantidad = 4
            break
        else:
            print("  Opción inválida. Intente de nuevo.")

    separador()
    print(f"Tipo seleccionado: {tipo}")
    print(f"Número de personas a registrar: {cantidad}")
    separador()

    clientes = []

    for i in range(cantidad):
        print(f"Persona {i+1} de {cantidad}")
        persona = registrar_persona()
        clientes.append(persona)

    # -------- RESUMEN FINAL --------
    separador()
    print("RESUMEN DE CLIENTES REGISTRADOS")
    separador()

    for i, c in enumerate(clientes, start=1):
        print(f"Cliente {i}:")
        print(f"  Nombre:    {c['nombre']}")
        print(f"  Apellido:  {c['apellido']}")
        print(f"  Documento: {c['documento']}")
        print("-" * 40)

    print("Registro finalizado.\n")
    return clientes


# Prueba del módulo
if __name__ == "__main__":
    registrar_llegada()
