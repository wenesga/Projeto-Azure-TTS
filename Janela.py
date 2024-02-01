import tkinter as tk
from tkinter import ttk

class StyledCombobox(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._handle_popdown_font()

    def _handle_popdown_font(self):
        popdown = self.tk.eval('ttk::combobox::PopdownWindow %s' % self)
        self.tk.call('%s.f.l' % popdown, 'configure', '-font', self['font'])

class MinhaJanela:
    def __init__(self, root):
        self.root = root
        root.title("Minha Janela Principal")

        # Definindo a fonte padrão
        fonte_padrao = ("Ubuntu", 12)

        # Obtendo a largura e altura da tela
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()

        # Definindo o tamanho da janela
        largura_janela = 430
        altura_janela = 580

        # Calculando as coordenadas para centralizar a janela
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
        root.resizable(False, False)  # Desativa o redimensionamento

        # Criando um frame
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(padx=20, pady=20)

        # Adicionando um rótulo à esquerda
        rotulo_esquerda = tk.Label(self.frame_principal, text="Rótulo à Esquerda:", font=fonte_padrao)
        rotulo_esquerda.grid(row=0, column=0, sticky="w", padx=(0, 10))

        # Adicionando uma caixa de seleção à direita usando StyledCombobox
        opcoes = ["Escolha uma opção", "Opção 1", "Opção 2", "Opção 3"]
        caixa_selecao = StyledCombobox(self.frame_principal, values=opcoes, font=fonte_padrao, state="readonly", width=16)
        caixa_selecao.set(opcoes[0])
        caixa_selecao.grid(row=0, column=1, sticky="e")

        # Adicionando um novo rótulo abaixo
        rotulo_abaixo = tk.Label(self.frame_principal, text="Rótulo Abaixo:", font=fonte_padrao)
        rotulo_abaixo.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(10, 0))

        # Adicionando uma caixa de texto abaixo do rótulo
        caixa_texto = tk.Text(self.frame_principal, wrap="word", font=fonte_padrao, height=16, width=38)
        caixa_texto.grid(row=2, column=0, columnspan=2, pady=(5, 10), padx=(0, 0), sticky="w")

        # Adicionando um rótulo abaixo da caixa de texto (centralizado)
        rotulo_abaixo_caixa_texto = tk.Label(self.frame_principal, text="Rótulo Abaixo da Caixa de Texto:", font=fonte_padrao)
        rotulo_abaixo_caixa_texto.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="n", padx=(0, 0))

        # Adicionando dois botões na mesma linha
        botao_esquerda = tk.Button(self.frame_principal, text="Esquerda", font=fonte_padrao, width=10, height=2)
        botao_esquerda.grid(row=4, column=0, pady=(20, 30), padx=(0, 0), sticky="w")

        botao_direita = tk.Button(self.frame_principal, text="Direita", font=fonte_padrao, width=10, height=2)
        botao_direita.grid(row=4, column=1, pady=(20, 30), padx=(0, 0), sticky="e")

if __name__ == "__main__":
    root = tk.Tk()
    app = MinhaJanela(root)
    root.mainloop()
