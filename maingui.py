import tkinter as tk
from tkinter import ttk
from tkinter.constants import RIDGE

class MainGUI:
    

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vektorplotter")

    def makeMainframe(self):
        self.mainframe = tk.Frame(self.root, padx = 12, pady = 12)
        self.mainframe.grid(column = 0, row = 0, sticky = tk.N + tk.E + tk.S + tk.W)
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)


    def makeVlistFrame(self):
        self.vlistFrame = tk.Frame(self.mainframe, padx = 12, pady = 12, borderwidth = 1, bg = "#EEEEEE", relief = RIDGE)
        self.vlistFrame.grid(column = 0, row = 0, sticky = tk.N + tk.E + tk.S)


    def makeCanvasFrame(self):
        self.canvasFrame = tk.Frame(self.mainframe, padx = 12, pady = 12, borderwidth=1, bg = "#DDDDDD", relief = RIDGE)
        self.canvasFrame.grid(column = 1, row = 0, sticky = tk.N + tk.W + tk.S)


    def makeLabel(self):
        self.myLabel = tk.Label(self.vlistFrame, text = "Hello World!", padx = 5, pady = 3).grid(row=0, column=0)
        self.myLabelCanvas = tk.Label(self.canvasFrame, text = "Hello World 2!", padx = 5, pady = 3).grid(row=0, column=0)


    def mainloop(self):
        self.makeMainframe()
        self.makeVlistFrame()
        self.makeCanvasFrame()
        self.makeLabel()
        self.root.mainloop()

Example = MainGUI()

Example.mainloop()