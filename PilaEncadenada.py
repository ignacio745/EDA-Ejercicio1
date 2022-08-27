from Celda import Celda

class PilaEncadenada:
    __cabeza = None

    def __init__(self) -> None:
        self.__cabeza = None
    
    def apilar(self, elemento):
        unaCelda = Celda(elemento)
        unaCelda.setSiguiente(self.__cabeza)
        self.__cabeza = unaCelda
    
    def desapilar(self):
        item = self.__cabeza.getItem()
        self.__cabeza = self.__cabeza.getSiguiente()
        return item
    
    def vacia(self):
        return self.__cabeza==None