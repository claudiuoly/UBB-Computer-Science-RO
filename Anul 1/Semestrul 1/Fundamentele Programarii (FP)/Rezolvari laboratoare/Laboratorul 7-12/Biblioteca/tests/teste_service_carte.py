import unittest
from domain.validare_carte import ValidatorCarte
from repository.repository_carte import RepositoryCarti
from service.controller_carte import ControllerCarti

class TestControllerCarti(unittest.TestCase):
    def setUp(self):
        self.test_repo = RepositoryCarti("test_carti.txt")
        self.test_repo.clear_all()
        self.test_val = ValidatorCarte()
        self.test_ctrl = ControllerCarti(self.test_repo, self.test_val)

    def tearDown(self):
        self.test_repo.clear_all()

    def test_adauga_carte(self):
        self.assertEqual(len(self.test_ctrl.get_all()), 0)

        self.test_ctrl.adauga_carte(1, "Mândrie și prejudecată", "Roman clasic englez", "Jane Austen")
        self.assertEqual(len(self.test_ctrl.get_all()), 1)

        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_carte(1, "1984", "Roman distopic", "George Orwell")

        with self.assertRaises(ValueError):
            self.test_ctrl.adauga_carte(2, "", "", "George Orwell")

    def test_actualizeaza_carte(self):
        self.assertEqual(len(self.test_ctrl.get_all()), 0)

        self.test_ctrl.adauga_carte(1, "Ion", "Roman social", "Liviu Rebreanu")
        self.test_ctrl.adauga_carte(2, "La Medeleni", "Roman de formare", "Ionel Teodoreanu")
        self.assertEqual(len(self.test_ctrl.get_all()), 2)

        self.test_ctrl.actualizeaza_carte(1, "Ion - Editie Speciala", "Roman social cu note de critica", "Liviu Rebreanu")
        updated_book = self.test_ctrl.find_carte(1)
        self.assertEqual(updated_book.get_titlu(), "Ion - Editie Speciala")
        self.assertEqual(updated_book.get_descriere(), "Roman social cu note de critica")

        with self.assertRaises(ValueError):
            self.test_ctrl.actualizeaza_carte(3, "Cartea necitita", "Despre ceva necunoscut", "Necunoscut")

        with self.assertRaises(ValueError):
            self.test_ctrl.actualizeaza_carte(2, "", "", "")

    def test_delete_carte(self):
        self.assertEqual(len(self.test_ctrl.get_all()), 0)

        self.test_ctrl.adauga_carte(1, "Mândrie și prejudecată", "Roman clasic englez", "Jane Austen")
        self.test_ctrl.adauga_carte(2, "1984", "Roman distopic", "George Orwell")
        self.assertEqual(len(self.test_ctrl.get_all()), 2)

        self.test_ctrl.delete_carte(1)
        self.assertEqual(len(self.test_ctrl.get_all()), 1)

        with self.assertRaises(ValueError):
            self.test_ctrl.delete_carte(5)

    def test_add_default(self):
        self.test_ctrl.add_default()
        self.assertEqual(len(self.test_ctrl.get_all()), 4)

        all_books = self.test_ctrl.get_all()
        titluri = [carte.get_titlu() for carte in all_books]
        self.assertIn("Mândrie și prejudecată", titluri)
        self.assertIn("1984", titluri)
        self.assertIn("La Medeleni", titluri)
        self.assertIn("Ion", titluri)

if __name__ == '__main__':
    unittest.main()
