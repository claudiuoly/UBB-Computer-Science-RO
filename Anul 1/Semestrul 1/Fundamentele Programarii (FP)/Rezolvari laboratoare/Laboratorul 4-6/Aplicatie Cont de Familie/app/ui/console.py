from app.domain.cheltuiala_familie import generate_payment
from app.list_manager.list_manager import edit_payment, delete_payment_by_day, \
    delete_payment_by_interval, sterge_cheltuieli_tip
from app.tests.tests import run_tests


def afiseaza_meniu():
    """
    Afișează meniul principal cu opțiunile disponibile.
    """
    print("1. Adauga o cheltuiala")
    print("2. Actualizeaza o cheltuiala")
    print("3. Tipareste toate cheltuielile mai mari decat o suma pe care o vei introduce")
    print("4. Tipareste toate cheltuielile efectuate înainte de o zi si mai mici decat o suma pe care o vei introduce")
    print("5. Tipareste toate cheltuielile de un anumit tip")
    print("6. Sterge toate cheltuielile dintr-o zi pe care o vei introduce")
    print("7. Sterge cheltuielile pentru un interval de timp")
    print("8. Sterge toate cheltuielile de un anumit tip")
    print("9. Afiseaza lista de cheltuieli")
    print("10. Tipărește suma totală pentru un anumit tip de cheltuială")
    print("11. Găsește ziua în care suma cheltuită e maximă")
    print("12. Tipărește toate cheltuielile ce au o anumită sumă")
    print("13. Tipărește cheltuielile sortate după tip")
    print("14. Elimină toate cheltuielile de un anumit tip")
    print("15. Elimină toate cheltuielile mai mici decât o sumă dată")
    print("16. Undo")
    print("17. Iesire din aplicatie")


def citeste_info_cheltuiala() -> tuple:
    """
    Citește informațiile unei cheltuieli de la utilizator (zi, sumă, tip).

    :return: Tuple (zi, suma, tip)
    """
    zi = input("Introduceti ziua in care s-a efectuat cheltuiala: ")
    zi = int(zi)
    suma = input("Introduceti pretul cheltuielii: ")
    suma = float(suma)
    tip = input("Introduceti tipul din care face parte cheltuiala: ")
    return zi, suma, tip


def afiseaza_cheltuielile(list_cheltuieli):
    """
    Afișează toate cheltuielile dintr-o listă dată. Dacă lista este goală, afișează un mesaj corespunzător.

    :param list_cheltuieli: Lista de cheltuieli
    """
    if not list_cheltuieli:  # Verifică dacă lista este goală
        print("Nu există nici o cheltuială de afișat.")
    else:
        for i, cheltuiala in enumerate(list_cheltuieli):
            print("Cheltuiala #" + str(i) + ": ", end="")
            cheltuiala_info = ""
            for key, value in cheltuiala.items():
                cheltuiala_info += key.capitalize() + ": " + str(value) + " | "
            print(cheltuiala_info)



def actualizeaza_cheltuiala(lista_cheltuieli):
    """
    Actualizează o cheltuială existentă pe baza zilei, sumei și tipului.

    :param lista_cheltuieli: Lista de cheltuieli existente
    """
    print("Introdu datele pentru cheltuiala pe care dorești să o actualizezi.")
    zi, suma, tip = citeste_info_cheltuiala()

    # Citim noile date pentru cheltuiala actualizată
    print("Introdu noile date pentru cheltuiala actualizată.")
    zi_noua, suma_noua, tip_nou = citeste_info_cheltuiala()

    cheltuiala_actualizata = generate_payment(zi_noua, suma_noua, tip_nou)

    if edit_payment(lista_cheltuieli, zi, suma, tip, cheltuiala_actualizata):
        print("Cheltuiala a fost actualizată cu succes!")
    else:
        print("Cheltuiala nu a fost găsită.")


def afiseaza_cheltuieli_filtrate1(lista_cheltuieli, x: float):
    """
    Afișează toate cheltuielile care sunt mai mari decât suma x.

    :param lista_cheltuieli: Lista de cheltuieli
    :param x: Suma minimă pentru filtrare
    """
    cheltuieli_filtrate = [c for c in lista_cheltuieli if c['suma'] > x]
    afiseaza_cheltuielile(cheltuieli_filtrate)


def afiseaza_cheltuieli_filtrate2(lista_cheltuieli, suma: float, zi: int):
    """
    Afișează toate cheltuielile care sunt efectuate înainte de o zi și mai mici decât o sumă dată.

    :param lista_cheltuieli: Lista de cheltuieli
    :param suma: Suma maximă pentru filtrare
    :param zi: Ziua limită pentru filtrare
    """
    cheltuieli_filtrate = [c for c in lista_cheltuieli if c['ziua'] < zi and c['suma'] < suma]
    afiseaza_cheltuielile(cheltuieli_filtrate)


def afiseaza_cheltuieli_filtrate3(lista_cheltuieli, tip: str):
    """
    Afișează toate cheltuielile de un anumit tip.

    :param lista_cheltuieli: Lista de cheltuieli
    :param tip: Tipul de cheltuială pentru filtrare
    """
    cheltuieli_filtrate = [c for c in lista_cheltuieli if c['tip'] == tip]
    afiseaza_cheltuielile(cheltuieli_filtrate)

def afiseaza_cheltuialasisumamax(lista_cheltuieli, tip: str):
    """
    Afișează suma totală a cheltuielilor de un anumit tip.

    :param lista_cheltuieli: Lista de cheltuieli
    :param tip: Tipul de cheltuială pentru care se va calcula suma totală
    """
    suma_totala = sum(c['suma'] for c in lista_cheltuieli if c['tip'] == tip)

    if suma_totala > 0:
        print(f"Suma totală pentru cheltuielile de tip '{tip}' este: {suma_totala}")
    else:
        print(f"Nu există cheltuieli de tip '{tip}'.")

def afiseaza_cheltuieli_dupasuma(lista_cheltuieli, suma: float):
    """
    Afișează cheltuielile care au exact suma specificată.

    :param lista_cheltuieli: Lista de cheltuieli
    :param suma: Suma pentru filtrare
    """
    cheltuieli_filtrate = [c for c in lista_cheltuieli if c['suma'] == suma]
    if cheltuieli_filtrate:
        afiseaza_cheltuielile(cheltuieli_filtrate)
    else:
        print(f"Nu există cheltuieli cu suma de {suma}.")


def gaseste_ziua_maxima(lista_cheltuieli):
    """
    Găsește ziua în care suma cheltuită este maximă și o afișează.

    :param lista_cheltuieli: Lista de cheltuieli
    """
    # Dicționar pentru a ține suma cheltuielilor pe fiecare zi
    cheltuieli_pe_zi = {}

    # Parcurgem lista de cheltuieli și adunăm sumele pe fiecare zi
    for cheltuiala in lista_cheltuieli:
        zi = cheltuiala['ziua']
        suma = cheltuiala['suma']
        if zi in cheltuieli_pe_zi:
            cheltuieli_pe_zi[zi] += suma
        else:
            cheltuieli_pe_zi[zi] = suma

    # Găsim ziua cu suma maximă
    zi_maxima = max(cheltuieli_pe_zi, key=cheltuieli_pe_zi.get)
    suma_maxima = cheltuieli_pe_zi[zi_maxima]

    print(f"Ziua cu suma maximă este {zi_maxima}, cu suma totală de {suma_maxima:.2f} lei.")


def sorteaza_cheltuieli_tip(lista_cheltuieli):
    """
    Sortează lista de cheltuieli după tip.

    :param lista_cheltuieli: Lista de cheltuieli
    """
    n = len(lista_cheltuieli)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_cheltuieli[j]['tip'] > lista_cheltuieli[j + 1]['tip']:
                lista_cheltuieli[j], lista_cheltuieli[j + 1] = lista_cheltuieli[j + 1], lista_cheltuieli[j]
    # afiseaza_cheltuielile(lista_cheltuieli)


def sterge_cheltuieli_tip_2(lista_cheltuieli, tip: str):
    """
    Sterge toate cheltuielile de un anumit tip din lista de cheltuieli.

    :param lista_cheltuieli: Lista de cheltuieli
    :param tip: Tipul de cheltuială ce trebuie șters
    :return: Lista de cheltuieli actualizată
    """
    lista_cheltuieli = [cheltuiala for cheltuiala in lista_cheltuieli if cheltuiala['tip'] != tip]
    return lista_cheltuieli


def sterge_cheltuieli_mici_decat_suma(lista_cheltuieli, suma_minima: float):
    """
    Sterge toate cheltuielile care au suma mai mică decât valoarea minimă specificată.

    :param lista_cheltuieli: Lista de cheltuieli
    :param suma_minima: Suma minimă sub care cheltuielile vor fi eliminate
    :return: Lista de cheltuieli actualizată
    """
    lista_cheltuieli = [cheltuiala for cheltuiala in lista_cheltuieli if cheltuiala['suma'] >= suma_minima]
    return lista_cheltuieli


def run():
    run_tests()
    lista_cheltuieli = []
    stack_stari = []  # Stack pentru a salva stările listei de cheltuieli
    is_running = True
    while is_running:
        afiseaza_meniu()
        optiune = input("Introduceti optiunea: ")
        match optiune:
            case "1":
                # Salvează starea listei înainte de a adăuga o cheltuială
                stack_stari.append(lista_cheltuieli[:])  # Copie superficială a listei
                zi, suma, tip = citeste_info_cheltuiala()
                cheltuiala = generate_payment(zi, suma, tip)
                lista_cheltuieli.append(cheltuiala)
                print("Cheltuiala a fost adaugata cu succes!")
            case "2":
                # Salvează starea listei înainte de a actualiza o cheltuială
                stack_stari.append(lista_cheltuieli[:])  # Copie superficială a listei
                actualizeaza_cheltuiala(lista_cheltuieli)
            case "3":
                suma = float(input("Introduceți suma minimă: "))
                afiseaza_cheltuieli_filtrate1(lista_cheltuieli, suma)
            case "4":
                zi = int(input("Introduceți ziua: "))
                suma = float(input("Introduceți suma maximă: "))
                afiseaza_cheltuieli_filtrate2(lista_cheltuieli, suma, zi)
            case "5":
                tip = input("Introduceți tipul: ")
                afiseaza_cheltuieli_filtrate3(lista_cheltuieli, tip)
            case "6":
                # Salvează starea listei înainte de a șterge o cheltuială
                stack_stari.append(lista_cheltuieli[:])  # Copie superficială a listei
                zi = int(input("Introduceti ziua pentru cheltuielile pe care vreti sa le stergeti: "))
                lista_cheltuieli = delete_payment_by_day(lista_cheltuieli, zi)
                print(f"Cheltuielile care au fost facute in ziua {zi} au fost stearse cu succes!")
            case "7":
                # Salvează starea listei înainte de a șterge cheltuielile pe interval
                stack_stari.append(lista_cheltuieli[:])  # Copie superficială a listei
                zi_inceput = int(input("Introduceti prima zi de cand doriti sa stergeti cheltuielile: "))
                zi_final = int(input("Introduceti ziua pana cand doriti sa stergeti cheltuielile: "))
                lista_cheltuieli = delete_payment_by_interval(lista_cheltuieli, zi_inceput, zi_final)
                print(f"Cheltuielile din perioada [{zi_inceput}, {zi_final}] au fost sterse cu succes!")
            case "8":
                # Salvează starea listei înainte de a șterge cheltuielile după tip
                stack_stari.append(lista_cheltuieli[:])  # Copie superficială a listei
                tip = input("Introduceti tipul de cheltuiala pe care vreti sa il stergeti: ")
                lista_cheltuieli = sterge_cheltuieli_tip(lista_cheltuieli, tip)
                print(f"Cheltuielile care au fost de tipul {tip} au fost stearse cu succes!")
            case "9":
                afiseaza_cheltuielile(lista_cheltuieli)
            case "10":
                tip = input("Introduceti tipul de cheltuiala la care vreti sa vedeti suma totala: ")
                afiseaza_cheltuialasisumamax(lista_cheltuieli, tip)
            case "11":
                gaseste_ziua_maxima(lista_cheltuieli)
            case "12":
                suma = int(input("Introuceti suma pentru care sa arete cheltuielile: "))
                afiseaza_cheltuieli_dupasuma(lista_cheltuieli, suma)
            case "13":
                sorteaza_cheltuieli_tip(lista_cheltuieli)
                afiseaza_cheltuielile(lista_cheltuieli)
            case "14":
                tip = input("Introduceti tipul de cheltuiala pe care vreti sa il stergeti: ")
                lista_cheltuieli = sterge_cheltuieli_tip_2(lista_cheltuieli, tip)
                print(f"Toate cheltuielile de tipul '{tip}' au fost eliminate.")
            case "15":
                suma_minima = float(input("Introduceti suma minima pentru stergerea cheltuielilor: "))
                lista_cheltuieli = sterge_cheltuieli_mici_decat_suma(lista_cheltuieli, suma_minima)
                print(f"Toate cheltuielile mai mici decât {suma_minima} au fost eliminate.")
            case "16":
                if stack_stari:
                    lista_cheltuieli = stack_stari.pop()  # Recuperăm ultima stare salvată
                    print("Operațiunea a fost anulată. Lista a revenit la starea anterioară.")
                else:
                    print("Nu există operații anterioare pentru a face undo.")
            case "17":
                print("Ati iesit din aplicatie, o zi frumoasa!")
                is_running = False