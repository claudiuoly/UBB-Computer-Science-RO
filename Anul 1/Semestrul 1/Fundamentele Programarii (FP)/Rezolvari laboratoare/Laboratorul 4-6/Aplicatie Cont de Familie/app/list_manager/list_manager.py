def add_to_list(lst_cheltuieli: list, cheltuiala: dict) -> None:
    """
    Adauga cheltuiala data la lista de cheltuieli
    :param lst_cheltuieli: lista de cheltuieli
    :param cheltuiala: cheltuiala care se adauga
    :return: -; lista data se modifica prin adaugarea cheltuielii la finalul listei
    """
    lst_cheltuieli.append(cheltuiala)


def edit_payment(lst_cheltuieli: list, ziua: int, suma: float, tip: str, cheltuiala_actualizata: dict) -> bool:
    """
    Actualizeaza o cheltuiala existenta în lista cu noile valori specificate
    :param lst_cheltuieli: lista de cheltuieli
    :param ziua: ziua cheltuielii care trebuie actualizata
    :param suma: suma cheltuielii care trebuie actualizata
    :param tip: tipul cheltuielii care trebuie actualizata
    :param cheltuiala_actualizata: noua cheltuiala cu noile valori (ziua, suma, tip)
    :return: True dacă cheltuiala a fost gasita și actualizata, altfel False
    """
    for i, cheltuiala in enumerate(lst_cheltuieli):
        if cheltuiala['ziua'] == ziua and cheltuiala['suma'] == suma and cheltuiala['tip'] == tip:
            lst_cheltuieli[i] = cheltuiala_actualizata
            return True

    return False


def delete_payment_by_day(lst_cheltuieli, ziua: int) -> list:
    """
        Șterge toate cheltuielile pentru ziua data.

        :param lst_cheltuieli: lista de cheltuieli
        :param ziua: ziua pentru care să fie șterse cheltuielile
        :return: lista actualizată de cheltuieli fara cheltuielile din ziua respectiva
        """
    return [cheltuiala for cheltuiala in lst_cheltuieli if cheltuiala['ziua'] != ziua]


def delete_payment_by_interval(lst_cheltuieli, zi_inceput: int, zi_final: int) -> list:
    """
        Șterge cheltuielile pentru un interval de timp dat.

        :param lst_cheltuieli: Lista de cheltuieli
        :param zi_inceput: Ziua de inceput a intervalului
        :param zi_final: Ziua de sfarsit a intervalului
        :return: Lista actualizata de cheltuieli fara cheltuielile din intervalul specificat
        """
    return [cheltuiala for cheltuiala in lst_cheltuieli if not (zi_inceput <= cheltuiala['ziua'] <= zi_final)]


def sterge_cheltuieli_tip(lst_cheltuieli, tip: str) -> list:
    """
            Șterge toate cheltuielile pentru un tip dat.

            :param lst_cheltuieli: lista de cheltuieli
            :param tip: tipul pentru care sa fie sterse cheltuielile
            :return: lista actualizata de cheltuieli fara cheltuielile din ziua respectiva
            """
    return [cheltuiala for cheltuiala in lst_cheltuieli if cheltuiala['tip'] != tip]
