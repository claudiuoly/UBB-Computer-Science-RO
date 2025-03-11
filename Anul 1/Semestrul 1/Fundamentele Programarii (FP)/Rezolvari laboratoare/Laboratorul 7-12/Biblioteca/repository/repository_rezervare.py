from domain.rezervare import Rezervare


class RepositoryRezervari:
    def __init__(self, filename="rezervari.txt", repo_clienti=None, repo_carti=None):
        self.__elements = []
        self.__filename = filename
        self.__repo_clienti = repo_clienti
        self.__repo_carti = repo_carti
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(",")
                    id_rezervare = int(parts[0])
                    id_client = int(parts[1])
                    id_carte = int(parts[2])
                    data_inchiriere = parts[3]
                    data_returnare = parts[4] if len(parts) > 4 else None

                    client = self.__repo_clienti.find(id_client)
                    carte = self.__repo_carti.find(id_carte)

                    if client and carte:
                        rezervare = Rezervare(id_rezervare, client, carte, data_inchiriere, data_returnare)
                        self.__elements.append(rezervare)
        except FileNotFoundError:
            print(f"Fisierul {self.__filename} nu a fost gasit. Se va crea un fisier nou.")

    def __save_to_file(self):
        with open(self.__filename, "w") as f:
            for rezervare in self.__elements:
                f.write(f"{rezervare.get_id()},{rezervare.get_book_id()},{rezervare.get_client_id()}\n")

    def find(self, id: int) -> Rezervare:
        """
        Căutăm rezervarea cu id-ul dat
        :param id: id-ul căutat
        :return: obiect de tip Rezervare dacă există rezervare cu id dat, None altfel
        """
        for rezervare in self.__elements:
            if rezervare.get_id() == id:
                return rezervare
        return None

    def store(self, rezervare: Rezervare):
        """
        Adaugă o rezervare la colecția de rezervări
        :param rezervare: rezervarea de adăugat
        :return: -; colecția de rezervări se modifică prin adăugarea rezervării
                postcondiție: rezervarea apartine colecției de rezervări
        :raises: ValueError dacă se încearcă adăugarea unei rezervări cu id care există deja
        """
        if self.find(rezervare.get_id()) is not None:
            raise ValueError("Există deja o rezervare cu acest id.")
        self.__elements.append(rezervare)
        self.__save_to_file()

    def __find_pos(self, id: int):
        """
        Găsește poziția în lista a rezervării cu id dat (dacă o astfel de rezervare există)
        :param id: id-ul căutat
        :return: poziția în lista a rezervării cu id dat, pos returnat între 0 și len(self.__elements) dacă rezervarea există
                -1 dacă nu există rezervare cu id dat
        """
        pos = -1
        for index, rezervare in enumerate(self.__elements):
            if rezervare.get_id() == id:
                pos = index
                break
        return pos

    def update(self, rezervare_actualizata: Rezervare):
        """
        Actualizează rezervarea din listă cu ID-ul rezervării date ca parametru
        :param rezervare_actualizata: rezervarea actualizată
        :return:
        """
        pos = self.__find_pos(rezervare_actualizata.get_id())
        if pos == -1:
            raise ValueError("Nu există rezervare cu id dat.")
        self.__elements[pos] = rezervare_actualizata
        self.__save_to_file()

    def delete(self, id: int):
        """
        Șterge rezervarea cu id-ul dat
        :param id: id-ul rezervării de șters
        :return: -
        """
        pos = self.__find_pos(id)
        if pos == -1:
            raise ValueError("Nu există rezervare cu id dat.")
        del self.__elements[pos]
        self.__save_to_file()

    def get_all(self) -> list:
        """
        Returnează colecția de rezervări
        :return: colecția de rezervări
        """
        return self.__elements

    def get_size(self) -> int:
        """
        Returnează numărul de rezervări din colecție
        :return: numărul de rezervări
        """
        return len(self.__elements)