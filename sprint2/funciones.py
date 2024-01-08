#%% Definir una funcion para determinar si un numero es par o impar.

def par(num):
    if num%2 ==0:
       return True
    else:
       return False 
#Esto es aparte de la funcion 
valor= 40   
resultado= par(valor)
print("El",valor,"es par:",resultado)
# %% Definir una funcion que permita sumar dos numeros

def suma(num1,num2):
    resultado= num1+num2
    return resultado

valor1=(5)
valor2= (10)
resultado= suma(valor1,valor2)
print("La suma de los valores",valor1,"y",valor2,"es:",resultado)



# %% Implementar la funcion voltear texto, que reciba un string y retorna el string invertido.

def invertir_Texto(texto):
    resultado= texto [::-1] #se utilizo un slicing
    return resultado

frase= input("Escriba su frase: ")
resultado= invertir_Texto(frase)
print("Su texto original:",frase)
print("Su texto invertido:",resultado)

# %% Implemente la funcion multLista(lista), reciba una lista de numeros y retorna la multiflicaion total de los valores conteniudos en la lista

def mulList(lista):
    resultado = 1
    for num in lista:
        resultado= resultado*num
    return resultado

num= [7,8,6,8,9]
resultado= mulList(num)
print("Tu lista de numeros",num,"multiplicando todos sus valores,da como resultado:",resultado)


# %% desarrollar una calculadora aritmetica utilizando funciones

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1 / num2

valor1=int(input("Ingrese un número: "))
valor2= int(input("Ingrese otro número: "))
operacion= input("Ingrese la operación[+ - * /]: ")

if operacion=="+":
    resultado= suma(valor1, valor2)
elif operacion == "-":
    resultado= resta(valor1, valor2)
elif operacion=="*":
    resultado= multiplicacion(valor1, valor2)
elif operacion=="/":
    resultado= division(valor1, valor2)
else:
    print("operación fallida")
    
#Formateo de string (F-String)
print(f"El resultado de su operacion {valor1} {operacion} {valor2} es igual a: {resultado}")


# %%
