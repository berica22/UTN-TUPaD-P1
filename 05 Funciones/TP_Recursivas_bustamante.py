#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario
#Función recursiva que calcule el factorial de un número
def factorial(n):
    # Caso base: si n es 0  su factorial es 1
    if n == 0:
        return 1
    # Llamada recursiva
    else:
        return n * factorial(n - 1)
    
#Pedir número al usuario
ultimo_factorial=int(input("Ingrese un número entero positivo:"))

# calcular  factorial de todos los números enteros entre 1 y el número que indique el usuario
#Recorre los números desde 1 hasta el número ingresado (inclusive).
for i in range(1, ultimo_factorial + 1): 
#Llama a la función factorial(i) para calcular el factorial de ese número.
    print(f"{i}! = {factorial(i)}")           

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci_recursivo(posicion):
#Cuando la posición es 0 o 1, se devuelve ese mismo número.Primeros dos términos de la secuencia.
    if posicion==0:
        return 0
    elif posicion ==1:
        return 1
    else:
#Llamada recursiva.Para cualquier posición ≥ 2, se calcula
        return fibonacci_recursivo(posicion-1)+ fibonacci_recursivo(posicion-2)

#Muestra la serie completa hasta la posición que el usuario especifique. 
#Solicitar posicion

Ultima_posicion=int(input("Ingrese un número entero positivo:"))

for i in range (Ultima_posicion):
    print(f"En la posicion {i} obtenemos el valor de fibonacci:{fibonacci_recursivo(i)}")


#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
#. Prueba esta función en un algoritmo general.

#Funcion recursiva que calcula la potencia parametros base y el expnente

def potencia_recursiva(base, exponente):
#si el exponente es 1 el resultado es 0, esta es la condicion base de la funcion 
    if exponente==0:
        return 1
#Si el exponente no es 0 devolvemos la recursion la funcion se llama a sí misma con el exponente reducido en 1y multiplica la base por ese resultado
    else:
        return base * potencia_recursiva(base, exponente-1)
    
#. Prueba esta función en un algoritmo general. 
# Solicitar los valores al usuario
base = int(input("Ingresá la base (número entero): "))
exponente = int(input("Ingresá el exponente (entero positivo): "))

if exponente<0:
    print("Solo se permite el ingreso de exponente positivo.")
else:
    resultado=potencia_recursiva(base,exponente)
    print(f"{base}^{exponente}= {resultado}")



#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

#Funcion recursiva
def decimal_binario(decimal):
#caso base 
    if decimal == 0:
        return "0"
    elif decimal== 1:
        return "1"
#llamada recursiva
    else:
#La función se llama a sí misma con ndecimal // 2, hasta llegar a 1 o 0
        return decimal_binario(decimal//2)+str(decimal%2)  
        

binario= decimal_binario(5)
print(binario)

print(5%2)


#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra)<=1:            #caso base si la palabra tiene 
        return True
#Si la primera y la ultima letra son diferentes no es palindromo
    elif palabra[0]!=palabra[-1]:
        return False
    else:
#Llamada recursiva sin la primera y la ultima letra
        return es_palindromo(palabra[1:-1])

palabra=input("Escriba palabra sin espacios ni tildes para verificar si es palidromo:")

palindromo=(es_palindromo(palabra))

if palindromo == True:
    print("La palabra ingresa es un palindromo")
else:
    print("La palabra ingresada no es un palidromo ")
#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
 #Restricciones:#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.Ejemplos:suma_digitos(1234) → 10 (1 + 2 + 3 + 4)suma_digitos(9) → 9suma_digitos(305) → 8 (3 + 0 + 5)

#Funcion recursiva 

def suma_digitos(n):
    if n <10 :#caso base si es un solo digito lo devuelvo 
        return n
    else:
        return (n%10)+ suma_digitos(n//10)# obtiene el último dígito del número y lo elimina con la division entera



n=int(input("Ingrese número entero positivo:"))


print(f"La suma de los digitos de {n} es de : {suma_digitos(n)}")


#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque.Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que 
# necesita para construir toda la pirámide. Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)


def contar_bloques(n):
    if n == 1:          # caso base: si queda un solo nivel, se necesita 1 bloque
        return 1
    else:
        return n + contar_bloques(n 