import numpy as np
from vector3Dclass import Vector3D
from pointclass import Point
from planeclass import Plane
from lineclass import Line
from colorAssignclass import ColorAssign
from nameAssignclass import NameAssign
from listclass import ObjectLists


class Solvers():
    
    def __init__(self):
        pass

    @classmethod
    def solveForSchnittstelle(self,
                              line1,
                              line2):
        coefficientMatrix = [
            [line1.dirVec.x,-line2.dirVec.x],
            [line1.dirVec.y,-line2.dirVec.y],
            [line1.dirVec.z,-line2.dirVec.z]
            ]
        equalMatrix = [
            line2.posVec.x-line1.posVec.x,
            line2.posVec.y-line1.posVec.y,
            line2.posVec.z-line1.posVec.z
            ]
        try:
            answers = np.linalg.solve(
                np.array(
                    [
                        coefficientMatrix[0],
                        coefficientMatrix[1]
                    ]
                    ),
                np.array(
                    [
                        equalMatrix[0],
                        equalMatrix[1]
                    ]
                         )
                )
        except np.linalg.LinAlgError:
            try:
                answers = np.linalg.solve(
                    np.array(
                        [
                            coefficientMatrix[0],
                            coefficientMatrix[2]
                         ]
                        ),
                    np.array(
                        [
                            equalMatrix[0],
                            equalMatrix[2]
                        ]
                             )
                    )
            except np.linalg.LinAlgError:
                try:
                    answers = np.linalg.solve(
                        np.array(
                            [
                                coefficientMatrix[0],
                                coefficientMatrix[1]
                             ]
                            ),
                        np.array(
                            [
                                equalMatrix[0],
                                equalMatrix[1]
                            ]
                                 )
                        )
                except np.linalg.LinAlgError:
                    answers = None
        return answers

    @classmethod
    def solveForSchnittgerade(self,
                              plane1,
                              plane2):
        pass

    @classmethod
    def schnittpunkt(self,
                     line1,
                     line2):
        schnittstelle = self.solveForSchnittstelle(line1, line2)
        schnittpunkt = line1.pointOnLine(schnittstelle[0])
        return schnittpunkt

    @classmethod
    def schnittgerade(self,
                      plane1,
                      plane2):
        pass

    @classmethod
    def checkParallel(self,
                      objekt1,
                      objekt2):
        pass

    @classmethod
    def checkPointInLine(self,
                         line,
                         point):
        pass

    @classmethod
    def checkColinear(self,
                      obj1,
                      obj2):
        pass

    @classmethod
    def solveForSchnittwinkel(self,
                              objekt1,
                              objekt2):
        winkel = None
        if type(objekt1) == Line and type(objekt2) == Line:
            pass
        elif type(objekt1) == Line and type(objekt2) == Plane:
            pass
        elif type(objekt1) == Plane and type(objekt2) == Plane:
            pass
        else:
            print("We cannot calculate this Angle.")
        return winkel


v1= Vector3D(0,0,0)
v2 = Vector3D(1,1,1)
v3= Vector3D(1,0,0)
v4= Vector3D(0,1,0)
lin1= Line(v1,v3)
lin2 = Line(v2,v4)
print("lins created")
print(Solvers.schnittpunkt(lin1,lin2))
print(type(lin1)==Line)
