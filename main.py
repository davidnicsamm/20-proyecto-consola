"""

- Menú prncipal  login o registro.
- Registro , crea un nuevo usuario pala la BBDD.
- Login se ingresa con un usuario y se muestra el menú nota, mostrar notas, borrar notas.

"""
# Importar paquetes

from usuarios import acciones


#creación del objeto acción de un usuario.
accion = acciones.Acciones()




# Menú inicial

print("""

Menú inicial:
    [0]: Nuevo usuario
    [1]: Login

""")



opcion = -1
while(opcion != 0 and opcion != 1):
    opcion = int(input("\nSeleccione una opción: "))



if(opcion == 0):
    accion.registro()
    
elif opcion == 1:
    accion.login()




    
