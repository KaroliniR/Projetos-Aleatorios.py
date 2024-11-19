import tkinter as tk
from tkinter import messagebox
import random

# Funções do jogo
def verificar_vencedor():
    """Verifica se há um vencedor ou se deu empate."""
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
            finalizar_jogo("X")
            return True
        elif valores == ["O", "O", "O"]:
            finalizar_jogo("O")
            return True

    if all(botao["text"] != "" for botao in btns):
        finalizar_jogo("Empate")
        return True

    return False

def finalizar_jogo(vencedor):
    """Exibe a mensagem do resultado e encerra o jogo."""
    if vencedor == "Empate":
        messagebox.showinfo("Jogo da Velha", "O jogo terminou em empate!")
    else:
        messagebox.showinfo("Jogo da Velha", f"Jogador {vencedor} venceu!")
    reiniciar_jogo()

def jogar(posicao):
    """Executa uma jogada para o jogador atual."""
    botao = btns[posicao]
    if botao["text"] == "":
        botao["text"] = jogador_atual[0]
        if not verificar_vencedor():
            alternar_jogador()

def jogar_maquina():
    """Executa uma jogada da máquina."""
    jogadas_disponiveis = [i for i, btn in enumerate(btns) if btn["text"] == ""]
    if jogadas_disponiveis:
        posicao = random.choice(jogadas_disponiveis)
        btns[posicao]["text"] = "O"
        verificar_vencedor()

def alternar_jogador():
    """Altera o jogador atual."""
    jogador_atual[0] = "O" if jogador_atual[0] == "X" else "X"
    if modo_jogo[0] == "IA" and jogador_atual[0] == "O":
        jogar_maquina()

def reiniciar_jogo():
    """Reinicia o tabuleiro do jogo."""
    for botao in btns:
        botao["text"] = ""
    jogador_atual[0] = "X"

def selecionar_modo(modo):
    """Define o modo de jogo (2 jogadores ou IA) e reinicia o jogo."""
    modo_jogo[0] = modo
    reiniciar_jogo()

# Configuração da janela principal
root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("400x500")

# Variáveis globais
btns = []  # Lista de botões do tabuleiro
jogador_atual = ["X"]  # Jogador atual ("X" ou "O")
modo_jogo = ["Amigo"]  # Modo de jogo ("Amigo" ou "IA")

# Título
lbl_titulo = tk.Label(root, text="Jogo da Velha", font=("Arial", 24, "bold"))
lbl_titulo.pack(pady=10)

# Tabuleiro
frame_tabuleiro = tk.Frame(root)
frame_tabuleiro.pack()

for i in range(3):
    for j in range(3):
        botao = tk.Button(frame_tabuleiro, text="", font=("Arial", 20), width=5, height=2,
                          command=lambda pos=len(btns): jogar(pos))
        botao.grid(row=i, column=j, padx=5, pady=5)
        btns.append(botao)

# Botões para seleção de modo
frame_modo = tk.Frame(root)
frame_modo.pack(pady=20)

btn_amigo = tk.Button(frame_modo, text="Jogar com Amigo", font=("Arial", 12),
                       command=lambda: selecionar_modo("Amigo"))
btn_amigo.grid(row=0, column=0, padx=10)

btn_maquina = tk.Button(frame_modo, text="Jogar com Máquina", font=("Arial", 12),
                        command=lambda: selecionar_modo("IA"))
btn_maquina.grid(row=0, column=1, padx=10)

# Botão para reiniciar
btn_reiniciar = tk.Button(root, text="Reiniciar Jogo", font=("Arial", 12), bg="#f44336", fg="white",
                          command=reiniciar_jogo)
btn_reiniciar.pack(pady=10)

# Loop principal da interface
root.mainloop()