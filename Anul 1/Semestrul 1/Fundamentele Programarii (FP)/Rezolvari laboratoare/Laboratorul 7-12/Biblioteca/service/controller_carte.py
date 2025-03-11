import random

from colorama import Fore, Style

from domain.carte import Carte
from domain.validare_carte import ValidatorCarte
from repository.repository_carte import RepositoryCarti


class ControllerCarti:
    def __init__(self, repo: RepositoryCarti, validator: ValidatorCarte):
        self.__repo = repo
        self.__validator = validator

    def merge_sort(self, key=lambda carte: carte.get_titlu(), reverse=False):
        """
        Sortează cărțile folosind algoritmul MergeSort.
        :param key: funcția de cheie pentru sortare (default: titlu)
        :param reverse: dacă True, ordonează descrescător
        :return: lista sortată
        """

        def merge(left, right):
            """
            Combină două liste sortate într-o listă sortată.
            :param left: prima listă sortată
            :param right: a doua listă sortată
            :return: lista combinată și sortată
            """
            sorted_list = []
            while left and right:
                # Compara elementele din cele doua liste si adauga-l pe cel mai mic
                if (key(left[0]) <= key(right[0])) != reverse:
                    sorted_list.append(left.pop(0))  # Adauga elementul din lista 'left'
                else:
                    sorted_list.append(right.pop(0))  # Adauga elementul din lista 'right'

            # Adauga elementele ramase din oricare lista
            sorted_list.extend(left or right)
            return sorted_list

        def merge_sort_recursiv(items):
            """
            Funcția recursivă care aplică algoritmul MergeSort pe o listă.
            :param items: lista de elemente care trebuie sortată
            :return: lista sortată
            """
            if len(items) <= 1:
                return items  # Dacă lista are un singur element sau este goală, este deja sortată

            mid = len(items) // 2  # Găsește mijlocul listei
            left = merge_sort_recursiv(items[:mid])  # Sortează partea stângă a listei
            right = merge_sort_recursiv(items[mid:])  # Sortează partea dreaptă a listei

            # Combină cele două părți sortate
            return merge(left, right)

        # Obține lista completă de cărți din repo
        carti = self.__repo.get_all()

        # Aplică funcția de sortare recursivă
        return merge_sort_recursiv(carti)

    def bingo_sort(self):
        carti = self.get_all()
        n = len(carti)

        while not self.is_sorted(carti):
            random_indices = random.sample(range(n), min(n, 5))
            for i in random_indices:
                for j in range(i + 1, n):
                    if carti[i].get_titlu() > carti[j].get_titlu():
                        carti[i], carti[j] = carti[j], carti[i]

        self.__repo.clear_all()
        for carte in carti:
            self.__repo.store(carte)

        print(Fore.GREEN + "Cărțile sortate cu BingoSort:" + Style.RESET_ALL)
        for carte in carti:
            print(f"ID: {carte.get_id()}, Titlu: {carte.get_titlu()}, Autor: {carte.get_autor()}")

    def is_sorted(self, carti):
        """
        Verifică dacă lista este deja sortată.
        :param carti: lista de cărți
        :return: True dacă este sortată, False altfel
        """
        for i in range(1, len(carti)):
            if carti[i-1].get_titlu() > carti[i].get_titlu():
                return False
        return True

    def quick_sort(self, key=lambda carte: carte.get_titlu(), reverse=False):
        """
        Sortează cărțile folosind algoritmul QuickSort.
        :param key: funcția de cheie pentru sortare (default: titlu)
        :param reverse: dacă True, ordonează descrescător
        :return: lista sortată
        """
        def partition(carti, left, right):
            pivot = carti[left]
            i = left + 1
            for j in range(left + 1, right + 1):
                if (key(carti[j]) <= key(pivot)) != reverse:  # Comparatie cu cheia si ordonarea dorita
                    carti[i], carti[j] = carti[j], carti[i]  # Schimba elementele
                    i += 1
            carti[left], carti[i - 1] = carti[i - 1], carti[left]  # Pune pivotul in pozitia corecta
            return i - 1

        def quick_sort_recursiv(carti, left, right):
            if left < right:
                pos = partition(carti, left, right)  # Obtine pozitia pivotului
                quick_sort_recursiv(carti, left, pos - 1)  # Ordoneaza partea stanga
                quick_sort_recursiv(carti, pos + 1, right)  # Ordoneaza partea dreapta

        carti = self.__repo.get_all()
        quick_sort_recursiv(carti, 0, len(carti) - 1)
        return carti

    def actualizeaza_carte(self, id: int, titlu_nou: str, descriere_noua: str, autor_nou: str):
        """
        Actualizează cartea cu id-ul dat cu informațiile noi
        :param id: id-ul cărții de actualizat
        :param titlu_nou: noul titlu al cărții
        :param descriere_noua: noua descriere a cărții
        :param autor_nou: noul autor al cărții
        :return: -; lista de cărți se modifică prin actualizarea cărții cu id-ul dat
        :raises: ValueError dacă din informațiile date nu se poate construi o carte validă
                 ValueError dacă nu există o carte cu id-ul dat
        """
        carte_noua = Carte(id, titlu_nou, descriere_noua, autor_nou)
        self.__validator.validate(carte_noua)
        self.__repo.update(carte_noua)

    def find_carte(self, id: int):
        """
        Căutăm cartea cu id-ul dat
        :param id: id-ul după care se caută
        :return: cartea cu id-ul dat, dacă aceasta există, None altfel
        """
        return self.__repo.find(id)

    def delete_carte(self, id: int):
        """
        Șterge o carte după id
        :param id: id-ul cărții de șters
        :return: -
        :raises: ValueError dacă nu există o carte cu id-ul dat
        """
        self.__repo.delete(id)

    def get_all(self) -> list:
        """
        Returnează toate cărțile
        :return: lista de cărți
        """
        return self.__repo.get_all()

    def add_default(self):
        """
        Adaugă câteva cărți implicite în colecție
        """
        self.adauga_carte(1, "Mândrie și prejudecată", "Roman clasic englez", "Jane Austen")
        self.adauga_carte(2, "1984", "Roman distopic", "George Orwell")
        self.adauga_carte(3, "La Medeleni", "Roman de formare", "Ionel Teodoreanu")
        self.adauga_carte(4, "Ion", "Roman social", "Liviu Rebreanu")