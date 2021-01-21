from notas import nota

class Acciones:
    def crear(self,usuario):
        print("\nNueva Nota")

        titulo = input("\nTítulo de la nota: ")
        descripcion = input("Contenido de la nota: ")
       
        notaUsuario = nota.Nota(usuario[0],titulo,descripcion)
        resultado = notaUsuario.guardar()

        if resultado[0] >= 1:
            print("Nota guardada con éxito")
           
        else:
            print("La nota no pudo ser guardada")

    def mostrar(self,usuario):
        print(f"\nNotas del usuario: {usuario[1]}")
        notaUsuario = nota.Nota(usuario[0],"","")
        notas = notaUsuario.listar()

        for nota1 in notas:
            print("\n***************************************************")
            
            print(f"\n{nota1[4]}")
            print(f"{nota1[2]}")
            print(f"{nota1[3]}")
            print("***************************************************")
    
    def borrar(self,usuario):
        print("\nBorrar nota")
        
        titulo = input("Título de la nota a borrar: ")
        notaUsuario = nota.Nota(usuario[0],titulo,"")
        eliminar = notaUsuario.eliminar()

        if eliminar[0] >= 1:
            print(f"Nota \"{titulo}\" eliminada")
        else:
            print(f"Nota \"{titulo}\" no fué eliminada")




       



           

