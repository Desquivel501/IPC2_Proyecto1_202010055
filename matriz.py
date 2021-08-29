from nodos import Nodo, nodoEncabezado
from encabezado import listaEncabezado
import graphviz
import os
from pathlib import Path

class matriz:
    
    def __init__(self, nombre):
        self.nombre = nombre
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
        



    def renderizar(self):

        eFila = self.eFilas.primero
        
        graphviz = '''
        digraph L{
            node[shape=box fillcolor="#91d1c9" style =filled shape=ellipse]

            subgraph cluster_p{
                label= " ''' + self.nombre +  ''' "
                bgcolor = "#0C6399"
                edge[dir = "both"]
                
                '''
        contGrupo = 1
        contFila = 1
        while eFila is not None:
            actual = eFila.accesoNodo
            ancla = "nodo"+str(actual.columna)+"_"+str(actual.fila)
            while actual is not None:
                graphviz += '''nodo'''+str(actual.columna)+'''_'''+str(actual.fila)+'''[label = "'''+str(actual.valor)+'''", group='''+str(contGrupo)+ ''']\n'''
                if contGrupo !=  1:
                    graphviz += "nodo"+str(actual.columna-1)+"_"+str(actual.fila)+"->"+"nodo"+str(actual.columna)+"_"+str(actual.fila)+"\n"
                    graphviz += '''{rank=same; '''+ str(ancla) +''';nodo'''+str(actual.columna) +'''_'''+str(actual.fila) +'''}\n'''
                
                if contFila != 1:
                    graphviz += "nodo"+str(actual.columna)+"_"+str(actual.fila-1)+"->"+"nodo"+str(actual.columna)+"_"+str(actual.fila)+"\n"
                    
                contGrupo += 1
                actual = actual.derecha
            contGrupo = 1
            contFila+=1
            eFila = eFila.siguiente
                
        graphviz += '''        
            }
        }
        '''
        
        archivo = open('grafico.dot',"w+")
        archivo.write(graphviz)
        print("Archivo generado en: ", os.getcwd())
        archivo.close()

        os.system('dot -Tpng grafico.dot -o grafico.png')
    



        



 
              