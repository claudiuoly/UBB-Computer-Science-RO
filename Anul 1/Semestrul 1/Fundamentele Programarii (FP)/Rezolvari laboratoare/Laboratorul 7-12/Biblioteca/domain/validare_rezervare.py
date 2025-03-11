from datetime import datetime
from domain.rezervare import Rezervare


class ValidatorRezervare:
    def validate(self, rezervare: Rezervare):
        """
        Validează o rezervare dată.
        :param rezervare: rezervarea de validat
        :return: -
        :raises: ValueError cu mesajele de eroare dacă rezervarea nu este validă
        """
        errors = []

        # Verificăm ID-ul rezervării
        if rezervare.get_id() <= 0:
            errors.append("ID-ul rezervării trebuie să fie un număr pozitiv.")

        # Verificăm data închirierii
        data_inchiriere = rezervare.get_data_inchiriere()
        if not isinstance(data_inchiriere, datetime):
            errors.append("Data închirierii nu este validă.")

        # Verificăm data returnării
        data_returnare = rezervare.get_data_returnare()
        if data_returnare and data_returnare < data_inchiriere:
            errors.append("Data returnării nu poate fi anterioară datei închirierii.")

        if len(errors) > 0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)
