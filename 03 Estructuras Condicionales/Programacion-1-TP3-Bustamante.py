#Trabajo practico de condicionales 
#Alumna Bustamante Erica
#Ejercico 1
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

#Determinamos la variable y solicitamos los datos al usuario
edad = int(input ("escribe tu edad "))
#determinamos condicional
edad >= 18
#Escribimos texto que saldrà por consola
print ("usted es mayor de edad")

#Ejercicio 2 
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

#Determinamos la variable y solicitamos datos al usuario
nota = int (input ("Por favor indique su nota"))
#Determinar condicional
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#ejercicio 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#úmero par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#ontrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#perador de módulo (%) en Python para evaluar si un número es par o impar.

#Definir la variable y solicitar al usuario por consola un numero 
num = int (input ("Por favor ingrse un numero"))
#Determinar los condicionales
if num % 2 == 0:
    print ("Ha ingresado un nùmero par")
else:
    print ("por favor ingrese un nùmero par")

#Ejercicio 4
#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#iguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

#Definir las Variables
edad = int ( ("Por favor ingrese su edad"))
if edad >= 0 and edad <= 12:
    print ("Eres un niño")
elif edad >= 13 and edad <= 17:
    print ("Eres un adolescente")
elif edad >= 18 and edad <=64:

    print ("Eres un adulto mayor")
else:
    print ("Eres adulto mayor")

#Ejercicio 5
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#antalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#antalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#e la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#omo una lista o un string.

#Definimos la variable

contra = int (input ("Ingrese una contraseña"))
num = len (contra)
if 8 <= num <= 14:
    print (" Ha ingresado una contraseña correcta")
else:
    print (" Ha ingresado una contraseña incorrecta")

#ejercicio 6 

# Importamos todas los paquetes y funciones que necesitamos utilizar
import random
from statistics import mode, median, mean

# Generamos una lista de 50 números de forma aleatoria
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos la moda, la mediana y la media de la lista numeros_aleatorios
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Si la media es mayor que la mediana y la mediana es mayor que la moda, imprimir "Sesgo positivo o a la derecha"
if media > mediana > moda:
  print("Sesgo positivo o a la derecha")
# Si la media es menor que la mediana y la mediana es menor que la moda, imprimir "Sesgo negativo o a la izquierda"
elif media < mediana < moda:
  print("Sesgo negativo o a la izquierda")
# Si la media, la mediana y la moda son iguales, imprimir "Sin sesgo"
elif media == mediana == moda:
  print("Sin sesgo")
# Si no se cumple ninguna de las condiciones anteriores, imprimir "No se puede determinar si esta distribución tiene sesgo o no"
else:
  print("No se puede determinar si esta distribución tiene sesgo o no") 

  #Ejercicio 7 Escribir  un  programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
  #añadir un signo de exclamación al final e imprimir el string resultante por pantalla;  en  caso  contrario,  dejar  el 
  #string tal cual lo ingresó el usuario e imprimirlo por pantalla

  # Pedimos al usuario que ingrese una frase o palabra
frase = input("Por favor, ingrese una frase o palabra: ")

# Para acceder a la última letra de un string podemos usar el índice -1
# Si la última letra de la frase (frase[-1]) es una vocal, agregar un signo
# de exclamación e imprimirla
if frase[-1] in ("AEIOUaeiou"):
  print(f"{frase}!")
# Sino, imprimir la frase tal cual fue ingresada
else:
  print(frase) 

#Ejercico 8 Escribir un programa que solicite al usuario que ingrese su nombre y 
#el número 1, 2 o 3 dependiendo de la opción que desee:
#1.   Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2.   Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3.   Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python 
#para convertir entre mayúsculas y minúsculas.

# Pedimos al usuario que ingrese su nombre
nombre = input("Por favor, ingrese su nombre: ")

# Imprimimos por pantalla las opciones posibles y pedimos al usuario que ingrese la opción que desea
print("""
En este programa puede realizar cualquiera de las siguientes operaciones:
1. Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.
""")
opcion = int(input("Ingrese el número de operación que desea realizar: "))


# Si el usuario eligió la opción 1, imprimimos su nombre en mayúsculas
if opcion == 1:
  nombre_mayuscula = nombre.upper()
  print(nombre_mayuscula)
# Si el usuario eligió la opción 2, imprimimos su nombre en minúsculas
elif opcion == 2:
  nombre_minuscula = nombre.lower()
  print(nombre_minuscula)
# Si el usuario eligió la opción 3, imprimimos su nombre con la primera letra en mayúscula
elif opcion == 3:
  nombre_title = nombre.title()
  print(nombre_title)
# Si el usuario eligió otro número de opción, imprimimos "Por favor, ingrese únicamente 1, 2 o 3"
else:
  print("Por favor, ingrese únicamente 1, 2 o 3")

  # Ejercico 9 Programa de magnitud

  # Pedimos al usuario que ingrese la magnitud del terremoto
magnitud_terremoto = float(input("Por favor, ingrese la magnitud del terremoto según la escala de Ritcher: "))

# Si la magnitud del terremoto es menor que 3, imprimimos "Muy leve"
if magnitud_terremoto < 3:
  print("Muy leve")
# Si la magnitud del terremoto es mayor o igual que 3 y menor que 4, imprimimos "Leve"
elif 3 <= magnitud_terremoto < 4:
  print("Leve")
# Si la magnitud del terremoto es mayor o igual que 4 y menor que 5, imprimimos "Moderado"
elif 4 <= magnitud_terremoto < 5:
  print("Moderado")
# Si la magnitud del terremoto es mayor o igual que 5 y menor que 6, imprimimos "Fuerte"
elif 5 <= magnitud_terremoto < 6:
  print("Fuerte")
# Si la magnitud del terremoto es mayor o igual que 6 y menor que 7, imprimimos "Muy fuerte"
elif 6 <= magnitud_terremoto < 7:
  print("Muy fuerte")
# En cualquier otro caso, imprimimos "Extremo". Esto en este caso equivale a decir
# elif magnitud_terremoto >= 7 porque es el único caso que no está cubierto hasta el momento
else:
  print("Extremo") 