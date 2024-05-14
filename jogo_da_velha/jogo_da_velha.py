import os
import re  # Importe o módulo re para lidar com expressões regulares

grade = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def grade_jogo(grade):  
    print("    1   2   3")
    print("  ┌───┬───┬───┐")
    for i in range(len(grade)):
        print(f"{i+1} │ " + " │ ".join(grade[i]) + " │ ")
        if i < len(grade) - 1:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘")

def vencedor(grade, jogador):
    for linha in grade:
        if all(jogada == jogador for jogada in linha):
            return True
    
    for coluna in range(3):
        if all(grade[linha][coluna] == jogador for linha in range(3)):
            return True
    
    if all(grade[i][i] == jogador for i in range(3)) or all(grade[i][2 - i] == jogador for i in range(3)):
        return True

def jogar_(grade, jogador, linha, coluna):
    if grade[linha - 1][coluna - 1] == " ":
        grade[linha - 1][coluna - 1] = jogador
        return True
    else:
        print("Essa posição já foi preenchida!! Jogue novamente.")
        return False

def entrada_valida(entrada): #
  
    return re.match("^[0-9]+$", entrada) is not None #expressão regular para verificar se a entrada contém apenas dígitos

def jogo_da_velha():
    while True:
        jogador = "X" 
        while True:
            os.system("cls")
            print("----------Jogo da Velha----------\n")
            print("OBS!!: O X é o primeiro jogador\n")
            print("Regra 1 - Escolha número entre: 1, 2 ou 3 para definir a sua linha e a coluna.")
            print("Regra 2 - Conseguir formar uma linha reta ou diagonal de três símbolos iguais (X ou O).")
            print("Regra 3 - Se todas as posições forem ocupadas e nenhum jogador conseguir uma sequência de três símbolos iguais, termina em empate.\n\n")
            grade_jogo(grade)
            
            linha = input(f"\nJogador ({jogador}) Digite a linha 1, 2, 3: ")
            coluna = input(f"Jogador ({jogador}) Digite a coluna 1, 2, 3: ")
            print("\n")

            # Verifique se as entradas são válidas (apenas números)
            if not entrada_valida(linha) or not entrada_valida(coluna):
                print("Entrada inválida. Digite apenas números.\n")
                continue

            linha = int(linha)
            coluna = int(coluna)

            if linha < 1 or linha > 3 or coluna < 1 or coluna > 3: 
                print("Jogada inválida. Jogue novamente! \n")
                continue
            
            if jogar_(grade, jogador, linha, coluna):
                if vencedor(grade, jogador):
                    os.system("cls")
                    grade_jogo(grade)
                    print(f"\nO jogador ({jogador}) Venceu!!!")
                    break
                elif " " not in [jogada for linha in grade for jogada in linha]:
                    os.system("cls")
                    grade_jogo(grade)
                    print("\nEmpate!!")
                    break
                jogador = "O" if jogador == "X" else "X" 

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        os.system("cls")
        if jogar_novamente.lower() != "s":
            print("Até a próxima. \n") 
            break

jogo_da_velha()  
