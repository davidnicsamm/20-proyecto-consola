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
       
        # Captura fallo en la consulta
        try:
            self.__cursor.executemany(consulta,datos)
            self.__database.commit()
            result = self.__cursor.rowcount
        except: 
            result = 0   

        return result


    def consultarDatos(self,consulta):
        self.__cursor.execute(consulta)
        return self.__cursor.rowcount


    def eliminarDatos(self,consulta): 
        self.__cursor.execute(consulta)
        return self.__cursor.rowcount 


    

