#Clase que contiene la funcionalidades del sistema
from usuarios import usuario
from notas import acciones

class Acciones:

    def registro(self):
        print("\nRegistro de  usuarios")

        nombre = input("\nIngrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        password = input("Ingresee una contraseña: ")

        user = usuario.Usuario(nombre,apellido,email,password)
        resultado = user.registrar()

        if resultado[0] >=1:
            print("\nRegistro exitoso !!!")
        else:
            print("\nEl registro no se pudo realizar. Verifique los datos.")



    def login(self):
        print("\nIdentificarsee en el sistema")
        email = input("\nIngrese su email: ")
        password = input("Ingresee una contraseña: ")

        user = usuario.Usuario('','',email,password)
        
        resultado = user.identificar(); #Recibe registro obtenido

        if resultado != None:
            print("\nLogin exitoso")
            self.__proximasAcciones(resultado)
        else:
            print("\nFalo en el login, intente más tarde")

    


    def __elegirFuncionNota(self,opcion,accionNota):

        accionesNotas = {
            0: accionNota.crear,
            1: accionNota.mostrar,
            # 2: accionNota.eliminar(),
        }

        func = accionesNotas.get(opcion)   
         
        return func

        
    def __proximasAcciones(self,usuario):

        accionNota = acciones.Acciones()
       
        print("""

        Menú de usuario:
        [0] Crear Nota
        [1] Mostrar notas
        [2] Eliminar nota
        [3] Salir
        
        """)
        opcion = int(input("\nSeleccione una opción: "))


        while opcion != 3:           
           
            funcionNota = self.__elegirFuncionNota(opcion,accionNota)
            if funcionNota is not None:            
                funcionNota(usuario)
               
            else:
                print("\nNo existe la opción selecionada")

            print("""

            Menú de usuario:
            [0] Crear Nota
            [1] Mostrar notas
            [2] Eliminar nota
            [3] Salir
            
            """)

            opcion = int(input("\nSeleccione una opción: "))

           
           

           

           


      
        
       
        

        