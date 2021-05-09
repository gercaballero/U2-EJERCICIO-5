import os
from claseAlumno import Alumno
from gestorAlumnos import Gestor

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, gestor):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(gestor)

    def salir(self, gestor):
        print('Salida del programa')

    def opcion1(self, gestor):
             os.system('cls')
             año=int(input('Ingrese AÑO: '))
             div=int(input('Ingrese DIVISION: '))
             gestor.listar(año,div)
             
    def opcion2(self, gestor):
             maximo= int(input("INGRESE MAXIMO DE ASITENCIAS: "))
             Alumno.cambiarMax(maximo)
             os.system('cls')
             print('~~~MAXIMO DE INASISTENCIAS ES {}~~~'.format(maximo))