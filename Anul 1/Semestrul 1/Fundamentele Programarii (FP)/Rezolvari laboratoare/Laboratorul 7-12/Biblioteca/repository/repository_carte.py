from domain.carte import Carte

class RepositoryCarti:
    def __init__(self, filename="carti.txt"):
        self.__elements = []
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                for line in lines:

                    if line.strip():
                        id, titlu, descriere, autor = line.strip().split(",")
                        carte = Carte(int(id), titlu, descriere, autor)
                        self.__elements.append(carte)
        except FileNotFoundError:
            print(f"Fisierul {self.__filename} nu a fost gasit. Se va crea un fisier nou.")

    def __save_to_file(self):
        with open(self.__filename, "w") as f:
            for carte in self.__elements:
                f.write(f"{carte.get_id()},{carte.get_titlu()},{carte.get_descriere()},{carte.get_autor()}\n")

    # Cazul cel mai optim O(1)
    # Cazul cel mai rau O(n)
    # Cazul mediu O(n) (In medie vor fi necesara (n/2) comparatii => O(n))
    def find(self, id: int) -> Carte:
        """
        Cauta o carte cu id-ul dat.
        :param id: id-ul cartii de cautat
        :return: cartea cu id-ul dat, sau None daca nu exista
        """
        for carte in self.__elements:
            if carte.get_id() == id:
                return carte
        return None

    def store(self, carte):
        """
        Adaugă o carte în repository
        :param carte: cartea de adăugat
        :raises: ValueError dacă există deja o carte cu același id
        """
        if self.find(carte.get_id()) is not None:
            raise ValueError("Există deja o carte cu acest id.")
        self.__elements.append(carte)
        self.__save_to_file()

    def update(self, carte_actualizata):
        """
        Actualizeaza o carte din repository.
        :param carte_actualizata: cartea actualizata
        :raises ValueError: daca nu exista o carte cu id-ul dat
        """
        pos = self.__find_pos(carte_actualizata.get_id())
        if pos == -1:
            raise ValueError("Nu există carte cu id dat.")
        self.__elements[pos] = carte_actualizata
        self.__save_to_file()

    def delete(self, id: int):
        """
        Șterge o carte după ID
        :param id: id-ul cărții de șters
        :raises: ValueError dacă nu există carte cu id-ul dat
        """
        pos = self.__find_pos(id)
        if pos == -1:
            raise ValueError("Nu există carte cu id dat.")
        self.__elements.pop(pos)
        self.__save_to_file()

    def get_all(self) -> list:
        """
        Returneaza toate cartile din repository.
        :return: o lista cu toate cartile
        """
        return self.__elements.copy()

    '''
        def get_size(self) -> int:
        """
        Returneaza numarul de carti din repository.
        :return: numarul de carti
        """
        return len(self.__elements)
    '''

    #RECURSIV
    def get_size(self) -> int:
        """
        Returnează numărul de cărți din repository folosind o metodă recursivă.
        :return: numărul de cărți
        """
        def count(elements):
            if not elements:  # Lista goala are dimensiunea 0
                return 0
            return 1 + count(elements[1:])  #Adauga 1 si merge mai departe
        return count(self.__elements)

    '''
    def __find_pos(self, id: int) -> int:
        """
        Gaseste pozitia unei carti in lista de elemente.
        :param id: id-ul cartii de cautat
        :return: pozitia cartii in lista, sau -1 daca nu exista
        """
        for i in range(len(self.__elements)):
            if self.__elements[i].get_id() == id:
                return i
        return -1
    '''
    #RECURSIV
    def __find_pos(self, id: int, index: int = 0) -> int:
        """
        Găsește poziția unei cărți în lista de elemente, recursiv.
        :param id: ID-ul cărții de căutat
        :param index: indexul curent (începe de la 0)
        :return: poziția cărții în listă sau -1 dacă nu există
        """
        if index >= len(self.__elements):  # Daca am ajuns la finalul listei
            return -1
        if self.__elements[index].get_id() == id:  # Daca am gasit cartea
            return index
        return self.__find_pos(id, index + 1)  # Continua cautarea

    def clear_all(self):
        """Clears all items from the repository and the file"""
        self.__elements = []
        with open(self.__filename, "w") as f:
            f.write("")  # Clear the file