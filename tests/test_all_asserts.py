import unittest
import sys


class AllAssertsTest(unittest.TestCase):
    def test_assert(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no-soy-entero")

        with self.assertRaises(ZeroDivisionError):
            10 / 0

    def test_assert_in(self):
        self.assertIn(10, [3, 4, 6, 87, 10])
        self.assertNotIn(10, [3, 4, 6, 67, 7, 8])

    def test_assert_dicts(self):
        user = {"name": "Julio", "lugar": "Quito"}
        self.assertDictEqual({"name": "Julio", "lugar": "Quito"}, user)

    @unittest.skip("Aún en implementacion, por habilitar")
    def test_skip(self):
        self.assertEqual(10, 10)

    SERVER = "ServerB"

    @unittest.skipIf(SERVER == "ServerB", "Prueba saltada por que no hay servidor")
    def test_skip_if(self):
        self.assertEqual(20, 20)

    # Para casos en los cuales hay fallos conocidos, mientras se trabajan en la corrección
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)

    @unittest.skipUnless(
        sys.platform.startswith("win"), "Se requiere plataforma windows"
    )
    def test_skip_unless(self):
        self.assertEqual(10, 10)
