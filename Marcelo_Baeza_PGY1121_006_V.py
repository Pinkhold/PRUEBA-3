
lotes_disponibles = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None],
    [None, None, None, None, None]
]


detalles_lotes = [
    {"numero": 1, "tamaño": "100 m²", "precio": "$100,000"},
    {"numero": 2, "tamaño": "200 m²", "precio": "$200,000"},
    {"numero": 3, "tamaño": "300 m²", "precio": "$300,000"},
    {"numero": 4, "tamaño": "400 m²", "precio": "$400,000"},
    {"numero": 5, "tamaño": "500 m²", "precio": "$500.000"},
    {"numero": 6, "tamaño": "100 m²", "precio": "$100,000"},
    {"numero": 7, "tamaño": "200 m²", "precio": "$200,000"},
    {"numero": 8, "tamaño": "300 m²", "precio": "$300,000"},
    {"numero": 9, "tamaño": "400 m²", "precio": "$400,000"},
    {"numero": 10, "tamaño": "500 m²", "precio": "$500.000"},
    {"numero": 11, "tamaño": "100 m²", "precio": "$100,000"},
    {"numero": 12, "tamaño": "200 m²", "precio": "$200,000"},
    {"numero": 13, "tamaño": "300 m²", "precio": "$300,000"},
    {"numero": 14, "tamaño": "400 m²", "precio": "$400,000"},
    {"numero": 15, "tamaño": "500 m²", "precio": "$500.000"},
    {"numero": 16, "tamaño": "100 m²", "precio": "$100,000"},
    {"numero": 17, "tamaño": "200 m²", "precio": "$200,000"},
    {"numero": 18, "tamaño": "300 m²", "precio": "$300,000"},
    {"numero": 19, "tamaño": "400 m²", "precio": "$400,000"},
    {"numero": 20, "tamaño": "500 m²", "precio": "$500.000"},
]

# Lista de clientes
clientes = []

def mostrar_lotes_disponibles():
    for fila in lotes_disponibles:
        for lote in fila:
            if lote is None:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print()

def seleccionar_lote():
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su teléfono: ")
    email = input("Ingrese su email: ")

    fila = int(input("Ingrese la fila del lote: "))
    columna = int(input("Ingrese la columna del lote: "))
    
    fila-=1
    columna-=1

    if fila < 0 or fila >= len(lotes_disponibles) or columna < 0 or columna >= len(lotes_disponibles[0]):
        print("Coordenadas inválidas.")
        return

    if lotes_disponibles[fila][columna] is None:
        lotes_disponibles[fila][columna] = "X"
        lote_seleccionado = {"fila": fila, "columna": columna, "rut": rut, "nombre": nombre, "telefono": telefono, "email": email}
        clientes.append(lote_seleccionado)
        print("Lote seleccionado con éxito.")
    else:
        print("El lote seleccionado no está disponible.")

    
def mostrar_detalles_lote_seleccionado():
    if len(clientes) > 0:
        cliente = clientes[-1]
        fila = cliente["fila"]
        columna = cliente["columna"]
        lote = detalles_lotes[columna + fila * len(lotes_disponibles[0])]
        print(f"Detalles del lote seleccionado:")
        print(f"Número de lote: {lote['numero']}")
        print(f"Tamaño del terreno: {lote['tamaño']}")
        print(f"Precio: {lote['precio']}")
    else:
        print("No hay lotes seleccionados.")

def mostrar_clientes():
    if len(clientes) > 0:
        print("Clientes que han comprado lotes:")
        for cliente in clientes:
            print(f"RUT: {cliente['rut']}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Email: {cliente['email']}")
            print()
    else:
        print("No hay clientes.")


while True:
    print("----- LoteosDUOC -----")
    print("1. Ver disponibilidad de lotes")
    print("2. Seleccionar un lote")
    print("3. Ver detalles del lote seleccionado")
    print("4. Ver clientes")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        mostrar_lotes_disponibles()
    elif opcion == "2":
        seleccionar_lote()
    elif opcion == "3":
        mostrar_detalles_lote_seleccionado()
    elif opcion == "4":
        mostrar_clientes()
    elif opcion == "5":
        print("Saliendo")
        break
    else:
        print("Opción inválida. ingresa una opcion Valida")
