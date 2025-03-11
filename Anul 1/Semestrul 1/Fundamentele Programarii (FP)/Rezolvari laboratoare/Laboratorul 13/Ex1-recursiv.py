def backtracking(monede, suma_finala, combinarile_curente, index):
    #Daca suma a ajuns la 5 afisam combinatiile de monede
    if suma_finala == 0:
        print(combinarile_curente)
        return


    # Daca suma e negativa sau am ajuns la sfarsitul listei, STOP
    if suma_finala < 0 or index == len(monede):
        return

    #Moneda curenta in combinatie si recursiv pentru restul
    backtracking(monede, suma_finala - monede[index], combinarile_curente + [monede[index]], index)

    # Fara a include moneda curenta ai recursiv pentru urmatoarele monede
    backtracking(monede, suma_finala, combinarile_curente, index + 1)


def gasire_combinatii(monede, suma_finala):
    if suma_finala <= 0:
        print("Suma nu poate fi platită.")
        return
    backtracking(monede, suma_finala, [], 0)

monede = [1, 2, 3]
suma_finala = 4
gasire_combinatii(monede, suma_finala)
