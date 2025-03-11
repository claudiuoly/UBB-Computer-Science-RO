from datetime import datetime

class Rezervare:
    def __init__(self, id: int, client, carte, data_inchiriere: str, data_returnare: str = None):

        try:
            datetime.strptime(data_inchiriere, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data închirierii trebuie să fie în format YYYY-MM-DD.")

        self.__id = id
        self.__client = client  # Obiectul Client
        self.__carte = carte    # Obiectul Carte
        self.__data_inchiriere = datetime.strptime(data_inchiriere, "%Y-%m-%d")
        self.__data_returnare = datetime.strptime(data_returnare, "%Y-%m-%d") if data_returnare else None

    def get_id(self):
        return self.__id

    def get_client(self):
        return self.__client

    def get_book_id(self):
        return self.__carte.get_id()

    def get_client_id(self):
        return self.__client.get_id()

    def get_carte(self):
        return self.__carte

    def get_data_inchiriere(self):
        return self.__data_inchiriere

    def get_data_returnare(self):
        return self.__data_returnare

    def set_data_returnare(self, data_returnare: str):
        self.__data_returnare = datetime.strptime(data_returnare, "%Y-%m-%d")

    def este_returnata(self):
        return self.__data_returnare is not None

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.__id

    def __str__(self):
        return f"[{self.__id}] Rezervare: Client = {self.__client.get_nume()}; Carte = {self.__carte.get_titlu()}; " \
               f"Data Închiriere = {self.__data_inchiriere.strftime('%Y-%m-%d')}; " \
               f"Data Returnare = {self.__data_returnare.strftime('%Y-%m-%d') if self.__data_returnare else 'Ne-returnată'}"
