# colisiones/test_colisiones.py
import unittest
from colisiones import conteo_colisiones

class TestConteoColisiones(unittest.TestCase):

    def test_basico(self):
        self.assertEqual(conteo_colisiones("RLRRLL"), 3)

    def test_sin_colisiones(self):
        self.assertEqual(conteo_colisiones("RRLL"), 0)

    def test_todos_izquierda(self):
        self.assertEqual(conteo_colisiones("LLLLL"), 0)

    def test_todos_derecha(self):
        self.assertEqual(conteo_colisiones("RRRRR"), 0)

    def test_alternados(self):
        self.assertEqual(conteo_colisiones("RLRLRLRLRL"), 5)

if __name__ == "__main__":
    unittest.main()
