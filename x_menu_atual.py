from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

def conectar_banco():
    global conexao
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='( o _ 0 )'
        )
        cursor = conexao.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS la_burguer')
        cursor.close()
        conexao.close()

        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='( o _ 0 )',
            database='la_burguer'
        )
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            lanche VARCHAR(255), 
            quantidade INT, 
            preco FLOAT, 
            VENDAS INT )''')
        conexao.commit()
        cursor.close()
        messagebox.showinfo("Sucesso", "Banco conectado com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco: {err}")
        exit()

def abrir_menu():
    janela_inicial.destroy()
    janela_menu.deiconify()

janela_inicial = Tk()
janela_inicial.title("La Burguer - Início")
janela_inicial.geometry("500x400")

Label(janela_inicial, text="Bem-vindo ao La Burguer", font=("Arial", 20, "bold")).pack(pady=60)
Button(janela_inicial, text="Acessar Menu", font=("Arial", 14), bg="green", fg="white", command=abrir_menu).pack(pady=20)
Button(janela_inicial, text="Conectar ao Banco de Dados", font=("Arial", 14), bg="blue", fg="white", command=conectar_banco).pack(pady=10)

janela_menu = Tk()
janela_menu.withdraw()
janela_menu.title("La_burguer_menu")
janela_menu.geometry("1300x1000")

papel_parede = Image.open("/home/joao-pedro/Documents/GitHub/La_Burguer/imagens/La-burguer (2).png")
tk_imagem = ImageTk.PhotoImage(papel_parede)
Label(janela_menu, image=tk_imagem).pack()

contador_itens = {'item1': 0, 'item2': 0, 'item3': 0, 'item4': 0}
label_do_contador = {
    'item1': Label(janela_menu, text="0"),
    'item2': Label(janela_menu, text="0"),
    'item3': Label(janela_menu, text="0"),
    'item4': Label(janela_menu, text="0")
}

label_do_contador['item1'].place(x=200, y=600)
label_do_contador['item2'].place(x=480, y=600)
label_do_contador['item3'].place(x=730, y=600)
label_do_contador['item4'].place(x=1000, y=600)

def atualizar_contadores(item):
    label_do_contador[item].config(text=str(contador_itens[item]))

def adiciona_do_contador(item):
    contador_itens[item] += 1
    atualizar_contadores(item)

def decrementa_do_carrinho(item):
    if contador_itens[item] > 0:
        contador_itens[item] -= 1
        atualizar_contadores(item)

Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item1')).place(x=200, y=550, width=135, height=35)
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item2')).place(x=480, y=550, width=135, height=35)
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item3')).place(x=730, y=550, width=135, height=35)
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item4')).place(x=1000, y=550, width=135, height=35)

Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item1')).place(x=250, y=585, width=80, height=30)
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item2')).place(x=520, y=585, width=80, height=30)
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item3')).place(x=780, y=585, width=80, height=30)
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item4')).place(x=1050, y=585, width=80, height=30)

def prosseguir_compra():
    total = sum(contador_itens.values())
    if total == 0:
        messagebox.showwarning("Carrinho vazio", "Adicione itens ao carrinho antes de prosseguir.")
    else:
        finalizar_compra()

Button(janela_menu, text="Prosseguir com a compra", fg="white", bg="green",
       font=("Arial", 12, "bold"), command=prosseguir_compra).place(x=550, y=630, width=200, height=40)

def finalizar_compra():
    janela_finaalizar = Toplevel()
    janela_finaalizar.title("Finalizar compra")
    janela_finaalizar.geometry("500x600")

    frame_itens = Frame(janela_finaalizar)
    frame_itens.pack(pady=20)

    Label(frame_itens, text="Itens selecionados", font="Arial 14 bold").pack()

    cardapio = {
        "Classico da casa": 24,
        "Egg burguer": 25,
        "Smash Tradicional": 27,
        "Cheese e bacon": 28
    }

    valor_total = 0
    contador = 1
    for nome, preco in cardapio.items():
        qtd = contador_itens[f'item{contador}']
        if qtd > 0:
            subtotal = preco * qtd
            Label(frame_itens, text=f"{nome} x{qtd} - R$ {subtotal:.2f}", font="Arial 12").pack()
            valor_total += subtotal
        contador += 1

    Label(janela_finaalizar, text=f"\nTotal a pagar: R$ {valor_total:.2f}", font="Arial 14 bold").pack()
    Label(janela_finaalizar, text="Digite o valor pago (R$):", font="Arial 12").pack(pady=5)
    entrada_valor_pago = Entry(janela_finaalizar, font="Arial 12")
    entrada_valor_pago.pack()

    def calcular_troco():
        try:
            valor_pago = float(entrada_valor_pago.get())
            if valor_pago < valor_total:
                messagebox.showerror("Erro", "Valor insuficiente.")
            else:
                troco = valor_pago - valor_total
                messagebox.showinfo("Pagamento aprovado", f"Troco: R$ {troco:.2f}")
                janela_finaalizar.destroy()
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido.")

    Button(janela_finaalizar, text="Confirmar pagamento", command=calcular_troco,
           bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

janela_inicial.mainloop()
