class Tuomari:
    def __init__(self):
        self.voitot = {"eka": 0, "toka": 0, "tasan": 0}

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        voittaja = self._kumpi_voittaa(ekan_siirto, tokan_siirto)
        self.voitot[voittaja] += 1

    def __str__(self):
        return f"Pelitilanne: {self.voitot["eka"]} - {self.voitot["toka"]}\nTasapelit: {self.voitot["tasan"]}"

    def _kumpi_voittaa(self, eka, toka):
        if eka == toka:
            return "tasan"
        if (eka, toka) in [("k", "s"), ("s", "p"), ("p", "k")]:
            return "eka"

        return "toka"
