import os 

grade = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def grade_jogo(grade):  
    print("    1   2   3")
    print("  ┌───┬───┬───┐")
    for i in range(len(grade)):
        print(f"{i+1} │ " + " │ ".join(grade[i]) + " │ ")
        if i < len(grade) - 1:
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘")


def vencedor(grade, jogador): #verifica se há um vencedor no jogo da velha e recebe o simbolo atual do 'jogador'

    for linha in grade: #verifica se todos os elementos da linha são iguais ao símbolo do jogador atual
        if all(jogada == jogador for jogada in linha):
            return True #retorna verdadeiro e signica que o jogador ganhou se tiver uma sequencia de simbolos iguais em alguma linha
        
    
    for coluna in range(3): #verifica se todos os elementos da coluna são iguais ao símbolo do jogador atual
        if all(grade[linha][coluna] == jogador for linha in range(3)): 
            return True #retorna verdadeiro e signica que o jogador ganhou se tiver uma sequencia de simbolos iguais em alguma coluna
        

    if all(grade[i][i] == jogador for i in range(3)) or all(grade[i][2 - i] == jogador for i in range(3)): #esta linha verifica se houve uma vitória na diagonal olhando a diagonal primaria, secundaria e terciaaria
        return True #se tiver sequencia de simbolos iguais, vai ser verificador e exibido o vencedor
    


def jogar_(grade, jogador, linha, coluna): #permite jogada na grade, recebe o simbolo atual e coordena a jogada de acordo com a escola
     if grade[linha-1][coluna-1] == " ": #verifica se algum posição esta sendo ocupada novamente
        grade[linha-1][coluna-1] = jogador
        return True #se sim, retorna a mensagem
     else:
          print("Essa posição já foi preenchida!! jogue novamente.")
          return False #se nao, segue o game


def jogo_da_velha():
    while True:
       
        grade = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

        jogador = "X" #preedifinimos o jogador para facilitar na alternação entre 'O' e 'X'
        while True:
            grade_jogo(grade)
            
            linha = int(input(f"\nJogador ({jogador}) Digite a linha 1, 2, 3: "))
            coluna = int(input(f"Jogador ({jogador}) Digite a coluna 1, 2, 3: "))
            print("\n")

            if linha < 1 or linha > 3 or coluna < 1 or coluna > 3: #invalida jogadas foram do codigo como números maior que 3 ou menor que 1
                print("Jogada inválida. Jogue novamente! \n")
                continue #serve para o codigo não para e voltar do inicio
            
            if jogar_(grade, jogador, linha, coluna): #exibe a grade preencida com a jogada atual
                if vencedor(grade, jogador):#exibe a grade quando houver algum vencedor
                    os.system("cls")
                    grade_jogo(grade)
                    print(f"\nO jogador ({jogador}) Venceu!!!")
                    break
                elif " " not in [jogada for linha in grade for jogada in linha]: #verifica se houve empate, vai ver se tem algum espaço vázio na grade, se não, deu empate 
                    os.system("cls")
                    grade_jogo(grade)
                    print("\nEmpate!!")
                    break #para o codigo totalmente, poderia ser um "return" tmb
                jogador = "O" if jogador == "X" else "X" #altera entre os simbolos

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        
        
        
        os.system("cls")
        
        
        if jogar_novamente.lower() != "s":
            print("Até a proxima. \n") 
            break
        


jogo_da_velha()
