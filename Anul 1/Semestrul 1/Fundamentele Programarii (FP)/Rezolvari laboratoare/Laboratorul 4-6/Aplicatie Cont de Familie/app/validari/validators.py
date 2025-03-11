def validare_zi(zi):
    if 1 <= zi <= 31:
        return True
    raise ValueError("Ziua trebuie să fie între 1 și 31.")

def validare_suma(suma):
    if suma > 0:
        return True
    raise ValueError("Suma trebuie să fie un număr pozitiv.")

def validare_tip(tip):
    categorii_cheltuieli = ["mancare", "intretinere", "imbracaminte", "telefon", "altele"]
    if tip in categorii_cheltuieli:
        return True
    raise ValueError("Tipul cheltuielii este invalid. Alege dintre: mancare, intretinere, imbracaminte, telefon, altele.")