import tkinter as tk
from tkinter import messagebox
import random

def rolar_dado():
    resultado = random.randint(1, 6)
    lbl_resultado.config(text=f"Resultado: {resultado}")

def fechar_simulador():
    resposta = messagebox.askyesno("Fechar", "Tem certeza que deseja sair?")
    if resposta:
        root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador de Dado")
root.geometry("300x200")
root.resizable(False, False)

# Elementos da interface
lbl_titulo = tk.Label(root, text="Simulador de Dado", font=("Arial", 16))
lbl_titulo.pack(pady=10)

btn_rolar = tk.Button(root, text="Rolar o Dado", font=("Arial", 12), command=rolar_dado)
btn_rolar.pack(pady=10)

lbl_resultado = tk.Label(root, text="Resultado: --", font=("Arial", 14))
lbl_resultado.pack(pady=10)

btn_fechar = tk.Button(root, text="Fechar", font=("Arial", 12), command=fechar_simulador)
btn_fechar.pack(pady=10)

# Loop principal da aplicação
root.mainloop()