def exercitiu_1(numar):
    ok = 0; k = numar+1
    while ok == 0:
        if este_prim(k):
            print('ceva ', k)
            ok = 1
        k += 1
    return k-1

def este_prim(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input("Introdu numarul:"))
    rezultat = exercitiu_1(n)
    print(f"Primul numar prim mai mare decat numarul {n} este: {rezultat}")