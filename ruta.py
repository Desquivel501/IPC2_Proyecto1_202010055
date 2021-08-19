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
        print(self.inicio_x, self.inicio_y)
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
        
        aux = inicial
        lista_ruta.insertar(inicial)
        # print("Final", final.fila, final.columna)
        
        first_pass = True
        
        cont = 0
        print("Inicio", inicial.columna, inicial.fila)
        while (aux.fila != self.final_y) and (aux.columna != self.final_x):
            
            if int(aux.fila) == int(self.final_y) and int(aux.columna) == int(self.final_x):
                break
            
            lista_aux = LL.LinkedList()
            
            if first_pass != True:
                
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and aux.abajo != None:
                    if (aux.abajo.fila == recorrido.y) and (aux.abajo.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                if pasado == False and aux.abajo != None:
                    lista_aux.insertar(aux.abajo) 
                    
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and aux.derecha != None:
                    if (aux.derecha.fila == recorrido.y) and (aux.derecha.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                if pasado == False and aux.derecha != None:
                    lista_aux.insertar(aux.derecha)
                                
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and aux.arriba != None:
                    if (aux.arriba.fila == recorrido.y) and (aux.arriba.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                if pasado == False and aux.arriba != None:
                    lista_aux.insertar(aux.arriba)
                
                recorrido =  lista_ruta.head   
                pasado = False
                while recorrido.sig != None and aux.izquierda != None:
                    if (aux.izquierda.fila == recorrido.y) and (aux.izquierda.columna == recorrido.x):
                        pasado = True
                        break
                    recorrido = recorrido.sig
                if pasado == False and aux.izquierda != None:
                    lista_aux.insertar(aux.izquierda)
            
            else:
                if aux.derecha != None:
                    lista_aux.insertar(aux.derecha)
                if aux.abajo != None:
                    lista_aux.insertar(aux.abajo)
                if aux.izquierda != None:
                    lista_aux.insertar(aux.izquierda)
                if aux.arriba != None:
                    lista_aux.insertar(aux.arriba)

          
            temp = lista_aux.head
            menor = temp
            
            # print(temp.valor.valor)
            # print(menor.valor.valor)
            # break
            
            while temp != None:
                if int(temp.valor.valor) < int(menor.valor.valor):
                    menor = temp
                temp = temp.sig
            
            aux = menor.valor
            lista_ruta.insertar(aux)
            first_pass = False
            cont += 1
            print("Nuevo",aux.columna,aux.fila)
            
        
        lista_ruta.imprimir()
            
