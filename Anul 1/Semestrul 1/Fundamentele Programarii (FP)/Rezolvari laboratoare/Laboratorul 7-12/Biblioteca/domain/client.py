class Client:
    def __init__(self, id: int, nume: str, cnp: str):
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, new_value):
        if not isinstance(new_value, str):
            raise ValueError("Numele poate fi doar de tip str.")
        self.__nume = new_value

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, value):
        self.__cnp = value

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.__id

    def __hash__(self):
        return hash(self.__id)

    def __str__(self):
        return f"[{self.__id}] Client: Nume = {self.__nume}; CNP = {self.__cnp}"
