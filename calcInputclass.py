from listclass import ObjectLists
from vector3Dclass import Vector3D
from pointclass import Point
from lineclass import Line
from planeclass import Plane
from solvers import Solvers
import re


class CalcInput:

    def __init__(self) -> None:
        pass

    @classmethod
    def handleInput(self, input):
        #Vectors
        addition = re.split(r"[+]", input)
        if not(len(addition) == 1):
            firstVec = ObjectLists.getObjDict().get(addition[0].strip())
            addedVec = firstVec
            for index in range(len(addition) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(addition[index + 1].strip())
                except IndexError:
                    pass
                except Exception:
                    pass
                addedVec = addedVec.add(nextVec)

            print(addedVec) # Testing Purposes

        subtraction = re.split(r"[-]", input)
        if not(len(subtraction) == 1):
            firstVec = ObjectLists.getObjDict().get(subtraction[0].strip())
            subtractedVec = firstVec
            for index in range(len(subtraction) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(subtraction[index + 1].strip())
                except IndexError:
                    pass
                except Exception:
                    pass
                subtractedVec = subtractedVec.subtract(nextVec)

            print(subtractedVec) # Testing Purposes