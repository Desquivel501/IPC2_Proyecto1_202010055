import linked_list_s as LL

class nodoRuta:
    def __init__(self, valor_nuevo, valor_anterior, peso):
        self.valor = valor_nuevo
        self.sig = None
        self.visitado = False
        self.peso = peso
        self.anterior = valor_anterior

class ListaRuta:
    def __init__(self):
        self.head = None
    
    # def imprimir(self):
    #     printval = self.head
    #     gasolina = 0
    #     while printval != None:
    #         print("X: " + printval.x + "    " + "Y: " + printval.y + "    " + "GAS: " + printval.valor)
    #         gasolina += int(printval.valor)
    #         printval = printval.sig
    #     print("")
    #     print("Gasolina usada: " + str(gasolina))
    #     print("")
    #     print("")
    
    def imprimir(self):
        aux = self.head
        while aux != None:
            print("X: " + aux.valor.columna + "    " + "Y: " + aux.valor.fila + "    " + "GAS: " + aux.valor.valor)
            aux = aux.sig

    
    def insertar(self, valor_nuevo, valor_anterior, peso):
        temp = self.head
        existe = False
        while temp is not None:
            if int(temp.valor.columna) == int(valor_nuevo.columna) and int(temp.valor.fila) == int(valor_nuevo.fila):
                existe = True
                break
            temp = temp.sig

        if existe:
            temp.anterior = valor_anterior
            temp.peso = peso
            
        else:
            nuevo = nodoRuta(valor_nuevo, valor_anterior, peso)
            if self.head == None:
                self.head = nuevo
                return
            aux = self.head
            while(aux.sig != None):
                aux = aux.sig
            aux.sig = nuevo
    
    def buscarPeso(self, nodo):
        aux = self.head
        while aux is not None:
            if int(aux.valor.columna) == int(nodo.columna) and int(aux.valor.fila) == int(nodo.fila):
                break
            aux = aux.sig
        peso = aux.peso
        return peso
    
    def existe(self, nodo):
        aux = self.head
        while aux is not None:
            if int(aux.valor.columna) == int(nodo.columna) and int(aux.valor.fila) == int(nodo.fila):
                return True
            aux = aux.sig
        return False
    
    def noVisitados(self):
        aux = self.head
        no_visitados = LL.LinkedList()
        while aux is not None:
            if aux.valor.visitado is False:
                no_visitados.insertar(aux)
            aux = aux.sig
        return no_visitados
    
    def buscarAnterior(self, nodo):
        aux = self.head
        while aux is not None:
            if int(aux.valor.columna) == int(nodo.columna) and int(aux.valor.fila) == int(nodo.fila):
                return aux.anterior
            aux = aux.sig
        return None