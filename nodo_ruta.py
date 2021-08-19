class nodoRuta:
    def __init__(self, valor, x, y):
        self.valor = valor
        self.sig = None
        self.x = x
        self.y = y

class ListaRuta:
    def __init__(self):
        self.head = None
    
    def imprimir(self):
        printval = self.head
        gasolina = 0
        while printval != None:
            print("X: " + printval.x + "    " + "Y: " + printval.y + "    " + "GAS: " + printval.valor)
            gasolina += int(printval.valor)
            printval = printval.sig
        print("")
        print("Gasolina usada: " + str(gasolina))
    
    def insertar(self, valor_nuevo):
        nuevo = nodoRuta(valor_nuevo.valor, valor_nuevo.columna, valor_nuevo.fila)
        if self.head == None:
            self.head = nuevo
            return
        aux = self.head
        while(aux.sig != None):
            aux = aux.sig
        aux.sig = nuevo