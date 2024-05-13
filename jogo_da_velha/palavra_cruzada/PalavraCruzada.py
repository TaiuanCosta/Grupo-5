import os

def cria_grade(grade_jogo):
    linhas = len(grade_jogo)
    colunas = len(grade_jogo[0])

    print("   ", end="")
    for col in range(colunas):
        print(f" {chr(col + 65)} ", end=" ")
    print()

    print("  ╔" + "═══╦" * (colunas - 1) + "═══╗")
    for i in range(linhas):
        print(f"{i + 1:2}║", end="")
        for j in range(colunas):
            if grade_jogo[i][j] == '*':
                print(" * ", end="")
            else:
                print(f" \033[94m{grade_jogo[i][j]}\033[0m ", end="")
            if j != colunas - 1:
                print("║", end="")
        print("║")
        if i != linhas - 1:  
            print("  ╠" + "═══╬" * (colunas - 1) + "═══╣")
    print("  ╚" + "═══╩" * (colunas - 1) + "═══╝")


def revela_palavra(grade, grade_jogo, palavra):
    palavra_encontrada = False
    for i in range(len(grade)):
        for j in range(len(grade[0])):
            if grade[i][j] == palavra[0]:
                if j + len(palavra) <= len(grade[0]) and \
                   all(grade[i][j+k] == palavra[k] for k in range(len(palavra))):
                    for k in range(len(palavra)):
                        grade_jogo[i][j+k] = palavra[k]
                    palavra_encontrada = True
                if i + len(palavra) <= len(grade) and \
                   all(grade[i+k][j] == palavra[k] for k in range(len(palavra))):
                    for k in range(len(palavra)):
                        grade_jogo[i+k][j] = palavra[k]
                    palavra_encontrada = True
    return palavra_encontrada


def jogo_1():
    grade = [
        ['*','*','*','a','c','e','r','o','l','a'],
        ['m','a','n','g','a','*','*','*','a','*'],
        ['e','*','*','*','c','*','*','*','r','*'],
        ['l','*','*','b','a','n','a','n','a','*'],
        ['a','*','*','*','u','*','*','*','n','*'],
        ['o','*','*','*','*','*','*','*','j','*'],
        ['*','*','*','g','o','i','a','b','a','*']
    ]

    grade_jogo = [
        ['*','*','*',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ','*','*','*',' ','*'],
        [' ','*','*','*',' ','*','*','*',' ','*'],
        [' ','*','*',' ',' ',' ',' ',' ',' ','*'],
        [' ','*','*','*',' ','*','*','*',' ','*'],
        [' ','*','*','*','*','*','*','*',' ','*'],
        ['*','*','*',' ',' ',' ',' ',' ',' ','*']
    ]

    while grade != grade_jogo:

        cria_grade(grade_jogo)
        print("\033[91m\nREGRA!: DIGITE NO MINIMO 5 LETRAS PARA VÁLIDAR SUA JOGADA\n\033[0m")
        print("Dica: o tema desse jogo são frutas \n")
        print("Dica2: Os () do inicio indicam a posição inicial da primeira letra de cada palavra! \n")
        print("(1 - D).Pequena e vermelha e azeda.",)
        print("(2 - A).Fruta tropical, amarela por dentro e bastante comida verde com sal.",)
        print("(7 - D).Fruta redonda, com casca verde e polpa rosada.",)
        print("(4 - D).Amarela e curvada, fonte de potássio.",)
        print("(1 - I).Fruta cítrica, fonte de vitamina C.",)
        print("(2 - A).Grande e redondo, com casca amarela e polpa branca parecida com melancia",)
        print("(1 - E).Fonte de antioxidantes, usado em chocolates.")
        palavra = input("\nDigite uma palavra: ").lower()
        if len(palavra) == 1 or len(palavra) == 2 or len(palavra) == 3 or len(palavra) == 4:
            os.system("cls")
            print("Por favor, digite uma palavra, não uma única letra. Tente novamente.\n")
            continue
        if revela_palavra(grade, grade_jogo, palavra):
            os.system("cls")
            print("\033[92mPalavra encontrada!\033[0m\n")
        else:
            os.system("cls")
            print("\033[93mPalavra não encontrada! Jogue novamente.\033[0m\n")

    cria_grade(grade_jogo)
    print("\nVocê ganhou.\n")



def jogo_2():
    grade = [
        ['c', 'a', 'v', 'a', 'l', 'o', '*', '*', '*', '*'],
        ['*', '*', 'a', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', 'c', '*', '*', '*', '*', 'g', '*', '*'],
        ['*', 'g', 'a', 'l', 'i', 'n', 'h', 'a', '*', '*'],
        ['*', '*', '*', 'o', '*', '*', '*', 't', '*', '*'],
        ['*', '*', '*', 'b', '*', '*', '*', 'o', '*', '*'],
        ['*', '*', '*', 'o', '*', '*', '*', '*', '*', '*']
    ]


    grade_jogo = [
        [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
        ['*', '*', ' ', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', ' ', '*', '*', '*', '*', ' ', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*'],
        ['*', '*', '*', ' ', '*', '*', '*', ' ', '*', '*'],
        ['*', '*', '*', ' ', '*', '*', '*', ' ', '*', '*'],
        ['*', '*', '*', ' ', '*', '*', '*', '*', '*', '*']
    ]


    while grade != grade_jogo:

        cria_grade(grade_jogo)
        print("\033[91m\nREGRA!: DIGITE NO MINIMO 4 LETRAS PARA VÁLIDAR SUA JOGADA\n\033[0m")
        print("Dica: o tema desse jogo são animais. \n")
        print("Dica2: Os () do inicio indicam a posição inicial da primeira letra de cada palavra! \n")
        print("(1 - A).Animal forte e rápido.",)
        print("(4 - B).Ave que produz ovos.",)
        print("(3 - H).Animal de estimação independente.",)
        print("(4 - D).Carnívoro selvagem em matilha.",)
        print("(1 - C).Produz leite e carne.",)
        palavra = input("\nDigite uma palavra: ").lower()
        if len(palavra) == 1 or len(palavra) == 2 or len(palavra) == 3:
            os.system("cls")
            print("Por favor, digite uma palavra, não uma única letra. Tente novamente.\n")
            continue
        if revela_palavra(grade, grade_jogo, palavra):
            os.system("cls")
            print("\033[92mPalavra encontrada!\033[0m\n")
        else:
            os.system("cls")
            print("\033[93mPalavra não encontrada! Jogue novamente.\033[0m\n")

    cria_grade(grade_jogo)
    print("\nVocê ganhou.\n")

def jogo_3():
    grade = [
        ['*', '*', '*', '*', 'b', 'o', 'l', 'a', '*', 't'],
        ['*', '*', '*', '*', '*', '*', '*', 'p', '*', 'r'],
        ['*', '*', 'c', 'h', 'u', 't', 'e', 'i', 'r', 'a'],
        ['*', '*', 'a', '*', '*', '*', '*', 't', '*', 'v'],
        ['c', 'a', 'm', 'i', 's', 'a', '*', 'o', '*', 'e'],
        ['*', '*', 'p', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', 'o', '*', '*', '*', '*', '*', '*', '*']
        ]


    grade_jogo = [
        ['*', '*', '*', '*', ' ', ' ', ' ', ' ', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', ' ', '*', ' '],
        ['*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['*', '*', ' ', '*', '*', '*', '*', ' ', '*', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*', ' '],
        ['*', '*', ' ', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', ' ', '*', '*', '*', '*', '*', '*', '*']
    ]

    while grade != grade_jogo:

        cria_grade(grade_jogo)
        print("\033[91m\nREGRA!: DIGITE NO MINIMO 4 LETRAS PARA VÁLIDAR SUA JOGADA\n\033[0m")
        print("Dica: o tema desse jogo é futebol. \n")
        print("Dica2: Os () do inicio indicam a posição inicial da primeira letra de cada palavra! \n  ")
        print("(1 - E).Objeto redondo principal do jogo.")
        print("(1 - H).Instrumento usado pelo árbitro para sinalizar faltas.")
        print("(1 - J).Faz parte da estrutura onde se marca gol.")
        print("(3 - C).Calçado específico para o esporte(futebol).")
        print("(3 - C).Superfície onde o jogo é disputado.")
        print("(5 - A).Vestimenta dos jogadores, identificando suas equipes(parte de cima).")

        palavra = input("\nDigite uma palavra: ").lower()
        if len(palavra) == 1 or len(palavra) == 2 or len(palavra) == 3:
            os.system("cls")
            print("Por favor, digite uma palavra, não uma única letra. Tente novamente.\n")
            continue
        if revela_palavra(grade, grade_jogo, palavra):
            os.system("cls")
            print("\033[92mPalavra encontrada!\033[0m\n")
        else:
            os.system("cls")
            print("\033[93mPalavra não encontrada! Jogue novamente.\033[0m\n")

    cria_grade(grade_jogo)
    print("\nVocê ganhou.\n")
    



def escolher_cenario():
    while True:
        print("Escolha o cenário de jogo: ")
        print("(1) - Cenário 1")
        print("(2) - Cenário 2")
        print("(3) - Cenário 3")
        escolha = input("(x) - Para sair: ")
        os.system("cls")
        if escolha.lower() == 'x':
            print("Obrigado por jogar, até a próxima!")
            return #Pode ser substituido por "Break"
        elif escolha == '1':
            jogo_1()
        elif escolha == '2':
            jogo_2()
        elif escolha == '3':
            jogo_3()
        else:
            print("\nEscolha inválida. Por favor, escolha um número de 1 a 3 ou 'x' para sair.\n")


escolher_cenario()
