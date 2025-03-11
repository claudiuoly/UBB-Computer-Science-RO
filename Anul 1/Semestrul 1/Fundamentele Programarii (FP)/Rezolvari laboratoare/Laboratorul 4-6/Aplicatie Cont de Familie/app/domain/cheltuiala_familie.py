def generate_payment(ziua: int, suma: float, tip: str) -> dict:
    """
    Creeaza o cheltuiala pe baza informațiilor date
    :param ziua: ziua din luna cand a fost realizata cheltuiala
    :param suma: suma cheltuielii
    :param tip: tipul cheltuielii (ex: mancare, intretinere, imbracaminte, telefon, altele)
    :return: un dictionar care reprezinta cheltuiala
    """
    categorii_cheltuieli = ['mancare', 'intretinere', 'imbracaminte', 'telefon', 'altele']

    if not (1 <= ziua <= 31):
        raise ValueError("Ziua trebuie să fie între 1 și 31.")

    if tip not in categorii_cheltuieli:
        raise ValueError(
            "Tipul cheltuielii nu este valid. Alege dintre: mancare, intretinere, imbracaminte, telefon, altele.")

    return {'ziua': ziua, 'suma': suma, 'tip': tip}


def get_day(cheltuiala) -> int:
    """
    Returneaza ziua in care s-a facut cheltuiala
    :param cheltuiala: cheltuiala data
    :return: ziua cheltuielii de tip int
    """
    return cheltuiala['ziua']

def get_price(cheltuiala) -> float:
    """
    Returneaza pretul cheltuielii
    :param cheltuiala: cheltuiala data
    :return: pretul cheltuielii de tip float
    """
    return cheltuiala['suma']


def get_type(cheltuiala) -> str:
    """
    Returneaza tipul cheltuielii date
    :param cheltuiala: cheltuiala data
    :return: tipul cheltuielii string
    """
    return cheltuiala['tip']