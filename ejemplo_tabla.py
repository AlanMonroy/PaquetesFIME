# -*- coding: utf-8 -*-


#=========== Python 3 ============#
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#ECCCCE", font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

        # Agregamos dos scrollbars 
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)



def ventana_reporte(parent=None):
    t3 = tk.Toplevel(parent, bg="#E8C8CD")
    t3.title("Reporte")
    t3.geometry('500x500')
    t3.configure(bg="#E8C8CD")
    t3.focus_set()
    t3.grab_set()

    clientes_headers = (u"Marca",   u"Facebook", u"Instagram",
                        u"Twitter", u"Correo",   u"Página web"
                        )


    clientes_tab = Table(t3, title="Clientes Registrados", headers=clientes_headers)
    clientes_tab.pack()

    #cursor.execute("SELECT Clientes.Marca,Facebook,Instagram,Twitter,Correo,Web FROM Clientes")
    cursor = ((u"Marca A", u"Facebook A", u"Instagram A", u"Twitter A", u"aaa@mail.com", u"www.aaa.com"),
              (u"Marca B", u"Facebook B", u"Instagram B", u"Twitter B", u"bbb@mail.com", u"www.bbb.com")
              )

    for row in cursor:
        clientes_tab.add_row(row)

    proyectos_headers = (u"Proyecto", u"Marca", u"Paquete")

    proyectos_tab = Table(t3, title="Proyectos Registrados", headers=proyectos_headers)
    proyectos_tab.pack()

    #cursor.execute("SELECT Proyectos.Proyecto,Marca,Paquete FROM Proyectos")
    cursor = ((u"Proyecto A", u"Marca A", "Paquete A"),
              (u"Proyecto B", u"Marca B", u"Paquete A"
               )
              )

    for row in cursor:
       proyectos_tab.add_row(row)




ventana  = tk.Tk()
ventana_reporte(parent=ventana)
ventana.mainloop()
