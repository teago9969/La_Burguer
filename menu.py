from tkinter import *
from PIL import ImageTk, Image

##---------Interface da janela --------------------##
janela_menu = Tk()
janela_menu.title("La_burguer_menu")
janela_menu.geometry("1300x1000")

##---------------imagem do la burguer -----------##
papel_parede = Image.open("/home/joao-pedro/Documents/GitHub/La-Burguer/imagens/La-burguer (2).png")
tk_imagem = ImageTk.PhotoImage(papel_parede)
label_da_imagem = Label(janela_menu, image=tk_imagem)
label_da_imagem.pack()

##---------------Contadores do carrinho --------------##
def atualizar_contadores(item):
    label_do_contador[item].config(text=str(contador_itens[item]))

def adiciona_do_contador(item):
    contador_itens[item] += 1
    atualizar_contadores(item)

def decrementa_do_carrinho(item):
    if contador_itens [item] >0:
       contador_itens [item] -=1
       atualizar_contadores(item)

##----------------contadores que serão exibidos--------------##
contador_itens = {
          'item1':0,
          'item2':0,
          'item3':0,
          'item4':0}

label_do_contador = {'item1':Label(janela_menu, text="0"),
                     'item2':Label(janela_menu, text="0"),
                     'item3':Label(janela_menu, text="0"),
                     'item4':Label(janela_menu, text="0")}

label_do_contador['item1'].place(x=200,y=600)
label_do_contador['item2'].place(x=480,y=600)
label_do_contador['item3'].place(x=730,y=600)
label_do_contador['item4'].place(x=1000,y=600)


##-------  Botões do carrinho   ----------------##
botao1 = Button(janela_menu,
                text='Adicionar ao carrinho',
                fg='blue',
                command=lambda:adiciona_do_contador('item1'))
botao1.place(x=200,y=550, width=135,height=35)

botao2 = Button(janela_menu,
                text='Adicionar ao carrinho',
                fg='blue',
                 command=lambda:adiciona_do_contador('item2'))
botao2.place(x=480,y=550,width=135,height=35)

botao3 = Button(janela_menu,
                text='Adicionar ao carrinho',
                fg='blue',
                 command=lambda:adiciona_do_contador('item3'))
botao3.place( x=730,y=550,width=135,height=35)

botao4 = Button(janela_menu,
               text='Adicionar ao carrinho',
                fg='blue',
                command=lambda:adiciona_do_contador('item4'))
botao4.place(x=1000,y=550,width=135,height=35)

##------------Botão para remover itens -------------------##
botao1_remover = Button(janela_menu,
                text='X',
                fg='red',
                bd=8,
                relief='groove',
                command=lambda:decrementa_do_carrinho('item1'))
botao1_remover.place(x=250,y=585, width=80,height=30)

botao2_remover = Button(janela_menu,
                text='X',
                fg='red',
                bd=8,
                relief='groove',
                  command=lambda:decrementa_do_carrinho('item2'))
botao2_remover.place(x=520,y=585, width=80,height=30)

botao3_remover = Button(janela_menu,
                text='X',
                fg='red',
                bd=8,
                relief='groove',
                  command=lambda:decrementa_do_carrinho('item3'))
botao3_remover.place( x=780,y=585, width=80,height=30)

botao4_remover = Button(janela_menu,
               text='X',
                fg='red',
                bd=8,
                relief='groove',
                command=lambda:decrementa_do_carrinho('item4'))
botao4_remover.place(x=1050,y=585, width=80,height=30) 
from tkinter import messagebox

def prosseguir_compra():
    total = sum(contador_itens.values())
    if total == 0:
        messagebox.showwarning("Carrinho vazio", "Adicione itens ao carrinho antes de prosseguir.")
    else:
        messagebox.showinfo("Compra iniciada", f"Você está comprando {total} item(ns).")

botao_prosseguir = Button(janela_menu,
                          text="Prosseguir com a compra",
                          fg="white",
                          bg="green",
                          font=("Arial", 12, "bold"),
                          command=prosseguir_compra)
botao_prosseguir.place(x=550, y=700, width=200, height=40)

janela_menu.mainloop()
