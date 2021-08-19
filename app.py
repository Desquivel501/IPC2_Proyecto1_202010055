import xml.etree.ElementTree as ET
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from nodos import *
from encabezado import *
from matriz import *
from ruta import *

text = ""

m = matriz()

def leer():
    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()
    
    for elemento in root.findall("terreno"):
        for subelemento in elemento.findall("posicion"):
            val_x = subelemento.attrib["x"]
            val_y = subelemento.attrib["y"]
            val = subelemento.text
            m.insertar(val_y, val_x, val)
        break
            
    # m.mostrarColumnas()
    # m.mostrarFilas()
    
    r = Ruta(5,5,1,1,m)
    r.buscar()

    # actual = m.eColumnas.primero
    # t = actual.accesoNodo
    # print(t.fila)
    # h = t.abajo
    # l = h.abajo
    # print(l.valor, l.fila, l.columna)

leer()