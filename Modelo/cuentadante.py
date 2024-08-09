class Cuentadante:
    def __init__(self,doc,nom,ape,cor,cel,id=None):
        self.__documento=doc
        self.__nombres=nom
        self.__apellidos=ape
        self.__correo=cor
        self.__celular=cel
        self.__id=id
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,val):
        self.__id=val
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self,val):
        self.__documento=val
    
    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self,val):
        self.__nombres=val
    
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self,val):
        self.__apellidos=val
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self,val):
        self.__correo=val
    
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self,val):
        self.__celular=val