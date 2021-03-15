import math
from listclass import ObjectLists
from nameAssignclass import NameAssign
from colorAssignclass import ColorAssign


class Vector3D:
    __idTag = "vec"
    __idCount = 0

    def __init__(self,
                 x=0.0,
                 y=0.0,
                 z=0.0,
                 name=None,
                 color=None,
                 show=True,
                 append=False
                 ):
        """The init function for the Vector3D class.
        Takes x, y and z values as int or float.
        Name has to be a string."""
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.show = show
        if name is None:
            self.__name = NameAssign.getNewName()
        else:
            self.__name = name
        if color is None:
            self.__color = ColorAssign.getNewColor()
        else:
            self.__color = color
        Vector3D.__idCount += 1
        self.__id = str(self.__idTag+str(self.__idCount))
        if append:
            ObjectLists.appendObjDict({str(self.__id) : self})
            ObjectLists.appendVecList(self)


    def __del__(self):
        ColorAssign.removeColor(self.__color)
        NameAssign.removeName(self.__name)
        try:
            ObjectLists.removeFromVecList(self)
            ObjectLists.removeFromObjDict(str(self.__id))
        except ValueError:
            pass

    def getX(self):
        """The get method for the x-komponent.
        Returns x as float."""
        return float(self.__x)

    def getY(self):
        """The get method for the y-komponent.
        Returns y as float."""
        return float(self.__y)

    def getZ(self):
        """The get method for the z-komponent.
        Returns z as float."""
        return float(self.__z)

    def getName(self):
        """The get method for the name.
        Returns name as string."""
        return str(self.__name)

    def getID(self):
        """The get method for the ID.
        Returns ID as string."""
        return str(self.__id)

    def getColor(self):
        """The get method for the color.
        Returns color as tuple of format:
        (Red, Green, Blue).
        Valuerange = 0 to 256"""
        return self.__color

    def setX(self, x=0):
        """The set method for the x-komponent.
        Takes x as float."""
        self.__x = float(x)

    def setY(self, y=0):
        """The set method for the y-komponent.
        Takes y as float."""
        self.__y = float(y)

    def setZ(self, z=0):
        """The set method for the z-komponent.
        Takes z as float."""
        self.__z = float(z)

    def setName(self, name):
        """The set method for the name.
        Takes name as string."""
        self.__name = str(name)

    def setColor(self, color):
        """The set method for the colour.
        Takes colour as tuple of format:
        (Red, Green, Blue).
        Valuerange = 0 to 256"""
        self.__color = color

    def add(self, other):
        """Returns the added vector of two given Vector3D instances
        as a new Vector3D instance."""
        return Vector3D(self.__x+other.__x,
                        self.__y+other.__y,
                        self.__z+other.__z)

    def subtract(self, other):
        """Returns the subtracted vector of two given Vector3D instances as
        a new Vector3D instance."""
        return Vector3D(self.__x-other.__x,
                        self.__y-other.__y,
                        self.__z-other.__z)

    def scalarProduct(self, other):
        """Returns the scalar product (defined as: length(a)*length(a)*cos(a,b))
        of two given Vector3D instances as a scalar (float)."""
        return float(self.__x*other.__x+self.__y*other.__y+self.__z*other.__z)

    def square(self):
        """Returns the scalar Product of a Vector3D with itself."""
        return self.scalarProduct(self)

    def scalarMultiplication(self, scalar):
        """Scalar multiplication (elongation by scalar) of
        a given Vector3D instance and a scalar (int or float).
        Returns new Vector3D instance."""
        scalar = float(scalar)
        return Vector3D(self.__x*scalar,
                        self.__y*scalar,
                        self.__z*scalar)

    def scalarDivision(self, scalar):
        """Returns the scalar devision (shortening by scalar) of
        a given Vector3D instance and a scalar (int or float).
        Returns new Vector3D instance."""
        scalar = float(scalar)
        scalar = 1/scalar
        return Vector3D(self.__x*scalar,
                        self.__y*scalar,
                        self.__z*scalar)

    def vectorProduct(self, other):
        """Returns the vector product of two given Vector3D instances
        as a new Vector3D instance."""
        x = ((self.__y * other.__z) - (self.__z * other.__y))
        y = ((self.__z * other.__x) - (self.__x * other.__z))
        z = ((self.__x * other.__y) - (self.__y * other.__x))
        return Vector3D(x, y, z)

    def length(self):
        """Returns the lenght of the given Vector3D instance."""
        return math.sqrt(self.__x**2+self.__y**2+self.__z**2)

    def __str__(self):
        """Str method for testing purposes.
        Uses given Vector3D instance, returns string."""
        return "("+str(self.__x)+"; "+str(self.__y)+"; "+str(self.__z)+")"

    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)
    name = property(getName, setName)
