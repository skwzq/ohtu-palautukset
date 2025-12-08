from abc import ABC, abstractmethod

class Komento(ABC):
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.edellinen_tulos = self.sovelluslogiikka.arvo()
        self.suorita_komento()
        Edellinen.komento = self

    @abstractmethod
    def suorita_komento(self):
        pass

    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self.edellinen_tulos)

class Summa(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita_komento(self):
        luku = 0

        try:
            luku = int(self.lue_syote())
        except Exception:
            pass

        self.sovelluslogiikka.plus(luku)

class Erotus(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita_komento(self):
        luku = 0

        try:
            luku = int(self.lue_syote())
        except Exception:
            pass

        self.sovelluslogiikka.miinus(luku)

class Nollaus(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita_komento(self):
        self.sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita_komento(self):
        Edellinen.komento.kumoa()

class Edellinen:
    komento = None
