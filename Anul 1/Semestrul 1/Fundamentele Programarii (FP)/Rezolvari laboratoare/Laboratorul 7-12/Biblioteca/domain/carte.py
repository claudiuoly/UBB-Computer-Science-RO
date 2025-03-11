class Carte:
    def __init__(self, id: int, titlu: str, descriere: str, autor: str):
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    @property
    def titlu(self):
        return self.__titlu

    @titlu.setter
    def titlu(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Titlul poate fi doar de tip str.")
        self.__titlu = new_value

    def get_descriere(self):
        return self.__descriere

    def set_descriere(self, value):
        self.__descriere = value

    def get_autor(self):
        return self.__autor

    def set_autor(self, value):
        self.__autor = value

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.__id

    def __hash__(self):
        return hash(self.__id)

    def __str__(self):
        return f"[{self.__id}] Carte: Titlu = {self.__titlu}; Autor = {self.__autor}; Descriere = {self.__descriere}"
