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

        self.window = window
        self.window.title(title)
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight() 
        self.window.geometry("%dx%d+%d+%d" % (self.w, self.h, -9, self.y))
        self.window.resizable(False, True)
        self.window.iconbitmap('images/icono.ico')
        self.window.configure(background="white")

        main_frame = Frame(self.window)
        main_frame.pack(fill=BOTH, expand=1)

        canvas_universal = Canvas (main_frame)
        canvas_universal.pack(side=LEFT,fill=BOTH,expand=1)

        scrollbar_universal= ttk.Scrollbar(main_frame, orient=VERTICAL, comman=canvas_universal.yview)
        scrollbar_universal.pack(side=RIGHT, fill=Y)

        canvas_universal.configure(yscrollcommand=scrollbar_universal.set)
        canvas_universal.bind("<Configure>", lambda e: canvas_universal.configure(scrollregion=canvas_universal.bbox("all")))

        FrameAll = Frame(canvas_universal)
        canvas_universal.create_window((0,0),window=FrameAll, anchor="nw")

        for thing in range(100):
            Button(FrameAll, text=f"Button {thing} Yo!").grid(row=thing,column=0,pady=10,padx=10)



if __name__ == "__main__":
    window = Tk()
    entrar_menu=Menu_organizacion(window,"Menú",1350,670)
    window.mainloop()
