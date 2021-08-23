class NodeLL:
    def __init__(self, valor = None ):
        self.valor = valor
        self.sig = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # def imprimir(self):
    #     printval = self.head
    #     while printval != None:
    #         print(printval.valor)
    #         printval = printval.sig
    
    def insertar(self, valor_nuevo):
        nuevo = NodeLL(valor_nuevo)
        if self.head == None:
            self.head = nuevo
            return
        aux = self.head
        while(aux.sig != None):
            aux = aux.sig
        aux.sig = nuevo
         
    def vacia(self):
        if self.head is None:
            return True
        return False
    
    def menor(self):
        aux = self.head
        menor = aux
        while aux is not None:
            if int(aux.valor.valor.valor) < int(menor.valor.valor.valor):
                menor = aux
            aux = aux.sig
        return menor.valor.valor
    
    def imprimir(self):
        printval = self.head
        gasolina = 0
        while printval != None:
            print("X: " + printval.valor.columna + "    " + "Y: " + printval.valor.fila + "    " + "GAS: " + printval.valor.valor)
            gasolina += int(printval.valor.valor)
            printval = printval.sig
        print("")
        print("Gasolina usada: " + str(gasolina))
        print("")
        print("")
        
    
    def print(self):
        aux = self.head
        while aux != None:
            print("X: " + aux.valor.valor.columna + "    " + "Y: " + aux.valor.valor.fila + "    " + "GAS: " + aux.valor.valor.valor)
            aux = aux.sig

        
