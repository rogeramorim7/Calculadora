import tkinter as tk
from tkinter import messagebox

def clicar(botao):
    """Atualiza o texto da entrada com o botão clicado."""
    entrada.insert(tk.END, botao)

def calcular():
    """Avalia a expressão na entrada."""
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida!")

def limpar():
    """Limpa a entrada."""
    entrada.delete(0, tk.END)

# janela principal
janela = tk.Tk()
janela.title("Calculadora")

# grade para expansão
for i in range(5):  # 4 linhas de botões + 1 linha de entrada
    janela.grid_rowconfigure(i, weight=1)  # Permite que as linhas expandam
for j in range(4):  # 4 colunas
    janela.grid_columnconfigure(j, weight=1)  # Permite que as colunas expandam

# campo de entrada
entrada = tk.Entry(janela, font=("Arial", 18), bd=8, justify='right')
entrada.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Ocupa as 4 colunas, ajusta com `sticky`

# botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# botões dinamicamente
linha = 1
coluna = 0
for botao in botoes:
    if botao == '=':
        tk.Button(janela, text=botao, bg='green', fg='white', font=("Arial", 16),
                  command=calcular).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
    elif botao == 'C':
        tk.Button(janela, text=botao, bg='red', fg='white', font=("Arial", 16),
                  command=limpar).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(janela, text=botao, font=("Arial", 16),
                  command=lambda b=botao: clicar(b)).grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
    
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# loop da interface gráfica
janela.mainloop()

