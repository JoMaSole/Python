#condicionales
#hay que testear todas y cada una de las condiciones
#caja de crista

import unittest

def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class CristalTest(unittest.TestCase):
    
    def test_mayor(self):
        edad = 20

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_menor(self):
        edad = 15

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado,True)


if __name__ == '__main__':
    unittest.main()