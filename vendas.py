import mysql.connector

conexao = mysql.connector.connect(user='root',password=' ,-, ',host='curioso',database='la_burguer')

cursor = conexao.cursor()

comando = '''INSERT INTO estoque(nome,preco,vendas,quantidades) 
values
('Classico da casa', 24,0,50),
('egg burguer',      25,0,50),
('smash tradicional',27,0,50),
('Cheese e bacon',   28,0,50)

ON DUPLICATE KEY UPDATE
preco = VALUES(preco),
quantidades = VALUES(quantidades)
'''
cursor.execute(comando)
conexao.commit()
print("sucesso....")


cursor.close()
conexao.close()
