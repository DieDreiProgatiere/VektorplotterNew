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
z = Plane.parameterForm(Vector3D(3, 4, 5), Vector3D(2, 2, 2), Vector3D(2, 2, 2))

class MainGUI(tk.Frame):
    width = 1200
    height = 700
    size = str(width) + "x" + str(height)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vektorplotter")
        self.root.geometry(self.size)
        #self.root.resizable(0, 0)

        self.makeMainframe()
        self.makeListFrame()
        self.makeMenuFrame()
        self.makeCanvasFrame()
        self.root.mainloop()

    def makeMainframe(self):
        self.mainframe = tk.Frame(self.root, height = self.height, width = self.width)
        self.mainframe.grid(column = 0, row = 0, sticky = "NESW")
        self.root.columnconfigure(0)
        self.root.rowconfigure(0)


    def makeListFrame(self):
        #self.listScrollbar = tk.Scrollbar(self.mainframe)
        #self.listScrollbar.grid(column = 1, row = 1, rowspan = 2) 
        self.listFrame = tk.Frame(self.mainframe, borderwidth = 1, height=self.mainframe.winfo_height())
        self.listFrame.grid(column = 0, row = 1, sticky = "NES")
        for element, index in zip(ObjectLists.getObjDict(), range(ObjectLists.getObjDictLen())):
            self.objButton = tk.Button(self.listFrame, text = str(element) + str(ObjectLists.getObjDict()[element]), width = 50, command = self.funktion) # funktion placeholder for future function
            self.objButton.grid(ipady = 10, column = 0, row = index, columnspan = 2)

        self.addVecButton = tk.Button(self.listFrame, text = "Add new Object +", width = 25, command = self.funktion) # funktion placeholder for future function
        self.addVecButton.grid(ipady = 10, column = 0, row = ObjectLists.getObjDictLen())
        self.addCalcButton = tk.Button(self.listFrame, text = "Add new Calculation +", width = 25, command = self.funktion) # funktion placeholder for future function
        self.addCalcButton.grid(ipady = 10, column = 1, row = ObjectLists.getObjDictLen())

    def funktion(self):
        pass

    def makeMenuFrame(self):
        self.menuFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.menuFrame.grid(columnspan = 2, column = 0, row = 0, sticky = "NWE")

        self.spurButton = tk.Button(self.menuFrame, text = "Spurpunkte", width = 10, command = self.funktion) # funktion placeholder for future function
        self.spurButton.grid(ipady = 10, column = 0, row = 0)


    def makeCanvasFrame(self):
        self.canvasFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.canvasFrame.grid(column = 2, row = 1, sticky = "NSW")
        self.canvasFrame.columnconfigure(1, weight = 1)
        self.canvasFrame.rowconfigure(1, weight = 1)
    

Example = MainGUI()