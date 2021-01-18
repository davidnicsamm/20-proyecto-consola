import mysql.connector


class Conexion:
    __database = None
    __cursor = None


    # Constructor

    def __init__(self,host,user,passwd,database, port):
        self.__database = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = database,
            port = port
        )
       
       
    # Conectar
    def conectar(self):
        self.__cursor = self.__database.cursor(buffered=True)  

    # Cerrar conexión
    def cerrarConexion(self):
        self.__database.close() 





    # Interacción 


    def guardarDatos(self,consulta,datos):
        # self.__cursor.execute(consulta)
        #self.__cursor.execute("insert into usuarios(nombre,apellido,email,password,fecha) values('david','samm','sfsf@sdfsf.com',1,'2021-01-01')")
        self.__cursor.executemany(consulta,datos)
        self.__database.commit()
        return self.__cursor.rowcount


    def consultarDatos(self,consulta):
        self.__cursor.execute(consulta)
        return self.__cursor.rowcount


    def eliminarDatos(self,consulta): 
        self.__cursor.execute(consulta)
        return self.__cursor.rowcount 


    

