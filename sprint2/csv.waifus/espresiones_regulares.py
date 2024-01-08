#%% Evaluar que una cadena tenga al menos un @
import re 
cadena= "Hola prim@"
if (re.search("@+",cadena)):
    print("Se encontro el @")
else:
    print("No se encontro un @")


# %% Evaluar si una cadena tiene un digito
import re
cadena= "Misaka tiene 16 años"

if (re.search("\d",cadena)):
    print("match")
else: 
    print("no match")
    
# %% Evaluar si una cadena tiene al menos un digito y una letra mayuscula

import re
cadena= "Misaka Mikoto"

if (re.search('\d*[A-Z]',cadena)):
    print("Si tiene un digito y una letra mayuscula")
else: 
    print("no match")
    
print(f"Tu frase es: {cadena}")
# %% Escriba una funcion que recibe un string y retorna un true o false, si el texto tiene algun saludo
#pendiente
import re
def existeSaludo(text):
    if (re.search('[ho*la]',cadena)):
        return True
    else:
        return False
    return resultado

cadena= input("Ingrese un saludo: ")
resultado= existeSaludo(cadena)
print(resultado)


# %% Evaluar que el nombre de un archivo correponda a un archivo de texto con extensiones: csv,.txt o .tsv
import re

def esArchivoTexto(nombre_archivo):
    patron= '\.(csv)$'
    
    coincidencia= re.search(patron,nombre_archivo)
    return bool(coincidencia)

nombre_archivo= ("estudiante.csv")
esValido=esArchivoTexto("nombre_archivo")
print(esValido)

# %%
