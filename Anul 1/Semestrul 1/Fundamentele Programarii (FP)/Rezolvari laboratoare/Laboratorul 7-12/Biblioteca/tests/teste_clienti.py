import unittest
from domain.client import Client
from domain.validare_client import ValidatorClient

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client1 = Client(1, "Ion Popescu", "1234567890123")
        self.validator = ValidatorClient()

    def test_getters_and_setters(self):
        self.assertEqual(self.client1.get_nume(), "Ion Popescu")
        self.assertEqual(self.client1.get_cnp(), "1234567890123")

        self.client1.set_cnp("2345678901234")
        self.assertEqual(self.client1.get_cnp(), "2345678901234")

        self.client1.nume = "Maria Ionescu"
        self.assertEqual(self.client1.get_nume(), "Maria Ionescu")

    def test_equality(self):
        client2 = Client(1, "Alt Nume", "1234567890123")
        self.assertEqual(self.client1, client2)

        client3 = Client(2, "Nume Diferit", "2345678901234")
        self.assertNotEqual(self.client1, client3)

    def test_validare_nume_scurt(self):
        client_invalid = Client(1, "Io", "1234567890123")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(client_invalid)
        self.assertIn("Numele clientului trebuie să aibă cel puțin 3 caractere.", str(context.exception))

    def test_validare_cnp_scurt(self):
        client_invalid = Client(2, "Ion Popescu", "12345678")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(client_invalid)
        self.assertIn("CNP-ul clientului trebuie să fie un număr de 13 caractere.", str(context.exception))

    def test_validare_cnp_non_numeric(self):
        client_invalid = Client(3, "Maria Ionescu", "abcdefghijklm")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(client_invalid)
        self.assertIn("CNP-ul clientului trebuie să fie un număr de 13 caractere.", str(context.exception))

    def test_validare_id_invalid(self):
        client_invalid = Client(-1, "Ion Popescu", "1234567890123")
        with self.assertRaises(ValueError) as context:
            self.validator.validate(client_invalid)
        self.assertIn("ID-ul clientului trebuie să fie un număr pozitiv.", str(context.exception))

    def test_validare_client_valid(self):
        client_valid = Client(5, "Ion Popescu", "1234567890123")
        try:
            self.validator.validate(client_valid)
        except ValueError:
            self.fail("Nu ar trebui să fie o eroare pentru client valid")

if __name__ == '__main__':
    unittest.main()
