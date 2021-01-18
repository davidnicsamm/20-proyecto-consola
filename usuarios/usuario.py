from baseDatos import conexion
import datetime
import hashlib #módulo para cifrado

class Usuario:
    # Constructor
    
    def __init__(self,nombre, apellido, email,password):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__password = password
    

    # Setters

    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setApellido(self,apellido):
        self.__apellido = apellido

    def setEmail(self,email):
        self.__email = email

    def setPassword(self,password):
        self.__password = password

     # Getters

    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido

    def getEmail(self):
        return self.__email 

    def getPassword(self):
        return self.__password

    # Métodos

    def registrar(self):

        try:     
            conn = conexion.Conexion("192.168.122.146","root","rootroot","master_python",3306)
            conn.conectar()      

            # Fecha actual
            fecha = datetime.datetime.now()
            fechaFormateada = fecha.strftime("%Y-%m-%d")

            # Cifrado de la contraseña

            #Elección de algoritmo de cifrado
            cifrado = hashlib.sha256() 

            # Cifrado de la contraseña
            cifrado.update(self.__password.encode('utf8')) # Este método recibe datos en bytes. Se codifica con el método encode



            # Se envían los datos para guardar

            #Se pasa el valor hexadecimal del del cifrado del password
            datos = [
                (self.__nombre, self.__apellido,self.__email,cifrado.hexdigest(),fechaFormateada)
            ]
            exito = conn.guardarDatos("INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)",datos)
            conn.cerrarConexion()
        except:
            exito = 0

        # 0 si no se guardó y <> 0 si se guardó con éxito
        return exito

    def identificar(self):
         return self.__nombre

    

    


