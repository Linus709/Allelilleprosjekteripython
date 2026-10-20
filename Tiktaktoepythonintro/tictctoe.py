import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple

"""welcome to TicTacToe game made by Linus"""

#step8 player and move class which makes a x and o and where it cordinates when i click with move
class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

#step10 making playeres x red and o blue
BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="x", color = "red"),
    Player(label="o", color = "blue"),
)

#step9 this is like the brain of the tictactoegame and is needed to make the game work
class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    #step11 we use class tictactoegame def like self winner combos and more to figure out the winner combinations and range of winning combinations
    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]    
        self._winning_combos = self._get_winning_combos()

#step12 we calculate the winning combos
    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

#step13 this code is calculating the player moves
    def is_valid_move(self,move):
            row, col = move.row, move.col
            move_was_not_played = self._current_moves[row][col].label == ""
            no_winner = not self._has_winner
            return no_winner and move_was_not_played
        

#step1 lager tittel til tictactoe displayet og intialiserer bruken av tkinter
class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe- Game")
        self._cells = {}
        #step6 these to lines adds a display and grid of cells
        self._create_board_display()
        self._create_board_grid()

#step2 selvekoden som lager display og åpner greien i termialen
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

#step3 this just makes so code is visible and makes a frame to hold the grid with cells in main window
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        #step4 makes the button and row a 9 by 9 aquare to look like a tictactoe board
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                #step5 makes it possible to clik and use the button class and places the button and fills the grid
                )
                self._cells[button] = (row, col)
                button.grid(
                        row=row,
                        column=col,
                        padx=5,
                        pady=5,
                        sticky="nsew"
                    )
#step7 this under here is needed to make the code run from the terminal
def main():
    """Create the games board and run its main loop"""
    board = TicTacToeGame() 
    board = TicTacToeBoard(game)
    board.mainloop()

if __name__ == "__main__":
    main()








