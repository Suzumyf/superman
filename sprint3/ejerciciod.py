class Persona: 
    def __int__(self, cedula:str, nombre:str, apellido:str)-> None:
        self.__cedula= cedula
        self.__nombre= nombre
        self.__apellido= apellido   
    
    def get_cedula(self) -> str:
        return self.__cedula
    
    def set_cedula(self, cedula)-> None:
        self.__cedula= cedula
       
    def get_nombre(self)-> str:
        return self.__nombre
    
    def set_cedula(self, nombre)-> None:
        self.__nombre= nombre
        
    def get_apellido(self)-> str:
        return self.__apellido
    
    def set_cedula(self, apellido)-> None:
        self.__apellido= apellido
    
    def __str__ (self) -> str:
        return f'Persona -> (cedula: {self.__cedula}, nombre: {self.__nombre}, apellido: {self.__apellido})'

class Cuenta:
    def __int__(self, nrocuenta: str, titular:Persona, monto:float)-> None:
        self.__nrocuenta= nrocuenta
        self.__titular= titular
        self.__monto= monto
        
    def get_nrocuenta(self) -> str:
        return self.__nrocuenta
    
    def set_nrocuenta(self, nrocuenta)-> None:
        self.__nrocuenta= nrocuenta
    
    def get_titular(self) -> Persona:
        return self.__titular
    
    def set_titular(self, titular:Persona)-> None:
        self.__titular= titular
        
    def get_monto(self) -> float:
        return self.__monto
    
    def set_monto(self, monto)-> None:
        self.__monto= monto
    
    def __str__ (self) -> str:
        return f'Cuenta -> (nrocuent: {self.__nrocuent}, titular: {self.__titular}, monto: {self.__monto})'

    
    def ingresar(self,cantidad:float) ->None:
        self.__monto += cantidad
        
    def retirar(self,cantidad:float) ->None:
        if cantidad <= self.__monto: 
            self.__monto += cantidad
            
class CuentaAhorros(Cuenta):
    COMISION= 1.00
    
    def ingresar(self, cantidad: float) -> None:
        if (cantidad > self.COMISION):
            super().ingresar(cantidad-self.COMISION)
        else:
            print(f'La cantidad a ingresar debe ser mayor que {self.COMISION}')
            
    def retirar(self, cantidad: float) -> None:
        super().retirar(cantidad+self.COMISION)
    
    @staticmethod
    def mostrar_politicas() -> None:
        print("Cuenta de Ahorro: Se cobrara una comision fija de $1 por cada ingreso o retiro.")

class CuentaCorriente(Cuenta):
    MONTO_LIMITE_SIN_COMISION = 100
    PORCENTAJE_COMISION = 0.01

    def ingresar(self, cantidad: float) -> None:
        if cantidad >= self.MONTO_LIMITE_SIN_COMISION:
            comision = cantidad * self.PORCENTAJE_COMISION
            cantidad -= comision
            print(f'Se aplicó una comisión del 1% por el ingreso: ${comision}')
        super().ingresar(cantidad)

    def retirar(self, cantidad: float) -> None:
        if cantidad >= self.MONTO_LIMITE_SIN_COMISION:
            comision = cantidad * self.PORCENTAJE_COMISION
            cantidad += comision
            print(f'Se aplicó una comisión del 1% por el retiro: ${comision}')
        super().retirar(cantidad)

    @staticmethod
    def mostrar_politicas() -> None:
        print("Cuenta Corriente: No hay comisión por retiros o ingresos menores a $100. Para cantidades mayores, se cobra una comisión del 1%.")



titular1 = Persona("1725102508", "Gabriel", "Villacis")

cuenta1 = CuentaAhorros("000001", titular1, 100)
cuenta2 = CuentaCorriente("000002", titular1, 50)

# Mostrar las políticas:
CuentaAhorros.mostrar_politicas()
CuentaCorriente.mostrar_politicas()

cuenta1.ingresar(150)
print(f'Saldo en cuenta de ahorros: {cuenta1.get_monto()}')

cuenta2.ingresar(150)
print(f'Saldo en cuenta corriente: {cuenta2.get_monto()}')
cuenta2.retirar(200)
print(f'Saldo en cuenta corriente: {cuenta2.get_monto()}')

            
    
