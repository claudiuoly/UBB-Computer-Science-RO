from domain.rezervare import Rezervare
from domain.validare_rezervare import ValidatorRezervare
from repository.repository_carte import RepositoryCarti
from repository.repository_client import RepositoryClienti
from repository.repository_rezervare import RepositoryRezervari


class ControllerRezervari:
    def __init__(self, repo_rezervari: RepositoryRezervari, repo_clienti: RepositoryClienti,
                 repo_carti: RepositoryCarti, validator: ValidatorRezervare):
        self.__repo_rezervari = repo_rezervari
        self.__repo_clienti = repo_clienti
        self.__repo_carti = repo_carti
        self.__validator = validator

    def adauga_rezervare(self, id_rezervare: int, id_client: int, id_carte: int, data_inchiriere: str):
        """
        Adaugă o rezervare
        :param id_rezervare: id-ul rezervării de adăugat
        :param id_client: id-ul clientului care face rezervarea
        :param id_carte: id-ul cărții rezervate
        :param data_inchiriere: data închirierii în format 'YYYY-MM-DD HH:MM:SS'
        :return: -; lista de rezervări se modifică prin adăugarea rezervării cu informațiile date
        :raises: ValueError dacă clientul sau cartea nu sunt valide
                 ValueError dacă rezervarea cu id-ul dat există deja
        """
        client = self.__repo_clienti.find(id_client)
        carte = self.__repo_carti.find(id_carte)

        if client is None:
            raise ValueError(f"Nu există client cu id {id_client}.")
        if carte is None:
            raise ValueError(f"Nu există carte cu id {id_carte}.")

        rezervare = Rezervare(id_rezervare, client, carte, data_inchiriere)
        self.__validator.validate(rezervare)
        self.__repo_rezervari.store(rezervare)

    def returneaza_carte(self, id_rezervare: int):
        """
        Returnează o carte bazată pe rezervare
        :param id_rezervare: id-ul rezervării de returnat
        :return: -; rezervarea este eliminată din repository
        :raises: ValueError dacă rezervarea nu există
        """
        rezervare = self.__repo_rezervari.find(id_rezervare)
        if rezervare is None:
            raise ValueError(f"Nu există rezervare cu id {id_rezervare}.")

        self.__repo_rezervari.delete(id_rezervare)

    def get_all_rezervari(self) -> list:
        """
        Returnează toate rezervările
        :return: lista de rezervări
        """
        return self.__repo_rezervari.get_all()

    def adauga_default(self):
        """
        Adaugă câteva rezervări implicite
        """
        # Presupunem că avem deja clienți și cărți în repository
        client = self.__repo_clienti.find(1)
        carte = self.__repo_carti.find(1)
        if client and carte:
            self.adauga_rezervare(101, 1, 1)

        client = self.__repo_clienti.find(2)
        carte = self.__repo_carti.find(2)
        if client and carte:
            self.adauga_rezervare(102, 2, 2)

        client = self.__repo_clienti.find(3)
        carte = self.__repo_carti.find(3)
        if client and carte:
            self.adauga_rezervare(103, 3, 3)

    def get_rezervari_client(self, id_client: int) -> list:
        """
        Returnează toate rezervările unui client
        :param id_client: id-ul clientului
        :return: lista de rezervări ale clientului
        """
        rezervari_client = [rezervare for rezervare in self.__repo_rezervari.get_all() if
                            rezervare.get_client().get_id() == id_client]
        return rezervari_client

    def delete_rezervare(self, id_rezervare: int):
        """
        Șterge o rezervare cu ID-ul specificat.
        """
        rezervare = self.__repo_rezervari.find(id_rezervare)
        if rezervare is None:
            raise ValueError(f"Nu există nicio rezervare cu ID-ul {id_rezervare}.")
        self.__repo_rezervari.delete(id_rezervare)

    def get_most_rented_books(self):
        """
        Returnează lista de cărți ordonate după numărul de închirieri.
        :return: listă de tupluri (carte, număr_închirieri)
        """
        book_rentals = {}
        for rezervare in self.__repo_rezervari.get_all():
            carte = rezervare.get_carte()
            book_rentals[carte] = book_rentals.get(carte, 0) + 1

        return sorted(book_rentals.items(), key=lambda x: x[1], reverse=True)

    def get_clients_sorted_by_name(self):
        """
        Returnează lista de clienți cu numărul lor de închirieri, ordonați alfabetic după nume.
        :return: listă de tupluri (client, număr_închirieri)
        """
        client_rentals = {}
        for rezervare in self.__repo_rezervari.get_all():
            client = rezervare.get_client()
            client_rentals[client] = client_rentals.get(client, 0) + 1

        return sorted(client_rentals.items(), key=lambda x: x[0].get_nume())

    def get_top_active_clients(self):
        """
        Returnează top 20% din cei mai activi clienți
        :return: listă de tupluri (client, număr_închirieri)
        """
        client_rentals = {}
        for rezervare in self.__repo_rezervari.get_all():
            client = rezervare.get_client()
            client_rentals[client] = client_rentals.get(client, 0) + 1

        sorted_clients = sorted(client_rentals.items(), key=lambda x: x[1], reverse=True)
        top_count = max(1, int(len(sorted_clients) * 0.2))  # Minimum 1 client
        return sorted_clients[:top_count]
