from domain.client import Client

class RepositoryClienti:
    def __init__(self, filename="clienti.txt"):
        self.__elements = []
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():
                        id, nume, cnp = line.strip().split(",")
                        client = Client(int(id), nume, cnp)
                        self.__elements.append(client)
        except FileNotFoundError:
            pass

    def __save_to_file(self):
        with open(self.__filename, "w") as f:
            for client in self.__elements:
                f.write(f"{client.get_id()},{client.get_nume()},{client.get_cnp()}\n")

    # Cazul cel mai optim O(1)
    # Cazul cel mai rau O(n)
    # Cazul mediu O(n) (In medie vor fi necesara (n/2) comparatii => O(n))
    def find(self, id: int):
        """
        Caută un client după ID
        :param id: id-ul clientului căutat
        :return: clientul găsit sau None dacă nu există
        """
        for client in self.__elements:
            if client.get_id() == id:
                return client
        return None

    def store(self, client):
        """
        Adaugă un client în repository
        :param client: clientul de adăugat
        :raises: ValueError dacă există deja un client cu același id
        """
        if self.find(client.get_id()) is not None:
            raise ValueError("Există deja un client cu acest id.")
        self.__elements.append(client)
        self.__save_to_file()

    def update(self, client):
        """
        Actualizează un client
        :param client: clientul cu datele noi
        :raises: ValueError dacă nu există clientul cu id-ul dat
        """
        pos = self.__find_pos(client.get_id())
        if pos == -1:
            raise ValueError("Nu există client cu id dat.")
        self.__elements[pos] = client
        self.__save_to_file()

    def delete(self, id: int):
        """
        Șterge un client după ID
        :param id: id-ul clientului de șters
        :raises: ValueError dacă nu există client cu id-ul dat
        """
        pos = self.__find_pos(id)
        if pos == -1:
            raise ValueError("Nu există client cu id dat.")
        self.__elements.pop(pos)
        self.__save_to_file()

    def get_all(self):
        """
        :return: lista cu toți clienții
        """
        return self.__elements.copy()

    def get_size(self):
        """
        :return: numărul de clienți din repository
        """
        return len(self.__elements)

    def __find_pos(self, id: int):
        """
        Găsește poziția unui client în lista de elemente
        :param id: id-ul clientului căutat
        :return: poziția clientului sau -1 dacă nu există
        """
        for i in range(len(self.__elements)):
            if self.__elements[i].get_id() == id:
                return i
        return -1

    def clear_all(self):
        """Șterge toți clienții din repository și din fișier"""
        self.__elements = []
        with open(self.__filename, "w") as f:
            f.write("")