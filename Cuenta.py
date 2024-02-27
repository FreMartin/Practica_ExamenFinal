from Persona import Persona


class Cuenta(Persona):
    def __init__(self, id: int, nombre: str, correo: str, numero_cuenta: int, saldo: float) -> None:

        super().__init__(id, nombre, correo)
        self.numero_cuenta= numero_cuenta
        self.saldo= saldo
