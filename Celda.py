class Celda:
    __item = None
    __sig = None

    def __init__(self, item) -> None:
        self.__item = item
        self.__sig = None
    
    def setSiguiente(self, sig):
        self.__sig = sig
    
    def getSiguiente(self):
        return self.__sig
    
    def getItem(self):
        return self.__item