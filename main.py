from menu import Menu
from gestorAlumnos import Gestor
from claseAlumno import Alumno
import os
def test():
    #TEST CON DIFERENTES CREACIONES DE OBJETOS DE LA CLASE ALUMNO
    print('  -----------TEST DE ALUMNOS-----------')
    print('\n\n ALUMNO 1: CON DATOS CORRECTOS')
    a1=Alumno('ALUMNO 1', 5, 5, 30)                             #SOLO PERMITE MOSTRAR LOS DATOS DE                                                     
    print(a1)
    print('\n\n ALUMNO 2: CON TIPO DE DATOS INCORRECTOS')
    a2=Alumno(124, 'cinco', 'segunda', 30.4)                             #SOLO PERMITE MOSTRAR LOS DATOS DE                                                     
    print(a2)
    print('\n\n ALUMNO 3: SIN UN DATO')
    a3=Alumno()                                                                             
    print(a3)                                                    
    print('\n\n ALUMNO 4: CON DATOS FALTANTES')
    a4=Alumno('ALUMNO 4',5)                                                                             
    print(a4) 
    print('------------------------------------------\n')

if __name__=='__main__':
    t=str(input('DESEA PROBAR EL TEST (S/N) : '))
    if t.lower()=='s':
        test()
        input()
    os.system('cls')
    gestor=Gestor()
    gestor.test()
    menu= Menu()
    salir= False
    band=True
    while band:
            while not salir:
                        print("\n-------------------Menu-------------------")
                        print(' 1- Listado')
                        print(' 2- Modificar maximo asistencias')
                        print(' 3- Salir')
                        op= (input('\n INGRESE UNA OPCION: '))
                        if op in ('1','2','3','4'):
                             menu.opcion(int(op),gestor)
                             if op=='3':
                                 salir=True
                        else:
                            os.system('cls')
                            print ("\t---OPCION NO VALIDA---")
                        band = False