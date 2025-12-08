class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        luku = 0

        try:
            luku = int(self.lue_syote())
        except Exception:
            pass

        self.sovelluslogiikka.plus(luku)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        luku = 0

        try:
            luku = int(self.lue_syote())
        except Exception:
            pass

        self.sovelluslogiikka.miinus(luku)

class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, lue_syote):
        pass

    def suorita(self):
        pass
