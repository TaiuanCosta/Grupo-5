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


def revela_palavra(grade, grade_jogo, palavra): #representa a grade das palavras e as das escondidas e a tentativa de acertos 
    palavra_encontrada = False #confirma se a palavra foi encontrada
    for i in range(len(grade)): #percorre a linha
        for j in range(len(grade[0])): #percorre as colunas
            if grade[i][j] == palavra[0]: #verifica se a primeira letra da palavra digitada é igual a da grade
                if j + len(palavra) <= len(grade[0]) and \
                   all(grade[i][j+k] == palavra[k] for k in range(len(palavra))): #esta linha verifica se é possível que a palavra esteja horizontalmente a partir da posição
                    for k in range(len(palavra)):
                        grade_jogo[i][j+k] = palavra[k] #compara o tamanho da palavra digitada na vertical utilizando o indice 'j'
                    palavra_encontrada = True
                if i + len(palavra) <= len(grade) and \
                   all(grade[i+k][j] == palavra[k] for k in range(len(palavra))): #esta linha verifica se é possível que a palavra esteja verticalmente a partir da posição 
                    for k in range(len(palavra)):
                        grade_jogo[i+k][j] = palavra[k] #compara o tamanho da palavra digitada na vertical utilizando o indice 'i'
                    palavra_encontrada = True
    return palavra_encontrada #faz a substituição da grade se a palavra atender aos requisitos


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

    while grade != grade_jogo: #faz com que o laço rode enquando as grades estiverem diferentes

        cria_grade(grade_jogo)
        print("\033[91m\nREGRA!: DIGITE NO MINIMO 5 LETRAS PARA VÁLIDAR SUA JOGADA\n\033[0m")
        print("Dica: o tema desse jogo são frutas \n")
        print("Dica2: Os () do inicio indicam a posição inicial da primeira letra de cada palavra! \n")
        print("(1 - D).Pequena e vermelha e azeda.\033[33m(7 - letras)\033[0m",)
        print("(2 - A).Fruta tropical, amarela por dentro e bastante comida verde com sal.\033[33m(5 -  letras)\033[0m",)
        print("(7 - D).Fruta redonda, com casca verde e polpa rosada.\033[33m(6 - letras)\033[0m",)
        print("(4 - D).Amarela e curvada, fonte de potássio.\033[33m(6 - letras)\033[0m",)
        print("(1 - I).Fruta cítrica, fonte de vitamina C.\033[33m(7 - letras)\033[0m",)
        print("(2 - A).Grande e redondo, com casca amarela e polpa branca parecida com melancia.\033[33m(5 - letras)\033[0m",)
        print("(1 - E).Fonte de antioxidantes, usado em chocolates.\033[33m(5 - letras)\033[0m")
        palavra = input("\nDigite uma palavra: ").lower()
        if len(palavra) == 1 or len(palavra) == 2 or len(palavra) == 3 or len(palavra) == 4: #limita a quantidade de letras digitadas
            os.system("cls")
            print("Por favor, digite uma palavra. Tente novamente.\n")
            continue
        if revela_palavra(grade, grade_jogo, palavra): #mostra a grade com as palavras acertadas dentro dela
            os.system("cls")
            print("\033[92mPalavra encontrada!\033[0m\n")
        else:
            os.system("cls")
            print("\033[93mPalavra não encontrada! Jogue novamente.\033[0m\n")

    cria_grade(grade_jogo) #puxa a grade jogo completra no final
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
        print("(1 - A).Animal forte e rápido.\033[33m(6 - letras)\033[0m",)
        print("(4 - B).Ave que produz ovos.\033[33m(7 - letras)\033[0m",)
        print("(3 - H).Animal de estimação independente.\033[33m(4 - letras)\033[0m",)
        print("(4 - D).Carnívoro selvagem em matilha.\033[33m(4 - letras)\033[0m",)
        print("(1 - C).Produz leite e carne.\033[33m(4 - letras)\033[0m",)
        palavra = input("\nDigite uma palavra: ").lower()
        if len(palavra) == 1 or len(palavra) == 2 or len(palavra) == 3:
            os.system("cls")
            print("Por favor, digite uma palavra. Tente novamente.\n")
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
        print("(1 - E).Objeto redondo principal do jogo.\033[33m(4 - letras)\033[0m")
        print("(1 - H).Instrumento usado pelo árbitro para sinalizar faltas.\033[33m(5 - letras)\033[0m")
        print("(1 - J).Faz parte da estrutura onde se marca gol.\033[33m(5 - letras)\033[0m")
        print("(3 - C).Calçado específico para o esporte.\033[33m(8 - letras)\033[0m")
        print("(3 - C).Superfície onde o jogo é disputado.\033[33m(5 - letras)\033[0m")
        print("(5 - A).Vestimenta dos jogadores, identificando suas equipes(parte de cima)\033[33m(6 - letras)\033[0m")

        palavra = input("\nDigite uma palavra: ").lower()
        if len(palavra) == 1 or len(palavra) == 2 or len(palavra) == 3:
            os.system("cls")
            print("Por favor, digite uma palavra. Tente novamente.\n")
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
