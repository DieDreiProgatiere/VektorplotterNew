

class Lists:

    __objDict = {}
    __vecList = []
    __poiList = []
    __linList = []
    __plaList = []

    def __init__(self) -> None:
        pass

    def getObjDict(self):
        return self.__objDict

    def getVecList(self):
        return self.__vecList

    def getPoiList(self):
        return self.__poiList

    def getLinList(self):
        return self.__linList

    def getPlaList(self):
        return self.__plaList

    def getObjDictLen(self):
        return len(self.__objDict)

    def getVecListLen(self):
        return len(self.__vecList)

    def getPoiListLen(self):
        return len(self.__poiList)

    def getLinListLen(self):
        return len(self.__linList)

    def getPlaListLen(self):
        return len(self.__plaList)

    def appendObjDict(self, x):
        self.__objDict.update(x)

    def appendVecList(self, x):
        self.__vecList.append(x)

    def appendPoiList(self, x):
        self.__poiList.append(x)

    def appendLinList(self, x):
        self.__linList.append(x)

    def appendPlaList(self, x):
        self.__plaList.append(x)


ObjectLists = Lists()