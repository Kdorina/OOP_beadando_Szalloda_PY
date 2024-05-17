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
    return "Sajnálattal közöljük, a szoba nem elérhető a kiválaszott dátumon"

def foglalas_lemondas(szoba_szam, datum):
    for foglalas in foglalasok:
        if foglalas.szoba_szam == szoba_szam and foglalas.datum == datum:
            foglalasok.remove(foglalas)
            return "Fogalalását sikeresen lemondta!"
    return "Nincs ilyen foglalás!"

def foglalas_listazas():
    foglalas_lista = []
    for f in foglalasok:
        foglalas_lista.append(f"Szoba: {f.szoba_szam}, Dátum: {f.datum}")
    return foglalas_lista

def felhasznaloi_interfesz():
    while True:
        print("1. Foglalás létrehozása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Kérem válasszon egy műveletet: ")

        if valasztas == "1":
            szoba_szam = int(input("Szoba száma: "))
            datum = input("Dátum (YYYY-MM-DD): ")
            datum = datetime.strptime(datum, "%Y-%m-%d").date()
            print(szoba_fogalalas(szalloda, szoba_szam, datum))
        elif valasztas == "2":
            szoba_szam = int(input("Szoba száma: "))
            datum = input("Dátum (YYYY-MM-DD): ")
            datum = datetime.strptime(datum, "%Y-%m-%d").date()
            print(foglalas_lemondas(szoba_szam, datum))
        elif valasztas == "3":
            for foglalas in foglalas_listazas():
                print(foglalas)
        elif valasztas == "4":
            break
        else:
            print("Érvénytelen választás, kérem próbálja újra.")

szalloda = Szalloda("Pandora Grand Hotel")
szalloda.szoba_felvetel(EgyagyasSzoba(101))
szalloda.szoba_felvetel(KetagyasSzoba(102))
szalloda.szoba_felvetel(KetagyasSzoba(103))

foglalasok.append(Foglalas(101, date(2024, 5, 20)))
foglalasok.append(Foglalas(101, date(2024, 5, 21)))
foglalasok.append(Foglalas(102, date(2024, 5, 20)))
foglalasok.append(Foglalas(102, date(2024, 5, 21)))
foglalasok.append(Foglalas(103, date(2024, 5, 22)))
