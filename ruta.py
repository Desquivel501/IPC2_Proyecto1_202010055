import nodo_ruta as NR
import linked_list_s as LL

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
        
        nodo_actual = inicial
        lista_ruta.insertar(inicial)
        # print("Final", final.fila, final.columna)
        
        first_pass = True

        while (nodo_actual.fila != self.final_y) or (nodo_actual.columna != self.final_x):


            caminos_disponibles = LL.LinkedList()
            
            if first_pass != True:
                
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and nodo_actual.abajo != None:
                    if (nodo_actual.abajo.fila == recorrido.y) and (nodo_actual.abajo.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                
                omitir = False
                if (nodo_actual.columna == self.final_x) and int(self.final_y) < int(nodo_actual.fila):
                    omitir = True  
                
                if pasado == False and nodo_actual.abajo != None and omitir == False:
                    caminos_disponibles.insertar(nodo_actual.abajo) 
                    
                #-----------------------------------------------------------------------------------------------------------------------------
                    
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and nodo_actual.derecha != None:
                    if (nodo_actual.derecha.fila == recorrido.y) and (nodo_actual.derecha.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                    
                omitir = False
                if (nodo_actual.fila == self.final_y) and int(self.final_y) < int(nodo_actual.columna):
                    omitir = True  
                    
                if pasado == False and nodo_actual.derecha != None:
                    caminos_disponibles.insertar(nodo_actual.derecha)
                    
                #-----------------------------------------------------------------------------------------------------------------------------
                                
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and nodo_actual.arriba != None:
                    if (nodo_actual.arriba.fila == recorrido.y) and (nodo_actual.arriba.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                
                omitir = False
                if (nodo_actual.columna == self.final_x) and int(self.final_y) > int(nodo_actual.fila):
                    omitir = True  
                
                if pasado == False and nodo_actual.arriba != None and omitir == False:
                    caminos_disponibles.insertar(nodo_actual.arriba)
                
                #-----------------------------------------------------------------------------------------------------------------------------
                
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and nodo_actual.izquierda != None:
                    if (nodo_actual.izquierda.fila == recorrido.y) and (nodo_actual.izquierda.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                
                omitir = False
                if (nodo_actual.fila == self.final_y) and int(self.final_y) > int(nodo_actual.columna):
                    omitir = True  
                
                if pasado == False and nodo_actual.izquierda != None and omitir == False:
                    caminos_disponibles.insertar(nodo_actual.izquierda)
                
                #-----------------------------------------------------------------------------------------------------------------------------
            
            else:
                if nodo_actual.derecha != None:
                    caminos_disponibles.insertar(nodo_actual.derecha)
                if nodo_actual.abajo != None:
                    caminos_disponibles.insertar(nodo_actual.abajo)
                if nodo_actual.izquierda != None:
                    caminos_disponibles.insertar(nodo_actual.izquierda)
                if nodo_actual.arriba != None:
                    caminos_disponibles.insertar(nodo_actual.arriba)
          
            temp = caminos_disponibles.head
            menor = temp

            
            while temp != None:
                if int(temp.valor.valor) < int(menor.valor.valor):
                    menor = temp
                temp = temp.sig
            
            nodo_actual = menor.valor
            lista_ruta.insertar(nodo_actual)
            first_pass = False         
        
        lista_ruta.imprimir()
            
