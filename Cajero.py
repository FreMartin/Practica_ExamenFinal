

from ast import List
from Cuenta import Cuenta

class Cajero():

    def __init__(self, cuentas: List[Cuenta], cuenta: int, valor: float):
        self.cuentas = cuentas
        self.cuenta = cuenta
        self.valor = valor
        
   
    def Consultar(self):
         
         for c in self.cuentas:
            if c.numero_cuenta == self.cuenta:
                print(f"Saldo: {c.saldo}")
            else:
                print("No existe la cuenta")
    
    
    def Deposito(self):
        
        for c in self.cuentas:
            if c.numero_cuenta == self.cuenta:
                c.saldo += self.valor
            else:
                print("No existe la cuenta")
    
    def Retiro(self):

        for c in self.cuentas:
            if c.numero_cuenta == self.cuenta:
                if c.saldo > self.valor:
                    c.saldo -= self.valor
                else:
                    print("Fondos insuficientes")
            else:
                print("No existe la cuenta")