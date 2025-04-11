import tkinter as tk
from tkinter import messagebox

# Função para verificar o login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Usuário e senha fixos para exemplo
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x200")

# Rótulos e entradas
tk.Label(janela, text="Usuário:").pack(pady=5)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

tk.Label(janela, text="Senha:").pack(pady=5)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack(pady=5)

# Botão de login
tk.Button(janela, text="Entrar", command=verificar_login).pack(pady=20)

# Executar a aplicação
janela.mainloop()
