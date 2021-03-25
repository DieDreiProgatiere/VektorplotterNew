from listclass import ObjectLists
from solvers import Solvers
import re


class CalcInput:

    def __init__(self) -> None:
        pass

    @classmethod
    def handleInput(self, input):
        
        if "+" in input:
            obj = self.handleAddition(self, input)
        elif "add" in input:
            pass #self.handleExplicitAddition(self, input)
        elif "-" in input:
            obj = self.handleSubtraction(self, input)
        elif "subtract" in input:
            pass #self.handleExplicitSubtraction(self, input)
        elif "*" in input:
            obj = self.handleScalarProduct(self, input)
        elif "scalarProduct" in input:
            pass #self.handleExplicitScalarProduct(self, input)
        elif ":" in input or "/" in input:
            obj = self.handleDivision(self, input)
        elif "divide" in input:
            pass #self.handleExplicitDivision(self, input)
        elif "x" in input:
            obj = self.handleVectorProduct(self, input)
        elif "kreuz" in input:
            pass #self.handleExplicitVectorProduct(self, input)
        elif "schneiden" in input or "Schneiden" in input:
            obj = self.handleSchneiden(self, input)
        elif "d" in input or "D" in input:
            obj = self.handleDistance(self, input)
        elif "winkel" in input:
            obj = self.handleAngle(self, input)
        else:
            print("nothing to handle!")

        return obj

        
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

            return str(input) + ": " + str(addedVec)


    def handleExplicitAddition(self, input):
        pass #Future Implementation

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

            return str(input) + ": " + str(subtractedVec)

    def handleExplicitSubtraction(self, input):
        pass #Future Implementation

    def handleScalarProduct(self, input):
        scalar = re.split(r"[*]", input)
        if not(len(scalar) == 1):
            firstVec = ObjectLists.getObjDict().get(scalar[0].strip())
            multVec = firstVec
            for index in range(len(scalar) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(scalar[index + 1].strip())
                    multNum = multVec.scalarProduct(nextVec)
                    return str(input) + ": " + str(multNum)
                except IndexError:
                    pass
                except Exception:
                    nextNum = scalar[index + 1].strip()
                    multVec = multVec.scalarMultiplication(nextNum)
                    return str(input) + ": " + str(multVec)


    def handleExplicitScalarProduct(self, input):
        pass #Future Implementation

    def handleDivision(self, input):
        try:
            division = re.split(r"[:]", input)
        except len(division) == 1:
            division = re.split(r"[/]", input)
        except Exception:
            pass

        if not(len(division) == 1):
            firstVec = ObjectLists.getObjDict().get(division[0].strip())
            divVec = firstVec
            for index in range(len(division) - 1):
                try:
                    nextNum = division[index + 1].strip()
                    divVec = divVec.scalarDivision(nextNum)
                except IndexError:
                    pass
                except Exception:
                    pass

            return str(input) + ": " + str(divVec)


    def handleExplicitDivision(self, input):
        pass #Future Implementation


    def handleVectorProduct(self, input):
        product = re.split(r"[x]", input)
        if not(len(product) == 1):
            firstVec = ObjectLists.getObjDict().get(product[0].strip())
            multVec = firstVec
            for index in range(len(product) - 1):
                try:
                    nextVec = ObjectLists.getObjDict().get(product[index + 1].strip())
                    multVec = multVec.vectorProduct(nextVec)
                except IndexError:
                    pass
                except Exception:
                    pass

            return str(input) + ": " + str(multVec)

    
    def handleExplicitVectorProduct(self, input):
        pass #Future Implementation
    

    def handleSchneiden(self, input):
        elements = re.split(r"[(,)]", input)
        firstElement = elements[1].strip()
        secondElement = elements[2].strip()

        if "lin" in firstElement:
            if "lin" in secondElement:
                point = Solvers.schnittpunkt(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + ": " + str(point)
            elif "pla" in secondElement:
                point = Solvers.solveForPointPlane(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + ": " + str(point)
            else:
                print("No valid arguments for Schneiden.")
        elif "pla" in firstElement:
            if "lin" in secondElement:
                point = Solvers.solveForPointPlane(ObjectLists.getObjDict().get(secondElement), ObjectLists.getObjDict().get(firstElement))
                return str(input) + ": " + str(point)
            elif "pla" in secondElement:
                line = Solvers.schnittgerade(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + ": " + str(point)
            else:
                print("No valid arguments for Schneiden.")
        else:
            print("No valid arguments for Schneiden.")


    def handleDistance(self, input):
        elements = re.split(r"[(,)]", input)
        firstElement = elements[1].strip()
        secondElement = elements[2].strip()

        if "poi" in firstElement:
            if "poi" in secondElement:
                distance = Solvers.distancePointPoint(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + "= " + str(distance)
            elif "lin" in secondElement:
                distance = Solvers.distancePointLine(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + "= " + str(distance)
            elif "pla" in secondElement:
                distance = Solvers.distancePlanePoint(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + "= " + str(distance)
            else:
                print("No valid arguments for Distance.")
        elif "lin" in firstElement:
            if "poi" in secondElement:
                distance = Solvers.distancePointLine(ObjectLists.getObjDict().get(secondElement), ObjectLists.getObjDict().get(firstElement))
                return str(input) + "= " + str(distance)
            elif "lin" in secondElement:
                distance = Solvers.distanceLineLine(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + "= " + str(distance)
            elif "pla" in secondElement:
                distance = Solvers.distanceLinePlane(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + "= " + str(distance)
            else:
                print("No valid arguments for Distance.")
        elif "pla" in firstElement:
            if "poi" in secondElement:
                distance = Solvers.distancePlanePoint(ObjectLists.getObjDict().get(secondElement), ObjectLists.getObjDict().get(firstElement))
                return str(input) + "= " + str(distance)
            elif "lin" in secondElement:
                distance = Solvers.distanceLinePlane(ObjectLists.getObjDict().get(secondElement), ObjectLists.getObjDict().get(firstElement))
                return str(input) + "= " + str(distance)
            elif "pla" in secondElement:
                distance = Solvers.distancePlanePlane(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
                return str(input) + "= " + str(distance)
            else:
                print("No valid arguments for Distance.")
        else:
            print("No valid arguments for Distance.")


    def handleAngle(self, input):
        elements = re.split(r"[(,)]", input)
        firstElement = elements[1].strip()
        secondElement = elements[2].strip()

        try:
            angle = Solvers.solveForSchnittwinkel(ObjectLists.getObjDict().get(firstElement), ObjectLists.getObjDict().get(secondElement))
            return str(input) + "= " + str(angle)
        except Exception:
            print("No valid arguments for Angle.")

    
