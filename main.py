
from email.mime import image
from tkinter import *
from tkinter import Tk, StringVar, ttk

from PIL import Image, ImageTk

# cores

co0 = "#2e2b2b"  # preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# Criando janela

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=TRUE, height=TRUE)

style = ttk.Style(janela)
style.theme_use("clam")


# Criando frames
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Abrindo imagem

app_img = Image.open('inventorio.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Controle', width=900,
                 compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# trabalhando no frame Meio

#  criando entradas

l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW,
               font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Sala', height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)

e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)


l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW,
               font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)


l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW,
               font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)


janela.mainloop()
