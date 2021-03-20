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
        
        if "+" in input:
            self.handleAddition(self, input)
        elif "add" in input:
            pass #self.handleOtherAddition(self, input)
        elif "-" in input:
            self.handleSubtraction(self, input)
        elif "subtract" in input:
            pass #self.handleOtherSubtraction(self, input)
        elif "*" in input:
            self.handleScalarProduct(self, input)
        elif "scalarProduct" in input:
            pass #self.handleOtherScalarProduct(self, input)
        elif ":" in input:
            pass
        elif "divide" in input:
            pass
        else:
            print("nothing to handle!")

        
    def handleAddition(self, input):
        addition = re.split(r"[+]", input)
        if not(len(addition) == 1):
            firstVec = ObjectLists.getObjDict().get(addition[0].strip())
            addedVec = firstVec
            for index in range(len(addition) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(addition[index + 1].strip())
                    addedVec = addedVec.add(nextVec)
                except IndexError:
                    pass
                except Exception:
                    pass

            print(addedVec) # Testing Purposes


    def handleSubtraction(self, input):
        subtraction = re.split(r"[-]", input)
        if not(len(subtraction) == 1):
            firstVec = ObjectLists.getObjDict().get(subtraction[0].strip())
            subtractedVec = firstVec
            for index in range(len(subtraction) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(subtraction[index + 1].strip())
                    subtractedVec = subtractedVec.subtract(nextVec)
                except IndexError:
                    pass
                except Exception:
                    pass

            print(subtractedVec) # Testing Purposes

    def handleScalarProduct(self, input):
        scalar = re.split(r"[*]", input)
        if not(len(scalar) == 1):
            firstVec = ObjectLists.getObjDict().get(scalar[0].strip())
            multVec = firstVec
            for index in range(len(scalar) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(scalar[index + 1].strip())
                    multNum = multVec.scalarProduct(nextVec)
                    print(multNum) # Testing Purposes
                except IndexError:
                    pass
                except Exception:
                    nextNum = scalar[index + 1].strip()
                    multVec = multVec.scalarMultiplication(nextNum)
                    print(multVec) # Testing Purposes

            
