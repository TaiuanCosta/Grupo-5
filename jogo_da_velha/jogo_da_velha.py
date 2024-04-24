grade = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def grade_jogo(grade):  #exibir a grade do jogo
    for linha in grade:
        print(" | ".join(linha))
        print("-" * 10)


def vencedor(grade, jogador): #verifica o vencedor

    #verificar linha
    for linha in grade:
        if all(jogada == jogador for jogada in linha):
            return True
        

    #verificar coluna
    for coluna in range(3):
        if all(grade[linha][coluna] == jogador for linha in range(3)):
            return True
        

    #verificar diagonal
    if all(grade[i][i] == jogador for i in range(3)) or all(grade[i][2 - i] == jogador for i in range(3)):
        return True
    


def jogar_(grade, jogador, linha, coluna): #substitui o espaço vazio pela jogada
     if grade[linha][coluna] == " ":
        grade[linha][coluna] = jogador
        return True
     else:
          print("Essa posição já foi preenchida!! jogue novamente.")
          return False


def jogo_da_velha():
    grade = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]

    jogador = "X" #define que a primeira jogada sera do jogador x
    while True:
        grade_jogo(grade)
        linha = int(input(f"Jogador ({jogador}) Digite a linha 0, 1, 2: "))
        coluna = int(input(f"Jogador ({jogador}) Digite a coluna 0, 1, 2: "))
        print("\n")

        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2: #verifica se a jogada1
            print("Jogada inválida. Jogue novamente!")
            continue
        if jogar_(grade, jogador, linha, coluna):
            if vencedor(grade, jogador):
                grade_jogo(grade)
                print(f"{jogador} Venceu!!!")
                break
            elif " " not in [jogada for linha in grade for jogada in linha]:
                grade_jogo(grade)
                print("Empate!!")
                break
            jogador = "O" if jogador == "X" else "X"

jogo_da_velha()
