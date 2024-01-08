import csv
print ("csv")
#Funcion leer_csv retornar el contenido de un archivo en un alista de diccionario
def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo,'r',encoding='UTF-8') as archivo:
            lector= csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe")
        return[]
#Funcion filtrar datos: Filtrar la lista de waifus y retorna la puntuacion de 90 
"""def filtrar_datos(lista_a_filtar,puntuacion):
    lista temp= []
    for d in lista_a_filtar:
        if (int(d.get('puntuacion'))>=puntuacion):
             lista temp.append(d)
        return  lista temp """
    
def filtrar_datos(lista_a_filtrar,puntuacion):
    return [e for e in lista_a_filtrar]
#Program principal
lista=leer_csv("waifus.csv")
lista_filtrada=filtrar_datos(lista,90)

for e in lista_filtrada:
    print(e)
# %%
