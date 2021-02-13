import math
import random
import matplotlib.pyplot as plt

class ColorAssign():
    __colorList = []
    __maxValues = (255,255,255)
    __minValues = (0,0,0)
    __protectionEnvironment = 50
    __illegalColors = [(0,0,0),(255,255,255)]
    
    def __init__(self):
        pass
    
    def getNewColor(self):
        """returns a new, not-yet-used color"""
        foundValidSeed = False
        newSeed = None
        while not foundValidSeed:
            print("Searching for valid seed")
            newSeed = (random.randrange(self.__minValues[0],self.__maxValues[0]+1),
                       random.randrange(self.__minValues[1],self.__maxValues[1]+1),
                       random.randrange(self.__minValues[2],self.__maxValues[2]+1)
                       )
            if len(self.__colorList+self.__illegalColors) == 0:
                foundValidSeed = True
                newColor = newSeed
            elif self.evaluateColor(newSeed) != 0:
                foundValidSeed = True
                newColor = self.discreteSpaceHillClimbing(newSeed)
        self.__colorList.append(newColor)
        return newColor
    
    def changeColor(self, objekt, desiredColor):
        pass
    
    def colorDistance(self,color1,color2):
        return math.sqrt((color1[0]-color2[0])**2+(color1[1]-color2[1])**2+(color1[2]-color2[2])**2)
    
    def evaluateColor(self,color):
        evaluationOutput = 0
        illegal = False
        for illegalColor in self.__illegalColors:
            if self.colorDistance(color,illegalColor) <= self.__protectionEnvironment:
                illegal = True
        if not illegal:
            evaluationOutput = 200
            for col in self.__illegalColors+self.__colorList:
                evaluationOutput -= 1/self.colorDistance(color,col)**2
        return (1/len(self.__illegalColors+self.__colorList))*evaluationOutput
    
    def adjacentColors(self,color):
        step = 5
        listOfAdjacentColors = [
            (color[0]+step,color[1]-step,color[2]+step),#Erst einmal nur die vier Ecken des "Würfels" um die eingegebene color
            (color[0]+step,color[1]+step,color[2]+step),
            (color[0]-step,color[1]+step,color[2]+step),
            (color[0]-step,color[1]-step,color[2]+step),
            (color[0]+step,color[1]-step,color[2]-step),
            (color[0]+step,color[1]+step,color[2]-step),
            (color[0]-step,color[1]+step,color[2]-step),
            (color[0]-step,color[1]-step,color[2]-step)
            ]
        for adjacentColor, index in zip(listOfAdjacentColors,range(0,9)):
            if adjacentColor[0]>=self.__maxValues[0] or adjacentColor[1]>=self.__maxValues[1] or adjacentColor[2]>=self.__maxValues[2] or adjacentColor[0]<=self.__minValues[0] or adjacentColor[1]<=self.__minValues[1] or adjacentColor[2]<=self.__minValues[2]:
                listOfAdjacentColors[index]=color
        return listOfAdjacentColors
    
    def discreteSpaceHillClimbing(self,startColor):#https://en.wikipedia.org/wiki/Hill_climbing
        currentColor = startColor
        topReached = False
        topColor = None
        while not topReached:
            #print(currentColor)#for testing purposes
            listOfAdjacentColors = self.adjacentColors(currentColor)
            nextEvaluation = 0
            nextColor = None
            for adjacentColor in listOfAdjacentColors:
                if (newEvaluation:=self.evaluateColor(adjacentColor)) > nextEvaluation:
                    nextColor = adjacentColor
                    nextEvaluation = newEvaluation#evaluateColor(adjacentColor)
            if nextEvaluation <= self.evaluateColor(currentColor):
                topReached = True
                topColor = currentColor
            currentColor = nextColor
        return topColor
    
    def addColor(self,color):
        self.__colorList.append(color)

    def getColorList(self):
        return self.__colorList
            
colAss = ColorAssign()
##colAss.addColor((255,0,0))
##colAss.addColor((0,255,0))
##colAss.addColor((0,0,255))
##colAss.addColor((255,255,0))
##colAss.addColor((0,255,255))
##colAss.addColor((255,0,255))
##colAss.addColor((0,0,0))
count = 0
while True:
    count += 1
    print("NewColor = "+str(colAss.getNewColor()))
    x = input()
    if x == "p":
        plt.figure(figsize=(count,1))
        colorList = colAss.getColorList()
        for n in range(count):
          ax = plt.subplot(1,count,n+1)
          plt.imshow([[colorList[n]]])#[[[colorList[n][0],colorList[n][0],[colorList[n][1],colorList[n][1]],[colorList[n][2],colorList[n][2]]]])
          plt.gray()
          ax.get_xaxis().set_visible(False)
          ax.get_yaxis().set_visible(False)
        plt.show()
