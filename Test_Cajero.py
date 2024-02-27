import unittest

from Cajero import Cajero

class TestCajeto(unittest.TestCase):

    def test_objeto_cajero (self):
        
        cuenta = [1, "Martín Farfán", "martin@gmail.com",1,0.0]
        numero_cuenta = 1
        valor = 100

        cajero1 = Cajero(cuenta, numero_cuenta, valor)

        self.assertEqual(cuenta, cajero1.cuenta, "No es la lista correcta")
        self.assertEqual(numero_cuenta, cajero1.numero_cuenta, "No es la cuenta correcta")
        self.assertEqual(valor, cajero1.valor, "No es el valor correcto")


if __name__ == "__main__":
    unittest.main()
