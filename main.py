"""

- Menú prncipal  login o registro.
- Registro , crea un nuevo usuario pala la BBDD.
- Login se ingresa con un usuario y se muestra el menú nota, mostrar notas, borrar notas.

"""


# Menú inicial

print("""

Menú inicial:
    [0]: Nuevo usuario
    [1]: Login

""")



accion = -1
while(accion != 0 and accion != 1):
    accion = int(input("\nSeleccione una opción: "))


if(accion == 0):
    print("\nRegistro de  usuarios")

    nombre = input("\nIngrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")
    password = input("Ingresee una contraseña: ")
elif accion == 1:
    print("\nIdentificarsee en el sistema")

    email = input("\nIngrese su email: ")
    password = input("Ingresee una contraseña: ")
