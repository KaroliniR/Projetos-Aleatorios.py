import random

def jogo_chute():
    print("Vou chutar um número de 0 a 20. Tente adivinhar!")
    numero_certo = random.randint(0, 20)
    while True:
        try:
            chute = int(input("Qual é o seu palpite? "))
            if chute < 0 or chute > 20:
                print("Por favor, escolha um número entre 0 e 20.")
            elif chute == numero_certo:
                print("Parabéns! Você acertou o número!")
                break
            else:
                print("Errado! Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

jogo_chute()
