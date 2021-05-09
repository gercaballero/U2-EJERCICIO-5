
class Alumno:
    __nombre=''
    __año=0
    __division=0
    __inasistencias=0
    inasisMax=20
    clases=150
    def __init__(self,nombre='',año=0,division=0,inasistencias=0):
        if isinstance(nombre, str) and isinstance(año, int) and isinstance(division, int) and isinstance(inasistencias, int):
            self.__nombre=nombre
            self.__año=año
            self.__division=division
            self.__inasistencias=inasistencias
    
    @classmethod
    def max(cls):
        return int(cls.inasisMax)
    @classmethod
    def cambiarMax(cls,max):
        if isinstance(max, int):
            cls.inasisMax=max
    def __str__(self):
        if self.__nombre=='' or self.__año==0 or self.__division == 0 or self.__inasistencias==0:
            retorna=('[OBJETO MAL CREADO]')
        else:
            retorna=('NOMBRE: {} AÑO:{} DIVISION:{} INASISTENCIAS:{}'.format(self.__nombre,self.__año,self.__division,self.__inasistencias))
        return retorna
    def getName(self):
        return self.__nombre
    def getAño(self):
        return int(self.__año)
    def getDivision(self):
        return int(self.__division)
    def getInasistencias(self):
        return int(self.__inasistencias)
    def porcentaje(self):
        p=(self.getInasistencias()*100)/Alumno.max()
        return float(p)

