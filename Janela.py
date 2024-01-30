import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        root.title("Leitor de Texto - Wenes Aquino")
        root.geometry("430x560")
        root.resizable(False, False) 

        # Centralizando a janela
        self.center_window()

        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack()

        self.RotuloCaixaSelecao = tk.Label(self.frame_principal, text="Escolha uma voz:", font=("Ubuntu", 12))
        self.RotuloCaixaSelecao.grid(row=0, column=0, pady=(12, 0), padx=(22, 0), sticky="w")

        vozes = ["Francisa", "Antonio", "Brenda", "Donato", "Elza", "Fábio", "Giovanna", "Humberto",
                 "Julio", "Leila", "Letícia", "Manuela", "Nicolau", "Valerio", "Yara"]

        
        self.CaixaSelecaoVoz = ttk.Combobox(self.frame_principal, values=vozes, font=("Ubuntu", 12), state="readonly", width=11)
        self.CaixaSelecaoVoz.grid(row=0, column=1, pady=(12, 0), padx=(0, 20), sticky="w")


        self.RotuloCaixaTexto = tk.Label(self.frame_principal, text="Texto processado em voz alta:", font=("Ubuntu", 12))
        self.RotuloCaixaTexto.grid(row=1, column=0, pady=(20, 0), padx=(22, 0), sticky="w")

        self.CaixaTexto = tk.Text(self.frame_principal, wrap="word", font=("Ubuntu", 12), height=16, width=38)
        self.CaixaTexto.grid(row=2, column=0, columnspan=2, pady=(10, 10), padx=(20, 20), sticky="w")
        

        self.RotuloStatus = tk.Label(self.frame_principal, text="Mensagem de Status", font=("Ubuntu", 12))
        self.RotuloStatus.grid(row=3, column=0, pady=(10, 0), padx=(0, 0), columnspan=2, sticky="nsew")

        self.BotaoIniciar = tk.Button(self.frame_principal, text="Iniciar", font=("Ubuntu", 12), width=10, height=1)
        self.BotaoIniciar.grid(row=4, column=0, pady=(20, 30), padx=(20, 0), sticky="w")

        self.BotaoParar = tk.Button(self.frame_principal, text="Parar", font=("Ubuntu", 12), width=10, height=1)
        self.BotaoParar.grid(row=4, column=1, pady=(20, 30), padx=(0, 20), sticky="e")
        
        
    def center_window(self):
        """Centraliza a janela na tela."""
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() - width) // 2
        y = (root.winfo_screenheight() - height) // 2
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
