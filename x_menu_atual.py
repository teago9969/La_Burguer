from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

##-----------------Conectando ao banco de dados -----------------##
def conectar_banco():
    global conexao
    try:
        ## -----------------entrar no mysql ------------- ##
        conexao = mysql.connector.connect(
                host='localhost',
                user = 'root',
                password = ' ( o _ 0 )',
            
            )
        cursor = conexao.cursor()
        ## -------- Criação do banco de dados caso não exista-------- ##
        cursor.execute('CREATE DATABASE IF NOT EXISTS la_burguer')
        cursor.close()
        conexao.close()

        ##----------------- Reconecar ao banco, para evitar erro ---------- ##
        conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='( o _ 0 )',
                database='la_burguer'
            )
        cursor = conexao.cursor()
            
        ## -------- Criação da tabela caso não exista--------- ##
        tabela  = ('''CREATE TABLE IF NOT EXISTS pedidos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            lanche VARCHAR(255), 
            quantidade INT, 
            preco FLOAT, 
            VENDAS INT )''')
        
        cursor.execute(tabela)
        conexao.commit()
        cursor.close()
        messagebox.showinfo("Conectado com sucesso")
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
        exit()
  
    




# ---- Janela principal ---- #
janela_menu = Tk()
janela_menu.title("La_burguer_menu")
janela_menu.geometry("1300x1000")

# ---- Imagem de fundo ---- #
papel_parede = Image.open("/home/joao-pedro/Documents/GitHub/La_Burguer/imagens/La-burguer (2).png")
tk_imagem = ImageTk.PhotoImage(papel_parede)
label_da_imagem = Label(janela_menu, image=tk_imagem)
label_da_imagem.pack()

# ---- Funções de controle do carrinho ---- #
def atualizar_contadores(item):
    label_do_contador[item].config(text=str(contador_itens[item]))

def adiciona_do_contador(item):
    contador_itens[item] += 1
    atualizar_contadores(item)

def decrementa_do_carrinho(item):
    if contador_itens[item] > 0:
        contador_itens[item] -= 1
        atualizar_contadores(item)

# ---- Contadores de itens ---- #
contador_itens = {'item1': 0, 'item2': 0, 'item3': 0, 'item4': 0}
label_do_contador = {
    'item1': Label(janela_menu, text="0"),
    'item2': Label(janela_menu, text="0"),
    'item3': Label(janela_menu, text="0"),
    'item4': Label(janela_menu, text="0")
}

# ---- Posicionamento dos contadores ---- #
label_do_contador['item1'].place(x=200, y=600)
label_do_contador['item2'].place(x=480, y=600)
label_do_contador['item3'].place(x=730, y=600)
label_do_contador['item4'].place(x=1000, y=600)

# ---- Botões "Adicionar ao carrinho" ---- #
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item1')).place(x=200, y=550, width=135, height=35)
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item2')).place(x=480, y=550, width=135, height=35)
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item3')).place(x=730, y=550, width=135, height=35)
Button(janela_menu, text='Adicionar ao carrinho', fg='blue',
       command=lambda: adiciona_do_contador('item4')).place(x=1000, y=550, width=135, height=35)

# ---- Botões "Remover item" ---- #
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item1')).place(x=250, y=585, width=80, height=30)
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item2')).place(x=520, y=585, width=80, height=30)
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item3')).place(x=780, y=585, width=80, height=30)
Button(janela_menu, text='X', fg='red', bd=8, relief='groove',
       command=lambda: decrementa_do_carrinho('item4')).place(x=1050, y=585, width=80, height=30)

# ---- Botão para prosseguir para pagamento ---- #
def prosseguir_compra():
    total = sum(contador_itens.values())
    if total == 0:
        messagebox.showwarning("Carrinho vazio", "Adicione itens ao carrinho antes de prosseguir.")
    else:
        finalizar_compra()

Button(janela_menu, text="Prosseguir com a compra", fg="white", bg="green",
       font=("Arial", 12, "bold"), command=prosseguir_compra).place(x=550, y=630, width=200, height=40)

# ---- Função que exibe a janela de pagamento ---- #
def finalizar_compra():
    janela_finaalizar = Toplevel()
    janela_finaalizar.title("Finalizar compra")
    janela_finaalizar.geometry("500x600")

    frame_itens = Frame(janela_finaalizar)
    frame_itens.pack(pady=20)

    Label(frame_itens, text="Itens selecionados", font="Arial 14 bold").pack()
##--------------- cardápio ---------------------------------------------------------##
    cardapio = {
        "Classico da casa": 24,
        "Egg burguer": 25,
        "Smash Tradicional": 27,
        "Cheese e bacon": 28
    }
##--------------------- logica para calcular o preço a ser pago -------------------------##
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
##---------------------------------lógica para calcular o troco -----------------------------------##
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

##-------------------------- Executa a janela principal -----------------------##
janela_menu.mainloop()
