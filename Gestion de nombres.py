name = ["samuel", "matias", "daniel","daniela", "veronica"]

print("Bienvenido al registro de nombres")

salir = 0
while salir == 0:
    print ("Que deseas hacer?: ")
    print("1.Agregar nombre")
    print("2.Mostrar nombres")
    print("3.Cambiar nombre existente por otro")
    print("4.Eliminar un nombre")
    menu = input("5.Salir sistema: ")
    
    
    match menu:
        case "1":
            nombre = input("ingrese un nuevo nombre: " )
            cont = 0

            for nom in name:
                if name[cont] == nombre:
                    print("Este nombre ya existe: ")
                    break
                elif name[cont] != nombre:
                    print("Nombre guardado con exito")
                    name.append(nombre)
                    break
                cont = cont + 1    
        case "2":
            print(f"Actualmente estos son los nombres existentes en el programa: {name}")
        case "3":
            nombre_cambiar = input("ingrese el nombre que quiere cambiar: " )
            cont = 0     
            for nom in name:
                
                if name[cont] == nombre_cambiar:
                    name[cont] = nombre_cambiar
                cont = cont + 1
        case "4":
            nombre_eliminar = input("ingrese el nombre que quiere eliminar: " )

            for nom in name:
                
                if name[cont] == nombre_eliminar:
                    name.remove(nombre_eliminar)
                    break
                cont = cont + 1
        case _:
            salir = 1

print("La lista ha quedado así: ",name)
