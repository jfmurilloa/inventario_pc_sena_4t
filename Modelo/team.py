class Equipo:
    def __init__(self,ser,mar,fec_com,ven_gar,tipo,cla,id_cue,id_ubi,id_pro,id=None):
        self.__serial=ser
        self.__marca=mar
        self.__fecha_compra=fec_com
        self.__vencimiento_garantia=ven_gar
        self.__tipo=tipo
        self.__clasificacion=cla
        self.__id_cuentadante= id_cue
        self.__id_ubicacion=id_ubi
        self.__id_proveedor=id_pro
        self.__id=id

    @property
    def serial(self):
        return self.__serial
        
    @serial.setter
    def serial(self,ser):
        self.__serial=ser
        
    @property
    def marca(self):
        return self.__marca
        
    @marca.setter
    def marca(self,mar):
        self.__marca=mar

    @property
    def fecha_compra(self):
        return self.__fecha_compra
        
    @fecha_compra.setter
    def fecha_compra(self,fec_com):
        self.__fecha_compra=fec_com
        
    @property
    def vencimiento_garantia(self):
        return self.__vencimiento_garantia
        
    @vencimiento_garantia.setter
    def vencimiento_garantia(self,ven_gar):
        self.__vencimiento_garantia=ven_gar
        
    @property
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo
        
    @property
    def clasificacion(self):
        return self.__clasificacion
        
    @clasificacion.setter
    def clasificacion(self,cla):
        self.__clasificacion=cla
        
    @property
    def id_cuentadante(self):
        return self.__id_cuentadante
        
    @id_cuentadante.setter
    def id_cuentadante(self,ser):
        self.__id_cuentadante=ser
        
    @property
    def id_ubicacion(self):
        return self.__id_ubicacion
        
    @id_ubicacion.setter
    def id_ubicacion(self,ubi):
        self.__id_cuentadante=ubi
        
    @property
    def id_proveedor(self):
        return self.__id_proveedor
        
    @id_proveedor.setter
    def id_proveedor(self,pro):
        self.__id_proveedor=pro
        
    @property
    def id(self):
        return self.__id
        
    @id.setter
    def id(self,id):
        self.__id=id
        
       