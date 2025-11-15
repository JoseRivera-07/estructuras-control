#Investigacion estructuras en python

## Listas
-Que son? 
    Una lista es una estructura de datos que permite almacenar varios elementos en una sola variable. Ej: una caja que contiene varias cosas
-Por qué son mutables?
    Una lista es mutable porque sus elementos pueden cambiar después de ser creada, esto significa que se puede agregar, cambiar, eliminar o mover los elementos sin tener que crear una lista nueva
-situaciones donde resultan utiles
    Las listas se usan cuando se necesita:

    Guardar varios datos relacionados (como nombres, edades, productos, notas, etc.).

    Recorrer elementos uno a uno con un for.

    Almacenar datos que van a cambiar a lo largo del programa.

    Guardar resultados de procesos (por ejemplo, almacenar los números generados por un ciclo).

    Crear estructuras más complejas como tablas, matrices o listas de listas.

-Ejemplo: 

    # 1. CREACIÓN
    frutas = ["manzana", "banana", "pera"]
    print("Lista original:", frutas)

    # 2. LECTURA
    print("Primera fruta:", frutas[0])      
    print("Última fruta:", frutas[-1])     

    # 3. MODIFICACIÓN
    frutas[1] = "mango"                     
    frutas.append("uva")                    
    print("Lista modificada:", frutas)

    # 4. ELIMINACIÓN
    del frutas[0]                           
    frutas.remove("pera")                   
    print("Lista final:", frutas)

## Tuplas

-Que son? 
    Una tupla es una estructura de datos similar a la lista, pero con una diferencia principal, sus elementos no son mutables (no se puede crudear) y estos se crean usando parentesis o no, es opcional.

-Por qué son inmutables?
    Las tuplas son inmutables porque una vez creadas, no permiten agregar, eliminar ni modificar sus el elementos, esto ocurre porque python las usa para representar datos fijos que no deben cambiarse, también porque al ser así, inmutables son más rápidas y seguras que las listas, asi el o los valores que se almacenan no se editan ni se eliminan por accidente. Se pueden usar como claves en diccionarios, cosa que las listas no permiten
-Situacion donde resulatan útiles
    Se usa una tupla cuando se quiere que asegurar que los datos no se modifiquen, por ejemplo con coordenadas, fechas, configuraciones, pueden agrupar datos fijos como si fueran una especie de registro. Puede tambien retornar varios valores desde una funcion, asi como tambien permite tener una colección más rápida y eficiente que una lista. otro de sus usos utiles es poder usarlas como claves en diccionarios.

-Ejemplo:

    colores = ("rojo", "verde", "azul")

    print("Primer color:", colores[0])     # rojo
    print("Último color:", colores[-1])    # azul

    print("Colores:")
    for color in colores:
        print(color)

## Diccionarios

-Que son? 
    Un dicccionario es una estructura de datos que almacena información en forma de {clave : valor}. Como así? Quiere decir que, en lugar de acceder a los elementos por posición (como en listas o tuplas), accedes usando una clave.

-Como almacenan la informacion? 
    Los diccionarios internamente usan tablas hash, esto permite que buscar un valor por clave sea muy rápido. Cada clave debe ser única e inmutable (Cadenas, Numeros, Tuplas, ). Los valores pueden ser cualquier tipo de dato (Listas, Diccionarios, Funciones, etc...)

-Diferencias clave frente a las listas
    Característica          Lista                               Tupla                   Diccionario

    Tipo de índice          Número(posición)                    Número(posición)        Clave

    Mutabilidad             Mutable                             Inmutable               Mutable

    Orden                   Mantiene orden de inserción         Mantiene orden          Mantiene orden

    Cuando usar             Datos que cambian                   Datos fijos             Datos con significado (nombre, edad)

    Velocidad de búsqueda   Normal                              Rápida                  Muy rápida (por clave)   

Ejemplo

# Diccionario inicial
estudiante = {
    "nombre": "Ana",
    "edad": 19,
    "programa": "Ingeniería"
}

print("Diccionario original:", estudiante)

# 1. AGREGAR
estudiante["nota_final"] = 4.5
print("Después de agregar:", estudiante)

# 2. CONSULTAR
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante.get("edad"))  

# 3. MODIFICAR
estudiante["edad"] = 20
print("Después de modificar:", estudiante)

# 4. ELIMINAR
del estudiante["programa"]      
print("Después de eliminar 'programa':", estudiante)

nota = estudiante.pop("nota_final")  
print("Nota eliminada:", nota)
print("Diccionario final:", estudiante)

## Match case

-Que es y desde que versión existe?
    match-case es una estructura de control introducida en Python 3.10.

    Funciona como un sistema de patrones que permiten comparar un valor contra multiples opciones, de forma parecida al switch en otros lenguajes, pero más potente.

-Para qué se usa?

    Se usa para evaluar un valor contra varios patrones, simplificar decisiones donde hay muchas opciones, hacer el código más ordenado y legible cuando reemplaza múltiples elif, desestructurar objetos más complejos (listas, tuplas, diccionarios).

