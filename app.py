import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from nodos import *
from encabezado import *
from matriz import *
from ruta import *
import linked_list_s as LL

terrenos = LL.LinkedList()
text = ""
root = ""


def leer(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    return root

def procesar(root, nombre_terreno, tipo, path):
    found = False
    valido = False
    for elemento in root.findall("terreno"):
        if (nombre_terreno) == elemento.attrib["nombre"]: 
            found = True
            nombre = elemento.attrib["nombre"]
            columnas =  elemento.attrib["n"]
            filas =  elemento.attrib["m"]
            
            if int(filas) > 100 or int(columnas) > 100:
                print("ERROR: Las dimensiones del terreno son invalidas")
                break

            m = matriz(nombre)
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
                m.insertar(int(val_y), int(val_x), val)
            
            start_x = m.eColumnas.primero.accesoNodo.columna
            start_y = m.eColumnas.primero.accesoNodo.fila
            
            if (int(start_x) <= int(inicio_x) <= int(columnas)) and (int(start_y) <= int(inicio_y) <= int(filas)):
                pass
            else:
                print("ERROR: Posicion de inicio no valida")
                break
                
            if (int(start_x) <= int(fin_x) <= int(columnas)) and (int(start_y) <= int(fin_y) <= int(filas)):
                pass
            else:
                print("ERROR: Posicion final no valida")
                break
                         
            try:
                r = Ruta(int(inicio_x), int(inicio_y), int(fin_x), int(fin_y), m, filas, columnas, tipo, path)
                aux = r.buscar()
                terrenos.insertar(aux)

            except Exception as e:
                print("ERROR: Ha ocurrido un error al procesar el terreno")      
                print(e)
                print("") 
    
    if found is False:
        print("ERROR: No se ha encontrado el terreno con el nombre:", nombre_terreno)
    
def grafica(root,nombre_terreno):
    for elemento in root.findall("terreno"):
        if (nombre_terreno) == elemento.attrib["nombre"]: 
            nombre = elemento.attrib["nombre"]
            columnas =  elemento.attrib["n"]
            filas =  elemento.attrib["m"]
            
            if int(filas) > 100 or int(columnas) > 100:
                print("ERROR: Las dimensiones del terreno son invalidas")
                break
             
            m = matriz(nombre)
            
            for subelemento in elemento.findall("posicion"):
                val_x = subelemento.attrib["x"]
                val_y = subelemento.attrib["y"]
                val = subelemento.text
                m.insertar(int(val_y), int(val_x), val)
            
            m.renderizar()

archivo_cargado = False


while(True):
    print("")
    print("--------------------------------------------")
    print("|| Seleccione accion a realizar:          ||")
    print("|| 1. Cargar Archivo                      ||")
    print("|| 2. Procesar Archivo                    ||")
    print("|| 3. Escribir Archivo de salida          ||")
    print("|| 4. Mostrar datos del estudiante        ||")
    print("|| 5. Generar Grafica                     ||")
    print("|| 6. Salir                               ||")
    print("--------------------------------------------")
    res = input()

    if res == "1":
        try:
            
            filename = askopenfilename()
            root = leer(filename)
            
            archivo_cargado = True
            print("Se ha leido el archivo correctamente")
            print("")
        except Exception as e:
            print("ERROR: No se ha podido leer el archivo")
            print(e)    
            print("")       

    elif res == "2" and archivo_cargado:
        
        try:
            nombre = input("Ingrese el nombre del terreno a procesar: ")
            procesar(root, nombre, "imprimir", None)
        except Exception as e:
            print("ERROR: Ha ocurrido un error al procesar el archivo")
            print(e)
            print("")
        
               
    elif res == "3" and archivo_cargado:
        try:
            nombre = input("Ingrese el nombre del que desea generar el archivo: ")
            path = input("Ingrese la ruta donde desea guardar el archivo: ")
            procesar(root, nombre, "xml", path)
           
        except Exception as e:
            print("ERROR: Ha ocurrido un error al generar el reporte") 
            print(e)
            
    elif res == "4":
        print("Derek Esquivel Diaz")
        print("202010055")
        print("Introduccion a la programacion y computacion 2 \"B\"")
        print("Ingenieria en Ciencias y Sistemas")
        print("4to Semestre")
        
    elif res == "5" and archivo_cargado:    
        try: 
            nombre = input("Ingrese el nombre del terreno del cual desea realizar una grafica: ")
            grafica(root, nombre) 
        except Exception as e:
            print("ERROR: ",e)
                
    elif res == "6":
        quit()
    
    elif res == "2" or res == "3" or res=="5" and archivo_cargado == False:
        print("ERROR: No se ha cargado ningun archivo")
         
    else:
        print("ERROR: Opcion no valida")