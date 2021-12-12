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

#from ttkthemes import themed_tk as tk
"""from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *"""

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
        self.window.configure(background = '#CCCCCC')
        self.window.wm_attributes("-transparentcolor","#60b26c")
        self.window.wm_attributes("-alpha",.9)

        def on_closing():
            if messagebox.askokcancel("Salir", "¿Estas seguro que quieres salir?"):
                self.window.destroy()

        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        """--------------Imagenes--------------"""
        self.img_fondo_fime1 = PhotoImage(file=r"images/fime2.png")
        self.img_label_fondo_fime1 = Label(self.window, image = self.img_fondo_fime1,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.img_label_fondo_fime1.place(x = 0, y = 0)

        """//////////////////////////////////////////////Frame Iniciar sesion//////////////////////////////////////////////"""
        self.FrameIniciarSesion = Frame(self.window)
        self.FrameIniciarSesion.pack()
        self.FrameIniciarSesion.config(width=404, height=504,bg="#CACACA")
        self.FrameIniciarSesion.place(x=205,y=20)

        #-----------------------------Imagenes del FRAME----------------------------------#
        self.img_fondo_w = PhotoImage(file=r"images/fondo_w2.png")
        self.label_img_fondo_w = Label(self.FrameIniciarSesion, image = self.img_fondo_w,bg="#CACACA", borderwidth = 0, highlightthickness = 0)
        self.label_img_fondo_w.place(x = 2, y = 2)

        self.img_fondo_up = PhotoImage(file=r"images/fondo_up2.png")
        self.label_img_fondo_up = Label(self.FrameIniciarSesion, image = self.img_fondo_up,bg="#CACACA", borderwidth = 0, highlightthickness = 0)
        self.label_img_fondo_up.place(x = 2, y = 2)

        self.img_logo_uanl = PhotoImage(file=r"images/logo_uanl1.png")
        self.label_img_logo_uanl = Label(self.FrameIniciarSesion, image = self.img_logo_uanl,bg="#16660A", borderwidth = 0, highlightthickness = 0)
        self.label_img_logo_uanl.place(x = 40, y = 2)

        self.img_oso_fime = PhotoImage(file=r"images/fime5.png")
        self.label_img_oso_fime = Label(self.FrameIniciarSesion, image = self.img_oso_fime,bg="#16660A", borderwidth = 0, highlightthickness = 0)
        self.label_img_oso_fime.place(x = 270, y = 2)

        btn_inactive=Image.open("images/im_desactivado1.png")
        btn_active=Image.open("images/im_activado.png")
        self.window.btn_inactive = ImageTk.PhotoImage(btn_inactive)
        self.window.btn_active = ImageTk.PhotoImage(btn_active)
        """-----Estilo botones-----"""
        #style = ttk.Style()
 
        #style.configure("MiEstilo.TButton", font =("Tahoma", 15), borderwidth = 2,foreground = "black",  highlightthickness = 7, activeforeground = "#34a32a",activebackground = "white",width = 12)

        #self.ingresar_ = Label(self.FrameIniciarSesion, text = "FIME", font = ("Tahoma", 20), foreground = "#16660A",bg="white")
        #self.ingresar_.place(x=220, y=5)
        #self.ingresar_.attributes("-alpha", 0.7)
        valorxPosicion=70
        valoryPosicion=190

        self.button = Button(self.FrameIniciarSesion,image=self.window.btn_inactive,bg="white",border=0,curso="hand2",borderwidth=0,activebackground="white",width=200,height=60, command = self.ingreso,relief="sunken")
        self.button.place(x=110,y=400)

        self.button.bind("<Enter>",self.on_enter)
        self.button.bind("<Leave>",self.on_leave)

        self.img_ico_u1 = PhotoImage(file=r"images/ico_u1.png")
        self.label_img_ico_u1 = Label(self.FrameIniciarSesion, image = self.img_ico_u1,bg="white", borderwidth = 0, highlightthickness = 0)
        self.label_img_ico_u1.place(x = valorxPosicion, y = valoryPosicion+3)

        self.img_ico_c1 = PhotoImage(file=r"images/ico_c1.png")
        self.label_img_ico_c1 = Label(self.FrameIniciarSesion, image = self.img_ico_c1,bg="white", borderwidth = 0, highlightthickness = 0)
        self.label_img_ico_c1.place(x = valorxPosicion, y = valoryPosicion+98)

        self.nombre = Label(self.FrameIniciarSesion, text = "Usuario", font = ("Tahoma", 14),bg="white",foreground = "black")
        self.nombre.place(x = valorxPosicion+40, y = valoryPosicion-20)

        self.nombreIn = Entry(self.FrameIniciarSesion, width = 20, font = ("Tahoma", 16),highlightthickness = 0,
                              background = "#CACACA", foreground = "black")
        self.nombreIn.place(x = valorxPosicion+40, y = valoryPosicion+5)
        self.nombreIn.bind("<Key>", self.key)
        self.nombreIn.bind("<FocusIn>", self.focus)
        self.nombreIn.bind("<FocusOut>", self.sinfocus)
        
        self.password = Label(self.FrameIniciarSesion, text = "Contraseña", font = ("Tahoma", 14), bg="white", foreground = "black")
        self.password.place(x = valorxPosicion+40, y = valoryPosicion+75)

        self.passwordIn = Entry(self.FrameIniciarSesion,show = "•", width = 20, font = ("Tahoma", 16),
                                background = "#CACACA", foreground = "black")
        self.passwordIn.place(x = valorxPosicion+40, y = valoryPosicion+100)
        self.passwordIn.bind("<Key>", self.key)
        self.passwordIn.bind("<FocusIn>", self.focus)
        self.passwordIn.bind("<FocusOut>", self.sinfocus)
    
    #///////////---------------Funciones visuales--------------//////////////////////////////
    def on_enter(self,event):
            self.button.config(image=self.window.btn_active)

    def on_leave(self,event):
            self.button.config(image=self.window.btn_inactive)

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
        if event.widget == self.button:
            self.passwordIn.configure(state = "active")
        else:
            event.widget.configure(background = "#16660A", foreground = "white")

    def sinfocus(self, event):
        if event.widget == self.button:
            self.passwordIn.configure(state = "normal")
        else:
            event.widget.configure(background = "white", foreground = "black")

    def ingreso(self):
        NombreUsuarioAdmin = "admin"
        PasswordAdmin = "ROOT1747264"
        self.db = Conexion()
        try:
            self.db.conectar()
        except:
            print("Error al conectar")

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Empleados").fetchall()

        """Comprobracion de login"""
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

        
        """user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.w= ancho
        self.h= alto
        print(ancho, alto)"""

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

        """main_frame = Frame(self.window, bg="white")
        main_frame.pack(fill=BOTH, expand=1)

        canvas_universal = Canvas (main_frame, bg="white")
        canvas_universal.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar_universal= ttk.Scrollbar(main_frame, orient=VERTICAL, comman=canvas_universal.yview)
        scrollbar_universal.pack(side=RIGHT, fill=Y)

        canvas_universal.configure(yscrollcommand=scrollbar_universal.set)
        canvas_universal.bind("<Configure>", lambda e: canvas_universal.configure(scrollregion=canvas_universal.bbox("all")))

        FrameAll = Frame(canvas_universal,bg="white")
        canvas_universal.create_window((0,0),window=FrameAll, anchor="nw")"""

        #for thing in range(10):
            #Button(FrameAll, text=f"Button {thing} Yo!").grid(row=thing,column=0,pady=10,padx=10)
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

        frame_arriba = Frame(self.window)
        frame_arriba.pack()
        frame_arriba.config(background = "#16660A", width=1350, height=100)
        frame_arriba.place(x = 0, y = 0)

        self.img_esquina_izquierda = PhotoImage(file=r"images/esquina1.png")
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
        self.label_img_oso_fime.place(x = 1050, y = 0)

        frame_selecciones = Frame(self.window)
        #frame_selecciones.pack()
        frame_selecciones.config(bg="white",width=1350, height=90)
        frame_selecciones.place(x = 30, y = 110)

        label_carrera=Label(frame_selecciones,text="Turno:",font=("Thoma",14),background="white")
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
        frame_treeview_grupos = Frame(self.window)
        #frame_treeview_grupos.pack()
        frame_treeview_grupos.config(width=360, height=470,bg="white")
        frame_treeview_grupos.place(x = 50, y = 170)

        #ima_fondo = PhotoImage(file=r"images/fondo1.png")
        """ima_fondo=Image.open("images/fondo1.png")
        self.window.ima_fondo = ImageTk.PhotoImage(ima_fondo)
        self.img_empLabel = Label(frame_treeview_grupos, image = self.window.ima_fondo,bg="white")
        self.img_empLabel.place(x = 0, y = 0)"""

        self.img_emp = PhotoImage(file=r"images/fondo1.png")
        self.img_empLabel = Label(frame_treeview_grupos, image = self.img_emp,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.img_empLabel.place(x = 0, y = 0)

        style = ttk.Style()
        #style.theme_use("Adapta")
        style.configure("Treeview")
        style.map("Treeview", background=[("selected","#34a32a")])

        self.label_treeview_grupos=Label(frame_treeview_grupos,text="Grupos organizados",font=("Thoma",12),foreground="white",background="#16660A")
        self.label_treeview_grupos.place(x = 110, y = 10)

        self.tabla_grupos = ttk.Treeview(frame_treeview_grupos,height=16)
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
        self.recogerinformacion_grupos=self.db.cursor.execute(f"SELECT * FROM Grupos").fetchall()
        for i in self.recogerinformacion_grupos:
            value0=i[0]
            value1=i[1]
            value2=i[2]
            value3=i[3]
            self.tabla_grupos.insert(parent="",index="end", text="", values=(value0,value1,value2,value3))
        #self.tabla.pack(pady=20)
        self.tabla_grupos.place(x=16,y=40)

        self.scrollvert=Scrollbar(self.window,command=self.tabla_grupos.yview)
        self.scrollvert.place(in_=self.tabla_grupos,relx=1, relheight=1, bordermode="outside")
        self.tabla_grupos.config(yscrollcommand=self.scrollvert.set)

        self.tabla_grupos.bind("<ButtonRelease-1>", self.click_treeview)
        #--------------------------------------Tabla------------------------------------------------------------#
        cuadro_informacion = Frame(self.window)
        cuadro_informacion.pack()
        cuadro_informacion.config(width=730, height=340, bg="white")
        cuadro_informacion.place(x = 550, y = 170)

        self.img_fondo2 = PhotoImage(file=r"images/fondo2.png")
        self.label_img_fondo2 = Label(cuadro_informacion, image = self.img_fondo2,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.label_img_fondo2.place(x = 0, y = 0)

        self.labelis=Label(cuadro_informacion,text="Materias del grupo",font=("Thoma",12),foreground="white",background="#16660A")
        self.labelis.place(x = 285, y = 0)

        self.tabla = ttk.Treeview(cuadro_informacion)
        self.tabla["columns"] = ("Agrupación","Plan","Materia","Carrera","Semestre","Empleado","Hora","Capacidad")
        self.tabla.column("#0",width=0,stretch=NO)
        self.tabla.column("Agrupación",anchor=CENTER,width=60)
        self.tabla.column("Plan",anchor=CENTER,width=60)
        self.tabla.column("Materia",anchor=CENTER,width=200)
        self.tabla.column("Carrera",anchor=CENTER,width=60)
        self.tabla.column("Semestre",anchor=CENTER,width=60)
        self.tabla.column("Empleado",anchor=CENTER,width=60)
        self.tabla.column("Hora",anchor=CENTER,width=60)
        self.tabla.column("Capacidad",anchor=CENTER,width=70)

        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("Agrupación",text="Agrupación",anchor=CENTER)
        self.tabla.heading("Plan",text="Plan",anchor=CENTER)
        self.tabla.heading("Materia",text="Materia",anchor=CENTER)
        self.tabla.heading("Carrera",text="Carrera",anchor=CENTER)
        self.tabla.heading("Semestre",text="Semestre",anchor=CENTER)
        self.tabla.heading("Empleado",text="Empleado",anchor=CENTER)
        self.tabla.heading("Hora",text="Hora",anchor=CENTER)
        self.tabla.heading("Capacidad",text="Capacidad",anchor=CENTER)
        #---------------Meter información--------------------#
        #self.tabla.pack(pady=20)
        self.tabla.place(x=16,y=28)

        self.scrollvert=Scrollbar(self.window,command=self.tabla.yview)
        self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
        self.tabla.config(yscrollcommand=self.scrollvert.set)
        #/////////////////////////////////////---------------------------BOTONES-----------------------------------/////////////////////////77
        frame_botones = Frame(frame_arriba)
        frame_botones.pack()
        frame_botones.config(width=400, height=100, bg="#16660A")
        frame_botones.place(x = 650, y = 0)

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#16660A")

        self.button = ttk.Button(frame_botones,text="Agregar materia",command=self.ir_agregar,curso="hand2")
        self.button.place(x=20,y=25)

        self.button1 = ttk.Button(frame_botones,text="Editar materia",curso="hand2")
        self.button1.place(x=160,y=25)

        self.button2 = ttk.Button(frame_botones,text="Analisis",curso="hand2")
        self.button2.place(x=290,y=25)


    def click_treeview(self,e):
        seleccion = self.tabla_grupos.focus()
        values = self.tabla_grupos.item(seleccion,"values")

        self.tabla.delete(*self.tabla.get_children())

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Informacion").fetchall()
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
                self.tabla.insert(parent="",index="end", text="", values=(value1,value2,value3,value4,value5,value6,value7,value8))

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
        self.window.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.window.resizable(False, False)
        self.window.iconbitmap('images/icono.ico')
        self.window.configure(background="white")

        frame_arriba = Frame(self.window)
        frame_arriba.pack()
        frame_arriba.config(background = "#16660A", width=1350, height=100)
        frame_arriba.place(x = 0, y = 0)

        self.img_esquina_izquierda = PhotoImage(file=r"images/esquina1.png")
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
        self.label_img_oso_fime.place(x = 1050, y = 0)

        #/////////////////////////////////////---------------------------BOTONES-----------------------------------/////////////////////////77
        frame_botones = Frame(frame_arriba)
        frame_botones.pack()
        frame_botones.config(width=400, height=100, bg="#16660A")
        frame_botones.place(x = 650, y = 0)

        ttk.Style().configure("TButton", padding=6, relief="flat",background="#16660A")

        self.button = ttk.Button(frame_botones,text="Menú",command=self.ir_menu,curso="hand2")
        self.button.place(x=40,y=25)

        self.button1 = ttk.Button(frame_botones,text="Editar materia",curso="hand2")
        self.button1.place(x=160,y=25)

        self.button2 = ttk.Button(frame_botones,text="Analisis",curso="hand2")
        self.button2.place(x=290,y=25)

        #--------------------------------------Tabla------------------------------------------------------------#
        cuadro_informacion = Frame(self.window)
        cuadro_informacion.pack()
        cuadro_informacion.config(width=730, height=340, bg="white")
        cuadro_informacion.place(x = 550, y = 170)

        self.img_fondo2 = PhotoImage(file=r"images/fondo2.png")
        self.label_img_fondo2 = Label(cuadro_informacion, image = self.img_fondo2,
                                  background = "white", borderwidth = 0, highlightthickness = 0)
        self.label_img_fondo2.place(x = 0, y = 0)

        self.labelis=Label(cuadro_informacion,text="Materias del grupo",font=("Thoma",12),foreground="white",background="#16660A")
        self.labelis.place(x = 285, y = 0)

        self.tabla = ttk.Treeview(cuadro_informacion)
        self.tabla["columns"] = ("Grupo Asignado","Plan","Materia","Carrera","Semestre","Empleado","Hora","Capacidad")
        self.tabla.column("#0",width=0,stretch=NO)
        self.tabla.column("Grupo Asignado",anchor=CENTER,width=60)
        self.tabla.column("Plan",anchor=CENTER,width=60)
        self.tabla.column("Materia",anchor=CENTER,width=200)
        self.tabla.column("Carrera",anchor=CENTER,width=60)
        self.tabla.column("Semestre",anchor=CENTER,width=60)
        self.tabla.column("Empleado",anchor=CENTER,width=60)
        self.tabla.column("Hora",anchor=CENTER,width=60)
        self.tabla.column("Capacidad",anchor=CENTER,width=70)

        self.tabla.heading("#0",text="",anchor=CENTER)
        self.tabla.heading("Grupo Asignado",text="Grupo Asignado",anchor=CENTER)
        self.tabla.heading("Plan",text="Plan",anchor=CENTER)
        self.tabla.heading("Materia",text="Materia",anchor=CENTER)
        self.tabla.heading("Carrera",text="Carrera",anchor=CENTER)
        self.tabla.heading("Semestre",text="Semestre",anchor=CENTER)
        self.tabla.heading("Empleado",text="Empleado",anchor=CENTER)
        self.tabla.heading("Hora",text="Hora",anchor=CENTER)
        self.tabla.heading("Capacidad",text="Capacidad",anchor=CENTER)
        #---------------Meter información--------------------#
        #self.tabla.pack(pady=20)
        self.tabla.place(x=16,y=28)

        self.scrollvert=Scrollbar(self.window,command=self.tabla.yview)
        self.scrollvert.place(in_=self.tabla,relx=1, relheight=1, bordermode="outside")
        self.tabla.config(yscrollcommand=self.scrollvert.set)

        self.recogerinformacion=self.db.cursor.execute(f"SELECT * FROM Informacion").fetchall()
        for i in self.recogerinformacion:
            value1=i[1]
            value2=i[2]
            value3=i[3]
            value4=i[4]
            value5=i[5]
            value6=i[6]
            value7=i[7]
            value8=i[8]
            self.tabla.insert(parent="",index="end", text="", values=(value1,value2,value3,value4,value5,value6,value7,value8))

    def ir_menu(self):
        self.window.destroy()
        window=ThemedTk(theme="adapta")
        llamada = Menu_organizacion(window, "Menú", 1350, 670)
        window.mainloop()

#///////////////////////////////////////////////////////////////////////////////////////////77

if __name__ == "__main__":
    #window = Tk()

    window=ThemedTk(theme="adapta")
    #login = Login(window, "Iniciar sesión", 800, 550)
    entrar_menu=Menu_organizacion(window,"Menú",1350,670)
    window.mainloop()
