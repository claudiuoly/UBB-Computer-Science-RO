import unittest
from domain.client import Client
from domain.validare_client import ValidatorClient
from repository.repository_client import RepositoryClienti
from service.controller_client import ControllerClienti


class TestServiceClient(unittest.TestCase):
    def setUp(self):
        self.test_repo = RepositoryClienti("test_clienti.txt")
        self.test_repo.clear_all()
        self.test_val = ValidatorClient()
        self.test_ctrl = ControllerClienti(self.test_repo, self.test_val)

    def tearDown(self):
        self.test_repo.clear_all()

    def test_adauga_client(self):
        self.assertEqual(len(self.test_ctrl.get_all()), 0)

        self.test_ctrl.adauga_client(1, "Ion Popescu", "1234567890123")
        self.assertEqual(len(self.test_ctrl.get_all()), 1)

        # Test duplicate ID
        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_client(1, "Maria Ionescu", "9876543210123")

        # Test empty name
        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_client(2, "", "9876543210123")

        # Test invalid CNP
        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_client(3, "Alexandru Georgescu", "12345")

    def test_actualizeaza_client(self):
        self.assertEqual(len(self.test_ctrl.get_all()), 0)

        self.test_ctrl.adauga_client(1, "Ion Popescu", "1234567890123")
        self.test_ctrl.adauga_client(2, "Maria Ionescu", "9876543210123")
        self.assertEqual(len(self.test_ctrl.get_all()), 2)

        self.test_ctrl.actualizeaza_client(1, "Ion Popescu Actualizat", "1234567890987")
        updated_client = self.test_ctrl.find_client(1)
        self.assertEqual(updated_client.get_nume(), "Ion Popescu Actualizat")
        self.assertEqual(updated_client.get_cnp(), "1234567890987")

        # Test non-existent client
        with self.assertRaises(ValueError):
            self.test_ctrl.actualizeaza_client(3, "Elena Stan", "3456789012345")

        # Test empty name
        with self.assertRaises(ValueError):
            self.test_ctrl.actualizeaza_client(2, "", "9876543210123")

    def test_delete_client(self):
        self.assertEqual(len(self.test_ctrl.get_all()), 0)

        self.test_ctrl.adauga_client(1, "Ion Popescu", "1234567890123")
        self.test_ctrl.adauga_client(2, "Maria Ionescu", "9876543210123")
        self.assertEqual(len(self.test_ctrl.get_all()), 2)

        self.test_ctrl.delete_client(1)
        self.assertEqual(len(self.test_ctrl.get_all()), 1)

        # Test deleting non-existent client
        with self.assertRaises(ValueError):
            self.test_ctrl.delete_client(3)

    def test_add_default(self):
        self.test_ctrl.add_default()
        self.assertEqual(len(self.test_ctrl.get_all()), 4)

        all_clients = self.test_ctrl.get_all()
        nume_clienti = [client.get_nume() for client in all_clients]

        self.assertIn("Ion Popescu", nume_clienti)
        self.assertIn("Maria Ionescu", nume_clienti)
        self.assertIn("Alexandru Georgescu", nume_clienti)
        self.assertIn("Elena Stan", nume_clienti)


if __name__ == '__main__':
    unittest.main()