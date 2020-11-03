# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:47:16 2020

@author: Dayra
"""

class Array:
    def __init__( self , tam ):
        self.__datos = [ 0 for x in range(tam)]
    
    def get_item( self ,index ):
        dato = 0
        if index >= 0 and index < len(self.__datos):
            dato = self.__datos[index]
        else:
            print("Error en el indice") 
        return dato

    def set_item( self  , dato , index  ):
        if index >= 0 and index < len(self.__datos):
            self.__datos[index] = dato
        else:
            print("Error en el indice")

    def get_length(self):
	    return len(self.__datos)
    
    def clear( self , dato ):
        self.__datos = [dato for x in range(self.__tam)]

    def __iter__( self ):
        return _getIterator( self.__datos )


class _getIterator:
    def __init__( self , arreglo ):
        self.__arreglo = arreglo
        self.__indice_actual = 0

    def __iter__( self ):
        return self

    def __next__( self  ):
        if self.__indice_actual < len(self.__arreglo):
            dato = self.__arreglo[self.__indice_actual]
            self.__indice_actual +=1
            return dato
        else:
            raise StopIteration



