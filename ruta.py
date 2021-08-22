import nodo_ruta as NR
import linked_list_s as LL
import math

class Ruta:
    
    def __init__(self, inicio_x, inicio_y, final_x, final_y, matriz):
        self.inicio_x = inicio_x
        self.inicio_y = inicio_y
        self.final_x = final_x
        self.final_y = final_y
        self.matriz = matriz
        self.lista_ruta = NR.ListaRuta()
        
    def buscar(self):
        print("Inicio", "x = ",self.inicio_x,"  ","y = ", self.inicio_y)
        print("Final" , "x = ",self.final_x,"  ","y = ", self.final_y)
        lista_ruta = NR.ListaRuta()
        eColumna = self.matriz.eColumnas.primero
        eFila = self.matriz.eFilas.primero
        if eColumna == None:
            print("Matriz Vacia")
        
        out = False
        while eColumna != None and out == False:
            actual = eColumna.accesoNodo 
            if int(actual.columna) == int(self.inicio_x):
                while actual != None:
                    if int(actual.fila) == int(self.inicio_y):
                        out = True
                        break
                    actual = actual.abajo
            eColumna = eColumna.siguiente
               
        inicial = actual
        
        # while eColumna != None:
        #     actual = eColumna.accesoNodo 
        #     if int(actual.columna) == int(self.final_x)  and int(actual.fila) == int(self.final_y):
        #         print("here")
        #         break
        #     eColumna = eColumna.siguiente
        # final = actual
        
        inicial.visitado = True
        nodo_actual = inicial
        lista_ruta.insertar(inicial)
        # print("Final", final.fila, final.columna)
        
        first_pass = True
        cont = 0
        while (nodo_actual.fila != self.final_y) or (nodo_actual.columna != self.final_x) :
            
            if cont == 20:
                break

            caminos_disponibles = LL.LinkedList()

            if nodo_actual.derecha != None and nodo_actual.derecha.visitado == False:
                caminos_disponibles.insertar(nodo_actual.derecha)
            if nodo_actual.abajo != None and nodo_actual.abajo.visitado == False:
                caminos_disponibles.insertar(nodo_actual.abajo)
            if nodo_actual.izquierda != None and nodo_actual.izquierda.visitado == False:
                caminos_disponibles.insertar(nodo_actual.izquierda)
            if nodo_actual.arriba != None and nodo_actual.arriba.visitado == False:
                caminos_disponibles.insertar(nodo_actual.arriba)
          
            temp = caminos_disponibles.head
            menor = temp

            while temp != None:
                if (temp.valor.fila == self.final_y) and (temp.valor.columna == self.final_x):
                    menor = temp
                    break     
                if temp.valor.visitado == False:
                    if int(temp.valor.valor) < int(menor.valor.valor):
                        menor = temp
                temp = temp.sig
            
            nodo_actual = menor.valor
            nodo_actual.visitado = True 
            lista_ruta.insertar(nodo_actual)

                   
        lista_ruta.imprimir()
            
