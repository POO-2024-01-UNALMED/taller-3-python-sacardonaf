class TV:
    _numTV=0
    def __init__(self, marca, estado:bool) -> None:
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None

        TV._numTV+=1

    @classmethod
    def getNumTV(cls)->int:
        return cls._numTV
    
    @classmethod
    def setNumTV(cls,numTV: int)->None:
        cls._numTV=numTV

    def getMarca(self):
        return self._marca
    def setMarca(self, marca)->None:
        self._marca=marca
    def getCanal(self)->int:
        return self._canal
    def setCanal(self,canal:int)->None:
        if self._canal>=1 and self._canal<=120:
            self._canal=canal
    def getPrecio(self)->int:
        return self._precio
    def setPrecio(self, precio)->None:
        self._precio=precio
    def getVolumen(self)->int:
        return self._volumen
    def setVolumen(self,volumen:int)->None:
        if self._volumen>=0 and self._volumen<=7:
            self._volumen=volumen
    def getControl(self):
        return self._control
    def setControl(self,control)->None:
        self._control=control
    def turnOn(self)->None:
        self._estado=True
    def turnOff(self)->None:
        self._estado=False
    def getEstado(self)->bool:
        return self._estado
    def canalUp(self)->None:
        if self._estado and self._canal>=1 and self._canal<=119:
            self._canal+=1
    def canalDown(self)->None:
        if self._estado and self._canal>=2 and self._canal<=120:
            self._canal-=1
    def volumenUp(self)->None:
        if self._estado and self._volumen>=0 and self._volumen<=6:
            self._volumen+=1
    def volumenDown(self)->None:
        if self._estado and self._volumen>=1 and self._volumen<=7:
            self._volumen-=1