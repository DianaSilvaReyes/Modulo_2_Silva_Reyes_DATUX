# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO "VENTAS "
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

# 1. CREA UN MENU ITERACTIVO QUE CUENTE CON LOS SIGUIENTES OPCIONES
def menu():
    print("El menu de opciones es el siguiente: ")
    print("\n--- Menú de Ventas ---")
    print("1. Mostrar el listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular la suma total de las ventas")
    print("4. Calcular el promedio de ventas")
    print("5. Mostrar el producto con más unidades vendidas")
    print("6. Mostrar el listado de productos")
    print("7. Salir")
    
    opcion=input("SELECCIONE UNA OPCION: ")
    if opcion=="1":
        Mostar_Ventas()
    elif opcion=="2":
        Nuevo_Producto()
    elif opcion=="3":
        Suma_Total()
    elif opcion=="4":
        Prom_Ventas()
    elif opcion=="5":
        Mas_Vendido()
    elif opcion=="6":
        Productos()
    elif opcion=="7":
        print("Vuelva pronto")
        break
    else:
        print("Opcion no valida") 

# 2. Mostrar el listado de ventas => puedes usar print(f"")
def Mostar_Ventas():
    for venta in ventas:
        print(f"Fecha: {ventas["fecha"]}, Producto: {ventas["producto"]}, Cantidad: {ventas["cantidad"]}, Precio: {ventas["precio"]}, Promocion: {ventas["promocion"]}")

# 3. Añadir un producto
def Nuevo_Producto():
    fecha=input("Ingresar nueva fecha (dd-mm-aaaa): ")
    producto=input("Ingresar producto (Producto_Letra): ")
    cantidad=input("Ingresar la cantidad: ")
    precio=float(input("Ingresar precio: "))
    promocion=input("¿Esta en promocion?si/no: ").lower==si
    nuevo[
        {
            "fecha":fecha,
            "producto":producto,
            "cantidad":cantidad,
            "precio":precio,
            "promocion":promocion
        }
    ]
ventas.append(nuevo)
print("Producto añadido de manera satisfactoria")
print("Las ventas son: ",ventas)

# 4. Calcular la suma total de las ventas
def Suma_Total ():
    suma=0
    for venta in ventas:
        suma+=venta["cantidad"]*venta["precio"]
        print("La suma de las ventas es ",suma)

# 5. Calcular el promedio de ventas
def Prom_Ventas():
    suma=0
    contador=0
    for venta in ventas:
        suma+=venta["cantidad"]*venta["precio"]
        contador+=1
    if contador>0:
        print("El promedio es: ", suma/contador)
    else:
        print("No se realizaron ventas")
        
# 6. Mostar el producto mas unidades vendidas
def Mas_Vendido():
    for cant in ventas:
        
# 7. Mostrar el listado de productos
def Productos():
    for prod in ventas:
        prod=ventas["producto"]
        print(f"El listado de productos es: {"producto"}")
