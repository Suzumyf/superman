# Estudiante: Ismael Cansignia
"""Sprint 1: Fundamentos de la programacion en Python.
Resolver los siguienetes ejercicios y entregar las soluciones en un solo archivo de Python
diviiendo cada ejercicio en celda """

#%% Ejercicio N°1: Conteo de letras Mayúsculas y minúsculas.
""" Escribe un programa que cuente cuantas letras mayúculas y cuantas letras minúsculas 
hay en una cadena de texto que sea ingresada por el ususario"""

cadena= str(input("Por favor ingrese su linea de texto: "))

mayusculas= 0
minusculas= 0

for t in cadena:
    if t.isupper ():
        mayusculas +=1
    elif t.islower():
        minusculas +=1 
           
print("Su frase es:",cadena)    
print("su frase contiene:",minusculas,"letras minisculas" )
print("su frase contiene:",mayusculas,"letras mayusculas" )

#%% Ejercicio N°2: Es palíndromo o no
""" Realice un programa que determine si una frase ingresada es un palíndromo,ignorando espacios,
mayúsculas y minúsculas y signos de puntuación. Los palíndromos son frases que independientemente
por cual lado comiences a leer obtendras el mismo resultado"""

frase = input("Ingresa una frase: ").replace(" ", "").lower()
print("Su frase es:",frase)
if frase == frase[::-1]:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")

#%% Ejercicio N°3: Año bisiesto
"""Escribe un programa que determine si un año ingresado por el usuario es un año Bisiesto o no.
Las reglas para determiniar si un año es bisiesto son las siguientes:
-Un año es bisiesto si es divicible por 4.
- Sin embargo, si el año también es divisible por 100, no es bisiesto,a menos que:
-El año sea divisible por 400, en cuyo caso si es bisiesto.  
"""
#Porfavor introduzca el año que desee averiguar si es considerado año bisiesto o no.
#Obtener el año del usuario
año=int(input("Por favor ingrese el año que desee consultar: "))
#Verificar si el año introducido es bisiesto o no
print("el año", año)
if (año % 4==0 and año%100 != 0) or (año%400==0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")


#%%Ejercicio N°4: Números consecutivos en una lista.
"""Asuma que existe una lista con números en ellas. Escriba un programa que encuentre cúantas veces hay
3 números consecutivos en la lista"""

def numeros_consecutivos(lista):
    contador= 0
    
    for i in range(len(lista)-2):
        if lista[i] + 1 == lista [i+1] and lista [i+1]+1 == lista [i+2]:
            contador +=1
    return contador

#lista predefinida

l1 = [1,2,3,4,5,6,8,9,10,11]
consecutivos = numeros_consecutivos(l1)
print(f"Veces en que hay 3 consecutivos = {consecutivos} veces")


# %%
