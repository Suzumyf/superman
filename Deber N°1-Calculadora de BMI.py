#%% Ejercicio N°1: 
"""
Pide al usuario ingresar su peso en kilogramos y su altura en metros. Calcula y muestra su BMI utilizando la siguiente formula: BMI=Peso/ (Altura^2).
Luego clasifica el BMI en las categorías: Bajo peso, Normal, SObrepeso u Obeso según los siguienes rangos:
-BMI menor que 18.5 = Bajo peso. 
-BMI mayor o igual que 18.5 y menor que 24.9 =Peso Normal. 
-#BMI mayor o igual que 24.9 y menor que 29.9 =sobrepeso.
-BMI mayor que 29.9 = Obeso.

"""
peso =float(input("Ingrese su peso en (KILOGRAMOS) "))
altura =float(input ("Ingrese su altura en (METROS) "))
print("Su peso es de", peso , "en Kilogramos ")
print("Su estatura es de", altura , "en Metros ")

bmi= peso/ (altura**2)
texto= ("Su BMI es de: ")

if bmi < 18.5:
    print(texto,bmi,"se encuentra bajo peso ")
elif bmi>= 18.5 and bmi < 24.9  :
    print(texto,bmi,"tiene un Peso normal")
elif bmi >= 24.9 and bmi < 29.9 :
    print(texto,bmi,"usted posee Sobrepeso")
else:
    print(texto,bmi,"usted tiene Obesidad")

# %%
