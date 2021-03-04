import tkinter as tk
from tkinter import Canvas, ttk
from tkinter.constants import RIDGE
from listclass import ObjectLists
from vector3Dclass import Vector3D
from pointclass import Point
from lineclass import Line
from planeclass import Plane
from nameAssignclass import NameAssign
from colorAssignclass import ColorAssign

x = Vector3D(3, 4, 5)
y = Plane.normalForm(Vector3D(1, 1, 1), Vector3D(2, 2, 2))

class MainGUI(tk.Frame):
    
    size = "1200x800"

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vektorplotter")
        self.root.geometry(self.size)
        self.root.resizable(0, 0)

    def makeMainframe(self):
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid(column = 0, row = 0, sticky = tk.N + tk.E + tk.S + tk.W)
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)


    def makeListFrame(self):
        self.listFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.listFrame.grid(column = 0, row = 1, sticky = tk.N + tk.E + tk.S)
        for element, index in zip(ObjectLists.getObjDict(), range(ObjectLists.getObjDictLen())):
            self.objButton = tk.Button(self.listFrame, text = str(element) + str(ObjectLists.getObjDict()[element]), width = 40, command = self.funktion) # funktion placeholder for future function
            self.objButton.grid(column = 0, row = index)

        self.addButton = tk.Button(self.listFrame, text = "Add new Object +", width = 40, command = self.funktion) # funktion placeholder for future function
        self.addButton.grid(column = 0, row = ObjectLists.getObjDictLen())

    def funktion(self):
        pass


    def makeCanvasFrame(self):
        self.canvasFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.canvasFrame.grid(column = 1, row = 1, sticky = tk.N + tk.W + tk.S)
        self.canvas = Canvas(self.canvasFrame, width = 800)
        self.canvas.grid(column = 0, row = 0)


    def makeMenuFrame(self):
        self.menuFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.menuFrame.grid(column = 0, row = 0, sticky = tk.N + tk.W + tk.E)


    def makeLabel(self):
        self.coord = 10, 10, 300, 300
        self.arc = self.canvas.create_arc(self.coord, start=0, extent=150, fill="red")
        self.myLabelMenu = tk.Label(self.menuFrame, text = "hello world3").grid(row = 0, column = 0)


    def mainloop(self):
        self.makeMainframe()
        self.makeListFrame()
        self.makeCanvasFrame()
        self.makeMenuFrame()
        self.makeLabel()
        self.root.mainloop()

Example = MainGUI()

Example.mainloop()