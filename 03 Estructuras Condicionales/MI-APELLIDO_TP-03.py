#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingresá tu edad: ")) 
if edad > 18:
    print("Es mayor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

nota = float(input("Ingresá tu nota: ")) 
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingresá un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingresá tu edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30: 
    print("Adulto/a joven")
else:
    print("Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string

contrasena = input("Ingresá tu contraseña: ")
longitud_contrasena = len(contrasena)
if longitud_contrasena >= 8 and longitud_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

texto = input("Ingresá una frase o palabra: ")
vocales = "aeiouAEIOU" 
ultimo_caracter = texto[-1]
if ultimo_caracter in vocales:
    string_resultante = texto + "!" 
    print(string_resultante)
else:
    print(texto)


#7) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre = input("Ingresá tu nombre: ")
print("\nOpciones de transformación:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con Primera Letra en Mayúscula")
opcion = int(input("Ingresá el número de la opción deseada (1, 2 o 3): "))

if opcion == 1:
    nombre_transformado = nombre.upper() 
    print("Tu nombre en MAYÚSCULAS es:", nombre_transformado)
elif opcion == 2:
    nombre_transformado = nombre.lower() 
    print("Tu nombre en minúsculas es:", nombre_transformado)
elif opcion == 3:
    nombre_transformado = nombre.title()
    print("Tu nombre con la Primera Letra en Mayúscula es:", nombre_transformado)
else:
    print("Opción no válida. Por favor, ingresá 1, 2 o 3.")



#8) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero #generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras #débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingresá la magnitud del terremoto (ej. 3.5): "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4: 
    print("Leve (ligeramente perceptible)")
elif magnitud < 5: 
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6: 
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7: 
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#9) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año: Desde el 21 de diciembre hasta el 20 de marzo (incluidos)
#Estación en el hemisferio norte: Invierno 
#Estación en el hemisferio sur: Verano 
#---------------------------------------------------------------------------------------
#Periodo del año: Desde el 21 de marzo hasta el 20 de junio (incluidos) 
#Estación en el hemisferio norte: Primavera
#Estación en el hemisferio sur: Otoño 
#---------------------------------------------------------------------------------------
#Periodo del año: Desde el 21 de junio hasta el 20 de septiembre (incluidos) 
#Estación en el hemisferio norte: Invierno 
#Estación en el hemisferio sur: Verano 
#---------------------------------------------------------------------------------------
#Periodo del año: Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) 
#Estación en el hemisferio norte: Otoño 
#Estación en el hemisferio sur: Primavera
#---------------------------------------------------------------------------------------
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
#---------------------------------------------------------------------------------------
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper() 
mes = input("Ingresá el mes (ej. enero, febrero): ").lower()
dia = int(input("Ingresá el día del mes: "))
meses_numeros = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}
numero_mes = meses_numeros.get(mes, 0) 
if numero_mes == 0 or not (1 <= dia <= 31):
    print("Fecha o mes ingresado no válido. Por favor, revisá tu entrada.")
else:
    estacion = "Desconocida" # Valor por defecto

    # Primer período: Desde el 21 de diciembre hasta el 20 de marzo
    if (numero_mes == 12 and dia >= 21) or \
       (numero_mes == 1) or \
       (numero_mes == 2) or \
       (numero_mes == 3 and dia <= 20):
        if hemisferio == "N":
            estacion = "Invierno"
        elif hemisferio == "S":
            estacion = "Verano"

    # Segundo período: Desde el 21 de marzo hasta el 20 de junio
    elif (numero_mes == 3 and dia >= 21) or \
         (numero_mes == 4) or \
         (numero_mes == 5) or \
         (numero_mes == 6 and dia <= 20):
        if hemisferio == "N":
            estacion = "Primavera"
        elif hemisferio == "S":
            estacion = "Otoño"

    # Tercer período: Desde el 21 de junio hasta el 20 de septiembre
    elif (numero_mes == 6 and dia >= 21) or \
         (numero_mes == 7) or \
         (numero_mes == 8) or \
         (numero_mes == 9 and dia <= 20):
        if hemisferio == "N":
            estacion = "Verano"
        elif hemisferio == "S":
            estacion = "Invierno"

    # Cuarto período: Desde el 21 de septiembre hasta el 20 de diciembre
    elif (numero_mes == 9 and dia >= 21) or \
         (numero_mes == 10) or \
         (numero_mes == 11) or \
         (numero_mes == 12 and dia <= 20):
        if hemisferio == "N":
            estacion = "Otoño"
        elif hemisferio == "S":
            estacion = "Primavera"

    if estacion != "Desconocida":
        print(f"Te encuentras en: {estacion}")
    else:
        print("No se pudo determinar la estación para la fecha ingresada.")
