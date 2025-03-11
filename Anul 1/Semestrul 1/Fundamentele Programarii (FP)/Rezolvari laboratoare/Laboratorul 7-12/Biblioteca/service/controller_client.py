from domain.client import Client
from domain.validare_client import ValidatorClient
from repository.repository_client import RepositoryClienti


class ControllerClienti:
    def __init__(self, repo: RepositoryClienti, validator: ValidatorClient):
        self.__repo = repo
        self.__validator = validator

    def adauga_client(self, id, nume, cnp):
        """
        Adaugă un client
        :param id: id-ul clientului de adăugat
        :param nume: numele clientului pe care vrem să-l adăugăm
        :param cnp: CNP-ul clientului
        :return: -; lista de clienți se modifică prin adăugarea clientului cu informațiile date
        :raises: ValueError dacă clientul nu este valid
                 ValueError dacă există deja un client cu id-ul dat
        """
        client = Client(id, nume, cnp)
        self.__validator.validate(client)
        self.__repo.store(client)

    def actualizeaza_client(self, id: int, nume_nou: str, cnp_nou: str):
        """
        Actualizează clientul cu id-ul dat cu informațiile noi
        :param id: id-ul clientului de actualizat
        :param nume_nou: noul nume al clientului
        :param cnp_nou: noul CNP al clientului
        :return: -; lista de clienți se modifică prin actualizarea clientului cu id-ul dat
        :raises: ValueError dacă din informațiile date nu se poate construi un client valid
                 ValueError dacă nu există un client cu id-ul dat
        """
        client_nou = Client(id, nume_nou, cnp_nou)
        self.__validator.validate(client_nou)
        self.__repo.update(client_nou)

    def find_client(self, id: int):
        """
        Căutăm clientul cu id-ul dat
        :param id: id-ul după care se caută
        :return: clientul cu id-ul dat, dacă acesta există, None altfel
        """
        return self.__repo.find(id)

    def delete_client(self, id: int):
        """
        Șterge un client după id
        :param id: id-ul clientului de șters
        :return: -
        :raises: ValueError dacă nu există un client cu id-ul dat
        """
        self.__repo.delete(id)

    def get_all(self) -> list:
        """
        Returnează toți clienții
        :return: lista de clienți
        """
        return self.__repo.get_all()

    def add_default(self):
        """
        Adaugă câțiva clienți implicați în colecție
        """
        self.adauga_client(1, "Ion Popescu", "1234567890123")
        self.adauga_client(2, "Maria Ionescu", "9876543210123")
        self.adauga_client(3, "Alexandru Georgescu", "1234987654321")
        self.adauga_client(4, "Elena Stan", "3456789012345")
