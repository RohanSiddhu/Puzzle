# puzzle.py: This file contains the starting point of the game.


# Import Modules

import tkinter as tk
from tkinter import ttk


# Global

TileOrderTuple = (
    0, 3, 14, 6,
    7, 9, 1, 10,
    13, 2, 5, 12,
    11, 8, 4, 15
)

TileOrderList = list(TileOrderTuple)


# Application class

class Application(tk.Tk):
    '''Main application class.'''
    def __init__(self, title = 'Tk'):
        super().__init__()
        self.title(title)

        self.gameboard = GameFrame(self)
        self.gameboard.show()
        self.bind('<Key>', self.gameboard.key_press)
        self.gameboard.grid(row = 0, column = 0)

        self.button = ttk.Button(self, text = "Sort", command = self.on_sort)
        self.button.grid(row = 0, column = 1)
    
    def on_sort(self):
        TileOrderList.sort()
        self.gameboard.show()


# Game Frame

class GameFrame(ttk.Frame):
    '''Game Board Frame'''
    def __init__(self, parent):
        super().__init__(parent, border = 20)
        self.parent = parent
        self.img = tk.PhotoImage(file = 'img/download1.png')
        self.emptyTile = 15
        self.tiles = []

        # row 1
        self.tiles.append(Tile(self, self.img, x = 0, y = 0, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -150, y = 0, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -300, y = 0, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -450, y = 0, width = 150, height = 150))
        # row 2
        self.tiles.append(Tile(self, self.img, x = 0, y = -150, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -150, y = -150, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -300, y = -150, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -450, y = -150, width = 150, height = 150))
        # row 3
        self.tiles.append(Tile(self, self.img, x = 0, y = -300, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -150, y = -300, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -300, y = -300, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -450, y = -300, width = 150, height = 150))
        # row 4
        self.tiles.append(Tile(self, self.img, x = 0, y = -450, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -150, y = -450, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -300, y = -450, width = 150, height = 150))
        self.tiles.append(Tile(self, self.img, x = -450, y = -450, width = 150, height = 150))

        self.columnconfigure(0, weight = 1)
    
    def show(self):
        for i in range(16):
            self.tiles[TileOrderList[i]].grid(row = i // 4, column = i % 4)
        self.tiles[15].grid_forget()
    
    def clear(self):
        for tile in self.tiles:
            tile.grid_forget()
    
    def is_sorted(self):
        for i in range(15):
            if (TileOrderList[i] > TileOrderList[i + 1]):
                return False
        else:
            return True
    
    def key_press(self, event):
        key = event.keysym
        print("<key>", key, sep = ' ')
        if key == 'Right':
            if self.emptyTile % 4:
                TileOrderList[self.emptyTile], TileOrderList[self.emptyTile - 1] = TileOrderList[self.emptyTile - 1], TileOrderList[self.emptyTile]
                self.emptyTile -= 1
        elif key == 'Left':
            if self.emptyTile % 4 != 3:
                TileOrderList[self.emptyTile], TileOrderList[self.emptyTile + 1] = TileOrderList[self.emptyTile + 1], TileOrderList[self.emptyTile]
                self.emptyTile += 1
        elif key == 'Down':
            if self.emptyTile // 4:
                TileOrderList[self.emptyTile], TileOrderList[self.emptyTile - 4] = TileOrderList[self.emptyTile - 4], TileOrderList[self.emptyTile]
                self.emptyTile -= 4
        elif key == 'Up':
            if self.emptyTile // 4 != 3:
                TileOrderList[self.emptyTile], TileOrderList[self.emptyTile + 4] = TileOrderList[self.emptyTile + 4], TileOrderList[self.emptyTile]
                self.emptyTile += 4
        self.show()
        
        if self.is_sorted():
            self.parent.destroy()


# Puzzle Tiles

class Tile(tk.Canvas):
    '''Canvas to hold the puzzle tile'''
    def __init__(self, parent, img, x = 0, y = 0, *args, **kwargs):
        super().__init__(parent, highlightthickness = 0, *args, **kwargs)
        self.create_image(x, y, anchor = tk.NW, image = img)
        self.columnconfigure(0, weight = 1)


# Starting point

if __name__ == '__main__':
    app = Application('Puzzle!')
    app.mainloop()
