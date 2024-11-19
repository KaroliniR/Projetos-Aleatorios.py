import tkinter as tk
from tkinter import messagebox

# Funções do jogo
def verificar_vencedor():
    """Verifica se há um vencedor ou empate."""
    combinacoes = [
        [btns[0], btns[1], btns[2]],
        [btns[3], btns[4], btns[5]],
        [btns[6], btns[7], btns[8]],
        [btns[0], btns[3], btns[6]],
        [btns[1], btns[4], btns[7]],
        [btns[2], btns[5], btns[8]],
        [btns[0], btns[4], btns[8]],
        [btns[2], btns[4], btns[6]],
    ]

    for combinacao in combinacoes:
        valores = [botao["text"] for botao in combinacao]
        if valores == ["X", "X", "X"]:
            destacar_vencedor(combinacao)
            finalizar_jogo("X")
            return True
        elif valores == ["O", "O", "O"]:
            destacar_vencedor(combinacao)
            finalizar_jogo("O")
            return True

    if all(botao["text"] != "" for botao in btns):
        finalizar_jogo("Empate")
        return True

    return False

def finalizar_jogo(vencedor):
    """Exibe o resultado e reinicia o jogo."""
    if vencedor == "Empate":
        messagebox.showinfo("Jogo da Velha", "O jogo terminou em empate!")
    else:
        messagebox.showinfo("Jogo da Velha", f"Jogador {vencedor} venceu!")
    reiniciar_jogo()

def destacar_vencedor(combinacao):
    """Destaca a combinação vencedora."""
    for botao in combinacao:
        botao.config(bg="#4CAF50")

def jogar(posicao):
    """Realiza a jogada do jogador atual."""
    botao = btns[posicao]
    if botao["text"] == "":
        botao["text"] = jogador_atual[0]
        botao.config(fg="blue" if jogador_atual[0] == "X" else "red")
        if not verificar_vencedor():
            alternar_jogador()

def alternar_jogador():
    """Alterna o jogador atual."""
    jogador_atual[0] = "O" if jogador_atual[0] == "X" else "X"
    atualizar_status()

def atualizar_status():
    """Atualiza o status do jogo."""
    lbl_status.config(text=f"Jogador atual: {jogador_atual[0]}")

def reiniciar_jogo():
    """Reinicia o jogo."""
    for botao in btns:
        botao.config(text="", bg="#f0f0f0")
    jogador_atual[0] = "X"
    atualizar_status()

# Configuração da janela principal
root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("400x500")

# Variáveis globais
btns = []  # Botões do tabuleiro
jogador_atual = ["X"]  # Jogador atual

# Título
lbl_titulo = tk.Label(root, text="Jogo da Velha", font=("Arial", 24, "bold"))
lbl_titulo.pack(pady=10)

# Status
lbl_status = tk.Label(root, text="Jogador atual: X", font=("Arial", 14))
lbl_status.pack()

# Tabuleiro
frame_tabuleiro = tk.Frame(root)
frame_tabuleiro.pack()

for i in range(3):
    for j in range(3):
        botao = tk.Button(frame_tabuleiro, text="", font=("Arial", 20), width=5, height=2,
                          command=lambda pos=len(btns): jogar(pos))
        botao.grid(row=i, column=j, padx=5, pady=5)
        btns.append(botao)

# Botão de reinício
btn_reiniciar = tk.Button(root, text="Reiniciar Jogo", font=("Arial", 12), bg="#f44336", fg="white",
                          command=reiniciar_jogo)
btn_reiniciar.pack(pady=10)

# Loop principal
root.mainloop()
