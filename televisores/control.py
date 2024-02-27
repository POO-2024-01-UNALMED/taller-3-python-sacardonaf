class Control:
    def enlazar(self, tv)->None:
        self._tv=tv
        self._tv.setControl(self)
    def getTv(self):
        return self._tv
    def setTv(self, tv)->None:
        self._tv=tv
    def turnOn(self)->None:
        self._tv.turnOn()
    def turnOff(self)->None:
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setCanal(self, canal:int):
        self._tv.setCanal(canal)
    def setVolumen(self, volumen:int):
        self._tv.setVolumen(volumen)