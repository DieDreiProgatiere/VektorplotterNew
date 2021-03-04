from vector3Dclass import Vector3D
from pointclass import Point
from lineclass import Line
from planeclass import Plane

from colorAssignclass import ColorAssign
from nameAssignclass import NameAssign

from listclass import ObjectLists
from solvers import Solvers

import tkinter as tk 
import numpy as np

from maingui import MainGUI


class Draw:

    def __init__(self) -> None:
        pass


    @classmethod
    def draw(self, canvas, object, color) -> None:
        self.canvas = canvas
        self.object = object
        self.color = color


    @classmethod
    def drawCoordinates(self, canvas, scale, angle):
        self.canvas = canvas
        self.scale = scale
        self.angle = angle

        self.xUnitVec = Vector3D(1, 0, 0)
        self.yUnitVec = Vector3D(0, 1, 0)
        self.zUnitVec = Vector3D(0, 0, 1)

        self.rotationMatrix = "platzhalter"

        self.yAxis = canvas.create_line()
        self.xAxis = canvas.create_line()
        self.zAxis = canvas.create_line()

