import time
import matriz
from colorama import Fore, Back, Style

class NodeLL:
    def __init__(self, valor = None ):
        self.valor = valor
        self.sig = None

class LinkedList:
    def __init__(self):
        self.head = None
    
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
    
    def imprimir(self, matriz):
        printval = self.head
        gasolina = 0
        print("--------------------------------------------")
        print("||       CALCULANDO LA MEJOR RUTA         ||")
        print("--------------------------------------------")
        time.sleep(0.7)
        while printval != None:
            print("X: " + str(printval.valor.columna) + "    " + "Y: " + str(printval.valor.fila) + "    " + "GAS: " + str(printval.valor.valor))
            gasolina += int(printval.valor.valor)
            printval = printval.sig
        print("")
        print("--------------------------------------------")
        print("||     CALCULANDO COMBUSTIBLE USADO       ||")
        print("--------------------------------------------")
        time.sleep(0.5)
        print("Gasolina usada: " + str(gasolina))
        print("")
        
        print("--------------------------------------------")
        print("||             CAMINO USADO               ||")
        print("--------------------------------------------")
        time.sleep(0.5)
        
        eFila = matriz.eFilas.primero
        if eFila == None:
            print("ERROR: Matriz Vacia")
            
        while eFila != None:
            actual = eFila.accesoNodo 
            while actual != None:
                if actual.valido:
                    print(Fore.BLUE + "| 1 |" + Style.RESET_ALL,  end=" " )
                else:
                    print("| 0 |", end=" ")
                actual = actual.derecha
            eFila = eFila.siguiente
            print("")
        
    
    def print(self):
        aux = self.head
        while aux != None:
            print("X: " + aux.valor.valor.columna + "    " + "Y: " + aux.valor.valor.fila + "    " + "GAS: " + aux.valor.valor.valor)
            aux = aux.sig

        
