from Cuenta import Cuenta
from Persona import Persona
from Cajero import Cajero

lista_personas = []
lista_cuentas = []

def main():

    lista_personas.append(Persona(1, "Martín Farfán", "martin@gmail.com"))
    lista_personas.append(Persona(2, "Juan Perez", "juan@gmail.com"))
    lista_personas.append(Persona(3, "Luis Lema", "luis@gmail.com"))


    lista_cuentas.append(Cuenta(1, "Martín Farfán", "martin@gmail.com",1,0.0))
    lista_cuentas.append(Cuenta(1, "Martín Farfán", "martin@gmail.com",2,0.0))
    lista_cuentas.append(Cuenta(3, "Luis Lema", "luis@gmail.com",3,0.0))
    lista_cuentas.append(Cuenta(2, "Juan Perez", "juan@gmail.com",4,0.0))


    dep1 = Cajero(lista_cuentas,1, 200)
    dep1.Deposito()
    
    dep2 = Cajero(lista_cuentas, 3, 500)
    dep2.Deposito()

    ret1 = Cajero(lista_cuentas, 1, 200)
    ret1.Retiro()

    ret2 = Cajero(lista_cuentas, 2, 100)
    ret2.Retiro()

    dep1.Consultar()





if __name__ == "__main__":
    main()