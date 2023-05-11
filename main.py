
from email.mime import image
from tkinter import *
from tkinter import Tk, StringVar, ttk


# importando Pillow
from PIL import Image, ImageTk

# importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

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

app_logo = Label(frameCima, image=app_img, text=' *', width=900,
                 compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# trabalhando no frame Meio

""" ---------------------------Criando entradas---------------------------------------- """

l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW,
               font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)

e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)


l_local = Label(frameMeio, text='Local', height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)

e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)


l_desecricao = Label(frameMeio, text='Desecrição', height=1, anchor=NW,
                     font=('Ivy 10 bold'), bg=co1, fg=co4)
l_desecricao.place(x=10, y=70)

e_desecricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_desecricao.place(x=130, y=71)


l_model = Label(frameMeio, text='Model', height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=100)

e_model = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=101)

""" ---------------------------Calandario---------------------------------------- """

l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW,
              font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, Background='darkblue',
                  bordewidht=2, year=2023)
e_cal.place(x=130, y=131)

""" ---------------------------valor-------------------------------------------- """

l_model = Label(frameMeio, text='Valor', height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=160)

e_model = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=161)


l_model = Label(frameMeio, text='Compra', height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=190)

e_model = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=191)


""" ---------------------------BOTAO INSERIR IMAGEM-------------------------------------------- """


l_carregar = Label(frameMeio, text='imagen do item', height=1, anchor=NW,
                   font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)


b_carregar = Button(frameMeio, width=29, text="carregar".upper(
), command=CENTER, overrelief=RIDGE, anchor=CENTER, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)


""" ---------------------------BOTAO ADICIONAR -------------------------------------------- """

img_add = Image.open('Add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)


b_inserir = Button(frameMeio, image=img_add, width=95, text='   ADICIONAR'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

""" ---------------------------BOTAO ATUALIZAR-------------------------------------------- """

img_update = Image.open('update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)


b_update = Button(frameMeio, image=img_update, width=95, text='   ADICIONAR'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

""" ---------------------------BOTAO DELETAR-------------------------------------------- """

img_deletar = Image.open('delete.png')
img_deletar = img_deletar.resize((20, 20))
img_deletar = ImageTk.PhotoImage(img_deletar)


b_deletar = Button(frameMeio, image=img_deletar, width=95, text='   DELETAR'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_deletar.place(x=330, y=90)

""" ---------------------------BOTAO ITEM-------------------------------------------- """
img_item = Image.open('item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)


b_item = Button(frameMeio, image=img_item, width=95, text='   VER ITEM'.upper(
), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=221)


""" ---------------------------LABEL QUANTIDADE TOTAL E VALORES-------------------------------------------- """

l_total1 = Label(frameMeio, text='', width=14, height=2, pady=5, anchor=CENTER,
                font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total1.place(x=450, y=17)

l_total = Label(frameMeio, text='  Valor total de todos os itens   ', height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=12)

# Quantidade

l_qtd1 = Label(frameMeio, text='', width=14, height=2, pady=5, anchor=CENTER,
              font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd1.place(x=450, y=90)

l_qtd = Label(frameMeio, text='  Quantidade Total de itens   ', height=1, anchor=NW,
              font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=92)



# tabela -----------------------------------------------------------

# creating a treeview with dual scrollbars
tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

lista_itens = []

global tree

tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameBaixo.grid_rowconfigure(0, weight=12)

hd=["center","center","center","center","center","center","center", 'center']
h=[40,150,100,160,130,100,100, 100]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


# inserindo os itens dentro da tabela
for item in lista_itens:
    tree.insert('', 'end', values=item)


quantidade = [8888,88]

for iten in lista_itens:
    quantidade.append(iten[6])

Total_valor = sum(quantidade)
Total_itens = len(quantidade)

l_total1['text'] = 'R$ {:,.2f}'.format(Total_valor)
l_qtd1['text'] = Total_itens


janela.mainloop()
