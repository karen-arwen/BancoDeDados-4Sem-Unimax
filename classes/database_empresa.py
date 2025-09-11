import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", # ou IP do servidor
    user="seu_usuario", # ex: "root"
    password="sua_senha", # ex: "123456"
)


try:
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="meu_banco"
    )
    print("Conexão bem-sucedida!")
except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")

cursor = conexao.cursor()


cursor.execute("SELECT * FROM sua_tabela")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)



cursor.close()
conexao.close()

