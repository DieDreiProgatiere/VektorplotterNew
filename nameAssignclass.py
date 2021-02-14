class NameAssign():
    __alphabet = (#letters used in the composition of new names
        "a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z"
        )
    __protectedNames = ["x","y","z"]#names that should not be assigned
    __nameList = []
    __userAssignedNames = []
    __freeNames = []
    __reuseRemovedNames = True#Standard: True
    __autoAssignedNameCount = 0
    
    def __init__(self):
        """placeholder, not nescessary"""
        pass
    
    def getNewName(self):
        """returns a new, not-yet-used or protected name"""
        newName = ""
        if self.__reuseRemovedNames and len(self.__freeNames) != 0:
            newName = self.__freeNames.pop()
        else:
            foundValidName = False
            while not foundValidName:
                if self.__autoAssignedNameCount >= len(self.__alphabet):
                    newName = self.__alphabet[(self.__autoAssignedNameCount//len(self.__alphabet))-1]+self.__alphabet[self.__autoAssignedNameCount%len(self.__alphabet)]
                else:
                    newName = self.__alphabet[self.__autoAssignedNameCount]
                if not newName in self.__protectedNames and not newName in self.__nameList:
                    foundValidName = True
                self.__autoAssignedNameCount += 1
        self.__nameList.append(newName)
        return newName
        
    def changeName(self,objekt,desiredName):
        """Funktion to change name of an objekt. Takes desiredName as string.
           The objekt passed needs a setName(self,name) and getName(self) method"""
        oldName = objekt.getName()
        objekt.setName(desiredName)
        self.removeName(oldName)
        self.__nameList.append(desiredName)
        self.__userAssignedNames.append(desiredName)
    
    def protectName(self,nameToProtect):
        """Deprotects a name given as string.
           Has no effect on existing Names."""
        self.__protectedNames.append(nameToProtect)
    
    def deprotectName(self,nameToDeprotect):
        """Protects a name given as string.
           Has no effect on existing Names."""
        if name in self.__protectedNames:#check if name is even in list
            self.__protectedNames.remove(name)
    
    def removeName(self,name):
        """Removes given name from self.__nameList.
           Takes name as string."""
        if name in self.__nameList:#check if name is even in list
            self.__nameList.remove(name)
            self.__freeNames.append(name)
        if name in self.__userAssignedNames:#check if name is even in list
            self.__userAssignedNames.remove(name)
            
    def addUserAssignedName(self,name):
        """Adds a name (string) to __userAssignedNames and __nameList.
           Doesn't give any objekt this name."""
        self.__userAssignedNames.append(name)
        self.__nameList.append(name)
