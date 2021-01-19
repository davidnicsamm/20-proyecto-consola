#Clase que contiene la funcionalidades del sistema
from usuarios import usuario

class Acciones:

    def registro(self):
        print("\nRegistro de  usuarios")

        nombre = input("\nIngrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        password = input("Ingresee una contraseña: ")

        user = usuario.Usuario(nombre,apellido,email,password)
        exito = user.registrar()

        if exito >=1:
            print("\nRegistro exitoso !!!")
        else:
            print("\nEl registro no se pudo realizar. Verifique los datos.")



    def login(self):
        print("\nIdentificarsee en el sistema")
        email = input("\nIngrese su email: ")
        password = input("Ingresee una contraseña: ")

        user = usuario.Usuario('','',email,password)
        
        exito = user.identificar();

        if exito == 1:
            print("\nLogin exitoso")
            self.__proximasAcciones(email)
        else:
            print("\nFalo en el login, intente más tarde", exito)

        
    def __proximasAcciones(self,usuario):

        notas = {
            0: "crearNota",
            1: "mostrarNotas",
            2: "eliminarNota",
            3: "salir"

        }

      
        print("""

        Menú de usuario:
        [0] Crear Nota
        [1] Mostrar notas
        [2] Eliminar nota
        [3] Salir

        
        """)

        opcion = int(input("\nSeleccione una opción: "))
        func = notas.get(opcion, lambda: "Opción inválida")

        print("Opción: " + func)


        