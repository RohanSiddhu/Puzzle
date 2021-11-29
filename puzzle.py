# puzzle.py: This file contains the starting point of the game.


#################
# Import Modules
#################

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


#########
# Global
#########

TileOrderTuple = (
    0, 3, 14, 6,
    7, 9, 1, 10,
    13, 2, 5, 12,
    11, 8, 4, 15
)


####################
# Application class
####################

class Application(tk.Tk):
    '''Main application class.'''
    def __init__(self, title = 'Tk'):
        '''Application constructor'''
        super().__init__()
        self.title(title)

        # GameFrame
        self.gameframe = GameFrame(self, 'img/download1.png')
        self.gameframe.grid(row = 0, column = 0)

        self.bind('<Key>', self.key_callback)       # Bind the key_callback to the root application.

    def key_callback(self, event):
        '''Application key callback'''
        self.gameframe.key_callback(event)

        # Check if the puzzle is complete
        if self.gameframe.puzzleboard.is_sorted():
            # If puzzle is complete then ask for restart.
            answer = messagebox.askretrycancel('Game Over!',
                'Your completed in ' + str(self.gameframe.puzzleboard.moves) + " moves.\n Do you want to retry?")
            if answer == True:
                self.gameframe.reset()
            else:
                self.destroy()

###################
# Game Frame Class
###################

class GameFrame(ttk.Frame):
    '''A ttk Frame for Play Screen'''
    def __init__(self, parent, imgPath = ''):
        '''GameFrame constructor'''
        super().__init__(parent, border = 10)

        # Puzzle Board
        self.puzzleboard  = PuzzleBoard(self, imgPath, order = TileOrderTuple)
        self.puzzleboard.show()
        self.puzzleboard.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Info Frame
        self.infoFrame = ttk.Frame(self)

        # Info Frame -> Preview Frame
        self.previewFrame = ttk.LabelFrame(self.infoFrame, text = 'Preview')

        self.previewImg = tk.PhotoImage(file = 'img/download1.png')
        self.previewImg = self.previewImg.subsample(4, 4)
        self.previewTile = Tile(self.previewFrame, img = self.previewImg, x = 0, y = 0, width = 150, height = 150)
        self.previewTile.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = (tk.N + tk.S + tk.W + tk.E))

        self.previewFrame.grid(row = 0, column = 0, columnspan = 2, sticky = (tk.N))

        # Info Frame -> Moves Label
        self.movesLabel = ttk.Label(self.infoFrame, text = "Moves:")
        self.movesLabel.grid(row = 1, column = 0, pady = 20)

        # Info Frame -> Moves Canvas (display number of moves)
        self.movesCanvas = tk.Canvas(self.infoFrame, width = 40, height = 20)
        self.movesCanvas_moves = self.movesCanvas.create_text(5, 5, anchor = tk.NW)
        self.movesCanvas.itemconfig(self.movesCanvas_moves, text = str(self.puzzleboard.moves))
        self.movesCanvas.grid(row = 1, column = 1, pady = 20, sticky = (tk.W + tk.N + tk.S))

        self.infoFrame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = (tk.N))

        # Reset Button
        self.resetButton = ttk.Button(self, text = "Reset", command = lambda: self.reset())
        self.resetButton.grid(row = 1, column = 0, columnspan = 2, pady = 5)

        self.columnconfigure(0, weight = 1)
    
    def reset(self):
        '''Reset the game frame to its initial state'''
        self.puzzleboard.reset()
        self.movesCanvas.itemconfig(self.movesCanvas_moves, text = str(self.puzzleboard.moves))
    
    def key_callback(self, event):
        '''GameFrame key callback'''
        self.puzzleboard.key_callback(event)
        self.movesCanvas.itemconfig(self.movesCanvas_moves, text = str(self.puzzleboard.moves))


###############
# Puzzle Board
###############

class PuzzleBoard(ttk.Frame):
    '''A ttk Frame to hold the puzzle tiles together to make a puzzle bord'''
    def __init__(self, parent, imagePath = '', subSample = None, gridSize = 4, boardSize = 600, order = None):
        '''PuzzleBoard constructor'''
        super().__init__(parent)

        self.tileSize = boardSize / gridSize
        self.moves = 0
        self.order = order or ()
        self.orderList = list(self.order)
        self.gridSize = gridSize
        self.lastTile = (gridSize ** 2) - 1
        self.emptyTile = self.lastTile

        self.img = tk.PhotoImage(file = imagePath)
        if subSample: self.img = self.img.subsample(subSample, subSample)
        self.tiles = []

        # creating tiles
        for i in range(gridSize):
            for j in range(gridSize):
                self.tiles.append(Tile(self, self.img, x = - (j * self.tileSize), y = - (i * self.tileSize),
                    width = self.tileSize, height = self.tileSize))        

    def show(self):
        '''Display the puzzle board'''
        for i in range(self.gridSize ** 2):
            self.tiles[self.orderList[i]].grid(row = i // self.gridSize, column = i % self.gridSize)
        self.tiles[self.lastTile].grid_forget()
    
    def clear(self):
        '''Clear the board'''
        for tile in self.tiles:
            tile.grid_forget()
    
    def reset(self):
        '''Reset the puzzle board to its initial state'''
        self.orderList = list(self.order)
        self.moves = 0
        self.emptyTile = self.lastTile
        self.show()
    
    def is_sorted(self):
        '''Return True if board is sorted and False if not'''
        for i in range((self.gridSize ** 2) - 1):
            if (self.orderList[i] > self.orderList[i + 1]):
                return False
        else:
            return True
    
    def key_callback(self, event):
        '''PuzzleBoard key callback'''
        key = event.keysym
        if key == 'Right':
            if self.emptyTile % self.gridSize:
                self.orderList[self.emptyTile], self.orderList[self.emptyTile - 1] = self.orderList[self.emptyTile - 1], self.orderList[self.emptyTile]
                self.emptyTile -= 1
                self.moves += 1
        elif key == 'Left':
            if self.emptyTile % self.gridSize != self.gridSize - 1:
                self.orderList[self.emptyTile], self.orderList[self.emptyTile + 1] = self.orderList[self.emptyTile + 1], self.orderList[self.emptyTile]
                self.emptyTile += 1
                self.moves += 1
        elif key == 'Down':
            if self.emptyTile // self.gridSize:
                self.orderList[self.emptyTile], self.orderList[self.emptyTile - self.gridSize] = self.orderList[self.emptyTile - self.gridSize], self.orderList[self.emptyTile]
                self.emptyTile -= self.gridSize
                self.moves += 1
        elif key == 'Up':
            if self.emptyTile // self.gridSize != self.gridSize - 1:
                self.orderList[self.emptyTile], self.orderList[self.emptyTile + self.gridSize] = self.orderList[self.emptyTile + self.gridSize], self.orderList[self.emptyTile]
                self.emptyTile += self.gridSize
                self.moves += 1
        self.show()


###############
# Puzzle Tiles
###############

class Tile(tk.Canvas):
    '''A tk Canvas to hold the puzzle tile'''
    def __init__(self, parent, img, x = 0, y = 0, thickness = 0, img_args = None, *args, **kwargs):
        '''Tile constructor'''
        super().__init__(parent, highlightthickness = thickness, *args, **kwargs)
        img_args = img_args or {}
        self.create_image(x, y, anchor = tk.NW, image = img, **img_args)
        self.columnconfigure(0, weight = 1)


#################
# Starting point
#################

if __name__ == '__main__':
    app = Application('Puzzle!')
    app.mainloop()
