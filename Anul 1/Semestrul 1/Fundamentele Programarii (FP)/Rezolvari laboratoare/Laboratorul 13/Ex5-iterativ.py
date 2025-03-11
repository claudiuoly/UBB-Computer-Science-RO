def genereaza_pronosticuri_iterativ(lista):
  rezultat = []
  for i in lista:
    for j in lista:
      for k in lista:
        if k != 'x':
          lista_temp = [i, j, k]
          cnt1 = 0
          for el in lista_temp:
            if el == 1:
              cnt1 += 1
          if cnt1 <= 2:
            rezultat.append(lista_temp)
  return rezultat

l = [1, 'x', 2]
rezultat= genereaza_pronosticuri_iterativ(l)
for r in rezultat:
    print(r)