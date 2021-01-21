import mysql.connector


class Conexion:
    __database = None
    __cursor = None


    # Constructor

    def __init__(self):
        self.__database = mysql.connector.connect(          
            host = "192.168.122.146",
            user = "root",
            passwd = "rootroot",
            database = "master_python",
            port = 3306
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


    def consultarDato(self,consulta,datos):
        
        try:
            self.__cursor.execute(consulta,datos)           
            result = self.__cursor.fetchone()           
        except:
            result = None       
        return result

    
    def consultarDatos(self,consulta,datos):
        print(datos)
            
        try:

            if datos is not None:
                self.__cursor.executemany(consulta,datos) 
            else:
                self.__cursor.execute(consulta)

            result = self.__cursor.fetchall()           
        except Exception as e:
            print("Fallo consulta",e)
            result = None       
        return result



    def eliminarDatos(self,consulta): 
        print(f"SQL: {consulta}")
        self.__cursor.execute(consulta)
        
        
        self.__database.commit()
        resultado = self.__cursor.rowcount
        print(f"Resultado: {resultado}")
        #return resultado.fetchone()
        
        return resultado

    

