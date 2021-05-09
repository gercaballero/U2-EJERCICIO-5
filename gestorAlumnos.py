import csv
from claseAlumno import Alumno
import os

class Gestor:

    def __init__(self):
        self.__lista=[]

    def test(self):
        archivo=open('alumnos.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                alumno=Alumno(str(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]))
                self.__lista.append(alumno)
        archivo.close()
    
    
    def listar(self, año, divi):
        os.system('cls')
        print ('\tALUMNO           PORCENTAJE')
        for i in range(len(self.__lista)):
            if self.__lista[i].getAño()==año and self.__lista[i].getDivision()==divi:
                if self.__lista[i].getInasistencias()>=Alumno.max():
                    print('%20s   \t%7.2f'%(self.__lista[i].getName(),self.__lista[i].porcentaje())+' %')


