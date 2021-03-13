import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px


from colorAssignclass import ColorAssign
from lineclass import Line
from listclass import ObjectLists
from nameAssignclass import NameAssign
from planeclass import Plane
from pointclass import Point
from solvers import Solvers
from vector3Dclass import Vector3D

def compileFig():
    dictionary = ObjectLists.getObjDict()
    fig = go.Figure()
    for elem in dictionary:
        if elem[0:3] == "vec":
            elem = dictionary[elem]
            if elem.show == True:
                fig.add_trace(go.Scatter3d(x=[0,elem.x], y=[0,elem.y], z=[0,elem.z],mode="lines",surfacecolor=elem.getColor()))
        elif elem[0:3] == "lin":
            elem = dictionary[elem]
            if elem.show==True:
                borders = [
                    Plane.normalForm(Vector3D(-50,0,0,show=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,color=(0,0,0)),show=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(50,0,0,show=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,color=(0,0,0)),show=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,-50,0,show=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,color=(0,0,0)),show=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,50,0,show=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,color=(0,0,0)),show=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,0,50,show=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,color=(0,0,0)),show=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,0,-50,show=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,color=(0,0,0)),show=False,color=(0,0,0))]
                schnittpunkte=[]
                for plane in borders:
                    schnittpunkt = Solvers.schnittpunkt(plane,elem)
                    if schnittpunkt != None:
                        schnittpunkte.append(schnittpunkt)
                fig.add_trace(go.Scatter3D(x=[x1,x2], y=[y1,y2], z=[z1,z2],mode="lines"))
        elif elem[0:3] == "pla":
            elem = dictionary[elem]
        elif elen[0:3] == "poi":
            elem = dictionary[elem]
    fig.show()

vec = Vector3D(1,2,3)
vec2 = Vector3D(2,3,4)
compileFig()
