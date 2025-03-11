from domain.client import Client


class ValidatorClient:
    def validate(self, client: Client):
        """
        Validează un client dat.
        :param client: clientul de validat
        :return: -
        :raises: ValueError cu mesajele de eroare dacă clientul nu este valid
        """
        errors = []

        # Verificăm numele
        if len(client.get_nume()) < 3:
            errors.append("Numele clientului trebuie să aibă cel puțin 3 caractere.")

        # Verificăm CNP-ul (doar lungimea de 13 caractere)
        cnp = client.get_cnp()
        if len(cnp) != 13 or not cnp.isdigit():
            errors.append("CNP-ul clientului trebuie să fie un număr de 13 caractere.")

        # Verificăm ID-ul clientului
        if client.get_id() <= 0:
            errors.append("ID-ul clientului trebuie să fie un număr pozitiv.")

        if len(errors) > 0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)
