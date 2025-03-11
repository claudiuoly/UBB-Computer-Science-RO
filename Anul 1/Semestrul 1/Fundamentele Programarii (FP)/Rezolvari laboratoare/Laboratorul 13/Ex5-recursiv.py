def genereaza_pronosticuri_recursiv(lista, index=0, lista_curenta=[]):
  if index == 3:
    if lista_curenta[-1] != 'x' and lista_curenta.count(1) <= 2:
      return [lista_curenta.copy()]
    else:
      return []

  rezultat = []
  for element in lista:
      lista_curenta.append(element)
      for sublista in genereaza_pronosticuri_recursiv(lista, index + 1, lista_curenta):
          rezultat.append(sublista)
      lista_curenta.pop()
  return rezultat

l = [1, 'x', 2]
rezultat = genereaza_pronosticuri_recursiv(l)
for r in rezultat:
    print(r)