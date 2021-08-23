import nodo_ruta as NR
import linked_list_s as LL
import math
import priority_queue as PQ

class Ruta:
    
    def __init__(self, inicio_x, inicio_y, final_x, final_y, matriz,nombre, lim_x, lim_y):
        self.inicio_x = inicio_x
        self.inicio_y = inicio_y
        self.final_x = final_x
        self.final_y = final_y
        self.matriz = matriz
        self.nombre = nombre
        self.lim_x = lim_x
        self.lim_y = lim_y
        
    def buscar(self):
        print("Terreno: ", self.nombre) 
        print("Inicio", "x = ",self.inicio_x,"  ","y = ", self.inicio_y)
        print("Final" , "x = ",self.final_x,"  ","y = ", self.final_y)
       
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
        
        inicial.visitado = True
        nodo_actual = inicial
        
        lista_ruta = NR.ListaRuta()
        lista_ruta.insertar(nodo_actual,None,nodo_actual.valor)
        visitado = LL.LinkedList()
        
        while (nodo_actual.fila != self.final_y) or (nodo_actual.columna != self.final_x):     

            nodo_actual.visitado = True
            visitado.insertar(nodo_actual)
            caminos_disponibles = LL.LinkedList()
            peso_a_nodo_actual = lista_ruta.buscarPeso(nodo_actual)
            
            if nodo_actual.derecha != None:
                caminos_disponibles.insertar(nodo_actual.derecha)

            if nodo_actual.abajo != None:
                caminos_disponibles.insertar(nodo_actual.abajo)
                
            if nodo_actual.izquierda != None:
                caminos_disponibles.insertar(nodo_actual.izquierda)
                
            if nodo_actual.arriba != None:
                caminos_disponibles.insertar(nodo_actual.arriba)
                   
            aux = caminos_disponibles.head
            
            while aux is not None:
                peso = int(peso_a_nodo_actual) + int(aux.valor.valor)
                if lista_ruta.existe(aux.valor) == False:
                    lista_ruta.insertar(aux.valor,nodo_actual,peso)
                else:
                    peso_menor_actual = lista_ruta.buscarPeso(aux.valor)
                    if int(peso_menor_actual) > int(peso):
                        lista_ruta.insertar(aux.valor,nodo_actual,peso)
                aux = aux.sig 
            
            #lista_ruta.imprimir()
            siguientes_caminos = lista_ruta.noVisitados()
              
            
            if siguientes_caminos.vacia():
                return "Not Posible"
            
                       
            nodo_actual = siguientes_caminos.menor()
            
        ruta_final = LL.LinkedList()
        while nodo_actual is not None:
            ruta_final.insertar(nodo_actual)
            nodo_anterior = lista_ruta.buscarAnterior(nodo_actual)
            nodo_actual = nodo_anterior

        
        ruta_final.imprimir()
            