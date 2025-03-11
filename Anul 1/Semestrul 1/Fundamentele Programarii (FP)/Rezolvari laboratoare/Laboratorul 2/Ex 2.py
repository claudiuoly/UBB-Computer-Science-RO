def main():
    print("Hello, World!")

def citire_lista():
    lista = input("Introduceti lista de numere: ")
    return lista

def numere_interval(lista):
    return [numar for numar in lista if 1 <= numar <= 10]

def numere_contra(lista):
    return [numar for numar in lista if numar < 0]

def menu():
    while True:
        print("[1] pentru a citi o lista de numere")
        print("[2] pentru a afisa numerele din intervalul [1,10]")
        print("[3] pentru a afisa oricare doua numere din lista cu semne contrare")
        print("[4] pentru a iesi din aplicatie")
        optiune = input("Introduceti optiunea: ")
        match optiune:
            case "1":
                lista = citire_lista()
            case "2":
                numere_interval = numere_interval(lista)
                print(numere_interval)
            case "3":
                numere_contra = numere_contra(lista)
                print(numere_contra)
            case "4":
                break
            case _:
                print("Optiune invalida")

if __name__ == '__main__':
    main()