# puzzle.py: This file contains the starting point of the game.


# Import Modules

import tkinter as tk
from tkinter import ttk


# Application class

class Application(tk.Tk):
    '''Main application class.'''
    def __init__(self, title = 'Tk', geometry = '100x100'):
        super().__init__()
        self.title(title)
        # self.geometry(geometry)

        self.gameboard = GameFrame(self)
        self.gameboard.grid(row = 0, column = 0)


# Game Frame

class GameFrame(ttk.Frame):
    '''Game Board Frame'''
    def __init__(self, parent):
        super().__init__(parent, border = 20)
        self.img = tk.PhotoImage(file = 'img/download1.png')
        self.tiles = {}

        # row 1
        self.tiles['Tile 1'] = Tile(self, self.img, x = 0, y = 0, width = 150, height = 150)
        self.tiles['Tile 1'].grid(row = 0, column = 0)
        self.tiles['Tile 2'] = Tile(self, self.img, x = -150, y = 0, width = 150, height = 150)
        self.tiles['Tile 2'].grid(row = 0, column = 1)
        self.tiles['Tile 3'] = Tile(self, self.img, x = -300, y = 0, width = 150, height = 150)
        self.tiles['Tile 3'].grid(row = 0, column = 2)
        self.tiles['Tile 4'] = Tile(self, self.img, x = -450, y = 0, width = 150, height = 150)
        self.tiles['Tile 4'].grid(row = 0, column = 3)
        # row 2
        self.tiles['Tile 5'] = Tile(self, self.img, x = 0, y = -150, width = 150, height = 150)
        self.tiles['Tile 5'].grid(row = 1, column = 0)
        self.tiles['Tile 6'] = Tile(self, self.img, x = -150, y = -150, width = 150, height = 150)
        self.tiles['Tile 6'].grid(row = 1, column = 1)
        self.tiles['Tile 7'] = Tile(self, self.img, x = -300, y = -150, width = 150, height = 150)
        self.tiles['Tile 7'].grid(row = 1, column = 2)
        self.tiles['Tile 8'] = Tile(self, self.img, x = -450, y = -150, width = 150, height = 150)
        self.tiles['Tile 8'].grid(row = 1, column = 3)
        # row 3
        self.tiles['Tile 9'] = Tile(self, self.img, x = 0, y = -300, width = 150, height = 150)
        self.tiles['Tile 9'].grid(row = 2, column = 0)
        self.tiles['Tile 10'] = Tile(self, self.img, x = -150, y = -300, width = 150, height = 150)
        self.tiles['Tile 10'].grid(row = 2, column = 1)
        self.tiles['Tile 11'] = Tile(self, self.img, x = -300, y = -300, width = 150, height = 150)
        self.tiles['Tile 11'].grid(row = 2, column = 2)
        self.tiles['Tile 12'] = Tile(self, self.img, x = -450, y = -300, width = 150, height = 150)
        self.tiles['Tile 12'].grid(row = 2, column = 3)
        # row 4
        self.tiles['Tile 13'] = Tile(self, self.img, x = 0, y = -450, width = 150, height = 150)
        self.tiles['Tile 13'].grid(row = 3, column = 0)
        self.tiles['Tile 14'] = Tile(self, self.img, x = -150, y = -450, width = 150, height = 150)
        self.tiles['Tile 14'].grid(row = 3, column = 1)
        self.tiles['Tile 15'] = Tile(self, self.img, x = -300, y = -450, width = 150, height = 150)
        self.tiles['Tile 15'].grid(row = 3, column = 2)
        self.tiles['Tile 16'] = Tile(self, self.img, x = -450, y = -450, width = 150, height = 150)
        self.tiles['Tile 16'].grid(row = 3, column = 3)

        self.columnconfigure(0, weight = 1)


# Puzzle Tiles

class Tile(tk.Canvas):
    '''Canvas to hold the puzzle tile'''
    def __init__(self, parent, img, x = 0, y = 0, *args, **kwargs):
        super().__init__(parent, highlightthickness = 1, *args, **kwargs)
        self.create_image(x, y, anchor = tk.NW, image = img)
        self.columnconfigure(0, weight = 1)


# Starting point

if __name__ == '__main__':
    app = Application('Puzzle!', '600x600')
    app.mainloop()
