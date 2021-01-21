from baseDatos import conexion

class Nota:
    def __init__(self, usuario_id,titulo,descripcion):
        self.__usuario_id = usuario_id
        self.__titulo = titulo
        self.__descripcion = descripcion

    def guardar(self):

        try:
            conn = conexion.Conexion()
            conn.conectar()            
            nota = [(self.__usuario_id,self.__titulo,self.__descripcion)]
            sql = "INSERT INTO notas VALUES(null,%s,%s,%s,NOW())" #Guarda la fecha con función now de mysql
            exito = conn.guardarDatos(sql,nota)            
            resultado = [exito,self]
            conn.cerrarConexion()            
        except:          
            resultado = [0,self]
            conn.cerrarConexion()
        return resultado


    def listar(self):

        try:           
            conn = conexion.Conexion()
            conn.conectar()
            sql = f"SELECT * FROM notas WHERE usuario_id = {self.__usuario_id} "
            resultado = conn.consultarDatos(sql,None)
            conn.cerrarConexion()

        except:
            resultado = None
            conn.cerrarConexion()

        return resultado

    def eliminar(self):
        try:
           
            conn = conexion.Conexion()
            conn.conectar()

            sql = f"DELETE FROM notas WHERE usuario_id = {self.__usuario_id} AND titulo LIKE \"%{self.__titulo}%\""
            exito = conn.eliminarDatos(sql)
            conn.cerrarConexion()
        except:
            exito = 0
            conn.cerrarConexion()
        
        return [exito,self]


    
        
        