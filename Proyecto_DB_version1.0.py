# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from Conexion import Conexion
from datetime import datetime
from PIL import Image, ImageTk
import tkinter.font as tkFont
import tkinter as tk
import tkinter.ttk as ttk
import pyodbc
import hashlib
import tkinter
from ttkthemes import ThemedTk
import ctypes

class Login:
    def __init__(self, window, title, w, h):

        self.w = w
        self.h = h
        self.x = int(window.winfo_screenwidth() / 5)
        self.y = int(window.winfo_screenheight() / 10)
        #self.x = 0
        #self.y = 0 
    
        self.window = window
        self.window.title(title)
        self.window.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        self.window.iconbitmap('images/icono.ico')
        self.window.configure(background = '#ffffff')
        #self.window.wm_attributes("-transparentcolor","#60b26c")
        #self.window.wm_attributes("-alpha",.9)

        def on_closing():
            if messagebox.askokcancel("Salir", "¿Estas seguro que quieres salir?"):
                self.window.destroy()

        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 550,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/background.png")
        background = self.canvas.create_image(375.0, 275.0,image=self.background_img)

        self.entry0_img = PhotoImage(file = f"images/img_textBox0.png")
        entry0_bg = self.canvas.create_image(400.0, 236.0,image = self.entry0_img)

        self.nombreIn = Entry(bd = 0,bg = "#c4c4c4",highlightthickness = 0, font = ("Tahoma", 14))
        self.nombreIn.place(x = 320.0, y = 216,width = 160.0,height = 38)
        self.nombreIn.bind("<Key>", self.key)
        self.nombreIn.bind("<FocusIn>", self.focus)
        self.nombreIn.bind("<FocusOut>", self.sinfocus)

        self.entry1_img = PhotoImage(file = f"images/img_textBox1.png")
        entry1_bg = self.canvas.create_image(400.0, 357.0,image = self.entry1_img)

        self.passwordIn = Entry(bd = 0,bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 14))
        self.passwordIn.place(x = 320.0, y = 337,width = 160.0,height = 38)
        self.passwordIn.bind("<Key>", self.key)
        self.passwordIn.bind("<FocusIn>", self.focus)
        self.passwordIn.bind("<FocusOut>", self.sinfocus)

        #--------------------------Boton---------------------------
        btn_inactive=Image.open(f"images/img0.png")
        btn_active=Image.open(f"images/img1.png")
        self.window.btn_inactive = ImageTk.PhotoImage(btn_inactive)
        self.window.btn_active = ImageTk.PhotoImage(btn_active)

        self.img0 = PhotoImage(file = f"images/img0.png")
        self.b0 = Button(self.window,image=self.window.btn_inactive,command = self.ingreso, borderwidth = 0, highlightthickness = 0,curso="hand2", relief = "flat")
        self.b0.place(x = 300, y = 411,  width = 200, height = 55)
        self.b0.bind("<Enter>",self.on_enter)
        self.b0.bind("<Leave>",self.on_leave)

    
    #///////////---------------Funciones visuales--------------//////////////////////////////
    def on_enter(self,event):
            self.b0.config(image=self.window.btn_active)

    def on_leave(self,event):
            self.b0.config(image=self.window.btn_inactive)

    def clear_entry(self, event):
        if event.widget == self.nombreIn:
            self.text1.set("")
        elif event.widget == self.passwordIn:
            self.text2.set("")

    def key(self, event):
        if event.char == "\r":
            if self.nombreIn.get().strip() != "" and self.passwordIn.get() != "":
                if self.user == self.nombreIn.get().strip() and self.passw == self.passwordIn.get():
                    messagebox.showinfo("Bienvenida", f"Bienvenido {self.nombreIn.get()}")
                    self.window.destroy()
                    window = Tk()
                    regProd = RegistrarProducto(window, "Registrar usuario", 650, 500)
                    window.mainloop()
                else:
                    messagebox.showinfo("Error", "Usuario o contraseña incorrectos.")
            else:
                messagebox.showinfo("Error", f"Se deben llenar todos los campos")
        else:
            pass

    def focus(self, event):
        if event.widget == self.b0:
            self.passwordIn.configure(state = "active")
        else:
            event.widget.configure(foreground = "white")

    def sinfocus(self, event):
        if event.widget == self.b0:
            self.passwordIn.configure(state = "normal")
        else:
            event.widget.configure(foreground = "black")

    def ingreso(self):
        NombreUsuarioAdmin = "admin"
        PasswordAdmin = "ROOT1747264"
        self.db = Conexion()
        try:
            self.db.conectar()
        except:
            print("Error al conectar")

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Empleados").fetchall()
        count1=0
        for row in self.recogerinformacion:
            count1=1
        if count1 == 0:
            pass
        else:
            if self.nombreIn.get() != "" and self.passwordIn.get() != "":
                for i in self.recogerinformacion:
                    valor=i
                    usuario=valor[9]
                    contraseña=valor[10]
                    if usuario == self.nombreIn.get() and contraseña == self.passwordIn.get():
                        contador_de_salida=1
                        break
                    elif NombreUsuarioAdmin == self.nombreIn.get() and PasswordAdmin == self.passwordIn.get():
                        contador_de_salida=1
                        break
                    else:
                        contador_de_salida=0
                if contador_de_salida==1:
                    messagebox.showinfo("Bienvenida", f"Bienvenido {self.nombreIn.get()}")
                    self.window.destroy()
                    #window= Tk()
                    window = ThemedTk(theme="adapta")
                    entrar_menu=Menu_organizacion(window,"Menú",1350,670)
                    window.mainloop()
                else:
                    messagebox.showinfo("Error", "Usuario o contraseña incorrectos.")
            else:
                messagebox.showinfo("Error", f"Se deben llenar todos los campos")

#Menu organizacion
class Menu_organizacion:
    def __init__(self,window,title,w,h):
        #self.w = w
        #self.h = h

        #self.x = int(window.winfo_screenwidth() / 2 - self.w / 2)
        #self.y = int(window.winfo_screenheight() / 2 - self.h / 2)
        self.x = 0
        self.y = 0

        self.db = Conexion()

        try:
            self.db.conectar()
        except:
            print("Error al conectar")

        self.window = window
        self.window.title(title)
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight() 
        self.window.geometry("%dx%d+%d+%d" % (self.w, self.h, -9, self.y))
        self.window.resizable(False, True)
        self.window.iconbitmap('images/icono.ico')
        self.window.configure(background="white")
        #self.window.attributes('-fullscreen', True) 
        #self.window.theme_use("Adapta")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/bg_menu.png")
        background = self.canvas.create_image(683.0, 325.5,image=self.background_img)
        #Barra menu
        barramenu=Menu(window) 
        window.config(menu=barramenu)
        Archivo=Menu(barramenu,tearoff=0)
        Editar=Menu(barramenu,tearoff=0)
        Ayuda=Menu(barramenu,tearoff=0)
        barramenu.add_cascade(label="Base de datos",menu=Archivo)
        barramenu.add_cascade(label="Editar",menu=Editar)
        barramenu.add_cascade(label="Ayuda",menu=Ayuda)
        #Submenus
        Archivo.add_command(label="Agregar", command=self.funcion_archivo)
        Archivo.add_command(label="Abrir archivo")
        Archivo.add_command(label="Abrir carpeta")

        Editar.add_command(label="Cortar")
        Editar.add_command(label="Copiar")
        Editar.add_command(label="Pegar")

        Ayuda.add_command(label="Documentación")
        Ayuda.add_command(label="Conseguir licencia")
        Ayuda.add_command(label="Acerca del programa")

        """self.img_esquina_izquierda = PhotoImage(file=r"images/esquina1.png")
        label_img_esquina_izquierda = Label(frame_arriba, image = self.img_esquina_izquierda,
                                  background = "#16660A", borderwidth = 0, highlightthickness = 0)
        label_img_esquina_izquierda.place(x = 0, y = 0)

        self.img_esquina_derecha = PhotoImage(file=r"images/esquina2.png")
        label_img_esquina_derecha = Label(frame_arriba, image = self.img_esquina_derecha,
                                  background = "#16660A", borderwidth = 0, highlightthickness = 0)
        label_img_esquina_derecha.place(x = 1150, y = 0)

        self.img_logo_uanl = PhotoImage(file=r"images/logo_uanl1.png")
        self.label_img_logo_uanl = Label(frame_arriba, image = self.img_logo_uanl,bg="#16660A", borderwidth = 0, highlightthickness = 0)
        self.label_img_logo_uanl.place(x = 200, y = 0)

        self.img_oso_fime = PhotoImage(file=r"images/fime5.png")
        self.label_img_oso_fime = Label(frame_arriba, image = self.img_oso_fime,bg="#16660A", borderwidth = 0, highlightthickness = 0)
        self.label_img_oso_fime.place(x = 1050, y = 0)"""

        #/////////////////////////////////////---------------------------BOTONES-----------------------------------/////////////////////////77
        frame_botones = Frame(self.window)
        frame_botones.pack()
        frame_botones.config(width=400, height=100, bg="#16660A")
        frame_botones.place(x = 650, y = 0)

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#16660A")

        self.button = ttk.Button(frame_botones,text="Editar grupos",command=self.ir_agregar,curso="hand2")
        self.button.place(x=160,y=25)

        self.button1 = ttk.Button(frame_botones,text="No disponible",curso="hand2")
        self.button1.place(x=270,y=25)

        frame_selecciones = Frame(self.window)
        #frame_selecciones.pack()
        frame_selecciones.config(bg="white",width=1350, height=90)
        frame_selecciones.place(x = 30, y = 110)

        label_carrera=Label(frame_selecciones,text="Carrera:",font=("Thoma",14),background="white")
        label_carrera.grid(row = 0, column = 1)
        carreras=["IAS","ITS","IMA","IME"]
        self.comb_carreras = Combobox(frame_selecciones,values = carreras, state = "readonly", font = ("Tahoma", 12),background = "white", foreground = "black", width = 5)
        self.comb_carreras.current(0)
        self.comb_carreras.grid( row=0, column = 2)

        label_semestre=Label(frame_selecciones,text="Semestre:",font=("Thoma",14),background="white")
        label_semestre.grid(row = 0, column = 4)
        semestres=["1", "2", "3","4","5","6","7","8"]
        self.comb_semestres = Combobox(frame_selecciones,values = semestres, state = "readonly", font = ("Tahoma", 12),background = "white", foreground = "black", width = 3)
        self.comb_semestres.current(0)
        self.comb_semestres.grid( row=0, column = 5)

        label_turno=Label(frame_selecciones,text="Turno:",font=("Thoma",14),background="white")
        label_turno.grid(row = 0, column = 7)
        turnos=["Matutino", "Vespertino", "Nocturno"]
        self.comb_turnos = Combobox(frame_selecciones,values = turnos, state = "readonly", font = ("Tahoma", 12),background = "white", foreground = "black", width = 8)
        self.comb_turnos.current(0)
        self.comb_turnos.grid( row=0, column = 8)

        #////////////////////////////////////////Tabla-Grupos/////////////////////////////////#
        """frame_treeview_grupos = Frame(self.window)
        #frame_treeview_grupos.pack()
        frame_treeview_grupos.config(width=360, height=470,bg="white")
        frame_treeview_grupos.place(x = 50, y = 170)"""

        #ima_fondo = PhotoImage(file=r"images/fondo1.png")
        """ima_fondo=Image.open("images/fondo1.png")
        self.window.ima_fondo = ImageTk.PhotoImage(ima_fondo)
        self.img_empLabel = Label(frame_treeview_grupos, image = self.window.ima_fondo,bg="white")
        self.img_empLabel.place(x = 0, y = 0)"""

        """self.img_emp = PhotoImage(file=r"images/fondo1.png")
        self.img_empLabel = Label(frame_treeview_grupos, image = self.img_emp,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.img_empLabel.place(x = 0, y = 0)"""

        style = ttk.Style()
        #style.theme_use("Adapta")
        style.configure("Treeview")
        style.map("Treeview", background=[("selected","#34a32a")])

        #self.label_treeview_grupos=Label(frame_treeview_grupos,text="Grupos organizados",font=("Thoma",12),foreground="white",background="#16660A")
        #self.label_treeview_grupos.place(x = 110, y = 10)

        self.tabla_grupos = ttk.Treeview(self.window,height=16)
        self.tabla_grupos["columns"] = ("Agrupación","Plan","Carrera","Turno")
        self.tabla_grupos.column("#0",width=0,stretch=NO)
        self.tabla_grupos.column("Agrupación",anchor=CENTER,width=60)
        self.tabla_grupos.column("Plan",anchor=CENTER,width=60)
        self.tabla_grupos.column("Carrera",anchor=CENTER,width=60)
        self.tabla_grupos.column("Turno",anchor=CENTER,width=80)

        self.tabla_grupos.heading("#0",text="",anchor=CENTER)
        self.tabla_grupos.heading("Agrupación",text="Agrupación",anchor=CENTER)
        self.tabla_grupos.heading("Plan",text="Plan",anchor=CENTER)
        self.tabla_grupos.heading("Carrera",text="Carrera",anchor=CENTER)
        self.tabla_grupos.heading("Turno",text="Turno",anchor=CENTER)
        #---------------Meter información--------------------#
        self.recogerinformacion_grupos=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
        count=0
        for row in self.recogerinformacion_grupos:
            count=1
        if count == 0:
            pass
        else:
            for i in self.recogerinformacion_grupos:
                value0=i[0]
                value1=i[1]
                value2=i[2]
                value3=i[3]
                self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value1,value2,value3))
        #self.tabla.pack(pady=20)
        self.tabla_grupos.place(x=77,y=220)

        self.scrollvert=Scrollbar(self.window,command=self.tabla_grupos.yview)
        self.scrollvert.place(in_=self.tabla_grupos,relx=1, relheight=1, bordermode="outside")
        self.tabla_grupos.config(yscrollcommand=self.scrollvert.set)

        self.tabla_grupos.bind("<ButtonRelease-1>", self.click_treeview)
        #--------------------------------------Tabla------------------------------------------------------------#
        """cuadro_informacion = Frame(self.window)
        cuadro_informacion.pack()
        cuadro_informacion.config(width=730, height=340, bg="white")
        cuadro_informacion.place(x = 550, y = 170)

        self.img_fondo2 = PhotoImage(file=r"images/fondo2.png")
        self.label_img_fondo2 = Label(cuadro_informacion, image = self.img_fondo2,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.label_img_fondo2.place(x = 0, y = 0)

        self.labelis=Label(cuadro_informacion,text="Materias del grupo",font=("Thoma",12),foreground="white",background="#16660A")
        self.labelis.place(x = 285, y = 0)"""

        self.tabla = ttk.Treeview(self.window)
        self.tabla["columns"] = ("Agrupación","Plan","Clave","Materia","Carrera","Semestre","Empleado","Hora","Día","Salón")
        self.tabla.column("#0",width=0,stretch=NO)
        self.tabla.column("Agrupación",anchor=CENTER,width=60)
        self.tabla.column("Plan",anchor=CENTER,width=60)
        self.tabla.column("Clave",anchor=CENTER,width=70)
        self.tabla.column("Materia",anchor=CENTER,width=200)
        self.tabla.column("Carrera",anchor=CENTER,width=60)
        self.tabla.column("Semestre",anchor=CENTER,width=60)
        self.tabla.column("Empleado",anchor=CENTER,width=60)
        self.tabla.column("Hora",anchor=CENTER,width=60)
        self.tabla.column("Día",anchor=CENTER,width=60)
        self.tabla.column("Salón",anchor=CENTER,width=60)

        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("Agrupación",text="Agrupación",anchor=CENTER)
        self.tabla.heading("Plan",text="Plan",anchor=CENTER)
        self.tabla.heading("Clave",text="Clave",anchor=CENTER)
        self.tabla.heading("Materia",text="Materia",anchor=CENTER)
        self.tabla.heading("Carrera",text="Carrera",anchor=CENTER)
        self.tabla.heading("Semestre",text="Semestre",anchor=CENTER)
        self.tabla.heading("Empleado",text="Empleado",anchor=CENTER)
        self.tabla.heading("Hora",text="Hora",anchor=CENTER)
        self.tabla.heading("Día",text="Día",anchor=CENTER)
        self.tabla.heading("Salón",text="Salón",anchor=CENTER)
        #---------------Meter información--------------------#
        #self.tabla.pack(pady=20)
        self.tabla.place(x=531,y=220)

        self.scrollvert=Scrollbar(self.window,command=self.tabla.yview)
        self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
        self.tabla.config(yscrollcommand=self.scrollvert.set)

    def click_treeview(self,e):
        seleccion = self.tabla_grupos.focus()
        values = self.tabla_grupos.item(seleccion,"values")

        self.tabla.delete(*self.tabla.get_children())

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
        count1=0
        for row in self.recogerinformacion:
            count1=1
        if count1 == 0:
            pass
        else:
            for i in self.recogerinformacion:
                valuei=int(i[1])
                if int(values[0]) == valuei:
                    value1=i[1]
                    value2=i[2]
                    value3=i[3]
                    value4=i[4]
                    value5=i[5]
                    value6=i[6]
                    value7=i[7]
                    value8=i[8]
                    value10=i[10]
                    value11=i[11]
                    self.tabla.insert(parent="",index="end", text="", values=(value1,value2,value3,value4,value5,value6,value7,value8,value10,value11))

        """self.recogerinformacion_grupos=self.db.cursor.execute(f"SELECT * FROM Grupos").fetchall()
        for i in self.recogerinformacion_grupos:
            value0=i[0]
            value1=i[1]
            value2=i[2]
            value3=i[3]
            self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value1,value2,value3))"""

        #self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Productos").fetchall()

        #self.tabla.insert(parent="",index="end", text="", values=(values[0],values[1],values[2],values[3]))

    def funcion_archivo(self):
        self.window.destroy()
        window = Tk()
        regProd = nueva_reservacion(window, "Reservación", 1350, 670)
        window.mainloop()

    def ir_agregar(self):
        self.window.destroy()
        window=ThemedTk(theme="adapta")
        llamada = Agregar(window, "Agregar registro", 1350, 670)
        window.mainloop()

class Agregar:
    def __init__(self,window,title,w,h):
        self.w = w
        self.h = h
        #self.x = int(window.winfo_screenwidth() / 2 - self.w / 2)
        #self.y = int(window.winfo_screenheight() / 2 - self.h / 2)
        self.x = 0
        self.y = 0

        self.db = Conexion()

        try:
            self.db.conectar()
        except:
            print("Error al conectar")

        self.window = window
        self.window.title(title)
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight() 
        self.window.geometry("%dx%d+%d+%d" % (self.w, self.h, -9, self.y))
        self.window.resizable(False, True)
        self.window.iconbitmap('images/icono.ico')
        self.window.configure(background="white")

        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"images/bg_agregar.png")
        background = self.canvas.create_image(683.0, 344.0,image=self.background_img)

        COMBOBOX=ttk.Style().configure("TCombobox",selectbackground="green",darkcolor="black")
        #COMBOBOX.theme_use("clam")


        self.entry0_img = PhotoImage(file = f"images/img_textBox_agregar.png")
        entry0_bg = self.canvas.create_image(268.0, 246.0, image = self.entry0_img)
        self.entry0 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0,font = ("Tahoma", 12))
        self.entry0.place(x = 208.0, y = 228, width = 120.0, height = 28)
        self.entry0.bind("<FocusIn>", self.focus)
        self.entry0.bind("<FocusOut>", self.sinfocus)

        entry1_bg = self.canvas.create_image(268.0, 297.0, image = self.entry0_img)
        self.entry1 = Entry(bd = 0,bg = "#c4c4c4", highlightthickness = 0,font = ("Tahoma", 12))
        self.entry1.place(x = 208.0, y = 279, width = 120.0, height = 28)
        self.entry1.bind("<FocusIn>", self.focus)
        self.entry1.bind("<FocusOut>", self.sinfocus)

        entry2_bg = self.canvas.create_image(268.0, 348.0, image = self.entry0_img)
        self.entry2 = Entry(bd = 0,bg = "#c4c4c4", highlightthickness = 0,font = ("Tahoma", 12))
        self.entry2.place(x = 208.0, y = 330, width = 120.0, height = 28)
        self.entry2.bind("<FocusIn>", self.focus)
        self.entry2.bind("<FocusOut>", self.sinfocus)

        """entry3_bg = self.canvas.create_image(268.0, 400.0, image = self.entry0_img)
        self.entry3 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0)
        self.entry3.place(x = 208.0, y = 382, width = 120.0, height = 28)"""

        Carrera=["IME","IMA","IAS","IEC","IEA","IMT","ITS","IMTC","Manufactura","Aeronáutica","Biomedico"]
        self.entry3 = ttk.Combobox(self.window,values = Carrera,width=7,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.entry3.current(0),
        self.entry3.place( x=148, y = 375)

        self.img_eliminar = PhotoImage(file = f"images/img_eliminar.png")
        self.Boton_eliminar = Button(image = self.img_eliminar,borderwidth = 0,highlightthickness = 0,curso="hand2",relief = "flat")
        self.Boton_eliminar.place(x = 1158, y = 540,width = 156,height = 35)

        """entry4_bg = self.canvas.create_image(268.0, 450.0, image = self.entry0_img)
        self.entry4 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0)
        self.entry4.place(x = 208.0, y = 432, width = 120.0, height = 28)"""

        Semestre=["1","2","3","4","5","6","7","8"]
        self.entry4 = ttk.Combobox(self.window,values = Semestre,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.entry4.current(0),
        self.entry4.place( x=148, y = 428)

        entry5_bg = self.canvas.create_image(268.0, 501.0, image = self.entry0_img)
        self.entry5 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0,font = ("Tahoma", 12))
        self.entry5.place(x = 208.0, y = 483, width = 120.0, height = 28)
        self.entry5.bind("<FocusIn>", self.focus)
        self.entry5.bind("<FocusOut>", self.sinfocus)

        """entry6_bg = self.canvas.create_image(268.0, 553.0, image = self.entry0_img)
        self.entry6 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0)
        self.entry6.place(x = 208.0, y = 535, width = 120.0, height = 28)"""

        horas=["M1", "M2", "M3","M4","M5","M6","V1","V2","V3","V4","V5","V6","N1","N2","N3","N4","N5","N6"]
        self.entry6 = ttk.Combobox(self.window,values = horas,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.entry6.current(0),
        self.entry6.place( x=325, y = 375)

        dias=["L-M-V","M-J"]
        self.entry8 = ttk.Combobox(self.window,values = dias,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.entry8.current(0),
        self.entry8.place( x=325, y = 428)

        entry9_bg = self.canvas.create_image(268.0, 552.0, image = self.entry0_img)
        self.entry9 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0,font = ("Tahoma", 12))
        self.entry9.place(x = 208.0, y = 534, width = 120.0, height = 28)
        self.entry9.bind("<FocusIn>", self.focus)
        self.entry9.bind("<FocusOut>", self.sinfocus)


        self.img0 = PhotoImage(file = f"images/img_aceptar.png")
        self.b0 = Button(image = self.img0,borderwidth = 0,highlightthickness = 0,command=self.agregar_elementos,curso="hand2",bg="#59B04C",activebackground="#59B04C",relief = "flat")
        self.b0.place(x = 196, y = 615,width = 100,height = 35)
        #////////////////77-----------------------------Botones---------------------------//////////////////
        frame_botones = Frame(self.window)
        frame_botones.pack()
        frame_botones.config(width=400, height=100, bg="#16660A")
        frame_botones.place(x = 650, y = 0)

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#16660A")

        self.button = ttk.Button(frame_botones,text="Menú",command=self.ir_menu,curso="hand2")
        self.button.place(x=150,y=25)

        self.button1 = ttk.Button(frame_botones,text="Actualizar grupos",command=self.eliminar_todo,curso="hand2")
        self.button1.place(x=250,y=25)

        #self.button3 = ttk.Button(frame_botones,text="Eliminar grupos",command=self.eliminar_todo,curso="hand2")
        #self.button3.place(x=10,y=25)

        #--------------------------------------Tabla------------------------------------------------------------#
        """cuadro_informacion = Frame(self.window)
        cuadro_informacion.pack()
        cuadro_informacion.config(width=730, height=340, bg="white")
        cuadro_informacion.place(x = 550, y = 170)

        self.img_fondo2 = PhotoImage(file=r"images/fondo2.png")
        self.label_img_fondo2 = Label(cuadro_informacion, image = self.img_fondo2,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.label_img_fondo2.place(x = 0, y = 0)

        self.labelis=Label(cuadro_informacion,text="Materias del grupo",font=("Thoma",12),foreground="white",background="#16660A")
        self.labelis.place(x = 285, y = 0)"""
        style = ttk.Style()
        #style.theme_use("Adapta")
        style.configure("Treeview")
        style.map("Treeview", background=[("selected","#34a32a")])

        self.tabla = ttk.Treeview(self.window)
        self.tabla["columns"] = ("ID Grupo","Plan","Clave","Materia","Carrera","Semestre","Empleado","Hora","Día","Salón")
        self.tabla.column("#0",width=0,stretch=NO)
        self.tabla.column("ID Grupo",anchor=CENTER,width=60)
        self.tabla.column("Plan",anchor=CENTER,width=60)
        self.tabla.column("Clave",anchor=CENTER,width=70)
        self.tabla.column("Materia",anchor=CENTER,width=200)
        self.tabla.column("Carrera",anchor=CENTER,width=60)
        self.tabla.column("Semestre",anchor=CENTER,width=60)
        self.tabla.column("Empleado",anchor=CENTER,width=60)
        self.tabla.column("Hora",anchor=CENTER,width=60)
        self.tabla.column("Día",anchor=CENTER,width=60)
        self.tabla.column("Salón",anchor=CENTER,width=60)

        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("ID Grupo",text="ID Grupo",anchor=CENTER)
        self.tabla.heading("Plan",text="Plan",anchor=CENTER)
        self.tabla.heading("Clave",text="Clave",anchor=CENTER)
        self.tabla.heading("Materia",text="Materia",anchor=CENTER)
        self.tabla.heading("Carrera",text="Carrera",anchor=CENTER)
        self.tabla.heading("Semestre",text="Semestre",anchor=CENTER)
        self.tabla.heading("Empleado",text="Empleado",anchor=CENTER)
        self.tabla.heading("Hora",text="Hora",anchor=CENTER)
        self.tabla.heading("Día",text="Día",anchor=CENTER)
        self.tabla.heading("Salón",text="Salón",anchor=CENTER)
        #---------------Meter información--------------------#
        #self.tabla.pack(pady=20)
        self.tabla.place(x=531,y=220)

        self.scrollvert=Scrollbar(self.window,command=self.tabla.yview)
        self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
        self.tabla.config(yscrollcommand=self.scrollvert.set)

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        count=0
        for row in self.recogerinformacion:
            count=1
        if count == 0:
            pass
        else:
            for i in self.recogerinformacion:
                value0=i[0]
                value1=i[1]
                value2=i[2]
                value3=i[3]
                value4=i[4]
                value5=i[5]
                value6=i[6]
                value7=i[7]
                value9=i[9]
                value10=i[10]
                self.tabla.insert(parent="",index="end", text="", values=(value0,value1,value2,value3,value4,value5,value6,value7,value9,value10))

    def eliminar_todo(self):
        decision2=messagebox.askquestion("Confirmar","¿Seguro que quieres actualizar los grupos?")
        if decision2 == "yes":
            self.db.cursor.execute(f"DELETE FROM Agrupacion")
            self.db.cursor.execute(f"DELETE FROM Grupos_ordenados")
            self.db.cursor.commit()
            self.crear_grupos()

    def focus(self, event):
        if event.widget == 1: pass
        else: event.widget.configure(foreground = "white")

    def sinfocus(self, event):
        if event.widget == 1: pass
        else: event.widget.configure(foreground = "black")

    def ir_menu(self):
        self.window.destroy()
        window=ThemedTk(theme="adapta")
        llamada = Menu_organizacion(window, "Menú", 1350, 670)
        window.mainloop()

    def checar_empleado_hora(self):
        self.variable_checar_empleado_hora=False
        self.tupla_checar_empleado_hora=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        count=0
        for row in self.tupla_checar_empleado_hora: 
            count=1
        if count == 0: 
            pass
        else:
            for chequeo_clave in self.tupla_checar_empleado_hora:
                atrapar_clave = chequeo_clave[6]
                atrapar_hora = chequeo_clave[7]
                if self.entry5.get() == atrapar_clave and self.entry6.get() == atrapar_hora:
                    self.variable_checar_empleado_hora=True

    def agregar_elementos(self):
        if self.entry0.get() != "" and self.entry1.get() != "" and self.entry2.get() != "" and self.entry3.get() != "" and self.entry4.get() != "" and self.entry5.get() != "" and self.entry6.get() != "" and self.entry8.get() != "" and self.entry9.get() != "":
            if messagebox.askokcancel(message="¿Deseas completar el registro?", title="Confirmar registro"):
                self.checar_clave()
                self.checar_empleado_hora()
                if self.ComprobacionClave==True:
                    messagebox.showinfo("Error","El valor Clave ya esta registrado en la base de datos.")
                elif self.variable_checar_empleado_hora==True:
                    messagebox.showinfo("Error","El valor Hora ya esta registrado en la base de datos con ese Empleado.")
                else:
                    self.entry7 = Entry()
                    self.definir_turno()
                    self.db.cursor.execute(f"INSERT INTO Grupos_desordenados (Plan, Materia, Carrera, Semestre, Empleado, Hora, Clave,Turno,Dias,Salon) VALUES ('{self.entry0.get()}', '{self.entry2.get()}', '{self.entry3.get()}','{self.entry4.get()}','{self.entry5.get()}','{self.entry6.get()}','{self.entry1.get()}','{self.entry7.get()}','{self.entry8.get()}','{self.entry9.get()}')")
                    self.db.cursor.commit()
                    self.entry0.delete(0, END)
                    self.entry1.delete(0, END)
                    self.entry2.delete(0, END)
                    self.entry3.delete(0, END)
                    self.entry4.delete(0, END)
                    self.entry5.delete(0, END)
                    self.entry6.delete(0, END)
                    self.entry7.delete(0, END)
                    self.entry8.delete(0, END)
                    self.entry9.delete(0, END)
                    messagebox.showinfo("Completado","Actualizacion de datos  completada.")
                    self.window.destroy()
                    window = ThemedTk(theme="adapta")
                    entrar_registro=Agregar(window,"Registro",1350,670)
                    window.mainloop()
        else:
            messagebox.showinfo("Error","Debe llenar todos los apartados.")

    def definir_turno(self):
        listaMatutino=["M1","M2","M3","M4","M5","M6"]
        listaVespertino=["V1","V2","V3","V4","V5","V6"]
        listaNocturno=["N1","N2","N3","N4","N5","N6"]
        valorturno = self.entry6.get()
        for i in listaMatutino:
            if i ==valorturno:
                self.entry7.insert(END,"Matutino")
                break
        for x in listaVespertino:
            if x ==valorturno:
                self.entry7.insert(END,"Vespertino")
                break
        for y in listaNocturno:
            if y ==valorturno:
                self.entry7.insert(END,"Nocturno")
                break

    def checar_clave(self):
        self.ComprobacionClave = False
        self.info_clave=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        count=0
        for row in self.info_clave:
            count=1
        if count == 0:
            pass
        else:
            for chequeo_clave in self.info_clave:
                atrapar_clave = chequeo_clave[2]
                if self.entry1.get() == atrapar_clave:
                    self.ComprobacionClave = True 

    def checar_turno(self):
        self.Veredicto = False
        self.inf_A=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
        count=0
        for row in self.inf_A:
            count=1
        if count == 0:
            pass
        else:
            for chequeo_hora in self.inf_A:
                atrapar_grupo = chequeo_hora[1]
                if int(self.ValorChequeoA) == int(atrapar_grupo):
                    if self.ValorChequeo == chequeo_hora[8]:
                        self.Veredicto = True 

    def crear_grupos(self):
        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        count=0
        for row in self.recogerinformacion:
            count=1
        if count == 0:
            pass
        else:
            tupla=list(self.recogerinformacion)
            print("tupla: ",tupla)
            print("-------------------------")
            for i in tupla:
                print(i)
                print("-------------------------")
                tupla.remove(i)
                print(tupla)
                print("-------------------------")

            for i in self.recogerinformacion:
                valorA0= i[0]; valorA1= i[1]; valorA2= i[2]; valorA3= i[3]; valorA4= i[4]; valorA5= i[5]; valorA6= i[6]; valorA7= i[7]; valorA8= i[8];valorA9= i[9];valorA10= i[10]

                self.db.cursor.execute(f"INSERT INTO Agrupacion (Plan, Carrera, Turno,id_primer_materia) VALUES ('{valorA1}','{valorA4}','{valorA8}','{valorA0}')")
                self.db.cursor.commit()
                self.info_agrupaciones=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
                #comprobar si esta vacia
                count=0
                for row in self.info_agrupaciones:
                    count=1
                if count == 0:
                    pass
                else:
                    for a in self.info_agrupaciones: #Conseguir la info de agrupaciones
                        VALORC0 = a[0]   #ID DEL GRUPO
                        VALORC4 = a[4]   # ID DE LA MATERIA CON LA QUE SE DIO DE ALTA LA AGRUPACION

                        if int(valorA0) == int(VALORC4): #COMPROBRA QUE EL ID DE LA LISTA ANALIZADA SEA IGUAL QUE EL ID DE LA MATERIA CON LA QUE SE DIO DE ALTA
                            self.db.cursor.execute(f"INSERT INTO Grupos_ordenados (Grupo_asignado,Plan, Clave,Materia, Carrera, Semestre, Empleado, Hora,Turno,Dias,Salon) VALUES ('{VALORC0}','{valorA1}','{valorA2}','{valorA3}', '{valorA4}', '{valorA5}', '{valorA6}', '{valorA7}', '{valorA8}','{valorA9}','{valorA10}')")
                            self.db.cursor.commit()
                            self.recogerinformacion.remove(i)
                            break
                    for x in self.recogerinformacion:
                        valorB0= x[0]; valorB1= x[1]; valorB2= x[2]; valorB3= x[3]; valorB4= x[4]; valorB5= x[5]; valorB6= x[6]; valorB7= x[7]; valorB8= x[8];valorB9= x[9];valorB10= x[10]
                        if valorA0 == valorB0: #compruba si el id de la primera lista es igual al del segundo
                            pass
                        else:
                            if valorA1 == valorB1 and valorA2 != valorB2 and valorA3 != valorB3 and valorA4 == valorB4 and valorA5 == valorB5 and valorA7 != valorB7 and valorA8 == valorB8:
                                self.ValorChequeo = valorB7
                                self.ValorChequeoA = VALORC0
                                self.checar_turno()
                                if self.Veredicto == False:
                                    self.db.cursor.execute(f"INSERT INTO Grupos_ordenados (Grupo_asignado,Plan, Clave,Materia, Carrera, Semestre, Empleado, Hora,Turno,Dias,Salon) VALUES ('{VALORC0}','{valorB1}','{valorB2}','{valorB3}', '{valorB4}', '{valorB5}', '{valorB6}', '{valorB7}', '{valorB8}','{valorB9}','{valorB10}')")
                                    self.db.cursor.commit()
                                    self.recogerinformacion.remove(x)

            messagebox.showinfo("Completado","Grupos creados satisfactoriamente.")
                    #self.recogerinformacion.remove(i)
#///////////////////////////////////////////////////////////////////////////////////////////77

if __name__ == "__main__":
    #window = Tk()

    window=ThemedTk(theme="adapta")
    #login = Login(window, "Iniciar sesión", 800, 550)
    entrar_menu=Agregar(window,"Agregar",1350,670)
    window.mainloop()
