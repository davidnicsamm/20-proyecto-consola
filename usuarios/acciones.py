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