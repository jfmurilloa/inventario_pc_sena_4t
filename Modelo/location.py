class Ubicacion:
    def __init__(self,nom,desc,id=None):        
        self.__nombre=nom
        self.__descripcion=desc
        self.__id=id
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,val):
        self.__id=val   
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,val):
        self.__nombre=val
    
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self,val):
        self.__descripcion=val
    
    