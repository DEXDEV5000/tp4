"""Ejercicio 1"""
#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro
#def es_primo(numero):
#    if numero <= 1:
#        return False
#    for i in range(2, int(numero**0.5) + 1):
#        if numero % i == 0:
#            return False
#    return True
#def numeros_primos_hasta_n(Numero):
#    for numer in range(1, Numero + 1):
#        if es_primo(numer):
#            print(numer)
#Numero = int(input("Ingrese un número n: "))
#numeros_primos_hasta_n(Numero)
"""Ejercicio 2"""
#Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecucion
#def hacer_sandwich():#Primer criterio
#    condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
#    while condimento.lower() != 'salir':
#        print(f"Se ha agregado {condimento} al sándwich.")
#        condimento = input("Ingrese otro condimento (o 'salir' para terminar): ")
#hacer_sandwich()
#def hacer_sandwich_alternativo(): #Segun criterio
#    while True:
#        condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
#        if condimento.lower() == 'salir':
#            break
#        print(f"Se ha agregado {condimento} al sándwich.")
#hacer_sandwich_alternativo()
"""Ejecicio 3"""
#A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes
#def hacer_remera(tamaño, mensaje): #Punto A
#    print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'")
#hacer_remera('M', 'Python es genial')
#hacer_remera(mensaje='Hola, mundo!', tamaño='S')
#def hacer_remera(tamaño='L', mensaje='Me gusta Python'): #Punto B
#    print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'")
#hacer_remera()
#hacer_remera('M', 'Python rocks!')
#hacer_remera(mensaje='Programador en acción')
"""Ejercicio 4"""
#Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 
#def fibonacci(numero):
#    fib_series = [0, 1]
#    while len(fib_series) < numero:
#        fib_series.append(fib_series[-1] + fib_series[-2])
#    return fib_series
#numero = int(input("Ingrese un número n para la serie de Fibonacci: "))
#print(Fibonacci(numero))
"""Ejercicio 5"""
#(Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
#la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
#el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
#calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.
#def suma(x, y):
#    return x + y
#def resta(x, y):
#    return x - y
#def multiplicacion(x, y):
#    return x * y
#def division(x, y):
#    if y != 0:
#        return x / y
#    else:
#        return "Error: división por cero"
#operaciones = {
#    1: suma,
#    2: resta,
#    3: multiplicacion
#    4: division
#}
#print("Operaciones disponibles:")
#print("1 Suma")
#print("2 Resta")
#print("3 Multiplicación")
#print("4 División")
#opcion = int(input("Ingrese el número de la operación que desea realizar: "))
#numero1 = float(input("Ingrese el primer número: "))
#numero2 = float(input("Ingrese el segundo número: "))
#if opcion in operaciones:
#    resultado = operaciones[opcion](numero1, numero2)
#    print("El resultado es:", resultado)
#else:
#    print("Opción inválida")
"""Ejercicio 6"""
#(Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir
#gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
#conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462
#libras = 1 gramo 
#def gramos_a_libras(gramos):
#    return gramos * 0.00220462
#def libras_a_gramos(libras):
#    return libras / 0.00220462
#def cm_a_pulgadas(cm):
#    return cm * 0.393701
#def pulgadas_a_cm(pulgadas):
#    return pulgadas / 0.393701
#def km_a_millas(km):
#    return km / 1.60934
#def millas_a_km(millas):
#    return millas * 1.60934
#print("Opciones de conversión:")
#print("1-Gramos a Libras")
#print("2-Libras a Gramos")
#print("3-Centímetros a Pulgadas")
#print("4-Pulgadas a Centímetros")
#print("5-Kilómetros a Millas")
#print("6-Millas a Kilómetros")
#valor=float(input("Ingrese el valor a convertir: "))    
#Traspaso=int(input("Ingrese el número de la conversión que desea realizar: "))
#if Traspaso==1:
#    resultado=gramos_a_libras(valor)
#elif Traspaso==2:
#    resultado=libras_a_gramos(valor)
#elif Traspaso==3:
#    resultado=cm_a_pulgadas(valor)
#elif Traspaso==4:
#    resultado=pulgadas_a_cm(valor)
#elif Traspaso==5:
#    resultado=km_a_millas(valor)
#elif Traspaso==6:
#    resultado=millas_a_km(valor)
#else:
#    resultado="Opción inválida"
#print("El resultado es:", resultado)
"""Ejercicio 7"""
#(Opcional) Cuando un año es bisiesto, el mes más corto del año, febrero, tiene 29 días en
#vez de 28. Esto sucede casi cada 4 años. Los tres criterios que permiten saber si un año es
#bisiesto en el calendario gregoriano (el nuestro) son los siguientes:
#• Si el año es divisible enteramente por 4, es bisiesto a menos que: o El año sea divisible por
#100, entonces NO es bisiesto, a menos que:
#▪ El año sea también divisible por 400. Entonces sí es un año bisiesto. Esto significa que
#en el calendario gregoriano los años 2000 y 2400 son bisiestos, mientras que los años 1900,
#2100, 2200 y 2300 no son bisiestos.
#a) Escriba una función que tome un año y diga si es bisiesto o no.
#b) Modifique su programa para que devuelva todos los años bisiestos entre el año
#actual y el año pasado a la función como parámetro (este debe ser posterior al año actual).    
#def es_bisiesto(year):#Punto A
#    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#        return True
#    else:
#        return False
#year = int(input("Ingrese un año: "))
#if es_bisiesto(year):
#    print(f"{year} es un año bisiesto.")
#else:
#    print(f"{year} no es un año bisiesto.")
#def es_bisiesto(year):#Punto B
#    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#        return True
#    else:
#        return False
#def años_bisiestos_entre(desde, hasta):
#    bisiestos = [year for year in range(desde, hasta + 1) if es_bisiesto(year)]
#    return bisiestos
#año_pasado = int(input("Ingrese el año pasado: "))
#año_actual = int(input("Ingrese el año actual: "))
#años_bisiestos = años_bisiestos_entre(año_actual, año_pasado)
#print("Años bisiestos entre", año_actual, "y", año_pasado, ":", años_bisiestos)
"""Ejercicio 8"""
#Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5,
#obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de todos los
#múltiplos de 3 o 5 menores a 1000.
#suma = 0
#for num in range(1, 1000):
#    if num % 3 == 0 or num % 5 == 0:
#        suma += num
#print("La suma de los múltiplos de 3 o 5 menores a 1000 es:", suma)

