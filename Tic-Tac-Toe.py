from tkinter import *
import random
from functools import partial
import tkinter as tk
from tkinter import messagebox
import math

def button1_clicked():
    PLAYER = -1
    AI = 1
    # Empty cell marker
    EMPTY = 0

    class TicTacToe(tk.Tk):
        def __init__(self):
            super().__init__()

            self.title("Tic Tac Toe")
            self.geometry("300x300")

            self.board = [[EMPTY, EMPTY, EMPTY],
                          [EMPTY, EMPTY, EMPTY],
                          [EMPTY, EMPTY, EMPTY]]

            self.buttons = [[None] * 3 for _ in range(3)]

            self.current_player = PLAYER
            self.game_over = False  # Flag to indicate whether the game is over

            self.create_board()

        def create_board(self):
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j] = tk.Button(self, text="", font=('Arial', 20), width=5, height=2,
                                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                    self.buttons[i][j].grid(row=i, column=j)

        def on_button_click(self, row, col):
            if not self.game_over and self.board[row][col] == EMPTY:
                self.board[row][col] = self.current_player
                self.update_button_text(row, col)
                winner = self.check_winner()
                if winner == PLAYER:
                    self.end_game("Player wins!")
                    self.game_over = True
                elif winner == AI:
                    self.end_game("AI wins!")
                    self.game_over = True
                elif self.check_draw():
                    self.end_game("It's a draw!")
                    self.game_over = True
                else:
                    self.current_player *= -1
                    if self.current_player == AI:
                        self.ai_move()

        def update_button_text(self, row, col):
            player = self.board[row][col]
            text = "X" if player == PLAYER else "O"
            self.buttons[row][col].config(text=text, state="disabled")

        def highlight_winning_row(self):
            winning_row = self.find_winning_row()
            if winning_row is not None:
                for col in range(3):
                    self.buttons[winning_row][col].config(bg='green')

        def find_winning_row(self):
            for row in range(3):
                if all(self.board[row][col] == self.board[row][0] != EMPTY for col in range(3)):
                    return row
            return None

        def ai_move(self):
            best_score = -math.inf
            best_move = None

            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == EMPTY:
                        self.board[row][col] = AI
                        score = self.minimax(self.board, 0, False)
                        self.board[row][col] = EMPTY
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)

            if best_move:
                row, col = best_move
                self.board[row][col] = AI
                self.update_button_text(row, col)
                winner = self.check_winner()
                if winner == AI:
                    self.end_game("AI wins!")
                    self.game_over = True
                elif self.check_draw():
                    self.end_game("It's a draw!")
                    self.game_over = True
                else:
                    self.current_player *= -1

        def minimax(self, board, depth, is_maximizing):
            result = self.evaluate(board)

            if result is not None:
                return result

            if is_maximizing:
                best_score = -math.inf
                for row in range(3):
                    for col in range(3):
                        if board[row][col] == EMPTY:
                            board[row][col] = AI
                            score = self.minimax(board, depth + 1, False)
                            board[row][col] = EMPTY
                            best_score = max(score, best_score)
                return best_score
            else:
                best_score = math.inf
                for row in range(3):
                    for col in range(3):
                        if board[row][col] == EMPTY:
                            board[row][col] = PLAYER
                            score = self.minimax(board, depth + 1, True)
                            board[row][col] = EMPTY
                            best_score = min(score, best_score)
                return best_score

        def evaluate(self, board):
            # Check rows
            for row in board:
                if all(cell == PLAYER for cell in row):
                    return PLAYER
                elif all(cell == AI for cell in row):
                    return AI

            # Check columns
            for col in range(3):
                if all(board[row][col] == PLAYER for row in range(3)):
                    return PLAYER
                elif all(board[row][col] == AI for row in range(3)):
                    return AI

            # Check diagonals
            if all(board[i][i] == PLAYER for i in range(3)) or all(board[i][2 - i] == PLAYER for i in range(3)):
                return PLAYER
            elif all(board[i][i] == AI for i in range(3)) or all(board[i][2 - i] == AI for i in range(3)):
                return AI

            # Check for draw
            if all(cell != EMPTY for row in board for cell in row):
                return 0  # Draw

            # Game still ongoing
            return None

        def check_winner(self):
            return self.evaluate(self.board)

        def check_draw(self):
            return self.evaluate(self.board) == 0 and not any(EMPTY in row for row in self.board)

        def end_game(self, message):
            messagebox.showinfo("Game Over", message)
            if self.game_over:
                self.highlight_winning_row()

    if __name__ == "__main__":
        game = TicTacToe()
        game.mainloop()


def button2_clicked():
    global window
    window = Tk()
    window.title("Tic-Tac-Toe")
    players = ["X", "O"]
    player = random.choice(players)
    buttons = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
    label3 = Label(text=player + " turn", font=('consolas', 40))
    label3.pack(side="top")

    def next_turn(row, column):
        nonlocal player
        if buttons[row][column]['text'] == "" and check_winner() is False:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                if player == players[0]:
                    player = players[1]
                    label3.config(text=player + " turn")
                else:
                    player = players[0]
                    label3.config(text=player + " turn")
            elif check_winner() is True:
                label3.config(text=player + " wins")
            elif check_winner() == "Tie":
                label3.config(text="Tie")

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"
        else:
            return False

    def empty_spaces():
        spaces=9
        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text']!='':
                    spaces -=1
        if spaces==0:
            return  False
        else:
            return True

    def new_game():
        nonlocal player
        player = random.choice(players)
        label3.config(text=player + " turn")
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="",bg="#F0f0f0")

    reset_button = Button(window, text="Restart", font=('consolas', 20), command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('consolas', 20), width=5, height=2)
            buttons[row][column].config(command=partial(next_turn, row, column))
            buttons[row][column].grid(row=row, column=column)

    window.mainloop()

window2 = Tk()
window2.title("Choose The Mode")
label1 = Label(text="Choose the Game mode:", font=('consolas', 40))
label1.pack(side="top")
button1 = Button(text="1 Player", font=('consolas', 30), width=10, command=button1_clicked)
button1.pack(side="left")
button2 = Button(text="2 players", font=('consolas', 30), width=10, command=button2_clicked)
button2.pack(side="right")
window2.mainloop()
