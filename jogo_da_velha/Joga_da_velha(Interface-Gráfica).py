import os
import tkinter as tk
from tkinter import messagebox

grade = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def grade_jogo(grade, frame):
    for i in range(len(grade)):
        row = tk.Frame(frame)
        row.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        for j in range(len(grade[i])):
            cell = tk.Label(row, text=grade[i][j], width=6, height=3, relief=tk.RIDGE,
                            font=("Arial", 24))  # Definindo o tamanho da fonte para 24
            cell.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            cell.bind("<Button-1>", lambda event, i=i, j=j: jogar_celula(i, j))
            if j < len(grade[i]) - 10:
                tk.Label(row,width=2, height=3).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        if i < len(grade) - 10:
            separator = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN)
            separator.pack(fill=tk.X, padx=5, pady=5)


def vencedor(grade, jogador):
    for linha in grade:
        if all(jogada == jogador for jogada in linha):
            return True

    for coluna in range(3):
        if all(grade[linha][coluna] == jogador for linha in range(3)):
            return True

    if all(grade[i][i] == jogador for i in range(3)) or all(grade[i][2 - i] == jogador for i in range(3)):
        return True


def jogar_celula(i, j):
    global grade, jogador

    if grade[i][j] == " ":
        grade[i][j] = jogador
        if vencedor(grade, jogador):
            messagebox.showinfo("Fim do Jogo", f"O jogador ({jogador}) Venceu!!!")
            reiniciar_jogo()
        elif " " not in [jogada for linha in grade for jogada in linha]:
            messagebox.showinfo("Fim do Jogo", "Empate!!")
            reiniciar_jogo()
        jogador = "O" if jogador == "X" else "X"
        atualizar_interface()


def reiniciar_jogo():
    global grade, jogador
    grade = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    jogador = "X"
    atualizar_interface()


def atualizar_interface():
    for widget in root.winfo_children():
        widget.destroy()
    grade_jogo(grade, root)


def jogo_da_velha():
    global root, jogador
    root = tk.Tk()
    root.title("Jogo da Velha")
    jogador = "X"
    atualizar_interface()
    root.mainloop()


if __name__ == "__main__":
    jogo_da_velha()

