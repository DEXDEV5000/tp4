"""Ejercicio 1"""
#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro
"""def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def numeros_primos_hasta_n(Numero):
    for numer in range(1, Numero + 1):
        if es_primo(numer):
            print(numer)
Numero = int(input("Ingrese un número n: "))
numeros_primos_hasta_n(Numero)"""
"""Ejercicio 2"""
#Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecucion
"""def hacer_sandwich():#Primer criterio
    condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
    while condimento.lower() != 'salir':
        print(f"Se ha agregado {condimento} al sándwich.")
        condimento = input("Ingrese otro condimento (o 'salir' para terminar): ")
hacer_sandwich()
def hacer_sandwich_alternativo(): #Segun criterio
    while True:
        condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
        if condimento.lower() == 'salir':
            break
        print(f"Se ha agregado {condimento} al sándwich.")
hacer_sandwich_alternativo()"""
"""Ejecicio 3"""
#A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes
"""def hacer_remera(tamaño, mensaje): #Punto A
    print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'")
hacer_remera('M', 'Python es genial')
hacer_remera(mensaje='Hola, mundo!', tamaño='S')"""
"""def hacer_remera(tamaño='L', mensaje='Me gusta Python'): #Punto B
    print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'")
hacer_remera()
hacer_remera('M', 'Python rocks!')
hacer_remera(mensaje='Programador en acción')"""
"""Ejercicio 4"""
#Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 
"""def fibonacci(numero):
    fib_series = [0, 1]
    while len(fib_series) < numero:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
numero = int(input("Ingrese un número n para la serie de Fibonacci: "))
print(Fibonacci(numero))"""
"""Ejercicio 5"""
#(Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
#la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
#el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
#calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.
"""def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: división por cero"
operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division
}
print("Operaciones disponibles:")
print("1 Suma")
print("2 Resta")
print("3 Multiplicación")
print("4 División")
opcion = int(input("Ingrese el número de la operación que desea realizar: "))
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
if opcion in operaciones:
    resultado = operaciones[opcion](numero1, numero2)
    print("El resultado es:", resultado)
else:
    print("Opción inválida")"""
"""Ejercicio 6"""
#(Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir
#gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
#conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462
#libras = 1 gramo 