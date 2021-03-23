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
            pass #self.handleExplicitAddition(self, input)
        elif "-" in input:
            self.handleSubtraction(self, input)
        elif "subtract" in input:
            pass #self.handleExplicitSubtraction(self, input)
        elif "*" in input:
            self.handleScalarProduct(self, input)
        elif "scalarProduct" in input:
            pass #self.handleExplicitScalarProduct(self, input)
        elif ":" in input or "/" in input:
            self.handleDivision(self, input)
        elif "divide" in input:
            pass #self.handleExplicitDivision(self, input)
        elif "schneiden" in input or "Schneiden" in input:
            self.handleSchneiden(self, input)

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

    def handleExplicitAddition(self, input):
        pass


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

    def handleExplicitSubtraction(self, input):
        pass

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


    def handleExplicitScalarProduct(self, input):
        pass

    def handleDivision(self, input):
        try:
            division = re.split(r"[:]", input)
        except len(division) == 1:
            division = re.split(r"[/]", input)

        if not(len(division) == 1):
            firstVec = ObjectLists.getObjDict().get(division[0].strip())
            divVec = firstVec
            for index in range(len(division) - 1):
                nextNum = division[index + 1].strip()
                divVec = divVec.scalarDivision(nextNum)
                print(divVec) # Testing Purposes
                    

    def handleExplicitDivision(self, input):
        pass
    

    def handleSchneiden(self, input):
        elements = re.split(r"[(,)]", input)
        print(elements)
        firstElement = elements[1].strip()
        secondElement = elements[2].strip()

        if "lin" in firstElement:
            if "lin" in secondElement:
                point = Solvers.schnittpunkt(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                print(point)
            elif "pla" in secondElement:
                point = Solvers.solveForPointPlane(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                print(point)
            else:
                print("No valid arguments for Schneiden.")
        elif "pla" in firstElement:
            if "lin" in secondElement:
                point = Solvers.solveForPointPlane(ObjectLists.getObjDict().get(secondElement), ObjectLists.getObjDict().get(firstElement))
                print(point)
            elif "pla" in secondElement:
                line = Solvers.schnittgerade(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                print(line)
            else:
                print("No valid arguments for Schneiden.")
        else:
            print("No valid arguments for Schneiden.")

