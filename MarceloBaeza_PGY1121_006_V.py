departamentos_disponibles = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]


detalles_departamentos = [
    
    {"departamento": 1,"piso":"1", "letra": "A", "precio": "3800 UF"},
    {"departamento": 2, "piso":"1", "letra": "B", "precio": "3000 UF"},
    {"departamento": 3, "piso":"1", "letra": "C", "precio": "2800 UF"},
    {"departamento": 4, "piso":"1", "letra": "D", "precio": "3500 UF"},
    {"departamento": 5, "piso":"2", "letra": "A", "precio": "3800 UF"},
    {"departamento": 6, "piso":"2", "letra": "B", "precio": "3000 UF"},
    {"departamento": 7, "piso":"2", "letra": "C", "precio": "2800 UF"},
    {"departamento": 8, "piso":"2", "letra": "D", "precio": "3500 UF"},
    {"departamento": 9, "piso":"3", "letra": "A", "precio": "3800 UF"},
    {"departamento": 10, "piso":"3", "letra": "B", "precio": "3000 UF"},
    {"departamento": 11, "piso":"3", "letra": "C", "precio": "2800 UF"},
    {"departamento": 12, "piso":"3", "letra": "D", "precio": "3500 UF"},
    {"departamento": 13, "piso":"4", "letra": "A", "precio": "3800 UF"},
    {"departamento": 14, "piso":"4", "letra": "B", "precio": "3000 UF"},
    {"departamento": 15, "piso":"4", "letra": "C", "precio": "2800 UF"},
    {"departamento": 16, "piso":"4", "letra": "D", "precio": "3500 UF"},
    {"departamento": 17, "piso":"5", "letra": "A", "precio": "3800 UF"},
    {"departamento": 18, "piso":"5", "letra": "B", "precio": "3000 UF"},
    {"departamento": 19, "piso":"5", "letra": "C", "precio": "2800 UF"},
    {"departamento": 20, "piso":"5", "letra": "D", "precio": "3500 UF"},
    {"departamento": 21, "piso":"6", "letra": "A", "precio": "3800 UF"},
    {"departamento": 22, "piso":"6", "letra": "B", "precio": "3000 UF"},
    {"departamento": 23, "piso":"6", "letra": "C", "precio": "2800 UF"},
    {"departamento": 24, "piso":"6", "letra": "D", "precio": "3500 UF"},
    {"departamento": 25, "piso":"7", "letra": "A", "precio": "3800 UF"},
    {"departamento": 26, "piso":"7", "letra": "B", "precio": "3000 UF"},
    {"departamento": 27, "piso":"7", "letra": "C", "precio": "2800 UF"},
    {"departamento": 28, "piso":"7", "letra": "D", "precio": "3000 UF"},
    {"departamento": 29, "piso":"8", "letra": "A", "precio": "3800 UF"},
    {"departamento": 30, "piso":"8", "letra": "B", "precio": "3000 UF"},
    {"departamento": 31, "piso":"8", "letra": "C", "precio": "2800 UF"},
    {"departamento": 32, "piso":"8", "letra": "D", "precio": "3500 UF"},
    {"departamento": 33, "piso":"9", "letra": "A", "precio": "3800 UF"},
    {"departamento": 34, "piso":"9", "letra": "B", "precio": "3000 UF"},
    {"departamento": 35, "piso":"9", "letra": "C", "precio": "2800 UF"},
    {"departamento": 36, "piso":"9", "letra": "D", "precio": "3500 UF"},
    {"departamento": 37, "piso":"10", "letra": "A", "precio": "3800 UF"},
    {"departamento": 38, "piso":"10", "letra": "B", "precio": "3000 UF"},
    {"departamento": 39, "piso":"10", "letra": "C", "precio": "2800 UF"},
    {"departamento": 40, "piso":"10", "letra": "D", "precio": "3500 UF"},
]

#Lista de Clientes

clientes = []

def mostrar_departamentos_disponibles():
    for piso in departamentos_disponibles:
        for departamento in piso:
            if departamento is None:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print()

def seleccionar_departamento():
    rut = input("Ingrese su RUT: ") 
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su teléfono: ")
    email = input("Ingrese su email: ")

    piso = int(input("Ingrese el piso del Departamento: "))
    departamento = int(input("Ingrese la letra del departamento con numeros *A1,B2,C3,D4* "))

    piso-=1
    departamento-=1

    if piso < 0 or piso >= len(departamentos_disponibles) or departamento < 0 or departamento >= len(departamentos_disponibles[0]):
        print("Coordenadas inválidas.")
        return

    if departamentos_disponibles[piso][departamento] is None:
        departamentos_disponibles[piso][departamento] = "X"
        detalles_departamentos = {"piso": piso, "departamento": departamento, "rut": rut, "nombre": nombre, "telefono": telefono, "email": email}
        clientes.append(detalles_departamentos)
        print("Departamento seleccionado con éxito.")
    else:
        print("El departamento seleccionado no está disponible.")                


def validar_rut(rut):
    rut=rut.upper()
    rut=rut.append("-"," ")        
    rut=rut.replace("."," ")
    if rut < 0 or rut >= len(validar_rut):
        print ("Rut incorrecto")
        return validar_rut

def detalle_departamentos_disponibles():
    if len(clientes) > 0:
        cliente = clientes[-1]
        piso = cliente["piso"]
        departamento = cliente["departamento"]
        departamento = detalles_departamentos[piso + departamento * len(departamentos_disponibles[0])]
        print(f"Detalles del departamento seleccionado:")
        print(f"Piso del departamento: {departamento['piso']}")
        print(f"Letra de departamento: {departamento['letra']}")
        print(f"Precio: {departamento['precio']}")
    else:
        print("No hay lotes seleccionados.")

def mostrar_clientes():
    if len(clientes) > 0:
        print("Clientes que han comprado departamentos:")
        for cliente in clientes:
            print(f"RUT: {cliente['rut']}")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Email: {cliente['email']}")
            print()
    else:
        print("No hay clientes.")

while True:
    print("********** Inmobiliaria Casa Feliz **********")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. detalle departamento")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        seleccionar_departamento()
    elif opcion == "2":
        mostrar_departamentos_disponibles()
    elif opcion == "3":
        mostrar_clientes()
    elif opcion == "4":
        detalle_departamentos_disponibles()
    elif opcion == "5":
        print("Saliendo")
    
    else:
        print("Opción inválida. ingresa una opcion Valida")
       
