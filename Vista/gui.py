from tkinter import *
from tkinter import messagebox

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
        frame1.grid(row=1,columnspan=1,sticky='nsew')

        frame2=Frame(ventana,bg='CadetBlue1')
        frame2.grid(row=0,column=0,sticky='nsew')

        lbl_id=Label(frame1,text='Id:', width=15)
        lbl_id.grid(row=0,column=0,padx=10,pady=10)
        self.txt_caja1=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja1)
        self.txt_caja1.grid(row=0,column=1)

        lbl_documento=Label(frame1,text='Documento:', width=15)
        lbl_documento.grid(row=1,column=0,padx=10,pady=10)
        self.txt_caja2=Entry(frame1,width=20,font=('Arial',12),textvariable=self.caja2)
        self.txt_caja2.grid(row=1,column=1)

        ventana.focus()
        ventana.grab_set()


