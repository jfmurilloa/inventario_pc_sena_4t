import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from Modelo.cuentadante import *
from Modelo.location import *

class Dao:
    def __init__(self,db):
        self.db = db
    
    def crear_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular)
        insert='insert into cuentadante(documento,nombres,apellidos,correo,celular) values(%s,%s,%s,%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo registro','El cuentadante ha sido almacenado!!!')
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
    
    def buscar_cuentadante(self,doc):
        criterio=(doc,)
        select='select * from cuentadante where documento= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_cue= self.db.cursor.fetchone()
            return obj_cue
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_cuentadante(self,obj:Cuentadante):
        val=(obj.documento,obj.nombres,obj.apellidos,obj.correo,obj.celular,obj.id)
        update= 'update cuentadante set documento=%s, nombres=%s, apellidos=%s, correo=%s, celular=%s where id=%s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
    
    def eliminar_cuentadante(self,obj:Cuentadante):
        rta=messagebox.askquestion('Eliminar','Esta seguro de eliminar el registro?')
        if rta=='yes':
            delete='delete from cuentadante where id=%s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado')
                return True
            except mysql.connector.Error as e:
                messagebox.showerror('Eliminar',e)
                return False
    
    #CRUD ubicacion
    def crear_ubicacion(self,obj:Ubicacion):
        val=(obj.nombre,obj.descripcion)
        insert='insert into ubicacion(nombre,descripcion) values(%s,%s)'
        try:
            self.db.cursor.execute(insert,val)
            self.db.connection.commit()
            messagebox.showinfo('Nuevo registro','La ubicación ha sido almacenada!!!')
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
    
    def buscar_ubicacion(self,nom):
        criterio=(nom,)
        select='select * from ubicacion where nombre= %s'
        try:
            self.db.cursor.execute(select,criterio)
            obj_ubi= self.db.cursor.fetchone()
            return obj_ubi
        except mysql.connector.Error as e:
            messagebox.showerror('Error',e)
            return None
    
    def modificar_ubicacion(self,obj:Ubicacion):
        val=(obj.nombre,obj.descripcion,obj.id)
        update= 'update ubicacion set nombre=%s, descripcion=%s where id=%s'
        try:
            self.db.cursor.execute(update,val)
            self.db.connection.commit()
            messagebox.showinfo('Update','El registro ha sido modificado...')
        except mysql.connector.Error as e:
            messagebox.showerror('Update',e)
    
    def eliminar_ubicacion(self,obj:Ubicacion):
        rta=messagebox.askquestion('Eliminar','Esta seguro de eliminar el registro?')
        if rta=='yes':
            delete='delete from ubicacion where id=%s'
            try:
                self.db.cursor.execute(delete,(obj.id,))
                self.db.connection.commit()
                messagebox.showinfo('Eliminar','El registro ha sido eliminado')
                return True
            except mysql.connector.Error as e:
                messagebox.showerror('Eliminar',e)
                return False



