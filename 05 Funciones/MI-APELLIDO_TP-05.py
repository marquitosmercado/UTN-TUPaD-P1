#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 

multiplos_de_4 = list(range(4, 101, 4))
print("Lista de múltiplos de 4 entre 1 y 100:")
print(multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! 

mi_lista = ["rojo", "azul", "verde", "amarillo", "blanco"]
penultimo = mi_lista[-2]
print(f"La lista creada es: {mi_lista}")
print(f"El penúltimo elemento de la lista es: {penultimo}")


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 1 pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

mi_lista_vacia = []
mi_lista_vacia.append("manzana")
mi_lista_vacia.append("banana")
mi_lista_vacia.append("cereza")
print("La lista resultante es:")
print(mi_lista_vacia)


#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"] 

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("La lista de animales modificada es:")
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# números.remove(max(números))
# print(numerps)

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

mi_lista = list(range(10, 31, 5))
primeros_dos = mi_lista[0:2]
print(f"La lista completa es: {mi_lista}")
print(f"Los dos primeros elementos son: {primeros_dos}")

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. 
#autos = ["sedan", "polo", "suran", "gol"] 

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "camioneta"
autos[2] = "moto"
print("La lista de autos modificada es:")
print(autos)


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla. 

dobles = []
dobles.append(5 * 2)  # Agrega 10
dobles.append(10 * 2) # Agrega 20
dobles.append(15 * 2) # Agrega 30
print("La lista 'dobles' resultante es:")
print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
# ["agua"]] 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

print("Lista original de compras:")
print(compras)
print("-" * 30) 
compras[2].append("jugo")
print("Después de agregar 'jugo' al tercer cliente:")
print(compras)
print("-" * 30)
compras[1][1] = "tallarines"
print("Después de reemplazar 'fideos' por 'tallarines' en el segundo cliente:")
print(compras)
print("-" * 30)
compras[0].remove("pan")
print("Después de eliminar 'pan' del primer cliente:")
print(compras)
print("-" * 30)
print("Lista final resultante:")
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.


lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("La lista anidada creada es:")
print(lista_anidada)
