from domain.validare_carte import ValidatorCarte
from domain.validare_client import ValidatorClient
from domain.validare_rezervare import ValidatorRezervare
from repository.repository_carte import RepositoryCarti
from repository.repository_client import RepositoryClienti
from repository.repository_rezervare import RepositoryRezervari
from service.controller_carte import ControllerCarti
from service.controller_client import ControllerClienti
from service.controller_rezervare import ControllerRezervari
from tests.run_tests import run_tests_all
from ui.console import LibraryConsole
import sys


def main():
    #Rulează toate testele înainte de a porni aplicația
    tests_passed = run_tests_all()
    if not tests_passed:
        print("\nAplicația nu poate porni din cauza erorilor în teste.")
        sys.exit(1)

    print("\nPornire aplicație...\n")

    # Inițializarea validatorilor
    validator_carti = ValidatorCarte()
    validator_clienti = ValidatorClient()
    validator_rezervari = ValidatorRezervare()

    # Inițializarea repository-urilor cu fișiere specifice pentru producție
    repo_carti = RepositoryCarti("data/carti.txt")
    repo_clienti = RepositoryClienti("data/clienti.txt")
    repo_rezervari = RepositoryRezervari("data/rezervari.txt", repo_clienti, repo_carti)

    # Inițializarea controller-elor
    controller_carti = ControllerCarti(repo_carti, validator_carti)
    controller_clienti = ControllerClienti(repo_clienti, validator_clienti)
    controller_rezervari = ControllerRezervari(repo_rezervari, repo_clienti, repo_carti, validator_rezervari)

    # Inițializarea UI
    library_ui = LibraryConsole(controller_carti, controller_clienti, controller_rezervari)

    # Pornirea aplicației
    library_ui.run()


if __name__ == "__main__":
    main()
