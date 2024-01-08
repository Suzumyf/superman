# EJERCICIO DE BIBLIOTECA
from abc import ABC,abstractmethod

class Libro(ABC):
    
    def __int__(self, titulo:str, autor:str)-> None:
        self.titulo= titulo
        self.autor= autor 
        
    @abstractmethod
    def calcularprecio(self)-> float:
        pass
    
class Librofisico(Libro):
    valor_base= 10
    precio_pagina= 0.1
    
    def __init__(self, titulo:str, autor:str, nmrpaginas: int ) -> None:
        super().__init__(titulo,autor) 
        self.nmrpaginas= nmrpaginas 
   
    def calcularprecio(self)-> float:
        precio= self.valor_base + (self.nmrpaginas * self.precio_pagina)
        return precio

class Librodigital(Libro):
    valor_base= 5
    precio_megab= 0.1
    
    def __init__(self, titulo:str, autor:str, nmrmeg: float) -> None:
        super().__init__(titulo,autor) 
        self.nmrmeg= nmrmeg 
   
    def calcularprecio(self)-> float:
        precio= self.valor_base + (self.nmrmeg * self.precio_megab)
        return precio
    

Librofisico = Librofisico("Dragon ball","Akira Toriyama",500)
print(f'Precio de su libro fisico": {Librofisico.calcularprecio()}')

Librodigital = Librodigital("Dragon ball","Akira Toriyama",500)
print(f'Precio de su libro digital": {Librodigital.calcularprecio()}')

#EJERCICIO DE FIGURAS GEOMETRICAS
    
from abc import ABC,abstractmethod

class Figurageometrica(ABC):
       
    @abstractmethod
    def calcular_area(self)-> float:
        pass

class Circulo(Figurageometrica):

    
    def __init__(self,pi:float, radio:float) -> None:
        self.radio= radio
        self.pi= pi
    
    
    def calcular_area(self)-> float:
        terreno= self.pi * (self.radio**2)
        return terreno

class Rectangulo(Figurageometrica):
    
    
    def __init__(self, base:float, altura:float) -> None:
        self.base= base
        self.altura= altura
        
    def calcular_area(self)-> float:
        terreno= self.base * self.altura 
        return terreno

Circulo= Circulo(3.14,7,7)
print(Circulo)
    