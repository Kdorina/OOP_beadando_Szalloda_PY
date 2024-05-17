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
