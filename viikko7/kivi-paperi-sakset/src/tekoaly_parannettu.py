class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = []
        self._muistin_koko = muistin_koko

    def aseta_siirto(self, siirto):
        if len(self._muisti) == self._muistin_koko:
            self._muisti.pop(0)

        self._muisti.append(siirto)

    def anna_siirto(self):
        if len(self._muisti) <= 1:
            return "k"

        viimeisin_siirto = self._muisti[-1]

        siirtojen_maara = {"k": 0, "p": 0, "s": 0}

        for i in range(len(self._muisti) - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]
                siirtojen_maara[seuraava] += 1

        eniten = max(siirtojen_maara.items(), key=lambda x: x[1])[0]

        if eniten == "k":
            return "p"
        if eniten == "p":
            return "s"

        return "k"
