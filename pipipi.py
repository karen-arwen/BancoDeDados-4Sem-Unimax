import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empresa"
    )
    return conexao

def inserir_funcionario():
    nome = input("Nome do funcionário: ")
    cargo = input("Cargo do funcionário: ")
    salario = float(input("Salário do funcionário: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO funcionarios (nome, cargo, salario)
        VALUES (%s, %s, %s)
        """, 
        (nome, cargo, salario))
    conexao.commit()
    print("Funcionário inserido com sucesso!")
    cursor.close()
    conexao.close()

def excluir_funcionario():
    nome = input("Nome do funcionário a ser excluído: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM funcionarios
        WHERE nome = %s
        """, (nome,))
    conexao.commit()
    print("Funcionário excluído com sucesso!")
    cursor.close()
    conexao.close()

def atualizar_funcionario():
    nome = input("Nome do funcionário a ser atualizado: ")
    novo_salario = float(input("Novo salário: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE funcionarios
        SET salario = %s
        WHERE nome = %s
        """, 
        (novo_salario, nome))
    conexao.commit()
    print("Funcionário atualizado com sucesso!")
    cursor.close()
    conexao.close()

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    print("Lista de Funcionários:")
    for funcionario in funcionarios:
        print(funcionario)
    cursor.close()
    conexao.close()

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        cargo VARCHAR(50),
        salario DECIMAL(10,2)
    )
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

criar_tabela()



def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir Funcionário")
        print("2. Excluir Funcionário")
        print("3. Atualizar Funcionário")
        print("4. Listar Funcionários")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            inserir_funcionario()
        elif escolha == '2':
            excluir_funcionario()
        elif escolha == '3':
            atualizar_funcionario()
        elif escolha == '4':
            listar_funcionarios()
        elif escolha == '5':
            break
        else:
            print("Opção inválida, tente novamente.")


#Interface gráfica com tkinter para preencher campos de banco de dados, botões de inserir, excluir, atualizar e listar
import tkinter as tk
from tkinter import messagebox
