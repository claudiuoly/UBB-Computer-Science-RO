def gasire_combinatii_iterativ(monede, suma_finala):
    if suma_finala <= 0:
        print("Suma nu poate fi platită.")
        return

    stack = [(suma_finala, [], 0)]  # (suma, combinatie curenta, indexul monedei curente)
    gasit_solutie = False

    while stack:
        suma_ramasa, combiantie_curenta, index = stack.pop()

        # Daca suma ramasa este 0 am gasit o combinatie
        if suma_ramasa == 0:
            print(combiantie_curenta)
            gasit_solutie = True
            continue

        # Daca suma devine negativa sau am ajuns la sfarsitul listei, continuam
        if suma_ramasa < 0 or index == len(monede):
            continue

        # Adaugam moneda curenta si continuam
        stack.append((suma_ramasa - monede[index], combiantie_curenta + [monede[index]], index))

        # Nu adaugam moneda curenta si trecem la urmatoarea
        stack.append((suma_ramasa, combiantie_curenta, index + 1))

    if not gasit_solutie:
        print("Suma nu poate fi platită.")


monede = [1, 2, 3]
suma_finala = 4
gasire_combinatii_iterativ(monede, suma_finala)
