import unittest
from datetime import datetime
from domain.rezervare import Rezervare
from domain.client import Client
from domain.carte import Carte
from domain.validare_rezervare import ValidatorRezervare

class TestRezervare(unittest.TestCase):
    def setUp(self):
        self.client1 = Client(1, "Ion Popescu", "1234567890123")
        self.carte1 = Carte(1, "Cartea 1", "Descrierea cartii 1", "Autor 1")
        self.validator = ValidatorRezervare()

    def test_getters_and_setters(self):
        rezervare1 = Rezervare(1, self.client1, self.carte1, "2024-11-01")
        self.assertEqual(rezervare1.get_id(), 1)
        self.assertEqual(rezervare1.get_client_id(), 1)
        self.assertEqual(rezervare1.get_book_id(), 1)
        self.assertEqual(rezervare1.get_data_inchiriere(),
                        datetime.strptime("2024-11-01", "%Y-%m-%d"))
        self.assertIsNone(rezervare1.get_data_returnare())

        rezervare1.set_data_returnare("2024-11-10")
        self.assertEqual(rezervare1.get_data_returnare(),
                        datetime.strptime("2024-11-10", "%Y-%m-%d"))

    def test_rezervare_with_return_date(self):
        rezervare2 = Rezervare(2, self.client1, self.carte1, "2024-11-01", "2024-11-05")
        self.assertEqual(rezervare2.get_data_returnare(),
                        datetime.strptime("2024-11-05", "%Y-%m-%d"))

    def test_equality(self):
        rezervare1 = Rezervare(1, self.client1, self.carte1, "2024-11-01")
        rezervare3 = Rezervare(1, self.client1, self.carte1, "2024-11-01")
        rezervare4 = Rezervare(3, self.client1, self.carte1, "2024-11-01")

        self.assertEqual(rezervare1, rezervare3)  # Should be equal based on ID
        self.assertNotEqual(rezervare1, rezervare4)  # Should be different

    def test_validare_id_invalid(self):
        rezervare1 = Rezervare(-1, self.client1, self.carte1, "2024-11-01")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(rezervare1)
        self.assertIn("ID-ul rezervării trebuie să fie un număr pozitiv.",
                     str(context.exception))

    def test_validare_data_returnare_invalida(self):
        rezervare3 = Rezervare(3, self.client1, self.carte1, "2024-11-10", "2024-11-01")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(rezervare3)
        self.assertIn("Data returnării nu poate fi anterioară datei închirierii.",
                     str(context.exception))

    def test_validare_rezervare_valida(self):
        rezervare4 = Rezervare(4, self.client1, self.carte1, "2024-11-01", "2024-11-10")
        try:
            self.validator.validate(rezervare4)
        except ValueError:
            self.fail("Nu ar trebui să fie o eroare pentru rezervare validă")

if __name__ == '__main__':
    unittest.main()
