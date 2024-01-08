#la suma 5+2 me retorna 7, el retorno es el resultado de la suma
#Sirve para todos los ejercicios + -  /

#%% Ejercicio 1, suma de dos numeros, ingresar dos números y mostrar el resultado de la suma de ambos numeros  
#suma, resta, multiplicacion y divion 
numero1=int(input("ingrese un numero: "))
numero2= int(input("Ingrese otro numero: "))

print(numero1, type(numero1))
print(numero2, type(numero2))

resultado= numero1+ numero2
print("El resultado  de la suma es:", resultado)

resultado= numero1-numero2
print("El resultado de la resta es:", resultado)
# SI AGREGAS UN DOBLE // EL RESULTADO SALDRA ENTERO Y SI SOLO ES UNO / EL RESULTADO SALDRA TANTO EN DECIMAL COMO EN  ENTERO
resultado= numero1/numero2
print("El resultado de la division es:", resultado)

resultado= numero1 * numero2
print("El resultado multiplicación es:", resultado)

# %% CONDICIONES
# == IGUAL QUE, != DISTINTO A, < MENOR QUE, > MAYOR QUE, >= MAYOR O IGUAL QUE, <= MENOR O IGUAL QUE
# OPERADORES LOGICOS: AND, OR, NOT
# AND SI (True) AMBOS VALORES SON VERDADEROS
# OR SI (True) ALMENOS UNO DE LOS VALORES ES VERDADERO
# NOT (True) SI EL VALOR ES FALSO, ES UN INVERSO DE FALSO A VERDADERO Y VICEVERSA

#%% ESTRUTURA DE CONTROL IF: 
a= 51
b= 10
if b < a:
    print("b es menor que a")

#%% EJERCICIO 1: INGRESE UN NUMERO E INDICAR SI ES PAR O IMPAR
#ASI ESCRIBES UNA CONDICION, no olvidarte de la estructura y de los espacios
numero=int(input("Ingrese un numero "))
if numero%2==0:
    print("El numero es par")
else:
    print("El numero es impar")

#%% EJERICICIO 2: POSITIVO O NEGATIVO: PEDIR AL USUARIO QUE INGRESE UN NUMERO E INDICAR SI ES POSITIVO O NEGATIVO

numero=int(input("Ingrese un numero "))
if numero>=1:
    print("El numero es positivo")
else:
    print("El numero es negativo")
    
#%% Ejercicio 3: CALCULADORA DE OPERACIONES BASICAS: VAMOS A INGRESAR DOS NUMEROS Y LA OPERACION QUE QUIERA REALIZAR.
#Sentencia pass, bloques de sentencia en el if con la palabra pass, no ñp tomara en cuenta

numero6 =float(input("Ingrese un numero "))
numero7 =float(input("Ingrese otro numero "))
operacion= str(input("Ingresar su operacion: "))
resultado=0

if operacion =="+":
    resultado= numero6 + numero7
elif operacion== "-":
    resultado= numero6 - numero7
elif operacion== "*":
    resultado= numero6 * numero7
elif operacion== "/":
    resultado= numero6 / numero7
else:
    print("Sin resultados")
print("El resultado de la ",operacion, "es", resultado )
