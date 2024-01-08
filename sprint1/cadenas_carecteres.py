#%%

texto= "Hola mundo, me llamo Ismael"
nro_carcateres= len(texto)
print(texto,"tiene",nro_carcateres,"caracteres")

#%% Ejercicio N°2:Concatenación de cadenas
nombre= "Ismael"
apellido="Cansignia" 

nombre_completo=nombre+apellido
print(nombre_completo)


# %% Ejercicio N°3: de mayusculas a minusculas 
frase= "Python es divertido"
frase_en_mayusculas= frase.upper()
frase_en_minusculas= frase.lower()
print(frase_en_mayusculas)
print(frase_en_minusculas)
# %% Ejercicio N°4: Dividir una cadena
frase= "python es mi lenguaje de programacion favorito"
palabras= frase.split(" ")
print(palabras)

# %%
frase= "spider man es mi personaje favorito de la ficcion"
palabras= frase.split(" ")
print(palabras) 

# %% EJERCICIO N°5:Pedir al usuario que ingrese una frase y contar cuantas palabras tiene
frase= input("Ingrese_su_frase")
palabras= frase.split () 
cantidad_de_palabras= len(palabras)
print ("la frase tiene{cantidad_de_palabras}palabras")


# %%
frase=input("Ingrese una frase")
frase_dividida= frase.split ("")
nro_de_palabras=len(frase_dividida)
print("La frase que ingreso tiene",nro_de_palabras,"palabras") 
# %%


# %%
