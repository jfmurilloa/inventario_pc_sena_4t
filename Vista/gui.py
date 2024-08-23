from tkinter import *
from tkinter import messagebox
from Controlador.conexion import *
from Controlador.logic import *

#variables globales para utilizar el paquete de control
db=DataBase()
obj_dao=Dao(db)

class VentanaPrincipal:
    def __init__(self,val):
        self.root= val
        self.root.title('Formulario Principal')
        self.root.config(bg='burlywood')
        self.root.state('zoomed')

        #Controles como atributos

        #Crear menu de opciones
        self.barraMenu= Menu(self.root)
        self.root.config(menu=self.barraMenu, width=600, height=600)

        #Opciones dentro de cada menu
        self.cuentadanteMenu= Menu(self.barraMenu, tearoff=0)
        self.cuentadanteMenu.add_command(label='Admon_Cuentadantes',command=self.frm_cuentadante)

        #Generar las cascadas en la barraMenu
        self.barraMenu.add_cascade(label='Cuentadantes', menu=self.cuentadanteMenu)

        #Variables vinculadas
        self.caja1=StringVar()
        self.caja2=StringVar()
        self.caja3=StringVar()
        self.caja4=StringVar()
        self.caja5=StringVar()
        self.caja6=StringVar()

        #Widgets para las ventanas secundarias
        self.txt_caja1=Entry()
        self.txt_caja2=Entry()
        self.txt_caja3=Entry()
        self.txt_caja4=Entry()
        self.txt_caja5=Entry()
        self.txt_caja6=Entry()

        #crear los botones
        self.btn_nuevo=Button()
        self.btn_buscar=Button()
        self.btn_modificar=Button()
        self.btn_eliminar=Button()

    
    def frm_cuentadante(self):
        ventana=Toplevel()
        ventana.title('Administración de Cuentadantes')
        ventana.config(width=500,height=500)

        # Para los controles se adapten mejor a la ventana
        ventana.columnconfigure(0, weight=1)
        ventana.rowconfigure(0, weight=25)
        ventana.columnconfigure(1, weight=2)
        ventana.rowconfigure(1, weight=1)

        frame1=Frame(ventana,bg='gray15')
        frame1.grid(row=0,column=0,sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=1,columnspan=1,sticky='nsew')

        lbl_id=Label(frame1,text='Id:', width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1,state='readonly')
        self.txt_caja1.grid(row=0,column=1)

        lbl_documento=Label(frame1,text='Documento:', width=15)
        lbl_documento.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2)
        self.txt_caja2.grid(row=1,column=1)

        lbl_nombres=Label(frame1,text='Nombres:', width=15)
        lbl_nombres.grid(row=2,column=0,padx=10,pady=10)
        self.txt_caja3=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja3)
        self.txt_caja3.grid(row=2,column=1)

        lbl_apellidos=Label(frame1,text='Apellidos:', width=15)
        lbl_apellidos.grid(row=3,column=0,padx=10,pady=10)
        self.txt_caja4=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja4)
        self.txt_caja4.grid(row=3,column=1)

        lbl_correo=Label(frame1,text='Correo:', width=15)
        lbl_correo.grid(row=4,column=0,padx=10,pady=10)
        self.txt_caja5=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja5)
        self.txt_caja5.grid(row=4,column=1)

        lbl_celular=Label(frame1,text='Celular:', width=15)
        lbl_celular.grid(row=5,column=0,padx=10,pady=10)
        self.txt_caja6=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja6)
        self.txt_caja6.grid(row=5,column=1)

        #controles del Frame2
        self.btn_nuevo=Button(frame2,width=10,font=('Arial',12,'bold'),text='Nuevo',bg='orange',bd=5,command=self.crear_cuentadante_v)
        self.btn_nuevo.grid(row=0,column=0,padx=10,pady=10)

        self.btn_buscar=Button(frame2,width=10,font=('Arial',12,'bold'),text='Buscar',bg='orange',bd=5)
        self.btn_buscar.grid(row=0,column=1,padx=10,pady=10)

        self.btn_modificar=Button(frame2,width=10,font=('Arial',12,'bold'),text='Modificar',bg='orange',bd=5)
        self.btn_modificar.grid(row=0,column=2,padx=10,pady=10)

        self.btn_eliminar=Button(frame2,width=10,font=('Arial',12,'bold'),text='Eliminar',bg='orange',bd=5)
        self.btn_eliminar.grid(row=0,column=3,padx=10,pady=10)

        ventana.focus()
        self.txt_caja2.focus()
        ventana.grab_set()
    
    def crear_cuentadante_v(self):
        if self.caja2.get() and self.caja3.get() and self.caja4.get() and self.caja5.get() and self.caja6.get() != '':
            obj_cuentadante=Cuentadante(self.caja2.get(),self.caja3.get(),self.caja4.get(),self.caja5.get(),self.caja6.get())
            obj_dao.crear_cuentadante(obj_cuentadante)
            self.limpiar()
        else:
            messagebox.showwarning('Error','Todos los campos son obligatorios...')
    
    def buscar_cuentadante_v(self):
        if self.caja2.get() != '':
            find_cuentadante= obj_dao.buscar_cuentadante(self.caja2.get())
            if find_cuentadante != None:
                obj_cue=Cuentadante(find_cuentadante[1],find_cuentadante[2],find_cuentadante[3],find_cuentadante[4],find_cuentadante[5],find_cuentadante[0])
            else:
                messagebox.showwarning('No encontrado','registro no encontrado...')
        else:
            messagebox.showwarning('No encontrado','debe ingresar un numero de cedula para la busqueda...')
            self.txt_caja2.focus()
    
    def limpiar(self):
        self.caja1.set('')
        self.caja2.set('')
        self.caja3.set('')
        self.caja4.set('')
        self.caja5.set('')
        self.caja6.set('')
        self.txt_caja2.focus()
    
    def buscar_cuentadante_v(self):
        if self.caja2.get() != '':
            pass
            



