# Importando o módulo time para poder temporizar os textos
import time

# Textos que vão aparecer na tela
def intro():
    print("Bem vindos a oficina do Segundo Ano de Redes de Computadores!")
    time.sleep(1)
    print("Você deseja jogar nosso jogo de aventura?")
    time.sleep(1)
    print("1. Sim")
    time.sleep(1)
    print("2. Não")
    time.sleep(1)

    escolha = input("Digite 1 ou 2: ")
    return escolha

def intro_seg():
    print("Você se encontra numa misteriosa caverna.")
    time.sleep(1)
    print("Seu objetivo é explorar a caverna e encontrar o tesouro.")
    time.sleep(1)
    print("Vamos começar!\n")

def esc_cam():
    print("Escolha seu caminho:")
    time.sleep(1)
    print("1. Entre o túnel escuro.")
    time.sleep(1)
    print("2. Abra a porta velha.")
    time.sleep(1)

    escolha = input("Digite 1 ou 2: ")
    return escolha

def tunel_escu():
    print("Você entra no túnel escuro.")
    time.sleep(1)
    print("É muito escuro para enxergar qualquer coisa.")
    time.sleep(1)
    print("Você pode:")
    time.sleep(1)
    print("1. Usar uma lanterna.")
    time.sleep(1)
    print("2. Ir mesmo assim.")

    escolha = input("Digite 1 ou 2: ")
    return escolha

def porta_velha():
    print("Você abre a porta velha.")
    time.sleep(1)
    print("Você se encontra num quarto com outras duas portas.")
    time.sleep(1)
    print("Você vai:")
    time.sleep(1)
    print("1. Para a esquerda.")
    time.sleep(1)
    print("2. Para a direita.")

    escolha = input("Digite 1 ou 2: ")
    return escolha

def tesouro_sala():
    print("Paranbéns! Você encontrou o tesouro.")
    time.sleep(1)
    print("Você ganhou!")

def fim_jogo():
    print("Fim de jogo! Tente novamente.")

# Aqui começa a brincadeira

def main():
    escolha = None                  # Inicializa a variável escolha
    intro()                         # Inicializa a introdução

    if escolha == "1":              # Se o input da pergunta da intro for 1 entao o intro avança para a esc_cam (escolha de caminhos)
        escolha = esc_cam()

    escolha = esc_cam()             # Se o input da pergunta da esc_cam for 1 entao ela irá avançar para o tunel_escu
    if escolha == "1":
        escolha = tunel_escu()

        if escolha == "1":          # Se a escolha do tune_escu for 1 entâo o jogador encontrará o tesouro
            tesouro_sala()
        else:                       # Senão, então o jogador perderá
            fim_jogo()

    elif escolha == "2":            # Se o jogador escolher 2 no esc_cam ele irá para o aminho da porta_velha
        escolha = porta_velha()

        if escolha == "1":          # Se o jogador escolher 1 no porta_velha ele irá achar o tesouro , sendo redirecionado assim para a tesouro_sala
            tesouro_sala()
        else:                       # Senão, o jogo finalizará e ele irá perder
            fim_jogo()
    else:                           # Se o input da perguna da intro não for 1 entao o intro 1 avança para o fim_jogo
        fim_jogo()

if __name__ == "__main__":
    main()
