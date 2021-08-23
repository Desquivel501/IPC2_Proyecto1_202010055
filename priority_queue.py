class NodePQ:
    def __init__(self, valor = None ):
        self.valor = valor
        self.sig = None
        self.ant = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def push(self, dato):
        self.length += 1
        nuevo_nodo = NodePQ(dato)
        if self.head == None:
            self.head = nuevo_nodo
            return
        aux = self.head
        while(aux.sig != None):
            aux = aux.sig
        aux.sig = nuevo_nodo
        nuevo_nodo.ant = aux
        
    
    def pop(self):
        aux = self.head
        menor = aux
        while aux is not None:
            if int(aux.valor.valor.valor) > int(menor.valor.valor.valor):
                menor = aux
            aux = aux.sig
        if menor.sig is not None and menor.ant is not None:
            pre = menor.ant
            aft = menor.sig
            pre.sig = aft
            aft.ant = pre
            menor.ant = None
            menor.pre = None
        if menor.sig is not None and menor.ant is None:
            aft = menor.sig
            aft.pre = None
            aft = self.head
        if menor.ant is not None and menor.sig is None:
            pre = menor.ant
            pre.sig = None

    
        return menor.valor.valor
            
        