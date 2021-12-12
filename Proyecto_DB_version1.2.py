# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
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
import pandas as pd

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

        self.passwordIn = Entry(bd = 0,show="•",bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 14))
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
        PasswordAdmin = "fime2021"
        self.db = Conexion()
        try:
            self.db.conectar()
        except:
            print("Error al conectar")

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Usuarios").fetchall()
        count1=0
        for row in self.recogerinformacion:
            count1=1
        if count1 == 0:
            pass
        else:
            if self.nombreIn.get() != "" and self.passwordIn.get() != "":
                for i in self.recogerinformacion:
                    valor=i
                    usuario=valor[1]
                    contraseña=valor[2]
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
        self.window.iconbitmap('images/ico_fime.ico')
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
        Archivo.add_command(label="Agregar")
        Archivo.add_command(label="Abrir archivo")
        Archivo.add_command(label="Abrir carpeta")

        Editar.add_command(label="Cortar")
        Editar.add_command(label="Copiar")
        Editar.add_command(label="Pegar")

        Ayuda.add_command(label="Documentación")
        Ayuda.add_command(label="Conseguir licencia")
        Ayuda.add_command(label="Acerca del programa")

        #/////////////////////////////////////---------------------------BOTONES-----------------------------------/////////////////////////77
        frame_botones = Frame(self.window)
        frame_botones.pack()
        frame_botones.config(width=250, height=100, bg="#16660A")
        frame_botones.place(x = 800, y = 0)

        #bg="#16660A"

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#16660A")

        self.button = ttk.Button(frame_botones,text="Editar grupos",command=self.ir_agregar,curso="hand2")
        self.button.place(x=10,y=25)

        self.button1 = ttk.Button(frame_botones,text="No disponible",curso="hand2")
        self.button1.place(x=120,y=25)

        frame_selecciones = Frame(self.window)
        #frame_selecciones.pack()
        frame_selecciones.config(bg="white",width=1350, height=90)
        frame_selecciones.place(x = 30, y = 110)

        self.img_mostrar = PhotoImage(file = f"images/mostrar.png")
        self.button_mostrar_todo = Button(frame_selecciones,image = self.img_mostrar, borderwidth = 0,highlightthickness = 0,curso="hand2",relief = "flat",bg="white",command=self.mostrarTodo)
        self.button_mostrar_todo.grid(row=0, column = 0)

        label_carrera=Label(frame_selecciones,text="Carrera:",font=("Thoma",14),background="white")
        label_carrera.grid(row = 0, column = 2)
        
        carreras=["","IME","IMA","IAS","IEC","IEA","IMT","ITS","IMTC","Manufactura","Aeronáutica","Biomedico"]

        self.comb_carreras = Combobox(frame_selecciones,values = carreras, state = "readonly", font = ("Tahoma", 12),background = "white", foreground = "black", width = 5)
        self.comb_carreras.current(0)
        self.comb_carreras.grid( row=0, column = 3)
        self.comb_carreras.bind("<<ComboboxSelected>>", self.seleccion_del_combobox)

        label_semestre=Label(frame_selecciones,text="Semestre:",font=("Thoma",14),background="white")
        label_semestre.grid(row = 0, column = 4)
        semestres=["","1", "2", "3","4","5","6","7","8"]
        self.comb_semestres = Combobox(frame_selecciones,values = semestres, state = "readonly", font = ("Tahoma", 12),background = "white", foreground = "black", width = 5)
        self.comb_semestres.current(0)
        self.comb_semestres.grid( row=0, column = 5)
        self.comb_semestres.bind("<<ComboboxSelected>>", self.seleccion_del_combobox)

        label_turno=Label(frame_selecciones,text="Turno:",font=("Thoma",14),background="white")
        label_turno.grid(row = 0, column = 6)
        turnos=["","Matutino", "Vespertino", "Nocturno"]
        self.comb_turnos = Combobox(frame_selecciones,values = turnos, state = "readonly", font = ("Tahoma", 12),background = "white", foreground = "black", width = 8)
        self.comb_turnos.current(0)
        self.comb_turnos.grid( row=0, column = 7)
        self.comb_turnos.bind("<<ComboboxSelected>>", self.seleccion_del_combobox)

        style = ttk.Style()
        #style.theme_use("Adapta")
        style.configure("Treeview")
        style.map("Treeview", background=[("selected","#34a32a")])

        #__________________________________________Tabla_grupos___________________________________________#
        self.tabla_grupos = ttk.Treeview(self.window,height=16)
        self.tabla_grupos["columns"] = ("Agrupación","Carrera","Turno","Semestre")
        self.tabla_grupos.column("#0",width=0,stretch=NO)
        self.tabla_grupos.column("Agrupación",anchor=CENTER,width=60)
        self.tabla_grupos.column("Carrera",anchor=CENTER,width=60)
        self.tabla_grupos.column("Turno",anchor=CENTER,width=80)
        self.tabla_grupos.column("Semestre",anchor=CENTER,width=60)

        self.tabla_grupos.heading("#0",text="",anchor=CENTER)
        self.tabla_grupos.heading("Agrupación",text="Agrupación",anchor=CENTER)
        self.tabla_grupos.heading("Carrera",text="Carrera",anchor=CENTER)
        self.tabla_grupos.heading("Turno",text="Turno",anchor=CENTER)
        self.tabla_grupos.heading("Semestre",text="Semestre",anchor=CENTER)

        #______________________Meter información en la tabla grupos__________________#
        self.recogerinformacion_grupos=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
        count=0
        for row in self.recogerinformacion_grupos:
            count=1
        if count == 0:
            pass
        else:
            for i in self.recogerinformacion_grupos:
                self.tabla_grupos.insert(parent="",index="end", text="", values=(i[0],i[2],i[3],i[5]))
        #self.tabla.pack(pady=20)
        self.tabla_grupos.place(x=77,y=220)

        self.scrollvert=Scrollbar(self.window,command=self.tabla_grupos.yview)
        self.scrollvert.place(in_=self.tabla_grupos,relx=1, relheight=1, bordermode="outside")
        self.tabla_grupos.config(yscrollcommand=self.scrollvert.set)

        self.tabla_grupos.bind("<ButtonRelease-1>", self.click_treeview)

        #________________________________________________Tabla_____________________________________#
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
        self.tabla.place(x=531,y=220)

        self.scrollvert=Scrollbar(self.window,command=self.tabla.yview)
        self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
        self.tabla.config(yscrollcommand=self.scrollvert.set)

    #________________________________Seleccion de los Combobox_____________________#
    def mostrarTodo(self):
        self.recogerinformacion_grupos=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
        if len(self.recogerinformacion_grupos) != 0:
            self.tabla_grupos.delete(*self.tabla_grupos.get_children())
            for i in self.recogerinformacion_grupos:
                self.tabla_grupos.insert(parent="",index="end", text="", values=(i[0],i[2],i[3],i[5]))

        self.comb_carreras.current(0)
        self.comb_semestres.current(0)
        self.comb_turnos.current(0)

    def seleccion_del_combobox(self, event):
        self.recogerinformacion_grupos=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
        if len(self.recogerinformacion_grupos) != 0:
            self.tabla_grupos.delete(*self.tabla_grupos.get_children())
            for i in self.recogerinformacion_grupos:
                value0=i[0];value2=i[2];value3=i[3];value5=i[5]

                # si estan seleccionados los 3 combobox
                if value2 == self.comb_carreras.get() and value5 == self.comb_semestres.get() and value3 == self.comb_turnos.get():
                    self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value2,value3,value5))

                # si estan seleccionados solo los 2 ultimos
                elif self.comb_carreras.get() == "" and value5 == self.comb_semestres.get() and value3 == self.comb_turnos.get():
                    self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value2,value3,value5))

                 # si estan seleccionados solo los 2 primeros
                elif self.comb_carreras.get() == value2 and self.comb_semestres.get() == value5 and self.comb_turnos.get() == "":
                    self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value2,value3,value5))

                # si estan seleccionadoel primero
                elif self.comb_carreras.get() == value2 and self.comb_semestres.get() == "" and self.comb_turnos.get() == "":
                    self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value2,value3,value5))

                # si estan seleccionados solo el ultimo
                elif self.comb_carreras.get() == "" and self.comb_semestres.get() == "" and value3 == self.comb_turnos.get():
                    self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value2,value3,value5))

                # si estan seleccionado el segundo
                elif self.comb_carreras.get() == "" and self.comb_semestres.get() == value5 and self.comb_turnos.get() == "":
                    self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value2,value3,value5))

    def click_treeview(self,e):
        seleccion = self.tabla_grupos.focus()
        values = self.tabla_grupos.item(seleccion,"values")

        self.tabla.delete(*self.tabla.get_children())

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
        if len(self.recogerinformacion) != 0:
            for i in self.recogerinformacion:
                if values[0] == i[1]:
                    self.tabla.insert(parent="",index="end", text="", values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[10],i[11]))

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
        self.window.iconbitmap('images/ico_fime.ico')
        self.window.configure(background="white")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

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
        self.entry0.insert(END, "401")
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

        dias=["L-M-V","Martes","Jueves"]
        self.entry8 = ttk.Combobox(self.window,values = dias,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.entry8.current(0),
        self.entry8.place( x=325, y = 428)

        entry9_bg = self.canvas.create_image(268.0, 552.0, image = self.entry0_img)
        self.entry9 = Entry(bd = 0, bg = "#c4c4c4", highlightthickness = 0,font = ("Tahoma", 12))
        self.entry9.place(x = 208.0, y = 534, width = 120.0, height = 28)
        self.entry9.bind("<FocusIn>", self.focus)
        self.entry9.bind("<FocusOut>", self.sinfocus)

        #____________________________Botones de la ventana_____________________________#

        self.img0 = PhotoImage(file = f"images/img_aceptar.png") #Boton Aceptar
        self.b0 = Button(image = self.img0,borderwidth = 0,highlightthickness = 0,command=self.agregar_elementos,curso="hand2",bg="#59B04C",activebackground="#59B04C",relief = "flat")
        self.b0.place(x = 196, y = 615,width = 100,height = 35)

        self.img_ButtonEditar = PhotoImage(file = f"images/img_editar.png") #Boton editar
        self.ButtonEditar = Button(
            image = self.img_ButtonEditar,command = self.crear_CRUD_edicion, curso= "hand2",
            borderwidth = 0,highlightthickness = 0, relief = "flat", bg="white", activebackground="white")
        self.ButtonEditar.place(x = 882, y = 545,width = 35,height = 38)

        self.img_ButtonEliminarRegistro = PhotoImage(file = f"images/img_eliminar.png") #Boton Eliminar
        self.ButtonEliminarRegistro = Button(
            image = self.img_ButtonEliminarRegistro, command = self.eliminar_registro, curso= "hand2",
            borderwidth = 0, highlightthickness = 0, relief = "flat", bg="white", activebackground="white")
        self.ButtonEliminarRegistro.place(x = 952, y = 545,width = 35,height = 38)

        """self.img_eliminar = PhotoImage(file = f"images/img_eliminar.png")
        self.Boton_eliminar = Button(image = self.img_eliminar,borderwidth = 0,bg="white",highlightthickness = 0,curso="hand2",relief = "flat",command=self.eliminar_registro)
        self.Boton_eliminar.place(x = 1158, y = 540,width = 156,height = 35)

        self.img_editar = PhotoImage(file = f"images/boton_editar.png")
        self.Boton_editar = Button(image=self.img_editar,borderwidth = 0,bg="white",highlightthickness = 0,curso="hand2",relief = "flat",command=self.crear_CRUD_edicion)
        self.Boton_editar.place(x = 1000, y = 540,width = 141,height = 35)"""

        #////////////////77-----------------------------Botones barra superior---------------------------//////////////////
        frame_botones = Frame(self.window)
        frame_botones.pack()
        frame_botones.config(width=600, height=100, bg="#16660A")
        frame_botones.place(x = 450, y = 0)

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#16660A")

        self.button = ttk.Button(frame_botones,text="Menú",command=self.ir_menu,curso="hand2")
        self.button.place(x=150,y=25)

        self.button1 = ttk.Button(frame_botones,text="Exportar",curso="hand2", command= self.Exportar_Archivo)
        self.button1.place(x=250,y=25)

        #self.button1 = ttk.Button(frame_botones,text="Importar", command=self.Importar_Archivo ,curso="hand2")
        #self.button1.place(x=350,y=25)

        self.button2 = ttk.Button(frame_botones,text="Vaciar base de datos",curso="hand2", command= self.crear_ventana_eliminar)
        self.button2.place(x=350,y=25)

        #--------------------------------------Tabla------------------------------------------------------------#
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
        if len(self.recogerinformacion) != 0:
            for i in self.recogerinformacion:
                self.tabla.insert(parent="",index="end", text="", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[9],i[10]))

        frame_selecciones = Frame(self.window)
        #frame_selecciones.pack()
        frame_selecciones.config(bg="white",width=50, height=20)
        frame_selecciones.place(x = 800, y = 120)

        label_registros=Label(frame_selecciones,text="Cantidad de registros:",font=("Thoma",14),background="white")
        label_registros.grid(row = 0, column = 0)

        self.entry_registros = Entry(frame_selecciones,bd = 0, background = "white", highlightthickness = 0,font = ("Tahoma", 14))
        self.longitud = len(self.recogerinformacion)
        self.entry_registros.insert(END,self.longitud)
        self.entry_registros.grid(row = 0, column=1)
        #entry_registros.configure(state="disable")

    ############################_______________________________Funciones de la ventana___________________#############################3
    #_________________________Funcion ventana eliminar________________________________#
    def vaciar_DB(self):
        if self.entry_ventana_eliminar.get() == "admin":
            self.db.cursor.execute(f"DELETE FROM Agrupacion")
            self.db.cursor.execute(f"DELETE FROM Grupos_ordenados")
            self.db.cursor.execute(f"DELETE FROM Grupos_desordenados")
            self.db.cursor.commit()
            messagebox.showinfo("Confirmar","Se ha eliminado la base de datos")
            self.top_eliminar.destroy()
            self.actualizar_treeview()
        else:
            messagebox.showinfo("Error","Escriba correctamente la palabra clave")
    #_____________________________________Ventana para confirmar borrado de la DB________________________#
    def crear_ventana_eliminar(self):
        self.top_eliminar=Toplevel()
        self.top_eliminar.grab_set()
        self.top_eliminar.transient(master=None)
        self.top_eliminar.title("Eliminar base de datos")
        self.top_eliminar.geometry("400x200+500+50")
        self.top_eliminar.resizable(False, True)
        self.top_eliminar.iconbitmap('images/ico_fime.ico')
        self.top_eliminar.configure(background="white")
        self.canvas_eliminar = Canvas(self.top_eliminar,bg = "#ffffff",height = 200,width = 400,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas_eliminar.place(x = 0, y = 0)

        self.background_img_ventana_eliminar = PhotoImage(file = f"images/bg_ventana_eliminar.png")
        background = self.canvas_eliminar.create_image(200.0, 100.0,image=self.background_img_ventana_eliminar)

        self.entry_img_ventana_eliminar = PhotoImage(file = f"images/img_texBox_ventana_eliminar.png")
        entry0_bg = self.canvas_eliminar.create_image(200.0, 100.0,image = self.entry_img_ventana_eliminar)

        self.entry_ventana_eliminar = Entry(self.top_eliminar,bd = 0,bg = "#D3D3D3",highlightthickness = 0,font = ("Tahoma", 12))
        self.entry_ventana_eliminar.place(x = 154.0, y = 84,width = 92.0,height = 30)
        self.entry_ventana_eliminar.bind("<FocusIn>", self.focus)
        self.entry_ventana_eliminar.bind("<FocusOut>", self.sinfocus)

        self.imgBVE = PhotoImage(file = f"images/img_BVE.png")
        b0 = Button(self.top_eliminar,image = self.imgBVE,borderwidth = 0,highlightthickness = 0,relief = "flat",bg="white",curso="hand2", command=self.vaciar_DB)
        b0.place(x = 150, y = 130,width = 100,height = 30)

    #__________________________________________________Exportar base de datos____________________________#
    def Exportar_Archivo(self):
        data_null={}
        df_null = pd.DataFrame(data_null)
        a = filedialog.asksaveasfilename(title="Abrir", initialdir = "C:/",filetypes = [("Archivo excel","*.xlsx")])

        if a != "":
            df_null.to_excel(f"{a}.xlsx",index=False)
            writer = pd.ExcelWriter(f"{a}.xlsx")

            #Agregar los valores de las materias a listas para el excel
            valores_to_excel=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
            d1 = []; d2 = []; d3 = []; d4 = []; d5 = []; d6 = []; d7 = []; d8 = []; d9 = []; d10 = []; d11 = []
            for i in valores_to_excel:
                d1.append(i[1]); d2.append(i[2]); d3.append(i[3]); d4.append(i[4]); d5.append(i[5]); d6.append(i[6])
                d7.append(i[7]); d8.append(i[8]); d9.append(i[9]); d10.append(i[10]); d11.append(i[11]);

            #Agregar los valores de las agrupaciones a listas para el excel
            valores_to_excel2=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
            E0 = []; E1 = []; E2 = []; E3 = []; E5 = []
            for i in valores_to_excel2:
                E0.append(i[0]); E1.append(i[1]); E2.append(i[2]); E3.append(i[3]); E5.append(i[5])

            data1 = {"Id":E0, "Plan":E1,"Carrera":E2,"Turno":E3,"Semestre":E5}
            df1=pd.DataFrame(data1)

            data2 = {"Agrupación asignada":d1,"Plan":d2,"Clave":d3,"Materia":d4,"Carrera":d5,"Semestre":d6,"Empleado":d7,"Hora":d8,"Turno":d9,"Dia":d10,"Salón":d11}
            df2=pd.DataFrame(data2)

            df1.to_excel(writer,"Agrupaciones",index=False)
            df2.to_excel(writer,"Materias",index=False)

            writer.save()
            writer.close()

            messagebox.showinfo("Completado","Excel creado.")

    #_________________________________________________Función para importar archivo______________________#
    def Importar_Archivo(self):
        archivoPath = filedialog.askopenfilename(title="Abrir", initialdir = "C:/", filetypes = [("Archivos excel","*.xlsx")])
        datos = pd.read_excel(archivoPath,header=0,engine = 'openpyxl')
        print(datos)
        print("_____________")
        print(datos["Semestre"])
        print(datos.ix[0:3])


    #__________________________________________Funcion al cerrar la aplicación________________________________#
    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Estas seguro que quieres salir?"):
            self.eliminar_todo()
            self.window.destroy()

    #________________________________Funcion para actualizar tabla______________________________#
    def actualizar_treeview(self):
        self.tabla.delete(*self.tabla.get_children())

        self.info_para_actualizar=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        #cin=len(self.info_para_actualizar)
        if len(self.info_para_actualizar) != 0:
            for i in self.info_para_actualizar:
                self.tabla.insert(parent="",index="end", text="", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[9],i[10]))

        self.entry_registros.delete(0, END)
        self.longitud = len(self.info_para_actualizar)
        self.entry_registros.insert(END,self.longitud)
    #___________________________Definir el turno extra______________________#
    def definir_turno2(self):
        listaMatutino=["M1","M2","M3","M4","M5","M6"]
        listaVespertino=["V1","V2","V3","V4","V5","V6"]
        listaNocturno=["N1","N2","N3","N4","N5","N6"]
        valorturno = self.extra_combobox_horas.get()
        for i in listaMatutino:
            if i ==valorturno:
                self.extra_combobox_turno.insert(END,"Matutino")
                break
        for x in listaVespertino:
            if x ==valorturno:
                self.extra_combobox_turno.insert(END,"Vespertino")
                break
        for y in listaNocturno:
            if y ==valorturno:
                self.extra_combobox_turno.insert(END,"Nocturno")
                break
    #______________________________FUNCION PARA ACTUALIZAR VALORES EDITADOS__________________________________#
    def actualizar(self):
        decision2=messagebox.askquestion("Confirmar","¿Seguro que quieres actualizar el registro?")
        if decision2 == "yes":
            self.extra_combobox_turno = Entry()
            self.definir_turno2()

            self.db.cursor.execute("UPDATE Grupos_desordenados SET Plan = ? WHERE Id = ?",self.extra_plan.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Materia = ? WHERE Id = ?",self.extra_materia.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Carrera = ? WHERE Id = ?",self.extra_combobox_carrera.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Semestre = ? WHERE Id = ?",self.extra_combobox_semestre.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Empleado = ? WHERE Id = ?",self.extra_empleado.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Hora = ? WHERE Id = ?",self.extra_combobox_horas.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Clave = ? WHERE Id = ?",self.extra_clave.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Turno = ? WHERE Id = ?",self.extra_combobox_turno.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Dias = ? WHERE Id = ?",self.extra_combobox_dias.get(),self.valor_extra0)
            self.db.cursor.execute("UPDATE Grupos_desordenados SET Salon = ? WHERE Id = ?",self.extra_salon.get(),self.valor_extra0)

            self.db.cursor.commit()
            self.top.destroy()
            messagebox.showinfo("Completado","Actualizacion de datos  completada.")
            self.actualizar_treeview()

    #_______________________________INCORPORAR VALORES PARA EDITAR__________________________________________#
    def meter_valores_extra(self):
        Carrera=["IME","IMA","IAS","IEC","IEA","IMT","ITS","IMTC","Manufactura","Aeronáutica","Biomedico"]
        Semestre=["1","2","3","4","5","6","7","8"]
        horas=["M1", "M2", "M3","M4","M5","M6","V1","V2","V3","V4","V5","V6","N1","N2","N3","N4","N5","N6"]
        dias=["L-M-V","Martes","Jueves"]

        seleccion = self.tabla.focus()
        values = self.tabla.item(seleccion,"values")

        self.infoC=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        if len(self.infoC) != 0:
            self.valor_extra0=values[0]
            valor_extra1 = values[1];valor_extra2 = values[2];valor_extra3 = values[3];valor_extra4 = values[4];valor_extra5 = values[5];valor_extra6 = values[6];valor_extra7 = values[7];valor_extra8 = values[8];valor_extra9 = values[9];
            self.extra_plan.insert(END,valor_extra1)
            self.extra_clave.insert(END,valor_extra2)
            self.extra_materia.insert(END,valor_extra3)
            self.extra_empleado.insert(END,valor_extra6)
            self.extra_salon.insert(END,valor_extra9)

            a=-1
            for xa in Carrera:
                a+=1
                if xa==valor_extra4:
                    self.extra_combobox_carrera.current(a)
                    break
            b=-1
            for xb in Semestre:
                b+=1
                if xb==valor_extra5:
                    self.extra_combobox_semestre.current(b)

            c=-1
            for xc in horas:
                c+=1
                if xc==valor_extra7:
                    self.extra_combobox_horas.current(c)

            d=-1
            for xd in dias:
                d+=1
                if xd==valor_extra8:
                    self.extra_combobox_dias.current(d)

    def crear_ventana_edicion(self):
        self.top=Toplevel()
        self.top.grab_set()
        self.top.transient(master=None)
        self.top.title("Editar registro")
        self.top.geometry("450x600+100+50")
        self.top.resizable(False, True)
        self.top.iconbitmap('images/ico_fime.ico')
        self.top.configure(background="white")
        self.canvas2 = Canvas(self.top,bg = "#ffffff",height = 600,width = 450,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas2.place(x = 0, y = 0)

        self.bg_ventanaExtra = PhotoImage(file = f"images/bg_extra.png")
        background = self.canvas2.create_image(224.0, 300.0,image=self.bg_ventanaExtra)

        #----------------------------------------Entry's-------------------------------------------------#
        extra_entry0_bg = self.canvas2.create_image(256.0, 144.0, image = self.entry0_img)
        self.extra_plan = Entry(self.top,bd = 0,bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 12))
        self.extra_plan.place(x = 196.0, y = 126,width = 120.0,height = 28)
        self.extra_plan.bind("<FocusIn>", self.focus)
        self.extra_plan.bind("<FocusOut>", self.sinfocus)

        extra_entry3_bg = self.canvas2.create_image(256.0, 195.0,image = self.entry0_img)
        self.extra_clave = Entry(self.top,bd = 0,bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 12))
        self.extra_clave.place(x = 196.0, y = 177,width = 120.0,height = 28)
        self.extra_clave.bind("<FocusIn>", self.focus)
        self.extra_clave.bind("<FocusOut>", self.sinfocus)

        extra_entry2_bg = self.canvas2.create_image(256.0, 246.0,image = self.entry0_img)
        self.extra_materia = Entry(self.top,bd = 0,bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 12))
        self.extra_materia.place(x = 196.0, y = 228,width = 120.0,height = 28)
        self.extra_materia.bind("<FocusIn>", self.focus)
        self.extra_materia.bind("<FocusOut>", self.sinfocus)

        extra_entry1_bg = self.canvas2.create_image(256.0, 399.0,image = self.entry0_img)
        self.extra_empleado = Entry(self.top,bd = 0,bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 12))
        self.extra_empleado.place(x = 196.0, y = 381,width = 120.0,height = 28)
        self.extra_empleado.bind("<FocusIn>", self.focus)
        self.extra_empleado.bind("<FocusOut>", self.sinfocus)

        extra_entry4_bg = self.canvas2.create_image(256.0, 450.0,image = self.entry0_img)
        self.extra_salon = Entry(self.top,bd = 0,bg = "#c4c4c4",highlightthickness = 0,font = ("Tahoma", 12))
        self.extra_salon.place(x = 196.0, y = 432,width = 120.0,height = 28)
        self.extra_salon.bind("<FocusIn>", self.focus)
        self.extra_salon.bind("<FocusOut>", self.sinfocus)

        #--------------------------------------Combobox-----------------------------------------#
        Carrera=["IME","IMA","IAS","IEC","IEA","IMT","ITS","IMTC","Manufactura","Aeronáutica","Biomedico"]
        self.extra_combobox_carrera = ttk.Combobox(self.top,values = Carrera,width=7,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.extra_combobox_carrera.current(0),
        self.extra_combobox_carrera.place( x=120, y = 270)

        Semestre=["1","2","3","4","5","6","7","8"]
        self.extra_combobox_semestre = ttk.Combobox(self.top,values = Semestre,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.extra_combobox_semestre.current(0)
        self.extra_combobox_semestre.place( x=120, y = 320)

        horas=["M1", "M2", "M3","M4","M5","M6","V1","V2","V3","V4","V5","V6","N1","N2","N3","N4","N5","N6"]
        self.extra_combobox_horas = ttk.Combobox(self.top,values = horas,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.extra_combobox_horas.current(0),
        self.extra_combobox_horas.place( x=305, y = 270)

        dias=["L-M-V","Martes","Jueves"]
        self.extra_combobox_dias = ttk.Combobox(self.top,values = dias,width=5,state = "readonly",cursor="hand2", font = ("Tahoma", 12),foreground = "black")
        self.extra_combobox_dias.current(0),
        self.extra_combobox_dias.place( x=305, y = 320)
        #----------------------------------Boton-------------------------------------
        self.extra_img0 = PhotoImage(file = f"images/img_actualizar.png")
        extra_boton_actualizar = Button(self.top,image = self.extra_img0,command=self.actualizar,borderwidth = 0,highlightthickness = 0,relief = "flat",curso="hand2",bg="#59B04C",activebackground="#59B04C")
        extra_boton_actualizar.place(x = 184, y = 496,width = 100,height = 35)

        self.meter_valores_extra()

    def crear_CRUD_edicion(self):
        seleccion = self.tabla.focus()
        values = self.tabla.item(seleccion,"values")

        if values =="":
            messagebox.showinfo("Error","No ha seleccionado un registro")
        else:
            self.infoC=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
            if len(self.infoC) != 0:
                self.crear_ventana_edicion()
                    

    def eliminar_todo(self):
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
        self.eliminar_todo()
        self.window.destroy()
        window=ThemedTk(theme="adapta")
        llamada = Menu_organizacion(window, "Menú", 1350, 670)
        window.mainloop()

    def checar_empleado_hora(self):
        self.variable_checar_empleado_hora=False
        self.tupla_checar_empleado_hora=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        count=0
        if len(self.tupla_checar_empleado_hora) != 0:
            for chequeo_clave in self.tupla_checar_empleado_hora:
                atrapar_clave = chequeo_clave[6]
                atrapar_hora = chequeo_clave[7]
                if self.entry5.get() == atrapar_clave and self.entry6.get() == atrapar_hora:
                    self.variable_checar_empleado_hora=True

    def checar_salon(self):
        self.variable_checar_salon=False
        self.tupla_checar_salon=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()

        if len(self.tupla_checar_salon) != 0:
            for recorrido in self.tupla_checar_salon:
                cheque_1 = recorrido[9]
                cheque_2 = recorrido[7]
                cheque_3 = recorrido[10]
                #dia,Hora,salon
                if self.entry8.get() == cheque_1 and self.entry6.get() == cheque_2 and self.entry9.get() == cheque_3:
                    self.variable_checar_salon=True

    def agregar_elementos(self):
        if self.entry0.get() != "" and self.entry1.get() != "" and self.entry2.get() != "" and self.entry3.get() != "" and self.entry4.get() != "" and self.entry5.get() != "" and self.entry6.get() != "" and self.entry8.get() != "" and self.entry9.get() != "":
            if messagebox.askokcancel(message="¿Deseas completar el registro?", title="Confirmar registro"):
                self.checar_clave()
                self.checar_empleado_hora()
                self.checar_salon()
                if self.ComprobacionClave==True:
                    messagebox.showinfo("Error","El valor Clave ya esta registrado en la base de datos.")
                elif self.variable_checar_empleado_hora==True:
                    messagebox.showinfo("Error","El valor Hora ya esta registrado en la base de datos con ese Empleado.")
                elif self.variable_checar_salon==True:
                    messagebox.showinfo("Error","El salón indicado ya tiene esa hora asignada.")
                else:
                    self.entry7 = Entry()
                    self.definir_turno()
                    self.db.cursor.execute(f"INSERT INTO Grupos_desordenados (Plan, Materia, Carrera, Semestre, Empleado, Hora, Clave,Turno,Dias,Salon) VALUES ('{self.entry0.get()}', '{self.entry2.get()}', '{self.entry3.get()}','{self.entry4.get()}','{self.entry5.get()}','{self.entry6.get()}','{self.entry1.get()}','{self.entry7.get()}','{self.entry8.get()}','{self.entry9.get()}')")
                    self.db.cursor.commit()
                    self.entry0.delete(0, END); self.entry1.delete(0, END); self.entry2.delete(0, END); self.entry3.delete(0, END); self.entry4.delete(0, END)
                    self.entry5.delete(0, END); self.entry6.delete(0, END); self.entry7.delete(0, END); self.entry8.delete(0, END);self.entry9.delete(0, END)
                    messagebox.showinfo("Completado","Actualizacion de datos  completada.")
                    self.actualizar_treeview()
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
        if len(self.info_clave) != 0:
            for chequeo_clave in self.info_clave:
                atrapar_clave = chequeo_clave[2]
                if self.entry1.get() == atrapar_clave:
                    self.ComprobacionClave = True 

    def checar_turno(self):
        self.Veredicto = False
        self.inf_A=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
        count=0
        if len(self.infoA) != 0:
            for chequeo_hora in self.inf_A:
                atrapar_grupo = chequeo_hora[1]
                if int(self.ValorChequeoA) == int(atrapar_grupo):
                    if self.ValorChequeo == chequeo_hora[8]:
                        self.Veredicto = True 

    def nueva_tabla_access(self):
        self.db.cursor.execute(f"DELETE FROM Tabla_temporal")
        self.db.cursor.commit()
        recogerinformacion_paraneuva_tabla=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()
        for i in recogerinformacion_paraneuva_tabla:
            valorA0=i[0]; valorA1= i[1];valorA2= i[2];valorA3= i[3];valorA4= i[4];valorA5= i[5];valorA6= i[6];valorA7= i[7];valorA8= i[8];valorA9= i[9];valorA10= i[10]
            self.db.cursor.execute(f"INSERT INTO Tabla_temporal (Id,Plan, Clave, Materia, Carrera, Semestre, Empleado, Hora,Turno,Dias,Salon) VALUES ('{valorA0}','{valorA1}','{valorA2}','{valorA3}','{valorA4}','{valorA5}','{valorA6}','{valorA7}','{valorA8}','{valorA9}','{valorA10}')")
        self.db.cursor.commit()

    def eliminar_registro(self):
        seleccion = self.tabla.focus()
        values = self.tabla.item(seleccion,"values")

        if values =="":
            messagebox.showinfo("Error","No ha seleccionado un registro")
        else:
            decision2=messagebox.askquestion("Confirmar","¿Seguro que quieres eliminar el registro?")
            if decision2 == "yes":
                self.infoC=self.db.cursor.execute(f"SELECT * FROM Grupos_desordenados").fetchall()

                if len(self.infoC) != 0:
                        valor_eliminar = values[0]
                        self.db.cursor.execute(f"DELETE FROM Grupos_desordenados WHERE Id = ?", valor_eliminar)
                        self.db.cursor.commit()
                        messagebox.showinfo("Completado","Registro eliminado.")
                        self.actualizar_treeview()

    def checar_turno_2(self):
        self.Veredicto2 = False
        self.inf_A2=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
        count=0
        if len(self.inf_A2) != 0:
            for chequeo_hora in self.inf_A2:
                atrapar_grupo = chequeo_hora[1]
                if int(self.ValorChequeoA2) == int(atrapar_grupo):
                    if self.ValorChequeo2 == chequeo_hora[8] and self.valor_dia2 == chequeo_hora[10]:
                        self.Veredicto2 = True

    def crear_grupos(self):
        self.nueva_tabla_access()
        self.info_crear_grupos=self.db.cursor.execute(f"SELECT * FROM Tabla_temporal").fetchall()

        if len(self.info_crear_grupos) != 0:
            for i in self.info_crear_grupos:
                comprobar_grupos_ordenados=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()
                comprobation=False
                for g6 in comprobar_grupos_ordenados:
                    v1=g6[0]
                    v2=i[0]
                    if v2 == v1 or i==None:
                        comprobation=True
                if comprobation==False:
                    valorA0= i[0]; valorA1= i[1]; valorA2= i[2]; valorA3= i[3]; valorA4= i[4]; valorA5= i[5]; valorA6= i[6]; valorA7= i[7]; valorA8= i[8];valorA9= i[9];valorA10= i[10]

                    self.db.cursor.execute(f"INSERT INTO Agrupacion (Plan, Carrera, Turno,id_primer_materia,semestre) VALUES ('{valorA1}','{valorA4}','{valorA8}','{valorA0}','{valorA5}')")
                    self.db.cursor.commit()

                    self.info_agrupaciones=self.db.cursor.execute(f"SELECT * FROM Agrupacion").fetchall()
                    for a in self.info_agrupaciones: #Conseguir la info de agrupaciones
                        valorlidadndo = a[0]   #ID DEL GRUPO
                        VALORC4 = a[4]   # ID DE LA MATERIA CON LA QUE SE DIO DE ALTA LA AGRUPACION

                        if int(valorA0) == int(VALORC4):
                            VALORC0 = valorlidadndo
                            self.db.cursor.execute(f"INSERT INTO Grupos_ordenados (Id,Grupo_asignado,Plan, Clave,Materia, Carrera, Semestre, Empleado, Hora,Turno,Dias,Salon) VALUES ('{valorA0}','{VALORC0}','{valorA1}','{valorA2}','{valorA3}', '{valorA4}', '{valorA5}', '{valorA6}', '{valorA7}', '{valorA8}','{valorA9}','{valorA10}')")
                            self.db.cursor.execute(f"DELETE FROM Tabla_temporal WHERE Id = ?", valorA0)
                            self.db.cursor.commit()

                    for x in self.info_crear_grupos:
                        valorB0= x[0]; valorB1= x[1]; valorB2= x[2]; valorB3= x[3]; valorB4= x[4]; valorB5= x[5]; valorB6= x[6]; valorB7= x[7]; valorB8= x[8];valorB9= x[9];valorB10= x[10]
                        if valorA0 == valorB0: #compruba si el id de la primera lista es igual al del segundo
                            pass
                        elif valorA9 ==valorB9:
                            if valorA1 == valorB1 and valorA2 != valorB2 and valorA3 != valorB3 and valorA4 == valorB4 and valorA5 == valorB5 and valorA7 != valorB7 and valorA8 == valorB8:
                                self.ValorChequeo = valorB7
                                self.ValorChequeoA = VALORC0
                                self.checar_turno()
                                if self.Veredicto == False:
                                    self.db.cursor.execute(f"INSERT INTO Grupos_ordenados (Id,Grupo_asignado,Plan, Clave,Materia, Carrera, Semestre, Empleado, Hora,Turno,Dias,Salon) VALUES ('{valorB0}','{VALORC0}','{valorB1}','{valorB2}','{valorB3}', '{valorB4}', '{valorB5}', '{valorB6}', '{valorB7}', '{valorB8}','{valorB9}','{valorB10}')")
                                    self.db.cursor.execute(f"DELETE FROM Tabla_temporal WHERE Id = ?", valorB0)
                                    self.db.cursor.commit()
                                    self.info_crear_grupos=self.db.cursor.execute(f"SELECT * FROM Tabla_temporal").fetchall()
                                    self.comprobar_grupos_ordenados=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()

                        elif valorA9 != valorB9:
                            if valorA1 == valorB1 and valorA2 != valorB2 and valorA3 != valorB3 and valorA4 == valorB4 and valorA5 == valorB5 and valorA8 == valorB8:
                                self.ValorChequeo2 = valorB7
                                self.ValorChequeoA2 = VALORC0
                                self.valor_dia2 = valorB9
                                self.checar_turno_2()
                                if self.Veredicto2 == False:
                                    self.db.cursor.execute(f"INSERT INTO Grupos_ordenados (Id,Grupo_asignado,Plan, Clave,Materia, Carrera, Semestre, Empleado, Hora,Turno,Dias,Salon) VALUES ('{valorB0}','{VALORC0}','{valorB1}','{valorB2}','{valorB3}', '{valorB4}', '{valorB5}', '{valorB6}', '{valorB7}', '{valorB8}','{valorB9}','{valorB10}')")
                                    self.db.cursor.execute(f"DELETE FROM Tabla_temporal WHERE Id = ?", valorB0)
                                    self.db.cursor.commit()
                                    self.info_crear_grupos=self.db.cursor.execute(f"SELECT * FROM Tabla_temporal").fetchall()
                                    self.comprobar_grupos_ordenados=self.db.cursor.execute(f"SELECT * FROM Grupos_ordenados").fetchall()

            #messagebox.showinfo("Completado","Grupos creados satisfactoriamente.")

#_____________________-----------------------------____________Constructor____________------------------------------_______________________

if __name__ == "__main__":
    #window = Tk()

    window=ThemedTk(theme="adapta")
    #login = Login(window, "Iniciar sesión", 800, 550)
    entrar_menu=Menu_organizacion(window,"Agregar",1350,670)
    window.mainloop()
