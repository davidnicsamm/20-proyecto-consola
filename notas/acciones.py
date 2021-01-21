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
        print(f"Notas del usuario: {usuario[1]}")
        notaUsuario = nota.Nota(usuario[0],"","")
        notas = notaUsuario.listar()
        print(notas)



           

