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
    # Koordinatenachsen
    fig.add_trace(go.Scatter3d(x=[-50, 50], y=[0, 0], z=[0, 0], mode="lines", line_color="rgb(0,0,0)", name="x"))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[-50, 50], z=[0, 0], mode="lines", line_color="rgb(0,0,0)", name="y"))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-50, 50], mode="lines", line_color="rgb(0,0,0)", name="z"))

    # Hinzugefügte Objekte
    for elem in dictionary:
        if elem[0:3] == "vec":
            elem = dictionary[elem]
            if elem.show is True:
                fig.add_trace(go.Scatter3d(x=[0, elem.x], y=[0, elem.y], z=[0, elem.z], mode="lines", line_color="rgb"+str(elem.getColor()), name=elem.getID()))
        elif elem[0:3] == "lin":
            elem = dictionary[elem]
            if elem.show is True:
                borders = [
                    Plane.normalForm(Vector3D(-50,0,0,show=False,append=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,append=False,color=(0,0,0)),show=False,append=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(50,0,0,show=False,append=False,color=(0,0,0)),normalVector=Vector3D(1,0,0,show=False,append=False,color=(0,0,0)),show=False,append=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,-50,0,show=False,append=False,color=(0,0,0)),normalVector=Vector3D(0,1,0,show=False,append=False,color=(0,0,0)),show=False,append=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,50,0,show=False,append=False,color=(0,0,0)),normalVector=Vector3D(0,1,0,show=False,append=False,color=(0,0,0)),show=False,append=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,0,50,show=False,append=False,color=(0,0,0)),normalVector=Vector3D(0,0,1,show=False,append=False,color=(0,0,0)),show=False,append=False,color=(0,0,0)),
                    Plane.normalForm(Vector3D(0,0,-50,show=False,append=False,color=(0,0,0)),normalVector=Vector3D(0,0,1,show=False,append=False,color=(0,0,0)),show=False,append=False,color=(0,0,0))]
                schnittpunkte = []
                for plane in borders:
                    schnittpunkt = Solvers.solveForPointPlane(elem,plane)
                    if schnittpunkt is not None:
                        schnittpunkte.append(schnittpunkt)
                if len(schnittpunkte) > 2:
                    x1 = schnittpunkte[0].x
                    x2 = schnittpunkte[1].x
                    y1 = schnittpunkte[0].y
                    y2 = schnittpunkte[1].y
                    z1 = schnittpunkte[0].z
                    z2 = schnittpunkte[1].z
                else:
                    x1 = schnittpunkte[0].x
                    x2 = schnittpunkte[1].x
                    y1 = schnittpunkte[0].y
                    y2 = schnittpunkte[1].y
                    z1 = schnittpunkte[0].z
                    z2 = schnittpunkte[1].z
                fig.add_trace(go.Scatter3d(x=[x1, x2], y=[y1, y2], z=[z1, z2], mode="lines", line_color="rgb"+str(elem.getColor()), name=elem.getID()))
        elif elem[0:3] == "pla":
            elem = dictionary[elem]
            if elem.show:
                edges = [
                    Line(Vector3D(50, 50, 50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(50, 0.1, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(50, 50, 50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 50, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(50, 50, 50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 0.1, 50, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, -50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(50, 0.1, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, -50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 50, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, -50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 0.1, 50, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, -50, 50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(50, 0.1, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, -50, 50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 50, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(50, -50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 0.1, 50, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(50, -50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 50, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, 50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(0.1, 0.1, 50, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False),
                    Line(Vector3D(-50, 50, -50, show=False, append=False, color=(0, 0, 0)),
                         Vector3D(50, 0.1, 0.1, show=False, append=False, color=(0, 0, 0)), name="edge", color=(0, 0, 0),
                         show=False, append=False)
                ]
                schnittpunkte = []
                for edge in edges:
                    schnittpunkt = Solvers.solveForPointPlane(edge, elem)
                    if schnittpunkt is not None:
                        schnittpunkte.append(schnittpunkt)
                        print(schnittpunkt)
                x = []
                y = []
                z = []
                for schnittpunkt in schnittpunkte:
                    if 51 > schnittpunkt.x > -51 and 51 > schnittpunkt.y > -51 and 51 > schnittpunkt.z > -51:
                        x.append(schnittpunkt.x)
                        y.append(schnittpunkt.y)
                        z.append(schnittpunkt.z)
                fig.add_trace(go.Mesh3d(x=x,y=y,z=z,color="rgb"+str(elem.getColor()),opacity=0.5,name=elem.getID(),showlegend=True))
        elif elem[0:3] == "poi":
            elem = dictionary[elem]
            if elem.show:
                fig.add_trace(go.Scatter3d(x=[elem.x], y=[elem.y], z=[elem.z], line_color="rgb"+str(elem.getColor()), name=elem.getID()))
    # fig.show()  # for showing the full figure in browser if planes do not render correctly in window
    return fig

