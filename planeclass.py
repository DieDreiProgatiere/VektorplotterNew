
from typing import Any
from math import sqrt
from listclass import ObjectLists
from vector3Dclass import Vector3D as Vector3D
from nameAssignclass import NameAssign
from colorAssignclass import ColorAssign
import numpy as np

class Plane:
    __idTag = "pla"
    __idCount = 0
    __typeOfPlane = None

    @classmethod
    def parameterForm(cls,
                      positionVector: Vector3D,
                      directionVectorOne: Vector3D,
                      directionVectorTwo: Vector3D,
                      name=None,
                      color=None):
        """The classmethod for initializing a Plane in parameter Form.
           Takes positionVector and directionVectorOne and directionVectorTwo as Vector3D, parameter as int or float,
           name as string and color as tuple of format: (Red, Green, Blue)(Valuerange = 0 to 256)."""
        plane = cls(positionVector, directionVectorOne, directionVectorTwo, None, None, name, color)
        cls.__typeOfPlane = "parameter"
        return plane

    @classmethod
    def normalForm(cls,
                   positionVector: Vector3D,
                   normalVector: Vector3D,
                   name=None,
                   color=None):
        """The classmethod for intializing a Plane in normal Form.
           Takes positionVector and normalVector as Vector3D, name as string and color as tuple of format:
           (Red, Green, Blue)(Valuerange = 0 to 256)."""
        plane = cls(positionVector, None, None, normalVector, None, name, color)
        cls.__typeOfPlane = "normal"
        return plane

    @classmethod
    def coordinateForm(cls,
                       normalVector :Vector3D,
                       scalarParameter :float,
                       name=None,
                       color=None):
        """The classmethod for initializing a Plane in coordinate Form.
           Takes a, b, c, d as float, name as string and color as tuple of format:
           (Red, Green, Blue)(Valuerange = 0 to 256).
           For a equation of the form: ax + by + cz = d."""
        plane = cls(None, None, None, normalVector, scalarParameter, name, color)
        cls.__typeOfPlane = "coordinate"
        return plane

    def __init__(self,
                 positionVector: Vector3D,
                 directionVectorOne: Vector3D,
                 directionVectorTwo: Vector3D,
                 normalVector: Vector3D,
                 scalarParameter: float,
                 name=None,
                 color=None):
        """The init method of the plane class.
           Takes positionVector and directionVectorOne and directionVectorTwo as Vector3D, parameter as int or float,
           name as string and color as tuple of format: (Red, Green, Blue)(Valuerange = 0 to 256)."""
        self.__positionVector = positionVector
        self.__directionVectorOne = directionVectorOne
        self.__directionVectorTwo = directionVectorTwo
        self.__normalVector = normalVector
        # Following code checks if a normalVector was passed. If not: generates normalVector from directionVectors.

        try:
            self.__scalarParameter = scalarParameter
        except Exception:
            pass

        if name is None:
            self.__name = NameAssign.getNewName()
        else:
            self.__name = name
        if color is None:
            self.__color = ColorAssign.getNewColor()
        else:
            self.__color = color
        Plane.__idCount += 1
        self.__id = str(self.__idTag) + str(self.__idCount)

        ObjectLists.appendObjDict({str(self.__id): self})
        ObjectLists.appendPlaList(self)

    def __del__(self):
        ColorAssign.removeColor(self.__color)
        NameAssign.removeName(self.__name)
        try:
            ObjectLists.removeFromPlaList(self)
            ObjectLists.removeFromObjDict(str(self.__id))
        except ValueError:
            pass

    def getPositionVector(self):
        """The get method for the positionVector. Returns the positionVector as type Vector3D."""
        return self.__positionVector

    def getDirectionVectorOne(self):
        """The get method for the driectionVectorOne. Returns the directionVectorOne as type Vector3D."""
        return self.__directionVectorOne

    def getDirectionVectorTwo(self):
        """The get method for the driectionVectorTwo. Returns the directionVectorTwo as type Vector3D."""
        return self.__directionVectorTwo

    def getNormalVector(self):
        """The get method for the normalVector. Returns normalVector as Vector3D."""
        return self.__normalVector

    def getScalarParameter(self):
        """The get method for the scalarParameter. Returns scalarParameter as float."""
        return float(self.__scalarParameter)

    def getName(self):
        """The get method for the name. Returns name as a string."""
        return str(self.__name)

    def getID(self):
        """The get method for the ID. Returns ID as string."""
        return str(self.__id)

    def getColor(self):
        """The get method for the color. Returns color as tuple of format: (Red, Green, Blue). Valuerange = 0 to 256"""
        return self.__color

    def getType(self):
        """The get method for the Type. Returns the type as a string."""
        return self.__typeOfPlane

    def setPositionVector(self,
                          posVector):
        """The set method for the positionVector. Takes the positionVector as type Vector3D."""
        self.__positionVector = posVector

    def setDirectionVectorOne(self,
                              directionVectorOne):
        """The set method for the driectionVectorOne. Takes the directionVectorOne as type Vector3D."""
        self.__directionVectorOne = directionVectorOne

    def setDirectionVectorTwo(self,
                              directionVectorTwo):
        """The set method for the driectionVectorTwo. Takes the directionVectorTwo as type Vector3D."""
        self.__directionVectorTwo = directionVectorTwo

    def setNormalVector(self,
                        normalVector):
        """The set method for the normalVector. Takes normalVector as type Vector3D."""
        self.__normalVector = normalVector

    def setScalarParameter(self,
                           scalarParameter):
        """The set method for the scalarParameter. Takes scalarParameter as int or float."""
        self.__scalarParameter = float(scalarParameter)

    def setName(self,
                name):
        """The set method for the name. Takes name as a string."""
        self.__name = str(name)


    def setColor(self,
                 color):
        """The set method for the color. Takes color as tuple of format: (Red, Green, Blue). Valuerange = 0 to 256"""
        self.__color = color
    
    

    def convertToHessianNormalForm(self):
        """Converts the given Instance to Hessian Normal Form.
        The Normal Vector is transformed into a Normal Vector of length 1."""
        if self.__typeOfPlane == "parameter":
            posVec = self.__positionVector
            normVec = self.getDirectionVectorOne().vectorProduct(self.getDirectionVectorTwo())
            nameVec = self.__name
            hess = Plane.normalForm(posVec, normVec, nameVec)
            hess.setNormalVector(normVec.scalarDivision(normVec.length()))
            self.__typeOfPlane = "normal"
        elif self.__typeOfPlane == "coordinate":
            normVec = self.getNormalVector().scalarDivision(self.__normalVector.length())
            scalParam = self.getScalarParameter()/self.getNormalVector().length()
            hess = Plane.coordinateForm(normVec,scalParam)
        elif self.__typeOfPlane == "normal":
            normVec = self.getNormalVector().scalarDivision(self.getNormalVector().length())
            hess = Plane.normalForm(self.getPositionVector(),normVec)
        return hess  

    def __str__(self):
        if self.__typeOfPlane == "normal":
            return str(self.__id)+": (x - "+ str(self.__positionVector)+" + ) * "+str(self.__normalVector)+" = 0"
        elif self.__typeOfPlane == "parameter":
            return str(self.__id)+": x = "+str(self.__positionVector)+" + r * "+str(self.__directionVectorOne)+" + s * "+str(self.__directionVectorTwo)
        elif self.__typeOfPlane == "coordinate":
            return str(self.__id)+": "+str(self.__normalVector.getX())+"x + "+str(self.__normalVector.getY())+"y + "+str(self.__normalVector.getZ())+"z = "+str(self.__scalarParameter)
        else:
            return "No valid plane!"

    posVec = property(getPositionVector, setPositionVector)

    normVec = property(getNormalVector, setNormalVector)

    dirVecOne = property(getDirectionVectorOne, setDirectionVectorOne)

    dirVecTwo = property(getDirectionVectorTwo, setDirectionVectorTwo)

    scalParam = property(getScalarParameter, setScalarParameter)

    name = property(getName, setName)
