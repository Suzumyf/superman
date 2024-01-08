waifus= [ ]
print(waifus)
waifus=["Misaka Mikoto", "Xenovia Quarta", "Chisato Nishikigui", "Ochako Uraraka", "Sinon", "Amy Rose", "Kurumi Tokisaki" ]
print(waifus)
#SLICING
#para ver datos en especifico, no es tomado en cuenta el ultimo termino sino el penultimo
print(waifus[1:4])
print(waifus[ 2:7])
#para llamar a un elemento en especifico
#No te olvides que en indices comenzamos con 0
print(waifus[2])

# ITERACION DE LISTAS

for waifus in waifus:
    print(waifus)
    
    
#%%
lista_vacia=[ ]
waifus=["Xenovia","Misaka","Sinon","Kurumi", "Chisato", "Roxane", "Lilith", "Nino" ]
print(lista_vacia)
print(waifus)

print(type(lista_vacia))
print(type(waifus))

# %% ACCEDER A LOS ELEMENTOS
print(waifus[5])

print(waifus[0:8])
print(waifus[-1 ])

# %% CAMBIAR EL ELEMENTO MISAKA POR AKENO
waifus[1]="Akeno"
print(waifus[1])
print(waifus)
# %%
print(waifus[6:8])
# %% AGREGAR UNA NUEVA WAIFU MISAKA

waifus= waifus + ["Misaka" ]
print(waifus)
waifus.append("Koneko")
print(waifus)

#%% LIMPIAR TODA LA LISTA

waifus.clear()
print(waifus)

# %%INSERTAR UN ALUMNO AL INICIO DE LA LISTA 
waifus.insert(0,"Kotori")
print(waifus)


# %%INTERANDO LISTAS

vocales= [ ]
print(vocales)
vocales=["a","e","i","o","u" ]
print(vocales[2 ])
for vocales in vocales:
    print(vocales.upper())

# %%
numeros=[ ]
print(numeros)
numeros=[10,30,40,8,2 ]
for numeros in numeros:
    resultado= numeros * 2
    print(resultado)
    
# %% DEFINE UNA LISTA DE NUMEROS Y ENCUENTRA EL NUMERO MÁS ALTO

numeros=[ ]
print(numeros)
l=[541,10,50,7000,8800,9774]
maximo = 0 
for numero in l:
    if numero > maximo:
        maximo = numero
print("El numero con mayor valor de la lista es:", maximo)
# %% ENCONTRAR EL NUMERO MENOR

numeros=[ ]
print(numeros)
l=[-5,1,70,0,80,74]
menor= 0
for numero in l:
    if numero< menor:
        menor=numero
print("El numero con menor valor es:", menor)

# %% ITERAR UNA SECUENCIA DE NUMEROS DEEL 1 AL 10
for n in range (1,26):
    print(n)


# %% CREAR UNA LISTA CON UN INCREMENTO DE 2 HASTA EL 100
elevados= [ ]
for n in range (1,101):
    elevado= n **3
    elevados.append(elevado)

print(elevados)

# %% 
