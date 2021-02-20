

class ObjectLists:

    __objDict = {}
    __vecList = []
    __poiList = []
    __linList = []
    __plaList = []

    def __init__(self) -> None:
        pass

    @classmethod
    def getObjDict(self):
        return self.__objDict

    @classmethod
    def getVecList(self):
        return self.__vecList

    @classmethod
    def getPoiList(self):
        return self.__poiList

    @classmethod
    def getLinList(self):
        return self.__linList

    @classmethod
    def getPlaList(self):
        return self.__plaList

    @classmethod
    def getObjDictLen(self):
        return len(self.__objDict)

    @classmethod
    def getVecListLen(self):
        return len(self.__vecList)

    @classmethod
    def getPoiListLen(self):
        return len(self.__poiList)

    @classmethod
    def getLinListLen(self):
        return len(self.__linList)

    @classmethod
    def getPlaListLen(self):
        return len(self.__plaList)

    @classmethod
    def appendObjDict(self, x):
        self.__objDict.update(x)

    @classmethod
    def appendVecList(self, x):
        self.__vecList.append(x)

    @classmethod
    def appendPoiList(self, x):
        self.__poiList.append(x)

    @classmethod
    def appendLinList(self, x):
        self.__linList.append(x)

    @classmethod
    def appendPlaList(self, x):
        self.__plaList.append(x)

    @classmethod
    def removeFromObjDict(self, x):
        self.__objDict.pop(x)

    @classmethod
    def removeFromVecList(self, x):
        self.__vecList.remove(x)

    @classmethod
    def removeFromPoiList(self, x):
        self.__poiList.remove(x)

    @classmethod
    def removeFromLinList(self, x):
        self.__linList.remove(x)

    @classmethod
    def removeFromPlaList(self, x):
        self.__plaList.remove(x)


