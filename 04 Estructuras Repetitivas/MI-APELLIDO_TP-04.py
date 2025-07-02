#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for numero in range(101):
    print(numero)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

numero_str = input("Ingresá un número entero: ")
if numero_str.startswith('-'): 
    numero_str = numero_str[1:] 
cantidad_digitos = len(numero_str)
print(f"El número ingresado tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 
valor1 = int(input("Ingresá el primer valor entero: "))
valor2 = int(input("Ingresá el segundo valor entero: "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1
suma_total = 0
for numero in range(valor1 + 1, valor2):
    suma_total += numero 
print(f"La suma de los números entre {valor1} y {valor2} (excluyéndolos) es: {suma_total}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

total_acumulado = 0
numero_ingresado = -1
while numero_ingresado != 0:
    numero_ingresado = int(input("Ingresá un número entero (0 para terminar): "))
    if numero_ingresado != 0:
        total_acumulado += numero_ingresado
print(f"La suma total de los números ingresados es: {total_acumulado}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
numero_secreto = random.randint(0, 9)
intentos = 0
suposicion = -1
print("¡Bienvenido al juego Adivina el Número!")
print("Estoy pensando en un número entre 0 y 9. ¿Podrás adivinarlo?\n")
while suposicion != numero_secreto:
    try:
        suposicion = int(input("Ingresá tu suposición: "))
        intentos += 1
        if suposicion < numero_secreto:
            print("Demasiado bajo. ¡Intentá de nuevo!")
        elif suposicion > numero_secreto:
            print("Demasiado alto. ¡Intentá de nuevo!")
    except ValueError:
        print("Entrada no válida. Por favor, ingresá un número entero.")
print(f"\n¡Felicitaciones! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

for numero in range(100, -1, -2):
    print(numero) 


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

while True: 
    try:
        limite = int(input("Ingresá un número entero positivo para el límite de la suma: "))
        if limite >= 0:
            break
        else:
            print("Por favor, ingresá un número positivo (o cero).")
    except ValueError:
        print("Entrada no válida. Por favor, ingresá un número entero.")
suma_total = 0

for numero in range(limite + 1):
    suma_total += numero
print(f"La suma de los números entre 0 y {limite} es: {suma_total}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

CANTIDAD_NUMEROS = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0
print(f"Por favor, ingresá {CANTIDAD_NUMEROS} números enteros.")
for i in range(CANTIDAD_NUMEROS):
    while True: 
        try:
            numero = int(input(f"Ingresá el número {i + 1}: "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresá un número entero.")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\n--- Resultados del Análisis ---")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

CANTIDAD_NUMEROS = 100 
suma_total = 0
print(f"Por favor, ingresá {CANTIDAD_NUMEROS} números enteros para calcular su media.")
for i in range(CANTIDAD_NUMEROS):
    while True:
        try:
            numero = int(input(f"Ingresá el número {i + 1}: "))
            break 
        except ValueError:
            print("Entrada no válida. Por favor, ingresá un número entero.")
    suma_total += numero
if CANTIDAD_NUMEROS > 0:
    media = suma_total / CANTIDAD_NUMEROS
    print(f"\nLa suma total de los números ingresados es: {suma_total}")
    print(f"La media (promedio) de los {CANTIDAD_NUMEROS} números es: {media:.2f}") 
else:
    print("\nNo se ingresaron números para calcular la media.")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_str = input("Ingresá un número entero: ")

numero_invertido_str = numero_str[::-1]
print(f"El número con los dígitos invertidos es: {numero_invertido_str}")
