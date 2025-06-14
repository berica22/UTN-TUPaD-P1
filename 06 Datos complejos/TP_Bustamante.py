#1)

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200      #se añade Naranja = 1200
precios_frutas['Manzana'] = 1500      #se añade Manzana = 1500
precios_frutas['Pera'] = 2300         #se añade Pera = 2300

print(precios_frutas)

#2) 

precios_frutas['Banana'] = 1330 # Se actualiza valor  Banana = 1330
precios_frutas['Manzana'] = 1700 # Se actualiza valor  Manzana = 1700
precios_frutas['Melón'] = 2800 # Se actualiza valor  Melón = 2800

print(precios_frutas)

#3)

lista_frutas=list(precios_frutas.keys())

print(lista_frutas)

#4)

contactos={}

nombre=0
telefono=0

#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.

for i in range(0,5):
    nombre=(input("Ingrese nombre del contacto:"))
    telefono=(input("Ingrese número de telefono:"))
    contactos[nombre]=telefono


print( contactos)
#Luego, pedí un nombre y mostrale el número asociado, si existe.
buscar_nombre=input("Ingrese contacto para buscar nombre:")

if buscar_nombre in contactos:
    print(f"El número de {buscar_nombre} es {contactos[buscar_nombre]}")
else:
    print("Ese contacto no existe.")


#5)

#Solicita al usuario una frase Imprime• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase=(input("Ingrese una frase:")).split()              # se solicita la frase .split ()para separar la frase en palabras

palabras_unicas=set(frase)                                       # set(frase)para mostrar las palabras únicas.

print(f"Las palabras unicas: {palabras_unicas}")
recuento={}

for palabra in frase:

    recuento[palabra] = recuento.get(palabra, 0) + 1               #recuento.get(palabra, 0) busca si la palabra ya tiene un número asignado.

print(recuento)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}         #diccionario

for i in range(3):
    nombre = input("Ingrese nombre del alumno: ")               #bucle se repite 3 veces 1 por alumno 
    
    nota1 = int(input("Ingrese nota 1: "))
    nota2 = int(input("Ingrese nota 2: "))
    nota3 = int(input("Ingrese nota 3: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)            ## guarda la tupla como valor



print(alumnos)

# Mostrar promedios
for nombre, notas in alumnos.items():             #Recorre cada alumno (nombre) y su tupla de notas (notas) en el diccionario.
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")


#7)#7

# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:

set_parcial_1={101,102,105,109,111,115,118,120}
set_parcial_2={101,105,107,108,111,112,115,118,120}

#• Mostrá los que aprobaron ambos parciales.


aprobaron_ambos=(set_parcial_1.intersection(set_parcial_2))     #método intersection().La intersección de dos conjuntos es un conjunto que contiene los elementos que pertenecen a ambos conjuntos.

print(f"Los ID de alumnos que aprobaron ambos parciales son los siguientes:{aprobaron_ambos}")   

#• Mostrá los que aprobaron solo uno de los dos.

aprobaron_uno=(set_parcial_1.symmetric_difference(set_parcial_2))      #metodo symmetric_difference()La diferencia simétrica entre dos conjuntos comprende todos los elementos que pertenecen a uno de los dos conjuntos, pero no a ambos a la vez. 

print(f"Los ID de alumnos que aprobaron un solo parcial son los siguientes:{aprobaron_uno}")    

#Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobaron=(set_parcial_1.union(set_parcial_2))                        #metodo .union()La unión dos conjuntos retorna un conjunto que contiene todos los elementos pertenecientes a alguno de los dos conjuntos. 

print(f" total de estudiantes que aprobaron al menos un parcial:{aprobaron}")    

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.



articulos_inalambricos =  {"auriculares": '100', "teclado": "50", "cargador" :"30","smartwatch":"20","impresora":"32"}

#• Consultar el stock de un producto ingresado.

llave=input("Ingrese el articulo para verificar stock:").lower()

if llave in articulos_inalambricos:
    print(f"Stock disponible: {articulos_inalambricos[llave]}")
else:
    print("El artículo no está registrado.")



#• Agregar unidades al stock si el producto ya existe.

producto= input("Ingrese articulo a modificar stock").lower()
nuevo_valor=input ("Ingrese stock actualizado")

if producto in articulos_inalambricos:
    articulos_inalambricos[producto] = nuevo_valor
    print("Stock actualizado.")
else:#• Agregar un nuevo producto si no existe.
    articulos_inalambricos[producto] = nuevo_valor
    print("Artículo agregado al inventario.")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("lunes", "10:00"): "Clase programación",
    ("lunes", "12:00"): "Clase Arquitectura",
    ("lunes", "15:00"): "Reunión de trabajo",
    ("martes", "09:00"): "Clase Matemática",
    ("lunes", "14:00"): "Trámite bancario",
    ("miércoles", "11:00"): "Clase de yoga",
   ("jueves", "16:00"): "Consulta médica"
}

#Permití consultar qué actividad hay en cierto día y hora.

dia=input("Ingrese día:").lower()
hora=input("ingrese hora (formato HH:MM):")

actividad = agenda.get((dia, hora))

if actividad:
    print("Actividad programada:", actividad)
else:
    print("No hay actividad programada en ese día y hora.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.


original={"Argentina":"Buenos Aires","Chile":"Santiago","Brasil":"Brasilia","Paraguay":"Asuncion","España":"Madrid","Italia":"Roma","Portugal":"Lisboa","Rusia":"Moscú"}



capital_a_pais={}

for pais, capital in original.items():

    capital_a_pais[capital] = pais 


print(capital_a_pais)