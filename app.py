import xml.etree.ElementTree as ET
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from nodos import *
from encabezado import *
from matriz import *
from ruta import *

text = ""


def leer():
    filename = askopenfilename()
    tree = ET.parse(filename)
    root = tree.getroot()
    
    
    for elemento in root.findall("terreno"):
        m = matriz()
        for i in elemento.findall("posicioninicio"):
            inicio_x = i.find("x").text
            inicio_y = i.find("y").text
        
        for j in elemento.findall("posicionfin"):
            fin_x = j.find("x").text
            fin_y = j.find("y").text
        
        for subelemento in elemento.findall("posicion"):
            val_x = subelemento.attrib["x"]
            val_y = subelemento.attrib["y"]
            val = subelemento.text
            m.insertar(val_y, val_x, val)
       
        r = Ruta(inicio_x, inicio_y, fin_x, fin_y, m)
        r.buscar()          
  

leer()