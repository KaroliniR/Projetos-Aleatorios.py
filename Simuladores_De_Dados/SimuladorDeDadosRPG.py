import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

def animar_rolagem(lados, quantidade):
    """Anima a rolagem dos dados antes de mostrar o resultado final."""
    for _ in range(10):  # Número de frames da animação
        resultados = [random.randint(1, lados) for _ in range(quantidade)]
        txt_resultados.config(state="normal")
        txt_resultados.delete(1.0, tk.END)
        txt_resultados.insert(tk.END, f"Rolando {quantidade}x D{lados}...\n")
        txt_resultados.insert(tk.END, f"Resultados: {', '.join(map(str, resultados))}\n")
        txt_resultados.config(state="disabled")
        root.update_idletasks()  # Atualiza a interface
        time.sleep(0.1)  # Pequena pausa para criar o efeito de animação

    return resultados

def rolar_dados():
    try:
        lados = int(cbx_tipo_dado.get()[1:])  # Obtém o número de lados do dado (exemplo: D6 -> 6)
        quantidade = int(spn_quantidade.get())  # Obtém a quantidade de dados a serem rolados
        if quantidade <= 0:
            messagebox.showerror("Erro", "A quantidade de dados deve ser pelo menos 1.")
            return

        # Animação
        resultados = animar_rolagem(lados, quantidade)

        # Exibe o resultado final
        total = sum(resultados)
        txt_resultados.config(state="normal")
        txt_resultados.delete(1.0, tk.END)
        txt_resultados.insert(tk.END, f"Rolando {quantidade}x D{lados}...\n")
        txt_resultados.insert(tk.END, f"Resultados: {', '.join(map(str, resultados))}\n")
        txt_resultados.insert(tk.END, f"Soma total: {total}")
        txt_resultados.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador de Dados de RPG")
root.geometry("400x400")
root.resizable(False, False)

# Título
lbl_titulo = tk.Label(root, text="Simulador de Dados de RPG", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# Seleção do tipo de dado
frame_tipo = tk.Frame(root)
frame_tipo.pack(pady=10)

lbl_tipo_dado = tk.Label(frame_tipo, text="Tipo de Dado:", font=("Arial", 12))
lbl_tipo_dado.pack(side=tk.LEFT, padx=5)

tipos_dados = ["D4", "D6", "D8", "D10", "D12", "D20", "D100"]
cbx_tipo_dado = ttk.Combobox(frame_tipo, values=tipos_dados, font=("Arial", 12), state="readonly")
cbx_tipo_dado.set("D6")  # Valor padrão
cbx_tipo_dado.pack(side=tk.LEFT, padx=5)

# Seleção da quantidade de dados
frame_quantidade = tk.Frame(root)
frame_quantidade.pack(pady=10)

lbl_quantidade = tk.Label(frame_quantidade, text="Quantidade:", font=("Arial", 12))
lbl_quantidade.pack(side=tk.LEFT, padx=5)

spn_quantidade = tk.Spinbox(frame_quantidade, from_=1, to=100, font=("Arial", 12), width=5)
spn_quantidade.pack(side=tk.LEFT, padx=5)

# Botão para rolar os dados
btn_rolar = tk.Button(root, text="Rolar Dados", font=("Arial", 14), bg="#4CAF50", fg="white", command=rolar_dados)
btn_rolar.pack(pady=20)

# Área de resultados
txt_resultados = tk.Text(root, font=("Arial", 12), height=8, width=40, state="disabled")
txt_resultados.pack(pady=10)

# Botão para sair
btn_sair = tk.Button(root, text="Sair", font=("Arial", 12), bg="#f44336", fg="white", command=root.destroy)
btn_sair.pack(pady=10)

# Loop principal da interface
root.mainloop()