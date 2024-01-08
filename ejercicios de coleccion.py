#%% ELIMINA DUPLICADOS DE LISTA
"""
Crear una lista con duplicados, escribir un programa que elimine duplicados y muestre otra lista sin ellos
"""

lista= (1,5,8,5,10,10,2,9,7,1,4,8,5,1)
lista_sin=[]

for i in lista:
    if i not in lista_sin:
        lista_sin.append(i)

print(lista_sin)
# %% DEBER, pendiente.
"""
Crea una tupla con un numero par de elementos
Escribe un program que divida la tupla en dos mitades y las muestre en pantalla
"""

tn= ("Xenovia",10,50,15,80,14,10,5,9,"Chisato")
lista_dividida= ()

tupla1= []
tupla2= []

for u in lista_dividida:
    

print(tupla1)
print(tupla2)

# %% Pendiente: sOLICITAR UNA FRASE Y UN CARACTER, EL PROGRAMA DEBE MOSTRAR AL USUARIO UN MENSAJE INDICANDO LOS INDICES EN LOS QUE APARECEN EL CARACTER
dialogo= input ("Ingrese una frase: ")
caracter = input("Ingrese la letra que desee investigar: ")
indice= []

for i in range(len(dialogo)):
    if dialogo[i] == caracter:
        indice.append(i)

print("La frase", dialogo)




# %% CONTEO REGRESIVO

num= int(input("ingrese un numero: "))
while num > 0:
    print(num)
    num= num-1

# %%PENDIENTE= SOLICITA AL USUARIO UN NUMERO ENTERO Y LUEGO SUMA TODOS LOS NUMEROS PARES DESDE 2 HASTA ESE NUMERO.

num= int(input("Ingrese un numero: "))
suma = 0
i=2


while i <= num:
    suma += i


    

# %% Pendiente: CREAR UN PROGRAMA EN DONDE LE PIDA NUMEROS AL USUARIO Y CUANDO PONGA SALIR EL PROGRAMA YA NO LE PIDA MAS NUMEROS

num= int(input("Ingrese un valor numerico "))



#%%

# Obtener la cadena de entrada del usuario
cadena = input("Ingresa una cadena: ")

# Inicializar los contadores
mayusculas = 0
minusculas = 0

# Recorrer la cadena y contar letras mayúsculas y minúsculas
for caracter in cadena:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1

# Mostrar los resultados
print("Letras mayúsculas:", mayusculas)
print("Letras minúsculas:", minusculas)
# %%
