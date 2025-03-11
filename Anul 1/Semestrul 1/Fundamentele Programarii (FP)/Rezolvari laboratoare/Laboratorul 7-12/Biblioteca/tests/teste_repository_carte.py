import unittest
from domain.carte import Carte
from repository.repository_carte import RepositoryCarti

class TestRepositoryCarti(unittest.TestCase):

    #black-box test
    def test_update_non_existing(self):
        """Test to update an existing book"""
        carte_inexistenta = Carte(1, "Titlu 99", "Descriere", "Autor")
        with self.assertRaises(ValueError):
            self.repo.update(carte_inexistenta)

    #white-box test
    def test_update_non_existing_whitebox(self):
        """Test to update an existing book"""
        # Verificăm inițial că lista internă este goală
        self.assertEqual(len(self.repo.get_all()), 0, "Repository-ul ar trebui să fie gol la început.")

        carte_inexistenta = Carte(1, "Titlu 99", "Descriere", "Autor")

        with self.assertRaises(ValueError) as context:
            self.repo.update(carte_inexistenta)

        self.assertEqual(
            str(context.exception),
            "Nu există carte cu id dat.",
            "Mesajul de eroare ar trebui să fie corect."
        )

        self.assertEqual(len(self.repo.get_all()), 0, "Repository-ul trebuie să rămână gol după încercarea de update.")

    def setUp(self):
        # Create a test-specific file
        self.test_filename = "test_carti.txt"
        # Creăm obiecte de tip Carte pentru teste
        self.carte1 = Carte(11, "Cartea 1", "Descrierea cartii 1", "Autor 1")
        self.carte2 = Carte(22, "Cartea 2", "Descrierea cartii 2", "Autor 2")
        self.carte3 = Carte(33, "Cartea 3", "Descrierea cartii 3", "Autor 3")
        self.repo = RepositoryCarti(self.test_filename)
        self.repo.clear_all()

    def tearDown(self):
        # Clean up after each test
        self.repo.clear_all()

    def test_store(self):
        # Testăm funcția store
        self.repo.store(self.carte1)
        self.repo.store(self.carte2)
        self.assertEqual(len(self.repo.get_all()), 2, "Repository-ul trebuie să conțină 2 cărți.")

    def test_store_with_duplicate_id(self):
        # Testăm funcția store cu ID duplicat (ar trebui să dea eroare)
        self.repo.store(self.carte1)
        with self.assertRaises(ValueError) as context:
            self.repo.store(self.carte1)
        self.assertEqual(str(context.exception), "Există deja o carte cu acest id.",
                         f"Eroare neașteptată: {str(context.exception)}")

    def test_find(self):
        # Testăm funcția find
        self.repo.store(self.carte1)
        found_carte = self.repo.find(11)
        self.assertEqual(found_carte, self.carte1, "Căutarea cărții cu ID 11 ar trebui să returneze cartea corectă.")

    # def test_find_non_existent(self):
    #     # Căutăm o carte inexistentă
    #     found_carte = self.repo.find(999)
    #     self.assertIsNone(found_carte, "Căutarea unei cărți inexistente ar trebui să returneze None.")

    def test_update(self):
        # Testăm funcția update
        self.repo.store(self.carte1)
        carte_actualizata = Carte(11, "Cartea 1 Actualizată", "Descrierea actualizată", "Autor 1")
        self.repo.update(carte_actualizata)
        found_carte = self.repo.find(11)
        self.assertEqual(found_carte.get_titlu(), "Cartea 1 Actualizată", "Cartea nu a fost actualizată corect.")

    def test_update_non_existent(self):
        # Testăm update cu ID inexistent
        carte_inexistentă = Carte(999, "Cartea Inexistentă", "Descriere", "Autor")
        with self.assertRaises(ValueError) as context:
            self.repo.update(carte_inexistentă)
        self.assertEqual(str(context.exception), "Nu există carte cu id dat.",
                         f"Eroare neașteptată: {str(context.exception)}")

    def test_delete(self):
        # Testăm funcția delete
        self.repo.store(self.carte1)
        self.repo.delete(11)
        self.assertEqual(len(self.repo.get_all()), 0, "Repository-ul trebuie să fie gol după ștergere.")

    def test_delete_non_existent(self):
        # Testăm delete cu ID inexistent
        with self.assertRaises(ValueError) as context:
            self.repo.delete(999)
        self.assertEqual(str(context.exception), "Nu există carte cu id dat.",
                         f"Eroare neașteptată: {str(context.exception)}")

    def test_get_size(self):
        # Testăm funcția get_size
        self.repo.store(self.carte1)
        self.assertEqual(self.repo.get_size(), 1, "Repository-ul ar trebui să conțină 1 carte.")

    def test_get_all(self):
        # Testăm funcția get_all
        self.repo.store(self.carte1)
        self.repo.store(self.carte2)
        carti = self.repo.get_all()
        self.assertEqual(len(carti), 2, "get_all ar trebui să returneze o listă cu 2 cărți.")
        self.assertEqual(carti[0], self.carte1, "Cărțile din repository nu sunt corecte.")
        self.assertEqual(carti[1], self.carte2, "Cărțile din repository nu sunt corecte.")