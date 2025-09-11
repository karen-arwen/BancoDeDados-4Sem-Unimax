import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ecommerce"
    )

def inserir():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    senha = entry_senha.get().strip()

    if not nome or not email or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha Nome, Email e Senha.")
        return

    cn = conectar(); cur = cn.cursor()
    cur.execute(
        "INSERT INTO Clientes (nome, `e-mail`, telefone, senha) VALUES (%s,%s,%s,%s)",
        (nome, email, telefone or None, senha)
    )
    cn.commit(); cur.close(); cn.close()
    listar(); limpar_campos()
    messagebox.showinfo("Sucesso", "Cadastro realizado.")

def atualizar():
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Seleção", "Selecione um cliente.")
        return
    id_clientes = tree.item(sel)["values"][0]

    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()
    senha = entry_senha.get().strip()

    cn = conectar(); cur = cn.cursor()
    cur.execute(
        "UPDATE Clientes SET nome=%s, `e-mail`=%s, telefone=%s, senha=%s WHERE idClientes=%s",
        (nome, email, telefone or None, senha, id_clientes)
    )
    cn.commit(); cur.close(); cn.close()
    listar(); limpar_campos()
    messagebox.showinfo("Atualizado", "Cadastro atualizado.")

def remover():
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Seleção", "Selecione um cliente.")
        return
    id_clientes = tree.item(sel)["values"][0]

    if not messagebox.askyesno("Confirmar", "Remover este cadastro?"):
        return

    cn = conectar(); cur = cn.cursor()
    cur.execute("DELETE FROM Clientes WHERE idClientes=%s", (id_clientes,))
    cn.commit(); cur.close(); cn.close()
    listar(); limpar_campos()
    messagebox.showinfo("Removido", "Cadastro removido.")

def listar():
    # Limpa a grid
    for i in tree.get_children():
        tree.delete(i)

    cn = conectar(); cur = cn.cursor()
    # Selecione explicitamente as colunas na ordem dos headers
    cur.execute("""
        SELECT idClientes, nome, `e-mail`, telefone, senha
        FROM Clientes
        ORDER BY idClientes DESC
    """)
    for row in cur.fetchall():
        tree.insert("", "end", values=row)
    cur.close(); cn.close()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_senha.delete(0, tk.END)

def iniciar():
    global entry_nome, entry_email, entry_telefone, entry_senha, tree
    janela = tk.Toplevel()
    janela.title("Cadastro de Clientes")
    janela.geometry("900x520")

    tk.Label(janela, text="Nome").grid(row=0, column=0, sticky="w", padx=8, pady=6)
    entry_nome = tk.Entry(janela, width=40); entry_nome.grid(row=0, column=1, padx=8)

    tk.Label(janela, text="Email").grid(row=1, column=0, sticky="w", padx=8, pady=6)
    entry_email = tk.Entry(janela, width=40); entry_email.grid(row=1, column=1, padx=8)

    tk.Label(janela, text="Telefone").grid(row=2, column=0, sticky="w", padx=8, pady=6)
    entry_telefone = tk.Entry(janela, width=40); entry_telefone.grid(row=2, column=1, padx=8)

    tk.Label(janela, text="Senha").grid(row=3, column=0, sticky="w", padx=8, pady=6)
    entry_senha = tk.Entry(janela, width=40, show="•"); entry_senha.grid(row=3, column=1, padx=8)

    tk.Button(janela, text="Inserir", command=inserir).grid(row=4, column=0, pady=10)
    tk.Button(janela, text="Atualizar", command=atualizar).grid(row=4, column=1, sticky="w")
    tk.Button(janela, text="Remover", command=remover).grid(row=4, column=1, sticky="e")

    cols = ("ID", "Nome", "Email", "Telefone", "Senha")
    tree = ttk.Treeview(janela, columns=cols, show="headings", height=14)
    for c in cols: tree.heading(c, text=c)
    tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    janela.grid_rowconfigure(5, weight=1)
    janela.grid_columnconfigure(2, weight=1)

    listar()
