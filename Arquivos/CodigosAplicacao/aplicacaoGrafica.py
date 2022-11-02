# Autor: Rômulo Souza Fernandes
# E-mail: 00119110559@pq.uenf.br
# Data de criação: 28/10/22
# Ciência da Computação - UENF
# Disciplina: PLP


# Importando todo conteúdo do Tkinter
from tkinter import *

# Classe que exibe os controles na tela


class Application:
    def __init__(self, master=None):
        # Criação do primeiro container, chamado widget1
        self.widget1 = Frame(master)
        # Informando o gerenciador de geometria pack
        self.widget1.pack()
        # Utilizando o widget label para imprimir na tela
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()


# Instanciando a classe TK()
# Ela permite que os widgets sejam utilizados na aplicação
root = Tk()

# Passando a variável root como parâmetro do metodo
# construtor da classe Application
Application(root)

# Chamada do metodo para exibir na tela
root.mainloop()
