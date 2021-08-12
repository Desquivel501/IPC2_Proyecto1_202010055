from nodos import Nodo, nodoEncabezado
from encabezado import listaEncabezado

class matriz:
    
    def __init__(self):
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado()
        
    def insertar(self,fila,columna,valor):
        nuevo = Nodo(fila,columna,valor)
        #insercion encabezado por filas
        
        eFila = self.eFilas.getEncabezado()
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
        
        
        eColumna = self.eColumnas.getEncabezado()
        if eColumna == None:
            eColumna = nodoEncabezado(fila)
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eFila)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.derecha = eColumna.accesoNodo
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



m = matriz()
#Parametros -> fila, columna, valor
m.insertar(1,0, "Derek")
m.insertar(2,0, "Luis")
m.insertar(3,1, "Mario")
m.insertar(1,1, "Javier")
m.insertar(0,0, "Federico")
m.insertar(3,0, "Paco")
m.insertar(2,2, "Pedro")




 
              