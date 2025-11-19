import random 

def menu_i():
    print("")
    exit = input("Deseas salir del programa? (y/n): ")
    
    if exit == "y":
        print("")
        print("Saliendo del programa...")
        return True
    elif exit == "n":
        print("Redireccionando al menu principal")
        print("")
        return False

def tuplas():
    print("Nueva tupla: ", new_tupla)
    print("Tupla original es: ", tupla)
    

catalogo_numeros = [1,2,3,4,5,6,7,8,9,10]
tupla = tuple(random.sample(catalogo_numeros,6))
new_tupla = ()

print(f"Esta es la tupla original: {tupla}")
print("")

salir = False
while salir != True:
    print("Bienvenido a la interaccion con tu primera tupla, esto es lo que puedes hacerle: ")
    print("1. agregar un valor al final")
    print("2. reemplazar un valor en la tupla")
    print("3. eliminar un valor por su posicion")
    print("4. imprimir tupla con su posición")
    menu = input("5. salir: ")
    
    
    match menu:
        case "1":
            #agregar un nuevo valor al final
            new_value = int(input("Ingresa el nuevo numero: "))

            new_tupla = tupla + (new_value,)
            tuplas()
            salir = menu_i()    

        case "2":
            print(f"La tupla original se ve así: {tupla}, modificaras es una tupla externa {new_tupla}")
            print("")
            old_value = int(input("Ingrese el numero de la tupla original que desea cambiar ( los cambios se reflejaran en su tupla): ")) 
            cont = 0
            for num in new_tupla:
                if old_value == new_tupla[cont]:
                    print("")
                    new_value = int(input("Digite el numero por el que lo quiere reemplazar: "))
                    
                    lista_temp = list(new_tupla)
                    lista_temp[cont] = new_value
                    
                    new_tupla = tuple(lista_temp)
                    tuplas()
                    break
                cont += 1    
        
        case "3":
            print("")
            tuplas()
            posicion = int(input("Digite la posicion del numero que quiere eliminar: "))
            posicion -= 1
            cont = 0
            for i in new_tupla:
                if posicion <= len(new_tupla):
                    
                    lista_temp = list(new_tupla)
                    lista_temp.pop(posicion)
                    new_tupla = tuple(lista_temp)
                    print("El elemento se ha eleminado exitosamente")
                    tuplas()
                    break
                elif posicion > len(new_tupla):
                    print("La posicion ingresada es mayor a la cantidad de posiciones")
                    salir = menu_i()
        case "4":
            print("")
            cont= 0
            print("")
            print("Tupla original") 
            for i in tupla:
                
                print(f"Posicion {cont}: Valor: {tupla[cont]}")
                cont += 1
            cont = 0
            
            if len(new_tupla) > 0:
                print("")
                print("Tupla nueva")
                for j in new_tupla:
                    
                    print(f"Posicion {cont}: Valor: {new_tupla[cont]}")
                    cont += 1
            else:
                print("")
                print("No existen valores en Tupla nueva")
                print("")        
        case "5":
            salir = True
               
mayor_t = tupla[0]               
cont = 0               
                            
for numero in tupla:
    if numero > mayor_t:
        mayor_t = numero
    cont += 1    
print("El numero mayor de la tupla original es: ", mayor_t, "y está en la posición: ", cont)
print("")

mayor_n = new_tupla[0]
cont = 0
for numero in new_tupla:
    if numero > mayor_n:
        mayor_n = numero
    cont +=1  
                                    
print("El numero mayor de la tupla nueva es: ", mayor_n, "y está en la posición: ", cont)  
print("")

menor = tupla[0]               
               
                            
for numero in tupla:
    if numero < menor:
        menor = numero                         

print("El numero menor de la tupla original es: ", menor)
print("") 

menor_n = new_tupla[0]

for numero in new_tupla:
    if numero < menor_n:
        menor_n = numero  
                                    
print("El numero menor de la tupla nueva es: ", menor_n)  
print("")   

acom = 0
cont = 0

for i in tupla:
    acom = acom + tupla[cont]
    cont +=1

acom_n = 0
cont = 0

for i in new_tupla:
    acom_n = acom_n + new_tupla[cont]
    cont += 1
    
print("La suma de los valores de la tupla original es: ", acom)    
print("La suma de la tupla nueva es: ", acom_n )    
    