class Nodo:
    def __init__(self, fila,columna,valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
        self.visitado = False
        
class nodoEncabezado:
    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None
        
        