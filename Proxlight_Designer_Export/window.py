from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1366x768")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    683.0, 344.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(268.0, 243.0,image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 208.0, y = 228,
    width = 120.0,
    height = 28)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    268.0, 498.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 208.0, y = 483,
    width = 120.0,
    height = 28)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    268.0, 345.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(
    x = 208.0, y = 330,
    width = 120.0,
    height = 28)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    268.0, 294.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry3.place(
    x = 208.0, y = 279,
    width = 120.0,
    height = 28)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 196, y = 615,
    width = 100,
    height = 35)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    268.0, 549.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry4.place(
    x = 208.0, y = 534,
    width = 120.0,
    height = 28)

self.img_ButtonEditar = PhotoImage(file = f"img1.png")
self.ButtonEditar = Button(
    image = self.img_ButtonEditar,command = self.crear_CRUD_edicion, curso= "hand2",
    borderwidth = 0,highlightthickness = 0, relief = "flat", bg="white", activebrackground="white")

self.ButtonEditar.place(x = 952, y = 545,width = 35,height = 38)

self.img_ButtonEliminarRegistro = PhotoImage(file = f"img2.png")
self.ButtonEliminarRegistro = Button(
    image = self.img_ButtonEliminarRegistro, command = self.eliminar_registro, curso= "hand2",
    borderwidth = 0, highlightthickness = 0, relief = "flat", bg="white", activebrackground="white")
self.ButtonEliminarRegistro.place(x = 882, y = 545,width = 35,height = 38)

window.resizable(False, False)
window.mainloop()
