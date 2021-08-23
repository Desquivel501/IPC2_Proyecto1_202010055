class NodeLL:
    def __init__(self, valor = None ):
        self.valor = valor
        self.sig = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def imprimir(self):
        printval = self.head
        while printval != None:
            print(printval.valor)
            printval = printval.sig
    
    def insertar(self, valor_nuevo):
        nuevo = NodeLL(valor_nuevo)
        if self.head == None:
            self.head = nuevo
            return
        aux = self.head
        while(aux.sig != None):
            aux = aux.sig
        aux.sig = nuevo