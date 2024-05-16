import tkinter as tk
from bot import *

class Connect4UI:
    def __init__(self, master):
        self.master = master
        self.game = Connect4Game()  # Initialize game
        self.bot = Connect4Bot(self.game)
        self.buttons = []
        self.create_board()

    def create_board(self):
        for row in range(self.game.rows):
            button_row = []
            for col in range(self.game.cols):
                button = tk.Button(self.master, text="", width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.game.is_valid_move(col):
            
            self.game.make_move(col,0)
            self.update_board()
            if self.game.winning_move(1):
                print("WIN POSSIBLE")
            if not self.game.isdone and not self.game.is_board_full():
                # Bot's turn (replace with your bot logic)
                bot_col = self.bot_make_move()
                print(bot_col)
                self.game.make_move(bot_col,1)
                self.update_board()
                
        else:
            print("Invalid move!")

    def update_board(self):
        for row in range(self.game.rows):
            for col in range(self.game.cols):
                value = self.game.board[row][col]
                self.buttons[row][col].config(text=value)

    def bot_make_move(self):
        # Implement your bot logic here
        # For now, just make a random valid move
        return self.bot.get_best_move()
