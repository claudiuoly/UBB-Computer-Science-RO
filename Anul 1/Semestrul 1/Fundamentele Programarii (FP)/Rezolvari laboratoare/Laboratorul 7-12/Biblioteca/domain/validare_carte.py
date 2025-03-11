from domain.carte import Carte


class ValidatorCarte:
    def validate(self, carte: Carte):
        """
        Validează o carte dată.
        :param carte: cartea de validat
        :return: -
        :raises: ValueError cu mesajele de eroare dacă cartea nu este validă
        """
        errors = []

        # Verificăm titlul
        if len(carte.titlu) < 2:
            errors.append("Titlul cărții trebuie să aibă cel puțin 2 caractere.")

        # Verificăm descrierea
        if len(carte.get_descriere()) < 10:
            errors.append("Descrierea cărții trebuie să aibă cel puțin 10 caractere.")

        # Verificăm autorul
        if len(carte.get_autor()) < 3:
            errors.append("Numele autorului trebuie să aibă cel puțin 3 caractere.")

        # Verificăm ID-ul
        if carte.get_id() <= 0:
            errors.append("ID-ul cărții trebuie să fie un număr pozitiv.")

        if len(errors) > 0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)
