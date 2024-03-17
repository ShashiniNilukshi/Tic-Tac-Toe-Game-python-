from tkinter import *
import random
from functools import partial

def button1_clicked():
  global window
  window=Tk()
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
      if buttons[row][column]['text'] == "" and evaluate(buttons) is False:
          # Human player's move
          buttons[row][column]['text'] = player
          if evaluate(buttons) is False:
              # Check if game is still ongoing
              if player == players[0]:
                  player = players[1]
                  label3.config(text=player + " turn")
                  # AI player's move
                  ai_move()
                  if evaluate(buttons) is True:
                      label3.config(text=player + " wins")
                  elif evaluate(buttons) == "Tie":
                      label3.config(text="Tie")
              else:
                  player = players[0]
                  label3.config(text=player + " turn")
          elif evaluate(buttons) is True:
              label3.config(text=player + " wins")
          elif evaluate(buttons) == "Tie":
              label3.config(text="Tie")

  def ai_move():
      best_val = -float('inf')
      best_move = None
      for i in range(3):
          for j in range(3):
              if buttons[i][j]['text'] == "":
                  buttons[i][j]['text'] = players[1]  # AI player
                  move_val = minimax(buttons, 0, False)
                  buttons[i][j]['text'] = ""  # Undo the move
                  if move_val > best_val:
                      best_val = move_val
                      best_move = (i, j)
      row, col = best_move
      buttons[row][col]['text'] = players[1]  # AI player

  def evaluate(buttons):

          for row in range(3):
              if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                  buttons[row][0].config(bg="green")
                  buttons[row][1].config(bg="green")
                  buttons[row][2].config(bg="green")
                  return 10 if player[row][0] == 'X' else -10

          for column in range(3):
              if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                  buttons[0][column].config(bg="green")
                  buttons[1][column].config(bg="green")
                  buttons[2][column].config(bg="green")
                  return 10 if player[0][column] == 'X' else -10

          if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
              buttons[0][0].config(bg="green")
              buttons[1][1].config(bg="green")
              buttons[2][2].config(bg="green")
              return 10 if player[0][0] == 'X' else -10

          if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
              buttons[0][2].config(bg="green")
              buttons[1][1].config(bg="green")
              buttons[2][0].config(bg="green")
              return 10 if player[0][2] == 'X' else -10

          elif empty_spaces() is False:
              for row in range(3):
                  for column in range(3):
                      buttons[row][column].config(bg="yellow")
              return "Tie"
              return 0
          else:
              return False

  def empty_spaces():
      spaces = 9
      for row in range(3):
          for column in range(3):
              if buttons[row][column]['text'] != '':
                  spaces -= 1
      if spaces == 0:
          return False
      else:
          return True


  def minimax(buttons,depth,is_max):
      score=evaluate(buttons)

      if score==10:
          return score-depth
      if score==-10:
          return score+depth
      if all(buttons[i][j] != ' ' for i in range(3) for j in range(3)):
          return 0

      if is_max:
          best = -float('inf')
          for i in range(3):
              for j in range(3):
                  if buttons[i][j] == ' ':
                      buttons[i][j] = 'X'
                      best = max(best, minimax(buttons, depth + 1, not is_max))
                      buttons[i][j] = ' '
          return best
      else:
          best = float('inf')
          for i in range(3):
              for j in range(3):
                  if buttons[i][j] == ' ':
                      buttons[i][j] = 'O'
                      best = min(best, minimax(buttons, depth + 1, not is_max))
                      buttons[i][j] = ' '
          return best

  def new_game():
      nonlocal player
      player = random.choice(players)
      label3.config(text=player + " turn")
      for row in range(3):
          for column in range(3):
              buttons[row][column].config(text="", bg="#F0f0f0")

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
