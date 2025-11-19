#pre definimos un inventario
inventario = [{
    1: {"Nombre": "Arroz", "Precio $":3000, "Cant":5},
    2: {"Nombre": "Panela", "Precio $":2500, "Cant":5},
    3: {"Nombre": "Leche", "Precio $":4000, "Cant":5},
    4: {"Nombre": "Atún", "Precio $": 3000, "Cant":5}
}]
#Creamos una funcion para buscar por nombre en el inventario
def buscar_prod(nombre_producto):
    productos = inventario[0]

    for id_prod, datos in productos.items():
        if datos["Nombre"].lower() == nombre_producto.lower():
            return id_prod  # regresamos el número del producto
    
    return None

def agregar_prod(nombre_producto):
    productos = inventario[0]

    # Buscar número del producto por nombre
    id_prod = buscar_prod(nombre_producto)

    if id_prod is None:
        print("❌ No existe un producto con ese nombre.")
        return

    producto = productos[id_prod]

    # Validar stock
    if producto["Cant"] <= 0:
        print("⚠️ No queda stock disponible.")
        return

    nombre = producto["Nombre"]
    precio = producto["Precio $"]

    # Agregar al carrito
    if id_prod in carrito:
        carrito[id_prod]["Cantidad"] += 1
    else:
        carrito[id_prod] = {
            "Nombre": nombre,
            "Precio $": precio,
            "Cantidad": 1
        }

    # Descontar stock
    producto["Cant"] -= 1

    print(f"🛒 Se agregó 1 unidad de '{nombre}' al carrito.")

def mostrar_inv():
    print(inventario[0][1])#Ajustar precio: caro
    print(inventario[0][2])
    print(inventario[0][3])
    print(inventario[0][4])#Ajustar precio: barato
    print("")
    
def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
        return

    print("\n--- CARRITO DE COMPRA ---")
    print(f"{'ID':<5}{'Nombre':<15}{'Precio':<10}{'Cant':<7}{'Subtot':<10}")
    print("-"*50)

    total = 0

    for id_prod, datos in carrito.items():
        nombre = datos["Nombre"]
        precio = datos["Precio $"]
        cant = datos["Cantidad"]
        subtotal = precio * cant
        total += subtotal

        print(f"{id_prod:<5}{nombre:<15}{precio:<10}{cant:<7}{subtotal:<10}")

    print("-"*50)
    print(f"TOTAL: {total}")


def eliminar_prod(nombre_prod):
    nombre_prod = nombre_prod.lower()
    productos = inventario[0]

    # 1. Buscar el ID del producto por el nombre
    id_en_carrito = None
    for id_prod, datos in carrito.items():
        if datos["Nombre"].lower() == nombre_prod:
            id_en_carrito = id_prod
            break

    # Si no lo encontró
    if id_en_carrito is None:
        print("❌ Ese producto no está en el carrito.")
        return

    cantidad_carrito = carrito[id_en_carrito]["Cantidad"]
    print(f"Tienes {cantidad_carrito} unidades de '{nombre_prod}' en el carrito.")

    devolver = input("¿Cuántas quieres devolver?: ")

    # Validación
    if not devolver.isdigit():
        print("❌ Debes ingresar un número.")
        return

    devolver = int(devolver)

    if devolver < 1:
        print("❌ No puedes devolver menos de 1.")
        return
    
    if devolver > cantidad_carrito:
        print("❌ No puedes devolver más de las que tienes.")
        return

    # 2. Restar del carrito
    nueva_cantidad = cantidad_carrito - devolver

    if nueva_cantidad == 0:
        del carrito[id_en_carrito]  # eliminar del carrito
        print(f"✔ '{nombre_prod}' eliminado del carrito.")
    else:
        carrito[id_en_carrito]["Cantidad"] = nueva_cantidad
        print(f"✔ Ahora tienes {nueva_cantidad} unidades en el carrito.")

    # 3. Devolver al inventario
    productos[id_en_carrito]["Cant"] += devolver
    print(f"✔ Inventario actualizado: ahora hay {productos[id_en_carrito]['Cant']} unidades de '{nombre_prod}'.")





#Damos ingreso al usuario a la tienda y definimos la salida como false para representar que está dentro de la tienda comprando

salida = False
print("Bienvenido user al mercadillo, que deseas hacer el dia de hoy? ")

#Creamos el carrito del user
carrito = {
    
}

#Creamos un bucle que nos permita que el user compre hasta que decida finalizar su compra
while salida != True:
    print("")
    print("1. Iniciar compra") #Aplicar cupon 
    print("2. Consultar precio del carrito")
    print("3. Eliminar prod del carrito")
    menu = input("4. Salir: ")
    print("")

    #Usamos match case para simplificar el menú 
    match menu:
        case "1":
            cont = 0
            cerrar_compra = False
            while cerrar_compra != True:
                print("Bienvenido estimado cliente, estos son los productos que tenemos disponibles para tí: ")
                mostrar_inv()
                compra = input("Que deseas comprar el dia de hoy?: ")
                print("")
                agregar_prod(compra)   
                cont += 1
                if cont >= 2:
                    print("")
                    menu_i = input("Desea regresar al menu principal? (y/n): ")
                    if menu_i == "y":
                        print("")
                        print("Redierccionando al menu principal...")
                        cerrar_compra = True
                    elif menu_i == "n":
                        print("")
                        print("Redireccionando al menu de compra...")
                else:
                    pass
                
        case "2":
            print("")
            mostrar_carrito()

                
                
        case "3":
            if not carrito:
                print("El carrito está vacío.")
            else:
                mostrar_carrito()
                producto = input("¿Qué producto quieres devolver?: ")
                eliminar_prod(producto)    
            


        case "4":
            salida = True
        case _:
            print("")
            print("ESa opcion no está en el menú")

print("Tus compras fueron: ")
print("")
mostrar_carrito()
print("")
print("Inventario disponible: ")
print("")
mostrar_inv()            
print("Has salido de nuestro sistema, gracias por comprar en mercadillo...")            
    
