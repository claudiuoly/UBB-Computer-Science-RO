import unittest
from domain.carte import Carte
from domain.client import Client
from domain.validare_rezervare import ValidatorRezervare
from repository.repository_carte import RepositoryCarti
from repository.repository_client import RepositoryClienti
from repository.repository_rezervare import RepositoryRezervari
from service.controller_rezervare import ControllerRezervari
import os


class TestServiceRezervare(unittest.TestCase):
    def setUp(self):
        # Path to test files
        self.test_file_rezervari = "test_rezervari.txt"
        self.test_file_clienti = "test_clienti.txt"
        self.test_file_carti = "test_carti.txt"

        # Clear contents of test files
        open(self.test_file_rezervari, 'w').close()
        open(self.test_file_clienti, 'w').close()
        open(self.test_file_carti, 'w').close()

        # Initialize repositories with empty test files
        self.test_repo_rezervari = RepositoryRezervari(self.test_file_rezervari)
        self.test_repo_clienti = RepositoryClienti(self.test_file_clienti)
        self.test_repo_carti = RepositoryCarti(self.test_file_carti)

        self.test_validator = ValidatorRezervare()
        self.test_ctrl = ControllerRezervari(
            self.test_repo_rezervari,
            self.test_repo_clienti,
            self.test_repo_carti,
            self.test_validator
        )

    def tearDown(self):
        os.remove(self.test_file_rezervari)
        os.remove(self.test_file_clienti)
        os.remove(self.test_file_carti)

    def test_adauga_rezervare(self):
        # Setup test data
        self.test_repo_clienti.store(Client(1, "Ion Popescu", "1234567890123"))
        self.test_repo_clienti.store(Client(2, "Maria Ionescu", "9876543210123"))
        self.test_repo_carti.store(Carte(1, "Cartea 1", "Descrierea cartii 1", "Autor 1"))
        self.test_repo_carti.store(Carte(2, "Cartea 2", "Descrierea cartii 2", "Autor 2"))

        self.assertEqual(len(self.test_ctrl.get_all_rezervari()), 0)

        # Test valid reservation
        self.test_ctrl.adauga_rezervare(101, 1, 1, "2024-11-21")
        self.assertEqual(len(self.test_ctrl.get_all_rezervari()), 1)

        # Test duplicate ID
        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_rezervare(101, 2, 2, "2024-11-21")

        # Test non-existent client
        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_rezervare(102, 3, 1, "2024-11-21")

        # Test non-existent book
        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_rezervare(103, 1, 3, "2024-11-21")

    def test_returneaza_carte(self):
        self.test_repo_clienti.store(Client(1, "Ion Popescu", "1234567890123"))
        self.test_repo_carti.store(Carte(1, "Cartea 1", "Descrierea cartii 1", "Autor 1"))

        self.test_ctrl.adauga_rezervare(101, 1, 1, "2024-11-21")
        self.assertEqual(len(self.test_ctrl.get_all_rezervari()), 1)

        self.test_ctrl.returneaza_carte(101)
        self.assertEqual(len(self.test_ctrl.get_all_rezervari()), 0)

        with self.assertRaises(ValueError):
            self.test_ctrl.returneaza_carte(102)

    def test_get_most_rented_books(self):
        client = Client(1, "Test Client", "1234567890123")
        carte1 = Carte(1, "Carte 1", "Descriere 1", "Autor 1")
        carte2 = Carte(2, "Carte 2", "Descriere 2", "Autor 2")

        self.test_repo_clienti.store(client)
        self.test_repo_carti.store(carte1)
        self.test_repo_carti.store(carte2)

        self.test_ctrl.adauga_rezervare(1, 1, 1, "2024-01-01")
        self.test_ctrl.adauga_rezervare(2, 1, 1, "2024-01-02")
        self.test_ctrl.adauga_rezervare(3, 1, 2, "2024-01-03")

        rezultate = self.test_ctrl.get_most_rented_books()
        self.assertEqual(len(rezultate), 2)
        self.assertEqual(rezultate[0][0], carte1)
        self.assertEqual(rezultate[0][1], 2)
        self.assertEqual(rezultate[1][0], carte2)
        self.assertEqual(rezultate[1][1], 1)

    def test_get_top_active_clients(self):
        client1 = Client(1, "Client 1", "1234567890123")
        client2 = Client(2, "Client 2", "2345678901234")
        client3 = Client(3, "Client 3", "3456789012345")
        carte = Carte(1, "Test Carte", "Descriere", "Autor")

        for client in [client1, client2, client3]:
            self.test_repo_clienti.store(client)
        self.test_repo_carti.store(carte)

        # Add reservations
        for i in range(3):
            self.test_ctrl.adauga_rezervare(i + 1, 1, 1, f"2024-01-0{i + 1}")
        for i in range(2):
            self.test_ctrl.adauga_rezervare(i + 4, 2, 1, f"2024-01-0{i + 4}")
        self.test_ctrl.adauga_rezervare(6, 3, 1, "2024-01-06")

        rezultate = self.test_ctrl.get_top_active_clients()
        self.assertEqual(len(rezultate), 1)
        self.assertEqual(rezultate[0][0], client1)
        self.assertEqual(rezultate[0][1], 3)


if __name__ == '__main__':
    unittest.main()
