# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:52:14 2020

@author: Dayra
"""
from Array import Array
from Empleado import Empleado

class Sueldos:
    def __init__( self ):
        self.__data = None
    
    
    
    def cargar_datos( self , ruta_archivo ):
        archivo = open( ruta_archivo , "rt" ,encoding='latin1' )
        lineas = archivo.readlines()
        archivo.close()
        self.__data = Array( len(lineas) -1 )
        # Su tarea
        datos = []
        
        #Dividiendo la informacion en 14 espacios de la lista
        for linea in lineas:
            datos.append(linea.split(','))
            
        #Eliminando el encabezado
        datos.pop(0)
        print(datos)
        
        #llenando la informacion a empleado y al Array
        for i in range(0,14):
            empleado = Empleado(datos[i][0],datos[i][1],datos[i][2],datos[i][3],datos[i][4],datos[i][5],datos[i][6])
            empleado.to_string()
            
            self.__data.set_item(empleado, i)
        
            
        print("-------------------------------------")
            # separar campos y casting de algunos campos
            # crear un objeto Empleado
            # cargar ese objeto a self.__data.set_item()
    
    def mayorMenosAntiguedad(self):
        #Mayor antiguedad
        mayor = self.__data.get_item(0).getAniosAntiguedad()
        mayores = []
        for i in range(self.__data.get_length()):
            
            if(mayor <= (self.__data.get_item(i).getAniosAntiguedad())):
                if(i == 0):
                    continue
                mayor = self.__data.get_item(i).getAniosAntiguedad()
                mayores.append(self.__data.get_item(i))

        print("Los empleados de mayor antiguedad son: ")
        for j in range(len(mayores)):    
            print(mayores[j].getNombre(), mayores[j].getApellidoPaterno(), mayores[j].getApellidoMaterno())
        print("-------------------------------------")                 
        #Menor antiguedad
        menor = self.__data.get_item(0).getAniosAntiguedad()
        menores = []
        for i in range(self.__data.get_length()):
            
            if(menor >= (self.__data.get_item(i).getAniosAntiguedad())):
                if(i == 0):
                    continue
                menor = self.__data.get_item(i).getAniosAntiguedad()
                menores.append(self.__data.get_item(i))

        print("\nLos empleados de menor antiguedad son: ")
        for j in range(len(menores)):    
            print(menores[j].getNombre(), menores[j].getApellidoPaterno(), menores[j].getApellidoMaterno())
        
        
        

    
ejemplo = Sueldos()
ejemplo.cargar_datos('junio.dat')
ejemplo.mayorMenosAntiguedad()


