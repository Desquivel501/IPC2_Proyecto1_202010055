from nodos import Nodo, nodoEncabezado
from encabezado import listaEncabezado

class matriz:
    
    def __init__(self):
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado()
        
    def insertar(self,fila,columna,valor):
        nuevo = Nodo(fila,columna,valor)
 
        
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = nodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else: 
                actual = eFila.accesoNodo
                while  actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual
        
        
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = nodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else: 
                actual = eColumna.accesoNodo
                while  actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def mostrarFilas(self):
        eFila = self.eFilas.primero
        print('--------FILAS---------')
        while eFila != None:
            
            actual = eFila.accesoNodo
            print('\nFila ',actual.fila)
            print('Columna      Valor')
            
            while actual !=None:
                print(actual.columna,'          ',actual.valor)
                actual = actual.derecha

            eFila = eFila.siguiente
            
        print('---------FIN----------')

    def mostrarColumnas(self):
  
        eColumna = self.eColumnas.primero
        print('--------COLUMNAS---------')
        while eColumna != None:
            actual = eColumna.accesoNodo
            print('\nColumna ',actual.columna)
            print('Fila      Valor')
            while(actual != None):
                print(actual.fila, '        ',actual.valor)
                actual = actual.abajo
            eColumna = eColumna.siguiente
        print('---------FIN----------')




# m = matriz()
# #Parametros -> fila, columna, valor
# m.insertar(1, 0, "adolfo")
# m.insertar(2, 1, "brandon")
# m.insertar(0, 1, "daniel")
# m.insertar(1, 2, "eduardo")
# m.insertar(0, 2, "diego")
# m.insertar(0, 0, "javier")

# m.mostrarColumnas()
# print("")
# m.mostrarFilas()


 
              