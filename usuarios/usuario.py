class Usuario:

    # Constructor
    
    def __init__(self,nombre, apellido, email,password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    

    # Setters

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellido(self,apellido):
        self.apellido = apellido

    def setEmail(self,email):
        self.email = email

    def setPassword(self,password):
        self.password = password

     # Getters

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getEmail(self):
        return self.email 

    def getPassword(self):
        return self.password

    # Métodos

    def registrar(self): 
       return self.nombre

    def identificar(self):
         return self.nombre
    
