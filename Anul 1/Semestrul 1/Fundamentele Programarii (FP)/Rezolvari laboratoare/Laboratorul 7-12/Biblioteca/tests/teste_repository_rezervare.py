from domain.client import Client
from domain.carte import Carte
from domain.rezervare import Rezervare
from repository.repository_rezervare import RepositoryRezervari


def test_repository_rezervari():
    # Creăm obiecte de tip Client și Carte pentru teste
    client1 = Client(1, "Client 1", "1234567890123")
    client2 = Client(2, "Client 2", "2345678901234")
    carte1 = Carte(1, "Carte 1", "Descriere 1", "Autor 1")
    carte2 = Carte(2, "Carte 2", "DEscriere 2", "Autor 2")

    # Creăm obiecte de tip Rezervare
    rezervare1 = Rezervare(1, client1, carte1, "2024-11-01", "2024-11-10")
    rezervare2 = Rezervare(2, client2, carte2, "2024-11-05", "2024-11-15")

    # Creăm repository
    repo = RepositoryRezervari()

    # Testăm funcția store
    repo.store(rezervare1)
    repo.store(rezervare2)
    assert len(repo.get_all()) == 2, "Repository-ul trebuie să conțină 2 rezervări."

    # Testăm funcția store cu ID duplicat (ar trebui să dea eroare)
    try:
        repo.store(rezervare1)
        assert False, "Se aștepta o eroare la adăugarea unei rezervări cu ID duplicat"
    except ValueError as ve:
        assert str(ve) == "Există deja o rezervare cu acest id.", f"Eroare neașteptată: {str(ve)}"

    # Testăm funcția find
    found_rezervare = repo.find(1)
    assert found_rezervare == rezervare1, "Căutarea rezervării cu ID 1 ar trebui să returneze rezervarea corectă."

    # Căutăm o rezervare inexistentă
    found_rezervare = repo.find(999)
    assert found_rezervare is None, "Căutarea unei rezervări inexistente ar trebui să returneze None."

    # Testăm funcția update
    rezervare_actualizata = Rezervare(1, client1, carte1, "2024-11-01", "2024-11-12")
    repo.update(rezervare_actualizata)
    found_rezervare = repo.find(1)
    assert found_rezervare.get_data_returnare() == rezervare_actualizata.get_data_returnare(), \
        "Rezervarea nu a fost actualizată corect."

    # Testăm update cu ID inexistent
    rezervare_inexistenta = Rezervare(999, client2, carte2, "2024-11-10", "2024-11-20")
    try:
        repo.update(rezervare_inexistenta)
        assert False, "Se aștepta o eroare pentru actualizarea unei rezervări inexistentă"
    except ValueError as ve:
        assert str(ve) == "Nu există rezervare cu id dat.", f"Eroare neașteptată: {str(ve)}"

    # Testăm funcția delete
    repo.delete(1)
    assert len(repo.get_all()) == 1, "Repository-ul trebuie să conțină 1 rezervare după ștergere."

    # Testăm delete cu ID inexistent
    try:
        repo.delete(999)
        assert False, "Se aștepta o eroare pentru ștergerea unei rezervări inexistentă"
    except ValueError as ve:
        assert str(ve) == "Nu există rezervare cu id dat.", f"Eroare neașteptată: {str(ve)}"

    # Testăm funcția get_size
    assert repo.get_size() == 1, "Repository-ul ar trebui să conțină 1 rezervare."

    # Testăm funcția get_all
    rezervari = repo.get_all()
    assert len(rezervari) == 1, "get_all ar trebui să returneze o listă cu 1 rezervare."
    assert rezervari[0] == rezervare2, "Rezervările din repository nu sunt corecte."
