
### CLASES

## La case Equipo crea los equipos a partir del nombre, posicion, presupuesto y fecha dada, el id lo coge de un contador
## la web la crea en funcion del nombre y si juega en europa lo crea a partir de su posicion, al principio no tiene uniforme
## cuando pulsamos la opcion 8 le compramos un uniforme y se le agrega 

from datetime import date

class Equipo():
    
    def __init__(self, id, nombre, posicion, presupuesto, año, mes, dia):
        self.id = id
        self.nombre = nombre.upper()
        self.web = webequipo(nombre)
        self.posicion = posicion
        self.europa = True if self.posicion > 0 and self.posicion < 5 else False
        self.presupuesto = presupuesto
        self.fundacion = date(año, mes, dia)
        self.uniforme = None

    def comprar_uniforme(self, uniforme):
        self.uniforme = uniforme
    
    def __str__(self):
        if not self.uniforme: 
            return f"ID: {self.id}\nNombre: {self.nombre}\nWeb: {self.web}\nPosicion {self.posicion}\nClasifica para Champions: {self.europa}\nPresupuesto: {self.presupuesto}M€\nFundación: {self.fundacion}"
        else:
            return f"ID: {self.id}\nNombre: {self.nombre}\nWeb: {self.web}\nPosicion {self.posicion}\nClasifica para Champions: {self.europa}\nPresupuesto: {self.presupuesto}M€\nFundación: {self.fundacion}\nCamiseta: {self.uniforme.camiseta}\nPantalón: {self.uniforme.pantalon}"

## La clase uniforme crea un uniforme a partir de un color de camiseta y pantalon y se le asigna a un equipo.
        
class Uniforme():
    
    def __init__(self, camiseta, pantalon):
        self.camiseta = camiseta
        self.pantalon = pantalon
    
### FUNCION MENU
## Nos muestra las distintas opciones que tiene si no pulsa una de ellas sigue haciendo un bucle aunque pulses esc no se cierra.

def ft_menu():
    menu = """Seleccione una opcion:\n
        - Opción 1: Imprimir todos los equipos de la lista.\n
        - Opción 2: Imprimir todos los equipos ordenados por posición.\n
        - Opción 3: Imprimir un equipo por su id.\n
        - Opción 4: Crear un nuevo equipo.\n
        - Opción 5: Actualizar info de equipo.\n
        - Opción 6: Borrar usuario por su id.\n
        - Opción 7: Borrar todos los usuarios.\n
        - Opción 8: Uniformar.\n
        - Opción 9: Salir.\n"""
    while True:
        try:
            option = int(input(menu))
            if option < 1 or option > 9:
                raise(ValueError)
            return option
        except:
            print("Opcion Incorrecta intentelo de nuevo.")
            print()

### FUNCION PARA OPCION 1
## en caso de que haya elementos a mostrar los muestra sino muestra un mensaje de error.
            
def verlista(lista):
    if len(lista) == 0:
        print("No hay elementos que mostrar")
        print()
    for elemento in lista:
        print(elemento)
        print()

### FUNCION PARA OPCION 2
## Ordena por posicion, nos pide insertar una opcion para ver el tipo de orden y debe ser correcto
## depende el tipo de ordenamiento escogido los ordena de una forma u otra

def listado_ordenado(lista):
    tipo = f"Opcion 1-Ascendente | Opcion 2-Descendente"
    while True:
        try:
            opcion = int(input(tipo))
            if opcion not in [1, 2]:
                raise ValueError
            break
        except:
            print("Opcion Incorrecta intentelo de nuevo.")
            print()
    if opcion == 1:
        ordenado = sorted(lista, key=lambda team : team.posicion)
    else:
        ordenado = sorted(lista, key=lambda team : team.posicion, reverse=True)
    verlista(ordenado)
    
### FUNCION PARA OPCION 3
## muestra la info de un equipo segun su id, si no hay con un equipo con esa id muestra error.

def mostrar_equipo_por_id(lista):
    while True:
        try:
            id = int(input("Inserte un id:"))
            if id <= 0:
                raise ValueError
            break
        except:
            print("Valor de id incorrecto intentelo de nuevo.")
            print()
    for elemento in lista:
        if elemento.id == id:
            print(f"{elemento}.")
            return
    print(f"Ningun equipo tiene ID {id}.")
    print()

### FUNCION PARA OPCION 4
## nos pide los diferentes datos para el equipo, las funciones checker sirven para filtrar errores en los parametros 
## luego llama a la clase Equipo con los parametros correctos
## por ultimo agrega haciendo append el equipo al csv

def nuevo_equipo(id):
    nombre = input("Ingrese el nombre del equipo:")
    posicion = posicion_checker()
    presupuesto = presupuesto_checker()
    año = año_checker()
    mes = mes_checker()
    dia = dia_checker(mes)
    nuevo_equipo = Equipo(id, nombre, posicion, presupuesto, año, mes, dia)
    agregarequipo_csv(nuevo_equipo)
    return nuevo_equipo

### FUNCION PARA OPCION 5
## comprueba el id del equipo, mediante el bucle for enumerate modificamos los elementos de la lista segun los nuevos paramentros
## en caso de no haber ningun equipo con ese id se devolvera mensaje de error
## hay que tener cuidado ya que si no se dan paramentros para actualizar se modificaran a blanco

def actualizar_datos_equipo_por_id(lista):
    while True:
        try:
            id = int(input("Inserte un id:"))
            if id <= 0:
                raise ValueError
            break
        except:
            print("Valor de id incorrecto intentelo de nuevo.")
            print()
    nombre = input("Ingrese el nombre del equipo:")
    posicion = posicion_checker()
    presupuesto = presupuesto_checker()
    año = año_checker()
    mes = mes_checker()
    dia = dia_checker(mes)
    for i, elemento in enumerate(lista):
        if elemento.id == id:
            print("Equipo ha actualizar:")
            print(f"{elemento}.")
            print()
            print("Equipo ha sido actualizado:")
            lista[i].nombre = nombre.upper()
            lista[i].web = webequipo(nombre)
            lista[i].posicion = posicion
            lista[i].europa = True if elemento.posicion > 0 and elemento.posicion < 5 else False
            lista[i].presupuesto = presupuesto
            lista[i].fundacion = date(año, mes, dia)
            print(f"{elemento}.")
            print()
            return
    print(f"Ningun equipo tiene ID {id}.")
    print()    

### FUNCION PARA OPCION 6
## buscamos un elemento por su id, primero asegurando que es una id correcta
## imprimos el elemento que vamos a borrar, lo borramos y nos salimos
## en caso de no encontrar el id muestra mensaje de error

def borrar_equipo_por_id(lista):
    while True:
        try:
            id = int(input("Inserte un id:"))
            if id <= 0:
                raise ValueError
            break
        except:
            print("Valor de id incorrecto intentelo de nuevo.")
            print()
    for elemento in lista:
        if elemento.id == id:
            print(f"Equipo {elemento.nombre} con ID {id} ha sido borrado.")
            print()
            lista.remove(elemento)
            return
    print(f"Ningun equipo tiene ID {id}.")
    print()  

### FUNCION PARA OPCION 7
## miramos que haya elementos a borrar, en caso de haberlos se muestran y se borra con un mensaje
## en caso contrario imprimimos que no hay naad que borrar
     
def borrar_listado(lista):
    if len(lista) > 0:
        verlista(lista)
        lista.clear()
        print("Estos elementos han sido borrados.")
        print()
    else:
        print("No hay elementos que borrar.")
        print()

### FUNCION PARA OPCION 8
## Buscamos un elemento por su id. pedimos color de pantalon y camiseta. creamos el uniforme llamando a la clase uniforme y lo asignamos al atributo uniforme del equipo

def uniformar_equipo_por_id(lista):
    while True:
        try:
            id = int(input("Inserte un id:"))
            if id <= 0:
                raise ValueError
            break
        except:
            print("Valor de id incorrecto intentelo de nuevo.")
            print()
    camiseta = input("Inserte Color de Camiseta")
    pantalon = input("Inserte Color de Pantalon")
    uniforme = Uniforme(camiseta, pantalon)
    for i, elemento in enumerate(lista):
        if id == elemento.id:
            lista[i].comprar_uniforme(uniforme)
            return
    print(f"Ningun equipo tiene ID {id}.")
    print()
    
### FUNCIONES AUXILIARES PARA CLASE Y OPCIONES 4 Y 5

## Borramos lo que no sea alfanumerico del nombre del equipo lo ponemos todo en minusculas y añadimos wwww. .es 

def webequipo(nombre):
    nombre = nombre.lower()
    web = ""
    for letra in nombre:
        if letra.isalnum():
            web += letra
    return f"www.{web}.es"

## Aseguramos que la posicion sea entre 1 y 20. Se admiten duplicados de posicion

def posicion_checker():
    while True:
        try:
            posicion = int(input("Inserte posición:"))
            if posicion < 0 or posicion > 20:
                raise ValueError
            return posicion
        except:
            print ("El valor de posicion es incorrecto intentelo de nuevo.")
            print()
            
## Aseguramos que el presupuesto en Millones € sea mayor que 0 y menor que un numero bastante grande
            
def presupuesto_checker():
    while True:
        try:
            presupuesto = round(float(input("Inserte presupuesto:")), 2)
            if presupuesto < 0 or presupuesto > 999999:
                raise ValueError
            return presupuesto
        except:
            print ("El valor de presupuesto es incorrecto intentelo de nuevo.")
            print()
            
## Aseguramos que el año este entre 1750 y 9999            
            
def año_checker():
    while True:
        try:
            año = int(input("Inserte año de fundación:"))
            if año < 1750 or año > 9999:
                raise ValueError
            return año
        except:
            print ("El valor de año es incorrecto intentelo de nuevo.")
            print()
            
## Aseguramos que el mes este entre enero y diciembre            
            
def mes_checker():
    while True:
        try:
            mes = int(input("Inserte mes de fundación:"))
            if mes < 1 or mes > 12:
                raise ValueError
            return mes
        except:
            print ("El valor de mes es incorrecto intentelo de nuevo.")
            print()
            
## Aseguramos que dependiendo que el dia sea mayor que 1 y dependiendo del mes no supere 28 o 30. No consideramos los años bisiestos 
            
def dia_checker(mes):
    while True:
        try:
            dia = int(input("Inserte día de fundación:"))
            if dia < 1 or dia > 31:
                raise ValueError
            elif mes == 2 and dia > 28:
                raise ValueError
            elif mes in [4, 6, 9, 11] and dia > 30:
                raise ValueError
            return dia
        except:
            print ("El valor de día es incorrecto intentelo de nuevo.")
            print()
            
## Borra el csv actual y lo sustituye con la lista nueva.            
            
def actualizar_csv(lista):
    rows = f"id,nombre,web,posicion,europa,presupuesto,fundacion"
    with open("equipos.txt", "w", encoding="utf-8") as file:
        file.write(rows)
        file.write("\n")
        for elemento in lista:
            file.write(f"{elemento.id},{elemento.nombre},{elemento.web},{elemento.posicion},{elemento.europa},{elemento.presupuesto},{elemento.fundacion}\n")
            
## agrega un elemento nuevo al csv            
            
def agregarequipo_csv(elemento):
    with open("equipos.txt", "a", encoding="utf-8") as file:
        file.write(f"{elemento.id},{elemento.nombre},{elemento.web},{elemento.posicion},{elemento.europa},{elemento.presupuesto},{elemento.fundacion}\n")