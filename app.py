import xml.etree.ElementTree as ET
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from nodos import *
from encabezado import *
from matriz import *

text = ""

m = matriz()

def leer():
    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()

    for elemento in root:
        print(elemento.tag)
        for subelemento in elemento:
            val_x = subelemento.attrib["x"]
            val_y = subelemento.attrib["y"]
            val = subelemento.text
        
            m.insertar(val_y, val_x, val)
    
    m.mostrarColumnas()
    m.mostrarFilas()

leer()