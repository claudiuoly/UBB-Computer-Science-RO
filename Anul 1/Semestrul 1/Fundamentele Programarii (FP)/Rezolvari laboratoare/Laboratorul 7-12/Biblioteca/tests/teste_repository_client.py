import unittest
from domain.client import Client
from repository.repository_client import RepositoryClienti

class TestRepositoryClienti(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_clienti.txt"
        self.repo = RepositoryClienti(self.test_filename)
        self.repo.clear_all()
        self.client1 = Client(1, "Client 1", "1234567890123")
        self.client2 = Client(2, "Client 2", "2345678901234")
        self.client3 = Client(3, "Client 3", "3456789012345")

    def tearDown(self):
        self.repo.clear_all()

    def test_find(self):
        self.repo.store(self.client1)
        found_client = self.repo.find(1)
        self.assertEqual(found_client, self.client1)

        found_client = self.repo.find(999)
        self.assertIsNone(found_client)

    def test_update_inexistent(self):
        client_inexistent = Client(999, "Client Inexistent", "1234567890123")
        with self.assertRaises(ValueError) as context:
            self.repo.update(client_inexistent)
        self.assertEqual(str(context.exception), "Nu există client cu id dat.")

    def test_delete(self):
        self.repo.store(self.client1)
        self.repo.store(self.client2)
        self.repo.delete(1)
        self.assertEqual(len(self.repo.get_all()), 1)

    def test_delete_inexistent(self):
        with self.assertRaises(ValueError) as context:
            self.repo.delete(999)
        self.assertEqual(str(context.exception), "Nu există client cu id dat.")

if __name__ == '__main__':
    unittest.main()
