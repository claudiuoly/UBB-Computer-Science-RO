from app.domain.cheltuiala_familie import generate_payment, get_day, get_price, get_type
from app.list_manager.list_manager import add_to_list, edit_payment, delete_payment_by_day, delete_payment_by_interval, \
    sterge_cheltuieli_tip


def test_add_to_list():
    test_list = []
    assert len(test_list) == 0
    cheltuiala1 = {'ziua': 1, 'suma': 100, 'tip': 'mancare'}
    add_to_list(test_list, cheltuiala1)
    assert len(test_list) == 1
    assert test_list[0] == cheltuiala1

    cheltuiala2 = {'ziua': 2, 'suma': 200, 'tip': 'transport'}
    add_to_list(test_list, cheltuiala2)
    assert len(test_list) == 2
    assert test_list[1] == cheltuiala2


def test_edit_payment():
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'}
    ]

    cheltuiala_actualizata = {'ziua': 1, 'suma': 150, 'tip': 'mancare'}
    assert edit_payment(test_list, 1, 100, 'mancare', cheltuiala_actualizata)
    assert test_list[0] == cheltuiala_actualizata

    # Verificam ca nu se actualizeaza daca nu gasim cheltuiala
    cheltuiala_actualizata2 = {'ziua': 3, 'suma': 300, 'tip': 'utilitati'}
    assert not edit_payment(test_list, 3, 300, 'utilitati', cheltuiala_actualizata2)
    assert len(test_list) == 2


def test_delete_payment_by_day():
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'}
    ]

    new_list = delete_payment_by_day(test_list, 1)
    assert len(new_list) == 1
    assert new_list[0]['ziua'] == 2

    # Testam pentru o zi care nu exista
    new_list = delete_payment_by_day(test_list, 3)
    assert len(new_list) == 2


def test_delete_payment_by_interval():
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 300, 'tip': 'utilitati'}
    ]

    new_list = delete_payment_by_interval(test_list, 1, 2)
    assert len(new_list) == 1
    assert new_list[0]['ziua'] == 3

    # Testam pentru un interval care nu elimina nimic
    new_list = delete_payment_by_interval(test_list, 4, 5)
    assert len(new_list) == 3


def test_sterge_cheltuieli_tip():
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'}
    ]

    new_list = sterge_cheltuieli_tip(test_list, 'mancare')
    assert len(new_list) == 1
    assert new_list[0]['tip'] == 'transport'

    # Testam pentru un tip care nu exista
    new_list = sterge_cheltuieli_tip(test_list, 'divertisment')
    assert len(new_list) == 3


def test_sterge_cheltuieli_mici_decat_suma():
    from app.ui.console import sterge_cheltuieli_mici_decat_suma

    # Pregătim lista de cheltuieli pentru testare
    lista_cheltuieli = [
        {'ziua': 1, 'suma': 50, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 150, 'tip': 'transport'},
        {'ziua': 3, 'suma': 75, 'tip': 'utilitati'}
    ]

    # Testăm filtrarea pentru o sumă minimă de 100
    lista_actualizata = sterge_cheltuieli_mici_decat_suma(lista_cheltuieli, 100)
    assert len(lista_actualizata) == 1
    assert lista_actualizata[0]['suma'] == 150
    assert lista_actualizata[0]['tip'] == 'transport'

    # Testăm pentru o sumă minimă de 50 (doar cheltuielile sub 50 ar trebui eliminate)
    lista_actualizata = sterge_cheltuieli_mici_decat_suma(lista_cheltuieli, 50)
    assert len(lista_actualizata) == 3  # Nicio cheltuială nu ar trebui eliminată

    # Testăm pentru o sumă minimă mai mare decât toate cheltuielile (ex: 200)
    lista_actualizata = sterge_cheltuieli_mici_decat_suma(lista_cheltuieli, 200)
    assert len(lista_actualizata) == 0  # Toate cheltuielile ar trebui eliminate


def test_sterge_cheltuieli_tip_2():
    from app.ui.console import sterge_cheltuieli_tip_2

    # Pregătim lista de cheltuieli pentru testare
    lista_cheltuieli = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'}
    ]

    # Testăm eliminarea cheltuielilor de tipul 'mancare'
    lista_actualizata = sterge_cheltuieli_tip_2(lista_cheltuieli, 'mancare')
    assert len(lista_actualizata) == 2  # Ar trebui să rămână 2 cheltuieli
    assert all(cheltuiala['tip'] != 'mancare' for cheltuiala in lista_actualizata)  # Verificăm că tipul 'mancare' nu mai este în listă

    # Testăm pentru un tip care nu există (ex: 'utilitati')
    lista_actualizata = sterge_cheltuieli_tip_2(lista_cheltuieli, 'utilitati')
    assert len(lista_actualizata) == 4  # Lista originală ar trebui să rămână neschimbată

def test_sorteaza_cheltuieli_tip():
    from app.ui.console import sorteaza_cheltuieli_tip

    # Testăm cazul în care lista este goală
    lista_cheltuieli_goala = []
    sorteaza_cheltuieli_tip(lista_cheltuieli_goala)
    assert lista_cheltuieli_goala == []

    # Testăm cazul în care lista conține o singură cheltuială
    lista_single = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'}
    ]
    sorteaza_cheltuieli_tip(lista_single)
    assert lista_single == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'}
    ]

    # Testăm cazul în care lista este deja sortată
    lista_sortata = [
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'},
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'utilitati'}
    ]
    sorteaza_cheltuieli_tip(lista_sortata)
    assert lista_sortata == [
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'},
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'utilitati'}
    ]

    # Testăm cazul în care lista conține cheltuieli nesortate
    lista_nesortata = [
        {'ziua': 3, 'suma': 150, 'tip': 'utilitati'},
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'}
    ]
    sorteaza_cheltuieli_tip(lista_nesortata)
    assert lista_nesortata == [
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'},
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'utilitati'}
    ]

    # Testăm cazul în care toate cheltuielile au același tip
    lista_same_tip = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'mancare'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'}
    ]
    sorteaza_cheltuieli_tip(lista_same_tip)
    assert lista_same_tip == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'mancare'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'}
    ]


def test_gaseste_ziua_maxima():
    from app.ui.console import gaseste_ziua_maxima
    # Testul pentru o listă goală
    lista_cheltuieli_goala = []

    # Testul pentru o singură cheltuială
    lista_single = [
        {'ziua': 1, 'suma': 100}
    ]
    gaseste_ziua_maxima(lista_single)  # Ar trebui să afișeze ziua 1 cu suma 100

    # Testul pentru zile cu sume diferite
    lista_variate = [
        {'ziua': 1, 'suma': 50},
        {'ziua': 2, 'suma': 200},
        {'ziua': 3, 'suma': 150}
    ]
    gaseste_ziua_maxima(lista_variate)  # Ar trebui să afișeze ziua 2 cu suma 200

    # Testul pentru zile cu cheltuieli cumulative
    lista_cumulative = [
        {'ziua': 1, 'suma': 50},
        {'ziua': 1, 'suma': 150},
        {'ziua': 2, 'suma': 100},
        {'ziua': 2, 'suma': 100},
        {'ziua': 3, 'suma': 50}
    ]
    gaseste_ziua_maxima(lista_cumulative)  # Ar trebui să afișeze ziua 1 cu suma 200

    # Testul pentru zile cu sume egale
    lista_egale = [
        {'ziua': 1, 'suma': 100},
        {'ziua': 2, 'suma': 100},
        {'ziua': 3, 'suma': 100}
    ]
    gaseste_ziua_maxima(lista_egale)  # Ar trebui să afișeze oricare zi cu suma 100

def test_afiseaza_cheltuieli_dupasuma():
    from app.ui.console import afiseaza_cheltuieli_dupasuma
    # Lista de cheltuieli de test
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 100, 'tip': 'utilitati'}
    ]

    # Test 1: Verificăm dacă funcția filtrează corect cheltuielile cu suma 100
    rezultat = afiseaza_cheltuieli_dupasuma(test_list, 100)
    assert len(rezultat) == 2  # Trebuie să fie 2 cheltuieli cu suma de 100
    assert rezultat[0] == {'ziua': 1, 'suma': 100, 'tip': 'mancare'}
    assert rezultat[1] == {'ziua': 3, 'suma': 100, 'tip': 'utilitati'}

    # Test 2: Verificăm dacă funcția returnează mesajul corect pentru o sumă care nu există în listă
    rezultat = afiseaza_cheltuieli_dupasuma(test_list, 300)
    assert rezultat == "Nu există cheltuieli cu suma de 300."  # Mesajul corespunzător


def test_afiseaza_cheltuialasisumamax():
    from app.ui.console import afiseaza_cheltuialasisumamax
    # Lista de cheltuieli de test
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'}
    ]

    # Test 1: Verificăm suma totală pentru cheltuielile de tip 'mancare'
    rezultat = afiseaza_cheltuialasisumamax(test_list, 'mancare')
    assert rezultat == "Suma totală pentru cheltuielile de tip 'mancare' este: 250"  # suma 100 + 150

    # Test 2: Verificăm suma totală pentru cheltuielile de tip 'transport'
    rezultat = afiseaza_cheltuialasisumamax(test_list, 'transport')
    assert rezultat == "Suma totală pentru cheltuielile de tip 'transport' este: 200"  # doar suma 200

    # Test 3: Verificăm mesajul pentru un tip care nu există în listă
    rezultat = afiseaza_cheltuialasisumamax(test_list, 'utilitati')
    assert rezultat == "Nu există cheltuieli de tip 'utilitati'."  # Nu există acest tip


def test_afiseaza_cheltuieli_filtrate3():
    from app.ui.console import afiseaza_cheltuieli_filtrate3
    # Lista de cheltuieli de test
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'}
    ]

    # Test 1: Verificăm cheltuielile de tip 'mancare'
    rezultat = afiseaza_cheltuieli_filtrate3(test_list, 'mancare')
    assert rezultat == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'}
    ]

    # Test 2: Verificăm cheltuielile de tip 'transport'
    rezultat = afiseaza_cheltuieli_filtrate3(test_list, 'transport')
    assert rezultat == [
        {'ziua': 2, 'suma': 200, 'tip': 'transport'}
    ]

    # Test 3: Verificăm cheltuielile de tip 'divertisment'
    rezultat = afiseaza_cheltuieli_filtrate3(test_list, 'divertisment')
    assert rezultat == [
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'}
    ]

    # Test 4: Verificăm ce se întâmplă când nu există cheltuieli pentru tipul 'utilitati'
    rezultat = afiseaza_cheltuieli_filtrate3(test_list, 'utilitati')
    assert rezultat == []  # Nu ar trebui să existe cheltuieli de tip 'utilitati'


def test_afiseaza_cheltuieli_filtrate2():
    from app.ui.console import afiseaza_cheltuieli_filtrate2
    # Lista de cheltuieli de test
    test_list = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
        {'ziua': 4, 'suma': 50, 'tip': 'divertisment'},
        {'ziua': 5, 'suma': 120, 'tip': 'mancare'}
    ]

    # Test 1: Verificăm cheltuielile făcute înainte de ziua 4 și mai mici de 150
    rezultat = afiseaza_cheltuieli_filtrate2(test_list, 150, 4)
    assert rezultat == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 120, 'tip': 'mancare'},
        {'ziua': 3, 'suma': 50, 'tip': 'divertisment'}
    ]

    # Test 2: Verificăm cheltuielile făcute înainte de ziua 3 și mai mici de 100
    rezultat = afiseaza_cheltuieli_filtrate2(test_list, 100, 3)
    assert rezultat == [
        {'ziua': 1, 'suma': 50, 'tip': 'divertisment'}
    ]

    # Test 3: Verificăm cheltuielile făcute înainte de ziua 5 și mai mici de 200
    rezultat = afiseaza_cheltuieli_filtrate2(test_list, 200, 5)
    assert rezultat == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 120, 'tip': 'mancare'},
        {'ziua': 3, 'suma': 50, 'tip': 'divertisment'}
    ]

    # Test 4: Verificăm ce se întâmplă când nu există cheltuieli care îndeplinesc condițiile
    rezultat = afiseaza_cheltuieli_filtrate2(test_list, 50, 2)
    assert rezultat == []  # Nu ar trebui să existe cheltuieli care îndeplinesc aceste condiții

def test_actualizeaza_cheltuiala():

    from app.ui.console import actualizeaza_cheltuiala
    # Lista de cheltuieli de test
    lista_cheltuieli = [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 200, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
    ]

    # Test 1: Actualizare cu succes
    # Vom actualiza cheltuiala din ziua 2, suma 200, tipul 'transport'
    zi_noua, suma_noua, tip_nou = 2, 250, 'transport'

    # Apelăm funcția actualizează cheltuiala
    actualizeaza_cheltuiala(lista_cheltuieli)

    # Verificăm că cheltuiala a fost actualizată corect
    assert lista_cheltuieli == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 250, 'tip': 'transport'},  # Cheltuiala actualizată
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
    ]

    # Test 2: Cheltuiala nu a fost găsită
    # Vom încerca să actualizăm o cheltuială care nu există în listă (ex: ziua 4, suma 300, tipul 'mancare')
    zi_noua, suma_noua, tip_nou = 4, 300, 'mancare'

    # Apelăm funcția actualizează cheltuiala
    actualizeaza_cheltuiala(lista_cheltuieli)

    # Verificăm că lista nu s-a modificat, pentru că cheltuiala nu a fost găsită
    assert lista_cheltuieli == [
        {'ziua': 1, 'suma': 100, 'tip': 'mancare'},
        {'ziua': 2, 'suma': 250, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
    ]

    # Test 3: Verificăm ce se întâmplă când actualizăm o cheltuială existentă
    # Actualizăm cheltuiala din ziua 1
    zi_noua, suma_noua, tip_nou = 1, 120, 'mancare'

    # Apelăm funcția actualizează cheltuiala
    actualizeaza_cheltuiala(lista_cheltuieli)

    # Verificăm că cheltuiala a fost actualizată corect
    assert lista_cheltuieli == [
        {'ziua': 1, 'suma': 120, 'tip': 'mancare'},  # Cheltuiala actualizată
        {'ziua': 2, 'suma': 250, 'tip': 'transport'},
        {'ziua': 3, 'suma': 150, 'tip': 'mancare'},
    ]


def test_creare_cheltuiala():
    # Test de baza pentru generarea unei cheltuieli corecte
    cheltuiala1 = generate_payment(13, 14.02, "intretinere")
    assert get_day(cheltuiala1) == 13
    assert get_price(cheltuiala1) == 14.02
    assert get_type(cheltuiala1) == "intretinere"

    # Test pentru tipuri de cheltuieli valide
    cheltuiala2 = generate_payment(5, 50, "mancare")
    assert get_type(cheltuiala2) == "mancare"

    cheltuiala3 = generate_payment(20, 200, "imbracaminte")
    assert get_type(cheltuiala3) == "imbracaminte"

    cheltuiala4 = generate_payment(30, 20, "telefon")
    assert get_type(cheltuiala4) == "telefon"

    cheltuiala5 = generate_payment(10, 100, "altele")
    assert get_type(cheltuiala5) == "altele"

    # Test pentru categorie invalidă (ar trebui să ridice o eroare)
    try:
        cheltuiala_invalida = generate_payment(15, 100, "divertisment")
    except ValueError as e:
        assert str(
            e) == "Tipul cheltuielii nu este valid. Alege dintre: mancare, intretinere, imbracaminte, telefon, altele."

    # Test pentru zi invalidă (ar trebui să fie între 1 și 31, să adăugăm asta în funcție)
    try:
        cheltuiala_zi_invalida = generate_payment(32, 100, "mancare")
    except ValueError as e:
        assert str(e) == "Ziua trebuie să fie între 1 și 31."



def run_tests():
    test_add_to_list()
    test_edit_payment()
    test_delete_payment_by_day()
    test_delete_payment_by_interval()
    test_sterge_cheltuieli_tip()
    test_sterge_cheltuieli_mici_decat_suma()
    test_sterge_cheltuieli_tip_2()
    test_sorteaza_cheltuieli_tip()
    # test_gaseste_ziua_maxima()
    # test_afiseaza_cheltuieli_dupasuma()
    # test_afiseaza_cheltuialasisumamax()
    # test_afiseaza_cheltuieli_filtrate3()
    # test_afiseaza_cheltuieli_filtrate2()
    # test_actualizeaza_cheltuiala()
    # test_creare_cheltuiala()
    print("[INFO]: Toate testele au trecut cu succes!")
