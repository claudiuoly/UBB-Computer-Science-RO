from datetime import datetime

from colorama import Fore, Style


class LibraryConsole:
    def __init__(self, book_controller, client_controller, rental_controller):
        self.book_controller = book_controller
        self.client_controller = client_controller
        self.rental_controller = rental_controller

    @staticmethod
    def afiseaza_meniu_principal():
        print(Fore.CYAN + "\n==== Biblioteca ====" + Style.RESET_ALL)
        print("1. Gestionarea Cărților")
        print("2. Gestionarea Clienților")
        print("3. Gestionarea Rezervărilor")
        print("4. Cautare carte după ID")
        print("5. Cautare client după ID")
        print("6. Rapoarte")
        print("7. Sortează cărțile folosind MergeSort")
        print("8. Sortează cărțile folosind BingoSort")
        print("9. Sorteaza cartile folosind QuickSort")
        print(Fore.RED + "0. Ieșire" + Style.RESET_ALL)

    def run(self):
        while True:
            self.afiseaza_meniu_principal()
            optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()

            if optiune == "1":
                self.menu_carti()
            elif optiune == "2":
                self.menu_clienti()
            elif optiune == "3":
                self.menu_rezervari()
            elif optiune == "4":
                self.menu_cautare_carte()
            elif optiune == "5":
                self.menu_cautare_client()
            elif optiune == "6":
                self.menu_rapoarte()
            elif optiune == "7":
                self.sorteaza_carti()
            elif optiune == "8":
                self.sorteaza_carti_bingo_sort()
            elif optiune == "9":
                self.sorteaza_carti_quick_sort()
            elif optiune == "0":
                print(Fore.RED + "La revedere!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Opțiune invalidă! Încercați din nou." + Style.RESET_ALL)

    def menu_carti(self):
        while True:
            print(Fore.GREEN + "\n-- Gestionarea Cărților --" + Style.RESET_ALL)
            print("1. Adaugă carte")
            print("2. Șterge carte")
            print("3. Modifică carte")
            print("4. Afișează toate cărțile")
            print(Fore.YELLOW + "0. Înapoi" + Style.RESET_ALL)

            optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()

            if optiune == "1":
                self.adauga_carte()
            elif optiune == "2":
                self.sterge_carte()
            elif optiune == "3":
                self.modifica_carte()
            elif optiune == "4":
                self.afiseaza_carti()
            elif optiune == "0":
                break
            else:
                print(Fore.RED + "Opțiune invalidă!" + Style.RESET_ALL)

    def adauga_carte(self):
        try:
            id_carte = int(input("ID-ul cărții: "))
            titlu = input("Titlul: ")
            descriere = input("Descrierea: ")
            autor = input("Autorul: ")

            self.book_controller.adauga_carte(id_carte, titlu, descriere, autor)
            print(Fore.GREEN + "Cartea a fost adăugată cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Erroare: {e}" + Style.RESET_ALL)

    def sterge_carte(self):
        try:
            id_carte = int(input("ID-ul cărții de șters: "))
            self.book_controller.delete_carte(id_carte)
            print(Fore.GREEN + "Cartea a fost ștearsă cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Erroare: {e}" + Style.RESET_ALL)

    def modifica_carte(self):
        try:
            id_carte = int(input("ID-ul cărții de modificat: "))
            titlu = input("Noul titlu: ")
            descriere = input("Noua descriere: ")
            autor = input("Noul autor: ")

            self.book_controller.actualizeaza_carte(id_carte, titlu, descriere, autor)
            print(Fore.GREEN + "Cartea a fost actualizată cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Erroare: {e}" + Style.RESET_ALL)

    def afiseaza_carti(self):
        carti = self.book_controller.get_all()
        if not carti:
            print(Fore.YELLOW + "Nu există cărți în bibliotecă." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Lista de cărți:" + Style.RESET_ALL)
            for carte in carti:
                print(f"ID: {carte.get_id()}, Titlu: {carte.get_titlu()}, Autor: {carte.get_autor()}")

    def menu_rapoarte(self):
        while True:
            print(Fore.YELLOW + "\n-- Rapoarte --" + Style.RESET_ALL)
            print("1. Cele mai închiriate cărți")
            print("2. Clienți cu cărți închiriate (ordonați după nume)")
            print("3. Top 20% cei mai activi clienți")
            print(Fore.YELLOW + "0. Înapoi" + Style.RESET_ALL)

            optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()

            if optiune == "1":
                self.raport_carti_inchiriate()
            elif optiune == "2":
                self.raport_clienti_ordonati()
            elif optiune == "3":
                self.raport_clienti_activi()
            elif optiune == "0":
                break
            else:
                print(Fore.RED + "Opțiune invalidă!" + Style.RESET_ALL)

    def raport_carti_inchiriate(self):
        print(Fore.CYAN + "\n-- Cele mai închiriate cărți --" + Style.RESET_ALL)
        rezultate = self.rental_controller.get_most_rented_books()
        if rezultate:
            for carte, numar in rezultate:
                print(f"Carte: {carte.get_titlu()} | Autor: {carte.get_autor()} | Număr închirieri: {numar}")
        else:
            print(Fore.YELLOW + "Nu există cărți închiriate." + Style.RESET_ALL)

    def raport_clienti_ordonati(self):
        print(Fore.CYAN + "\n-- Clienți cu cărți închiriate (ordonați după nume) --" + Style.RESET_ALL)
        rezultate = self.rental_controller.get_clients_sorted_by_name()
        if rezultate:
            for client, numar in rezultate:
                print(f"Client: {client.get_nume()} | CNP: {client.get_cnp()} | Cărți închiriate: {numar}")
        else:
            print(Fore.YELLOW + "Nu există clienți cu cărți închiriate." + Style.RESET_ALL)

    def raport_clienti_activi(self):
        print(Fore.CYAN + "\n-- Top 20% cei mai activi clienți --" + Style.RESET_ALL)
        rezultate = self.rental_controller.get_top_active_clients()
        if rezultate:
            for client, numar in rezultate:
                print(f"Client: {client.get_nume()} | CNP: {client.get_cnp()} | Cărți închiriate: {numar}")
        else:
            print(Fore.YELLOW + "Nu există clienți activi." + Style.RESET_ALL)

    def menu_clienti(self):
        while True:
            print(Fore.GREEN + "\n-- Gestionarea Clienților --" + Style.RESET_ALL)
            print("1. Adaugă client")
            print("2. Șterge client")
            print("3. Modifică client")
            print("4. Afișează toți clienții")
            print(Fore.YELLOW + "0. Înapoi" + Style.RESET_ALL)

            optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()

            if optiune == "1":
                self.adauga_client()
            elif optiune == "2":
                self.sterge_client()
            elif optiune == "3":
                self.modifica_client()
            elif optiune == "4":
                self.afiseaza_clienti()
            elif optiune == "0":
                break
            else:
                print(Fore.RED + "Opțiune invalidă!" + Style.RESET_ALL)

    def adauga_client(self):
        try:
            id_client = int(input("ID-ul clientului: "))
            nume = input("Numele: ")
            cnp = input("CNP-ul: ")

            self.client_controller.adauga_client(id_client, nume, cnp)
            print(Fore.GREEN + "Clientul a fost adăugat cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def sterge_client(self):
        try:
            id_client = int(input("ID-ul clientului de șters: "))
            self.client_controller.delete_client(id_client)
            print(Fore.GREEN + "Clientul a fost șters cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def modifica_client(self):
        try:
            id_client = int(input("ID-ul clientului de modificat: "))
            nume = input("Noul nume: ")
            cnp = input("Noul CNP: ")

            self.client_controller.actualizeaza_client(id_client, nume, cnp)
            print(Fore.GREEN + "Clientul a fost actualizat cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def afiseaza_clienti(self):
        clienti = self.client_controller.get_all()
        if not clienti:
            print(Fore.YELLOW + "Nu există clienți înregistrați." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Lista de clienți:" + Style.RESET_ALL)
            for client in clienti:
                print(f"ID: {client.get_id()}, Nume: {client.get_nume()}, CNP: {client.get_cnp()}")

    def menu_rezervari(self):
        while True:
            print(Fore.GREEN + "\n-- Gestionarea Rezervărilor --" + Style.RESET_ALL)
            print("1. Adaugă rezervare")
            print("2. Șterge rezervare")
            print("3. Afișează toate rezervările")
            print(Fore.YELLOW + "0. Înapoi" + Style.RESET_ALL)

            optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()

            if optiune == "1":
                self.adauga_rezervare()
            elif optiune == "2":
                self.sterge_rezervare()
            elif optiune == "3":
                self.afiseaza_rezervari()
            elif optiune == "0":
                break
            else:
                print(Fore.RED + "Opțiune invalidă!" + Style.RESET_ALL)

    def adauga_rezervare(self):
        try:
            id_rezervare = int(input("ID-ul rezervării: "))
            id_client = int(input("ID-ul clientului: "))
            id_carte = int(input("ID-ul cărții: "))

            data_inchiriere = input("Data închirierii (format YYYY-MM-DD, implicit data curentă): ").strip()
            if not data_inchiriere:
                data_inchiriere = datetime.now().strftime("%Y-%m-%d")

            self.rental_controller.adauga_rezervare(id_rezervare, id_client, id_carte, data_inchiriere)
            print(Fore.GREEN + "Rezervarea a fost adăugată cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Erroare: {e}" + Style.RESET_ALL)

    def sterge_rezervare(self):
        try:
            id_rezervare = input("ID-ul rezervării de șters: ")
            self.rental_controller.delete_rezervare(id_rezervare)
            print(Fore.GREEN + "Rezervarea a fost ștearsă cu succes!" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def afiseaza_rezervari(self):
        rezervari = self.rental_controller.get_all_rezervari()
        if not rezervari:
            print(Fore.YELLOW + "Nu există rezervări înregistrate." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Lista de rezervări:" + Style.RESET_ALL)
            for rezervare in rezervari:
                print(f"ID: {rezervare.get_id()}, Client ID: {rezervare.get_client_id()}, Carte ID: {rezervare.get_book_id()}")

    def menu_cautare_carte(self):
        try:
            id_carte = int(input("Introduceți ID-ul cărții: "))
            carte = self.book_controller.find_carte(id_carte)
            if carte:
                print(Fore.GREEN + "Carte găsită:" + Style.RESET_ALL)
                print(f"ID: {carte.get_id()}, Titlu: {carte.get_titlu()}, Autor: {carte.get_autor()}, Descriere: {carte.get_descriere()}")
            else:
                print(Fore.RED + f"Nu există carte cu ID-ul {id_carte}." + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def menu_cautare_client(self):
        try:
            id_client = int(input("Introduceți ID-ul clientului: "))
            client = self.client_controller.find_client(id_client)
            if client:
                print(Fore.GREEN + "Client găsit:" + Style.RESET_ALL)
                print(f"ID: {client.get_id()}, Nume: {client.get_nume()}, CNP: {client.get_cnp()}")
            else:
                print(Fore.RED + f"Nu există client cu ID-ul {id_client}." + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def sorteaza_carti(self):
        print(Fore.YELLOW + "\n-- Sortează cărțile --" + Style.RESET_ALL)
        print("1. După titlu (crescător)")
        print("2. După titlu (descrescător)")
        print("3. După autor (crescător)")
        print("4. După autor (descrescător)")

        optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()
        try:
            if optiune == "1":
                sorted_books = self.book_controller.merge_sort(key=lambda x: x.get_titlu(), reverse=False)
            elif optiune == "2":
                sorted_books = self.book_controller.merge_sort(key=lambda x: x.get_titlu(), reverse=True)
            elif optiune == "3":
                sorted_books = self.book_controller.merge_sort(key=lambda x: x.get_autor(), reverse=False)
            elif optiune == "4":
                sorted_books = self.book_controller.merge_sort(key=lambda x: x.get_autor(), reverse=True)
            else:
                print(Fore.RED + "Opțiune invalidă!" + Style.RESET_ALL)
                return

            print(Fore.GREEN + "Cărțile sortate:" + Style.RESET_ALL)
            for carte in sorted_books:
                print(f"ID: {carte.get_id()}, Titlu: {carte.get_titlu()}, Autor: {carte.get_autor()}")
        except ValueError as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def sorteaza_carti_bingo_sort(self):
        print(Fore.YELLOW + "\n-- Sortează cărțile folosind BingoSort --" + Style.RESET_ALL)
        try:
            self.book_controller.bingo_sort()  # Apelăm metoda bingo_sort
            print(Fore.GREEN + "Cărțile au fost sortate folosind BingoSort!" + Style.RESET_ALL)
            self.afiseaza_carti()  # Afișăm cărțile sortate
        except Exception as e:
            print(Fore.RED + f"Eroare: {e}" + Style.RESET_ALL)

    def sorteaza_carti_quick_sort(self):
        print(Fore.YELLOW + "\n-- Sortează cărțile folosind Quick Sort --" + Style.RESET_ALL)
        print("1. După titlu (crescător)")
        print("2. După titlu (descrescător)")
        print("3. După autor (crescător)")
        print("4. După autor (descrescător)")

        optiune = input(Fore.BLUE + "Alegeți o opțiune: " + Style.RESET_ALL).strip()
        try:
            if optiune == "1":
                sorted_books = self.book_controller.quick_sort(key=lambda x: x.get_titlu(), reverse=False)
            elif optiune == "2":
                sorted_books = self.book_controller.quick_sort(key=lambda x: x.get_titlu(), reverse=True)
            elif optiune == "3":
                sorted_books = self.book_controller.quick_sort(key=lambda x: x.get_autor(), reverse=False)
            elif optiune == "4":
                sorted_books = self.book_controller.quick_sort(key=lambda x: x.get_autor(), reverse=True)
            else:
                print(Fore.RED + "Opțiune invalidă!" + Style.RESET_ALL)
                return

            print(Fore.GREEN + "\nCărțile sortate folosind Quick Sort:" + Style.RESET_ALL)
            for carte in sorted_books:
                print(f"ID: {carte.get_id()}, Titlu: {carte.get_titlu()}, Autor: {carte.get_autor()}")

        except ValueError as e:
            print(Fore.RED + f"Erroare: {e}" + Style.RESET_ALL)
