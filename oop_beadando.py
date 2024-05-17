from abc import ABC, abstractmethod
from datetime import date, datetime

class Szoba(ABC):
    def __init__(self, szam, ar):
        self.szam = szam
        self.ar = ar

    @abstractmethod
    def szoba_tipus(self):
        pass
class EgyagyasSzoba(Szoba):
    def __init__(self, szam):
        super().__init__(szam, 10000)

    def szoba_tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def __init__(self, szam):
        super().__init__(szam, 15000)

    def szoba_tipus(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_felvetel(self, szoba):
        if szoba not in self.szobak:
            self.szobak.append(szoba)
        else:
            print(f"A {szoba.szam} számú szoba már létezik a szállodában.")

    def elerheto_szobak(self, datum):
        
        foglalt_szobak = set()
        for f in foglalasok:
            if f.datum == datum:
                foglalt_szobak.add(f.szoba_szam)
                
        elerheto_szobak = []
        for szoba in self.szobak:
            if szoba.szam not in foglalt_szobak:
                elerheto_szobak.append(szoba)
        
        return elerheto_szobak
    
class Foglalas:
    def __init__(self, szoba_szam, datum):
        self.szoba_szam = szoba_szam
        self.datum = datum

foglalasok = []

def szoba_fogalalas(szalloda, szoba_szam, datum):
    if datum <= date.today():
        return 'Kérem adjon meg jövőbeni dátumot!'
    elerheto_szobak = szalloda.elerheto_szobak(datum)
    for szoba in elerheto_szobak:
        if szoba_szam == szoba_szam:
            uj_foglalas = Foglalas(szoba_szam, datum)
            foglalasok.append(uj_foglalas)
            return f"Gratulálunk, foglalása sikeres volt! Foglalásának összege: {szoba.ar} Ft"