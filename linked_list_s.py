import time
from colorama import Fore, Back, Style

from lxml import etree


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
        
    def reporte(self, nombre, inicio_x, inicio_y, final_x, final_y,filas, columnas, path):
        root = etree.Element('terreno')
        tree = etree.ElementTree(root)
        root.set('nombre',nombre)
        root.set('n',str(columnas))
        root.set('m',str(filas))

        posicionFinal = etree.Element('posicionInicio')
        root.append(posicionFinal)
        xFinal = etree.Element('x')
        xFinal.text = str(final_x)
        yFinal = etree.Element('y')
        yFinal.text = str(final_y)
        posicionFinal.append(xFinal)
        posicionFinal.append(yFinal)
        
        posicionInicio = etree.Element('posicionFinal')
        root.append(posicionInicio)
        xInicio = etree.Element('x')
        xInicio.text = str(inicio_x)
        yInicio = etree.Element('y')
        yInicio.text = str(inicio_y)
        posicionInicio.append(xInicio)
        posicionInicio.append(yInicio)
        
        combustible = etree.Element("combustible")
        root.append(combustible)
        aux = self.head
        gasolina = 0
        while aux != None:
            gasolina += int(aux.valor.valor)
            aux = aux.sig 
        combustible.text = str(gasolina)
        
        aux = self.head

        while aux != None:
            posicion = etree.Element("posicion")
            posicion.set('x',str(aux.valor.columna))
            posicion.set('y',str(aux.valor.fila))
            posicion.text = str(aux.valor.valor)
            root.append(posicion)
            aux = aux.sig 
            
        filename = path + "/" + nombre + ".xml"
        
        try:
            tree.write(filename, pretty_print=True)
            print("El archivo se ha generado exitosamente")
        except Exception as e:
            print("ERROR: ",e)
        

            
    

        
