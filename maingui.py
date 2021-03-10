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

import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
matplotlib.use("TkAgg")

# Needed for testing of embedded matplotlib
import numpy as np 


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
        self.root.resizable(0, 0)

        self.makeMainframe()
        self.makeListFrame()
        self.makeMenuFrame()
        self.makeLabel()
        self.embedMatplotlib()
        self.root.mainloop()

    def makeMainframe(self):
        self.mainframe = tk.Frame(self.root, height = self.height, width = self.width)
        self.mainframe.grid(column = 0, row = 0, sticky = "NESW")
        self.root.columnconfigure(0)
        self.root.rowconfigure(0)


    def makeListFrame(self):
        self.listFrame = tk.Frame(self.mainframe, borderwidth = 1, height=self.mainframe.winfo_height())
        self.listFrame.grid(column = 0, row = 1, sticky = "NES")
        for element, index in zip(ObjectLists.getObjDict(), range(ObjectLists.getObjDictLen())):
            self.objButton = tk.Button(self.listFrame, text = str(element) + str(ObjectLists.getObjDict()[element]), width = 50, command = self.funktion) # funktion placeholder for future function
            self.objButton.grid(ipady = 10, column = 0, row = index)

        self.addButton = tk.Button(self.listFrame, text = "Add new Object +", width = 50, command = self.funktion) # funktion placeholder for future function
        self.addButton.grid(ipady = 10, column = 0, row = ObjectLists.getObjDictLen())

    def funktion(self):
        pass

    def makeMenuFrame(self):
        self.menuFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.menuFrame.grid(columnspan = 2, column = 0, row = 0, sticky = "NWE")


    def embedMatplotlib(self):
        self.canvasFrame = tk.Frame(self.mainframe, borderwidth = 1)
        self.canvasFrame.grid(column = 1, row = 1, sticky = "NSW")
        self.canvasFrame.columnconfigure(1, weight = 1)
        self.canvasFrame.rowconfigure(1, weight = 1)
        ### Testing embedded matplotlib
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111, projection="3d")
        t = np.arange(0, 3, 0.01)
        ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.mouse_init()
        ### Testing embedded matplotlib over
        self.canvas = FigureCanvasTkAgg(fig, master=self.canvasFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column = 0, row = 0)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        self.toolbar.update()
        self.canvas.get_tk_widget().grid(column = 0, row = 0)
    
        def on_key_press(event):
            print(f"you pressed {event.key}")
            key_press_handler(event, self.canvas, self.toolbar)
        self.canvas.mpl_connect("key_press_event", on_key_press)


    def makeLabel(self):
        self.myLabelMenu = tk.Label(self.menuFrame, text = "Menu").grid(row = 0, column = 0)


Example = MainGUI()
