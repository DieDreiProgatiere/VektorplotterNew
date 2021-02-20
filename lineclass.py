import math
from typing import Any
from listclass import ObjectLists
from vector3Dclass import Vector3D as Vector3D

class Line:
    __idTag = "lin"
    __idCount = 0


    def __init__(self, positionVector :Vector3D, directionVector :Vector3D, name :str = "", color :tuple = (0, 0, 0)):
        """The init method of the line class. Takes positionVector and directionVector as Vector3D, parameter as int or float, name as string and color as tuple of format: (Red, Green, Blue)(Valuerange = 0 to 256)."""
        self.__positionVector = positionVector
        self.__directionVector = directionVector
        self.__name = name
        self.__color = color
        self.__idCount += 1
        self.__id = str(self.__idTag) + str(self.__idCount)

        ObjectLists.appendObjDict({str(self.__id): str(self)})
        ObjectLists.appendLinList(str(self))


    def getPositionVector(self):
        """The get method for the positionVector. Returns the positionVector as type Vector3D."""
        return self.__positionVector


    def getDirectionVector(self):
        """The get method for the driectionVector. Returns the directionVector as type Vector3D."""
        return self.__directionVector


    def getName(self):
        """The get method for the name. Returns name as a string."""
        return str(self.__name)


    def getID(self):
        """The get method for the ID. Returns ID as string."""
        return str(self.__id)


    def getColor(self):
        """The get method for the color. Returns color as tuple of format: (Red, Green, Blue). Valuerange = 0 to 256"""
        return self.__color


    def setPositionVector(self, posVector):
        """The set method for the positionVector. Takes the positionVector as type Vector3D."""
        self.__positionVector = posVector


    def setPositionVectorX(self, x):
        """The set method for the x component of the positionVector. Takes the x component of the positionVector as float."""
        self.__positionVector.setX(x)


    def setPositionVectorY(self, y):
        """The set method for the y component of the positionVector. Takes the y component of the positionVector as float."""
        self.__positionVector.setY(float(y))


    def setPositionVectorZ(self, z):
        """The set method for the z component of the positionVector. Takes the z component of the positionVector as float."""
        self.__positionVector.setZ(z)


    def setDirectionVector(self, dirVector):
        """The set method for the driectionVector. Takes the directionVector as type Vector3D."""
        self.__directionVector = dirVector

    
    def setDirectionVectorX(self, x):
        """The set method for the x component of the directionVector. Takes the x component of the directionVector as float."""
        self.__directionVector.setX(x)


    def setDirectionVectorY(self, y):
        """The set method for the y component of the directionVector. Takes the y component of the directionVector as float."""
        self.__directionVector.setY(y)


    def setDirectionVectorZ(self, z):
        """The set method for the z component of the directionVector. Takes the z component of the directionVector as float."""
        self.__directionVector.setZ(z)


    def setName(self, name):
        """The set method for the name. Takes name as a string."""
        self.__name = str(name)


    def setColor(self, color):
        """The set method for the color. Takes color as tuple of format: (Red, Green, Blue). Valuerange = 0 to 256"""
        self.__color = color


    def normalizeDirectionVector(self):
        """Not yet implemented. Should make the length of the direction vector equal to 1, by dividing the vector with its length. (Einheitsnormalvektor)"""
        pass


    def __str__(self):
        """Str method. Using given line instance, returns string."""
        return str(self.__id)+": x = "+ str(self.__positionVector)+" + r * "+str(self.__directionVector)

    posVec = property(getPositionVector, setPositionVector)

    dirVec = property(getDirectionVector, setDirectionVector)

    name = property(getName, setName)

