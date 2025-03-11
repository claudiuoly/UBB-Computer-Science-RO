def main():
    menu()


def citire_lista():
    lista = input("Introduceti lista de numere: ")
    lista = list(map(int, lista.split()))
    return lista


def afisare_lista(lista):
    for el in lista:
        print(el, end=" ")


def menu():
    lista = []
    while True:
        print("\n[1] pentru a citi o lista de numere")
        print("[2] pentru a afisa secventa maxima cu diferenta prima intre elemente consecutive")
        print("[3] pentru a afisa secventa cu suma maxima")
        print("[4] pentru a afisa toate numerele din lista")
        print("[0] pentru a iesi din aplicatie\n")
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            lista = citire_lista()
        elif optiune == 2:
            rezultat = secventa_diferenta_prima(lista)
            print("Secventa maxima cu diferenta prima intre elemente consecutive:", *rezultat)
        elif optiune == 3:
            rezultat = secventa_suma_maxima(lista)
            print("Secventa cu suma maxima:", *rezultat)
        elif optiune == 4:
            afisare_lista(lista)
        elif optiune == 0:
            break
        else:
            print("Optiune invalida")


def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def secventa_diferenta_prima(lista):
    if len(lista) < 2:
        return lista

    secventa_maxima = []
    secventa_curenta = [lista[0]]

    for i in range(1, len(lista)):
        if este_prim(abs(lista[i] - lista[i - 1])):
            secventa_curenta.append(lista[i])
        else:
            if len(secventa_curenta) > len(secventa_maxima):
                secventa_maxima = secventa_curenta.copy()
            secventa_curenta = [lista[i]]

    if len(secventa_curenta) > len(secventa_maxima):
        secventa_maxima = secventa_curenta.copy()

    return secventa_maxima


def secventa_suma_maxima(lista):
    if not lista:
        return []

    suma_maxima = float('-inf')
    suma_curenta = 0
    start = 0
    end = 0
    start_temp = 0

    for i in range(len(lista)):
        suma_curenta += lista[i]
        if suma_curenta > suma_maxima:
            suma_maxima = suma_curenta
            start = start_temp
            end = i
        if suma_curenta < 0:
            suma_curenta = 0
            start_temp = i + 1

    return lista[start:end + 1]


def test_este_prim():
    assert este_prim(2) == True
    assert este_prim(3) == True
    assert este_prim(4) == False
    assert este_prim(17) == True
    assert este_prim(25) == False
    assert este_prim(-7) == False
    print("Toate testele pentru este_prim au trecut!")


def test_secventa_diferenta_prima():
    assert secventa_diferenta_prima([]) == []
    assert secventa_diferenta_prima([2]) == [2]
    assert secventa_diferenta_prima([2, 4, 6, 8]) == [2, 4, 6, 8]
    print("Toate testele pentru secventa_diferenta_prima au trecut!")


def test_secventa_suma_maxima():
    assert secventa_suma_maxima([]) == []
    assert secventa_suma_maxima([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]
    assert secventa_suma_maxima([1, 2, 3, -2, 5]) == [1, 2, 3, -2, 5]
    assert secventa_suma_maxima([-1, -2, -3, -4]) == [-1]
    print("Toate testele pentru secventa_suma_maxima au trecut!")


def ruleaza_teste():
    test_este_prim()
    test_secventa_diferenta_prima()
    test_secventa_suma_maxima()
    print("Toate testele au trecut cu succes!")


if __name__ == "__main__":
    ruleaza_teste()
    main()