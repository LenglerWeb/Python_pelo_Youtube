from tkinter import *

# Configurações da janela
janela = Tk()
janela.title("Tela de Login")
janela.geometry("300x500")

# Widgets
Label(janela, text="Usuário:").pack()
entry_usuario = Entry(janela)
entry_usuario.pack()

Label(janela, text="Senha:").pack()
entry_senha = Entry(janela, show="*")
entry_senha.pack()

Button(janela, text="Entrar", command=lambda: print("Usuário:", entry_usuario.get(), "Senha:", entry_senha.get())).pack()

janela.mainloop()
