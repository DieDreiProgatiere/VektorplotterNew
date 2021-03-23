import numpy as np
from vector3Dclass import Vector3D
from pointclass import Point
from planeclass import Plane
from lineclass import Line
from colorAssignclass import ColorAssign
from nameAssignclass import NameAssign
from listclass import ObjectLists
import math


class Solvers:
    
    def __init__(self):
        """Placeholder; not necessary."""
        pass

    @classmethod
    def solveForPointPlane(self, line: Line, plane: Plane):
        if plane.getType() == "normal":
            normVec = plane.getNormalVector()
            posVecP = plane.getPositionVector()
            scalarParam = posVecP.scalarProduct(normVec)
            posVec = line.getPositionVector()
            dirVec = line.getDirectionVector()
            xValNoVar = normVec.getX()*posVec.getX()
            yValNoVar = normVec.getY()*posVec.getY()
            zValNoVar = normVec.getZ()*posVec.getZ()
            xValVar = normVec.getX()*dirVec.getX()
            yValVar = normVec.getY()*dirVec.getY()
            zValVar = normVec.getZ()*dirVec.getZ()
            ValVar = xValVar+yValVar+zValVar
            ValNoVar = scalarParam - xValNoVar - yValNoVar - zValNoVar
            Var = ValNoVar/ValVar
            SchnittPoint = Point(posVec.getX()+Var*dirVec.getX(),posVec.getY()+Var*dirVec.getY(),posVec.getZ()+Var*dirVec.getZ(),color=(0,0,0))
            return SchnittPoint

        elif plane.getType() == "coordinate":
            normVec = plane.getNormalVector()
            scalarParam = plane.getScalarParameter()
            posVec = line.getPositionVector()
            dirVec = line.getDirectionVector()
            xValNoVar = normVec.getX()*posVec.getX()
            yValNoVar = normVec.getY()*posVec.getY()
            zValNoVar = normVec.getZ()*posVec.getZ()
            xValVar = normVec.getX()*dirVec.getX()
            yValVar = normVec.getY()*dirVec.getY()
            zValVar = normVec.getZ()*dirVec.getZ()
            ValVar = xValVar+yValVar+zValVar
            ValNoVar = scalarParam - xValNoVar - yValNoVar - zValNoVar
            Var = ValNoVar/ValVar
            SchnittPoint = Point(posVec.getX()+Var*dirVec.getX(),posVec.getY()+Var*dirVec.getY(),posVec.getZ()+Var*dirVec.getZ(),color=(0,0,0))
            return SchnittPoint
        elif plane.getType() == "parameter":
            normVec = plane.getDirectionVectorOne().vectorProduct(plane.getDirectionVectorTwo())
            posVecP = plane.getPositionVector()
            scalarParam = posVecP.scalarProduct(normVec)
            posVec = line.getPositionVector()
            dirVec = line.getDirectionVector()
            xValNoVar = normVec.getX()*posVec.getX()
            yValNoVar = normVec.getY()*posVec.getY()
            zValNoVar = normVec.getZ()*posVec.getZ()
            xValVar = normVec.getX()*dirVec.getX()
            yValVar = normVec.getY()*dirVec.getY()
            zValVar = normVec.getZ()*dirVec.getZ()
            ValVar = xValVar+yValVar+zValVar
            ValNoVar = scalarParam - xValNoVar - yValNoVar - zValNoVar
            Var = ValNoVar/ValVar
            SchnittPoint = Point(posVec.getX()+Var*dirVec.getX(),posVec.getY()+Var*dirVec.getY(),posVec.getZ()+Var*dirVec.getZ(),color=(0,0,0))
            return SchnittPoint

    @classmethod
    def solveForSchnittstelle(self,
                              line1: Line,
                              line2: Line):
        """Solves for the Schnittstelle between two Lines of dtype Line.
           Returns array of floatpoint numbers that are the coefficients for the Schnittstelle
           in the same order as given Lines."""
        coefficientMatrix = [
            [line1.dirVec.x, -line2.dirVec.x],
            [line1.dirVec.y, -line2.dirVec.y],
            [line1.dirVec.z, -line2.dirVec.z]
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
                              plane1: Plane,
                              plane2: Plane):
        """Use Solvers.schnittgerade()"""
        return self.schnittgerade(plane1, plane2)

    @classmethod
    def schnittpunkt(self,
                     line1: Line,
                     line2: Line):
        """Returns the Schnittpunkt between two Lines.
           Uses Solvers.solveForSchnittstelle.
           Returns a Point instance."""

        posVec1 = line1.getPositionVector()
        posVec2 = line2.getPositionVector()
        dirVec1 = line1.getDirectionVector()
        dirVec2 = line2.getDirectionVector()
        schnittstelle = self.solveForSchnittstelle(line1, line2)
        ValOne = posVec1.add(dirVec1.scalarMultiplication(schnittstelle[0]))
        ValTwo = posVec2.add(dirVec2.scalarMultiplication(schnittstelle[0]))
        if ValOne.getX() == ValTwo.getX() and ValOne.getY() == ValTwo.getY() and ValOne.getZ() == ValTwo.getZ():
            schnittpunkt = ValOne
            schnittpunkt = Point(ValOne.getX(),ValOne.getY(),ValOne.getZ())
        else: 
            schnittpunkt = None   
        return schnittpunkt

    @classmethod
    def schnittgerade(self,
                      plane1: Plane,
                      plane2: Plane):
        """Calculates and Returns the schnittgerade of two Planes.
           Returns a Line instance."""
        pla1 = plane1.convertToHessianNormalForm()
        pla2 = plane2.convertToHessianNormalForm()

        normvec1 = pla1.normVec
        normvec2 = pla2.normVec

        posnum1 = pla1.posVec.scalarProduct(normvec1)
        posnum2 = pla2.posVec.scalarProduct(normvec2)

        schnittgerade = not Solvers.checkLinearAbhaengig(normvec1, normvec2)  # Testing if the Planes are not Parallel

        if schnittgerade:
            dirVec = normvec1.vectorProduct(normvec2)
            posVecScalar1 = ((posnum1*normvec2.square())-(posnum2*normvec1.scalarProduct(normvec2)))/((normvec1.square()*normvec2.square())-normvec1.scalarProduct(normvec2)**2)
            posVecScalar2 = ((posnum2*normvec1.square())-(posnum1*normvec1.scalarProduct(normvec2)))/((normvec1.square()*normvec2.square())-normvec1.scalarProduct(normvec2)**2)
            normvec1 = normvec1.scalarMultiplication(posVecScalar1)
            normvec2 = normvec2.scalarMultiplication(posVecScalar2)
            posVec = normvec1.add(normvec2)
            schnittgerade = Line(posVec, dirVec, name=("Schnittgerade von "+pla1.name+" und "+pla2.name))
        return schnittgerade

    @classmethod
    def checkParallel(self,
                      objekt1,
                      objekt2):
        """Not jet completely integrated.
           Will return False if objects (pair of Line(s) and/or Plane(s)) are not parallel.
           Else returns True."""
        parallel = True
        if type(objekt1) == Line and type(objekt2) == Line:
            if Solvers.solveForSchnittstelle(objekt1, objekt2) is not None:
                parallel = False
        elif type(objekt1) == Line and type(objekt2) == Plane:
            pass  # still requires implementation of Line and Plane Schnittpunkt Calculations
        elif type(objekt1) == Plane and type(objekt2) == Line:
            pass  # see above
        elif type(objekt1) == Plane and type(objekt2) == Plane:
            if Solvers.schnittgerade(objekt1, objekt2) is not False:
                parallel = False
        else:
            print("We cannot check if these objekts are Parallel")
        return parallel

    @classmethod
    def checkPointInLine(self,
                         line: Line,
                         point: Point):
        """Uses Solvers.checkLinearAbhaengig to check if a given point is on a given line.
           Returns True if the point is on the Line.
           Else returns False.
           See Solvers.checkLinearAbhaengig."""
        return self.checkLinearAbhaengig(
            line.dirVec,
            Vector3D(point.x+line.posVec.x, point.y+line.posVec.y, point.z+line.posVec.z))

    @classmethod
    def checkPointInPlane(self, plane:Plane, point: Point):
        vector = Vector3D(point.getX(),point.getY(),point.getZ())
        typeOfPlane = plane.getType()
        pointInPlane = False
        if typeOfPlane == "normal":
           result = vector.subtract(plane.getPositionVector())
           answer = result.scalarProduct(plane.getNormalVector())
           if answer == 0:
               pointInPlane = True
           else:
               pointInPlane = False
        elif typeOfPlane == "parameter":
            dirVec1 = plane.getDirectionVectorOne()
            dirVec2 = plane.getDirectionVectorTwo()
            result = vector.subtract(plane.getPositionVector())
            arrayOne = np.array([[dirVec1.getX(),dirVec1.getY()], [dirVec2.getX(),dirVec2.getY()]])
            arrayTwo = np.array([result.getX(),result.getY()])
            solution = np.linalg.solve(arrayOne,arrayTwo)
            if solution[0]*dirVec1.getZ() + solution[1]*dirVec2.getZ() == result.getZ():
                pointInPlane = True
            else: 
                pointInPlane = False
        elif typeOfPlane == "coordinate":
            normVec = plane.getNormalVector()
            if point.getX()*normVec.getX() + point.getY()*normVec.getY() + point.getZ()*normVec.getZ() == plane.getScalarParameter():
                pointInPlane = True
            else:
                pointInPlane = False
        return pointInPlane

    @classmethod
    def checkColinear(self,
                      obj1,
                      obj2):
        """Still requires implementation."""
        pass

    @classmethod
    def checkLinearAbhaengig(self,
                             vec1: Vector3D,
                             vec2: Vector3D):
        """Tests if two vectors are "linear abhängig".
           Takes two Vector3D instances.
           Returns True if they are linear abhängig.
           Else returns False."""
        coefficientMatrix = np.array([
            [vec1.x],
            [vec1.y],
            [vec1.z]
            ])
        equalMatrix = np.array([
            vec2.x,
            vec2.y,
            vec2.z
            ])
        try:
            answer = np.linalg.solve(
                np.array([coefficientMatrix[0]]),
                np.array([equalMatrix[0]])
                )
        except np.linalg.LinAlgError:
            try:
                answer = np.linalg.solve(
                    np.array([coefficientMatrix[1]]),
                    np.array([equalMatrix[1]])
                    )
            except np.linalg.LinAlgError:
                try:
                    answer = np.linalg.solve(
                        np.array([coefficientMatrix[2]]),
                        np.array([equalMatrix[2]])
                        )
                except np.linalg.LinAlgError:
                    answer = False  # Wenn dieser Punkt erricht wird sind sie nicht Abhängig.
        if answer != False:
            print(answer)
            print(coefficientMatrix)
            coefficientMatrix = np.inner(coefficientMatrix, answer)
            print(coefficientMatrix)
            print(equalMatrix)
            if coefficientMatrix[0] == equalMatrix[0] and coefficientMatrix[1] == equalMatrix[1] and coefficientMatrix[2] == equalMatrix[2]:
                answer = True
            else:
                answer = False
        return answer

    @classmethod
    def solveForSchnittwinkel(self,
                              objekt1,
                              objekt2):
        """Calculates the Schnittwinkel of two Planes or Lines (or a Plane and a Line).
           Takes either Line or Plane instances for objekt1 and objekt2.
           Returns a angle as a floating point number of degrees."""
        winkel = None
        if type(objekt1) == Line and type(objekt2) == Line:
            if Solvers.solveForSchnittstelle(objekt1, objekt2) is not None:
                winkel = math.degrees(math.acos(
                    abs(objekt1.dirVec.scalarProduct(objekt2.dirVec)) /
                    (objekt1.dirVec.length()*objekt2.dirVec.length())))
        elif type(objekt1) == Line and type(objekt2) == Plane:
            winkel = math.degrees(math.asin(
                abs(objekt1.dirVec.scalarProduct(objekt2.convertToHessianNormalForm().normVec)) / (
                    objekt1.dirVec.length())
            ))
        elif type(objekt1) == Plane and type(objekt2) == Line:
            winkel = math.degrees(math.asin(
                abs(objekt2.dirVec.scalarProduct(objekt1.convertToHessianNormalForm().normVec)) / (
                    objekt2.dirVec.length())
            ))
        elif type(objekt1) == Plane and type(objekt2) == Plane:
            winkel = math.degrees(math.acos(
                abs(objekt1.convertToHessianNormalForm().normVec.scalarProduct(
                    objekt2.convertToHessianNormalForm().normVec))
                ))
        else:
            print("We cannot calculate this Angle.")
        return winkel

    @classmethod
    def distancePointPoint(self, point:Point, point1:Point):
        Vec = Vector3D(point.getX()-point1.getX(),point.getY()-point1.getY(),point.getZ()-point1.getZ())
        distance = abs(Vec.length())
        return distance

    @classmethod
    def distanceLineLine(self, line1:Line,line2:Line):
        if Solvers.checkLinearAbhaengig(line1.getDirectionVector(),line2.getDirectionVector()) == True:
            if Solvers.checkPointInLine(line1,line2.getPositionVector()) ==True:
                print("Identisch")
            else:
                distance = Solvers.distancePointLine(line2.getPositionVector(),line1)
        elif Solvers.schnittpunkt(line1,line2) is not None:
            distance = 0
        else:
            normVec = line1.getDirectionVector().vectorProduct(line2.getDirectionVector())
            scalarParam = normVec.scalarProduct(line1.getPositionVector())
            helpPlane = Plane.coordinateForm(normVec,scalarParam)
            distance = Solvers.distancePlanePoint(line2.getPositionVector(),helpPlane)
        return distance


    @classmethod
    def distancePlanePoint(self, point:Point, plane:Plane):
        if Solvers.checkPointInPlane(plane,point) == False:
            if plane.getType() == "coordinate":
                hess = plane.convertToHessianNormalForm()
                normVec = hess.getNormalVector()
                scalarParam = hess.getScalarParameter()
                distance = normVec.getX()*point.getX()+normVec.getY()*point.getY()+normVec.getZ()*point.getZ()-scalarParam
            else:
                hess = plane.convertToHessianNormalForm()
                pointVec = Vector3D(point.getX(),point.getY(),point.getZ())
                subtract = pointVec.subtract(hess.getPositionVector())
                distance = subtract.scalarProduct(hess.getNormalVector())
                distance = abs(distance)
        else:
            distance = 0
        return distance

    @classmethod
    def distanceLinePlane(self, line:Line, plane:Plane):
        if plane.getType() == "normal" or plane.getType() == "coordinate":
            normVec = plane.getNormalVector()
            if normVec.scalarProduct(line.getDirectionVector()) == 0:
                distance = Solvers.distancePlanePoint(line.getPositionVector(), plane)
            else: 
                distance = 0
            return distance
        else: 
            normVec = plane.getDirectionVectorOne().vectorProduct(plane.getDirectionVectorTwo())
            if normVec.scalarProduct(line.getDirectionVector()) == 0:
                distance = Solvers.distancePlanePoint(line.getPositionVector(), plane)
            else:     
                distance = 0
            return distance

    @classmethod
    def distancePointLine(self, point:Point, line:Line):
        helpPlane = Plane.normalForm(Vector3D(point.getX(),point.getY(),point.getZ()),line.getDirectionVector())
        pointSchnitt = Solvers.solveForPointPlane(line,helpPlane)
        schnittPoint = Point(pointSchnitt.getX(),pointSchnitt.getY(),pointSchnitt.getZ())
        distance = Solvers.distancePointPoint(schnittPoint,point)
        return distance

    @classmethod
    def distancePlanePlane(cls, plane1:Plane, plane2:Plane):
        pass
