# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:55:43 2020

@author: gallo
"""


class Empleado:
    def __init__( self , num , nom , pat , mat , he ,sb ,anio ):
        self.__num_trabajador = num
        self.__nombres = nom
        self.__paterno = pat
        self.__materno = mat
        self.__horas_extra = he
        self.__sueldo_base = sb
        self.__anio_ingreso = anio
    
    # get y set
    def getNumTrabajador(self):
        return self.__num_trabajador
    
    def getNombre(self):
        return self.__nombres

    def getApellidoPaterno(self):
        return self.__paterno
    
    def getApellidoMaterno(self):
        return self.__materno
    
    def getHorasExtra(self):
        return self.__horas_extra
    
    def getSueldoBase(self):
        return self.__sueldo_base
    
    def getAniosAntiguedad(self):
        return 2020 - int(self.__anio_ingreso)
    
    def setNumTrabajador(self, numero):
        self.__num_trabajador = numero
        
    def setNombre(self,nombre):
        self.__nombres = nombre
    
    def setApellidoPaterno(self, apellidoPat):
        self.__paterno = apellidoPat
    
    def setApellidoMaterno(self, apellidoMat):
        self.__materno = apellidoMat
        
    def setHorasExtra(self, horasExtra):
        self.__horas_extra = horasExtra
    
    def setSueldoBase(self, sueldo):
        self.__sueldo_base = sueldo
        
    def setAnioIngreso(self, anio):
        self.__anio_ingreso = anio
        
           

    # meétodos de uso gral : calculos  
    def calcularSueldos(self):
        sueldoTotal = 0
        horasCalc = float(self.getHorasExtra()) * 276.5
        aniosCalc = (float((self.getSueldoBase())) * 0.03) * self.getAniosAntiguedad()
        sueldoTotal = float(self.getSueldoBase()) + horasCalc + aniosCalc
        return sueldoTotal

    # to_string()
    def to_string(self):
        print("\nId Empleado: ", self.getNumTrabajador())
        print("Nombre: ", self.getNombre(), self.getApellidoPaterno(), self.getApellidoMaterno() )
        print("Anio Ingreso: ", self.__anio_ingreso, end="")
        print("Sueldo Total: ", self.calcularSueldos())