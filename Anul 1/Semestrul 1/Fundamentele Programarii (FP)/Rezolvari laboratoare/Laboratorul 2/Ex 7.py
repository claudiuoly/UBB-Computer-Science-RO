def prim(numar):
    if numar < 2:
        return False
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False
    return True

def factorii_primi(n):
    factori = []
    for i in range(2, n + 1):
        if n % i == 0 and prim(i):
            factori.append(i)
    return factori

def produsul_factorilor_primi(n):
    factori = factorii_primi(n)
    produs = 1
    for factor in factori:
        produs *= factor
    return produs

if __name__ == '__main__':
    n = int(input("Introdu un numar: "))
    produs = produsul_factorilor_primi(n)
    print(f"Produsul tuturor factorilor primi ai lui {n} este {produs}")

# ( 7 - 1 ) + 4 = 10 si 7