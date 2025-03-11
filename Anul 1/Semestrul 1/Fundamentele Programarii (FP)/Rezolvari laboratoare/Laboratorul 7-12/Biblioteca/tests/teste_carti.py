import unittest
from domain.carte import Carte
from domain.validare_carte import ValidatorCarte

class TestCarte(unittest.TestCase):
    def setUp(self):
        self.carte1 = Carte(1, "Titlu Carte", "Descrierea cărții", "Autor 1")
        self.validator = ValidatorCarte()

    def test_getters_and_setters(self):
        self.assertEqual(self.carte1.get_titlu(), "Titlu Carte")
        self.assertEqual(self.carte1.get_autor(), "Autor 1")
        self.assertEqual(self.carte1.get_descriere(), "Descrierea cărții")

        self.carte1.set_descriere("Noua descriere a cărții")
        self.assertEqual(self.carte1.get_descriere(), "Noua descriere a cărții")

        self.carte1.set_autor("Autor 2")
        self.assertEqual(self.carte1.get_autor(), "Autor 2")

        self.carte1.titlu = "Nou Titlu"
        self.assertEqual(self.carte1.get_titlu(), "Nou Titlu")

    def test_equality(self):
        carte2 = Carte(1, "Alt Titlu", "Altă descriere", "Alt Autor")
        self.assertEqual(self.carte1, carte2)

        carte3 = Carte(2, "Titlu diferit", "Descrierea cărții", "Autor 1")
        self.assertNotEqual(self.carte1, carte3)

    def test_validare_titlu_scurt(self):
        carte_invalida = Carte(1, "T", "Descriere validă", "Autor valid")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte_invalida)
        self.assertIn("Titlul cărții trebuie să aibă cel puțin 2 caractere.", str(context.exception))

    def test_validare_descriere_scurta(self):
        carte_invalida = Carte(2, "Titlu valid", "Scurt", "Autor valid")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte_invalida)
        self.assertIn("Descrierea cărții trebuie să aibă cel puțin 10 caractere.", str(context.exception))

    def test_validare_autor_scurt(self):
        carte_invalida = Carte(3, "Titlu valid", "Descriere validă", "Au")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte_invalida)
        self.assertIn("Numele autorului trebuie să aibă cel puțin 3 caractere.", str(context.exception))

    def test_validare_id_invalid(self):
        carte_invalida = Carte(-1, "Titlu valid", "Descriere validă", "Autor valid")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(carte_invalida)
        self.assertIn("ID-ul cărții trebuie să fie un număr pozitiv.", str(context.exception))

    def test_validare_carte_valida(self):
        carte_valida = Carte(5, "Titlu valid", "Descriere validă", "Autor valid")
        try:
            self.validator.validate(carte_valida)
        except ValueError:
            self.fail("Nu ar trebui să fie o eroare pentru carte validă")

if __name__ == '__main__':
    unittest.main()
