from detetime import date
class Computadora:
   
    def __init__(self, p_procesador, p_ram, p_conectiviad, p_esta_pagada, p_precio):
        self.procesador= "And Ryzen 5600x"
        self.ram= "32BG"
        self.conectividad= "wireless"
        self.esta_pagada= True
        self.precio= 1500
        self.tipo= "p_tipo"

computadora1= Computadora("And Ryzen 5600x", "32BG", "wireless",True, "p_precio")
print(computadora1.procesador)

computadora2= Computadora("p_procesador", "p_ram", "p_conectiviad", "p_esta_pagada","p_precio")
print(computadora2.procesador)

"""
#Ejercicio 2
class Carro:
   
    def __init__(self, color, marca, modelo,precio,combustible):
        self.__color= color
        self.__marca= marca
        self.__modelo= modelo
        self.__precio= precio
        self.__combustible= combustible
"""        


# Ejercicio 3

class Profesor:
    
    def __init__(self,nombre:str ,apellido:str):
        self.__nombre= nombre
        self.__apellido= apellido
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre= nuevo_nombre
      
    def get_apellido(self):
        return self.__apellido  
    
    def get_apellido(self,nuevo_apellido):
        self.__apellido= nuevo_apellido
    
    def __str__(self)-> str:
        return f'Profesor->(nombre{self.__nombre}, apellido{self.__apellido})'
    

class Estudiante: 
    
    def __int__(self,ID:int,nombre:str,apellido:str,año_nacimiento:date):
        self.__ID= ID
        self.__nombre= nombre
        self.__apellido= apellido
        self.__año_nacimiento= año_nacimiento
        
    def get_ID(self):
        return self.__ID
    def set_ID(self,nuevo_ID):
        self.__ID= nuevo_ID
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nuevo_nombre):
        self.__nombre= nuevo_nombre
        
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,nuevo_apellido):
        self.__apellido= nuevo_apellido 
        
    def get_año_nacimiento(self):
        return self.__año_nacimiento
    def set_año_nacimiento(self,nuevo_año_nacimiento):
        self.__año_nacimiento= nuevo_año_nacimiento
   
    def __str__(self)-> str:
        return f'Estudiante->(ID{self.__ID},nombre{self.__nombre}, apellido{self.__apellido},año_nacimiento{self.__año_nacimiento})'   

class Curso:
    def __init__(self, codigo:int,nombre:str,profesor:Profesor):
        self.__codigo= codigo
        self.__nombre= nombre
        self.__profesor= profesor
        
    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,nuevo_codigo):
        self.__codigo= nuevo_codigo
    
    def get_nombre(self):
        return self.__nombre
    def set_codigo(self,nuevo_nombre):
        self.__nombre= nuevo_nombre
    
    def get_profesor(self):
        return self.__profesor
    def set_codigo(self,nuevo_profesor):
        self.__profesor= nuevo_profesor

    def get_alumno(self):
        return self.__alumno
    def set_alumno(self,nuevo_alumno:List[alumno]):
        self.__alumno= nuevo_alumno
    
   
      
profe1= Profesor("Itsuki","Nakano")
profe1.set_nombre("Miku")
print(profe1)

estu1= Estudiante(1,"Itsuki", "Nakano",date(2004/8/10))
print(estu1)

  