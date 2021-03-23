import math
import random
# import matplotlib.pyplot as plt  # Needed only for displaying of colors using included testing code


class ColorAssign:
    __colorList = []
    __maxValues = (255, 255, 255)
    __minValues = (0, 0, 0)
    __protectionEnvironment = 50
    __illegalColors = [(0, 0, 0), (255, 255, 255)]

    def __init__(self):
        """placeholder; not necessary"""
        pass

    @classmethod
    def getNewColor(self):
        """returns a new, not-yet-used color"""
        foundValidSeed = False
        newSeed = None
        newColor = None
        while not foundValidSeed:  # Searching for valid seed
            newSeed = (random.randrange(self.__minValues[0],self.__maxValues[0]+1),
                       random.randrange(self.__minValues[1],self.__maxValues[1]+1),
                       random.randrange(self.__minValues[2],self.__maxValues[2]+1)
                       )
            if len(self.__colorList+self.__illegalColors) == 0:  # if: no illegal colors or normal colors
                foundValidSeed = True  # every seed is valid
                newColor = newSeed  # no other colors, so no distance optimasation nescessary
            elif self.evaluateColor(newSeed) != 0:  # if: seed is valid
                foundValidSeed = True
                newColor = self.discreteSpaceHillClimbing(newSeed)  # optimisation: maximising distance to other colors
        self.__colorList.append(newColor)
        return newColor

    @classmethod
    def changeColor(self,
                    objekt,
                    desiredColor):
        """Function to change color of an objekt. Takes desiredColor as tuple of ints: (r,g,b).
           The objekt passed needs a setColor(self,color) and getColor(self) method"""
        oldColor = objekt.getColor()
        objekt.setColor(desiredColor)
        self.removeColor(oldColor)
        self.__colorList.append(desiredColor)

    @classmethod
    def removeColor(self,
                    color):
        """Removes given color from self.__colorList.
           Takes color as tuple of ints: (r,g,b)."""
        if color in self.__colorList:  # check if color is even in list
            self.__colorList.remove(color)

    @classmethod
    def colorDistance(self,
                      color1,
                      color2):
        """Returns the pythagorian distance between 2 colors in 3D R,G,B space as Float.
           Colors are taken as tuples of 3 ints: (r,g,b)
           Uses pythagorian distance in 3dimensions (r,g,b)"""
        return math.sqrt((color1[0]-color2[0])**2+(color1[1]-color2[1])**2+(color1[2]-color2[2])**2)

    @classmethod
    def evaluateColor(self,
                      color):
        """Function used to evaluate a color based on distances to other colors.
           Takes color as tuple of three ints: (r,g,b)"""
        evaluationOutput = 0
        illegal = False
        for illegalColor in self.__illegalColors:
            if self.colorDistance(color, illegalColor) <= self.__protectionEnvironment:
                illegal = True  # enforce reqired minimum distance to illegalColors
        if not illegal:
            evaluationOutput = 200
            for col in self.__illegalColors+self.__colorList:
                evaluationOutput -= 1/self.colorDistance(color,col)**2
        return (1/len(self.__illegalColors+self.__colorList))*evaluationOutput

    @classmethod
    def adjacentColors(self,
                       color):
        """Returns a list of the adjacent colors of a color.
           Takes color as tuble of ints: (r,g,b)."""
        step = 5  # Standard: 5 (increase for faster optimization; decrease for more exact optimization)
        listOfAdjacentColors = [
            (color[0]+step,color[1]-step,color[2]+step),  # Erst einmal nur die acht Ecken des "Würfels"
            (color[0]+step,color[1]+step,color[2]+step),  # um die eingegebene color.
            (color[0]-step,color[1]+step,color[2]+step),  # Mehr Positionen auf diesem "Würfel" wären möglich,
            (color[0]-step,color[1]-step,color[2]+step),  # verlangsamen aber das optimieren.
            (color[0]+step,color[1]-step,color[2]-step),
            (color[0]+step,color[1]+step,color[2]-step),
            (color[0]-step,color[1]+step,color[2]-step),
            (color[0]-step,color[1]-step,color[2]-step)
            ]
        for adjacentColor, index in zip(listOfAdjacentColors,range(0,9)):  # ersetzen aller Farben außerhalb boundaries
            if adjacentColor[0] >= self.__maxValues[0] or adjacentColor[1] >= self.__maxValues[1] or adjacentColor[2] >= self.__maxValues[2] or adjacentColor[0] <= self.__minValues[0] or adjacentColor[1] <= self.__minValues[1] or adjacentColor[2] <= self.__minValues[2]:
                listOfAdjacentColors[index] = color
        return listOfAdjacentColors

    @classmethod
    def discreteSpaceHillClimbing(self,
                                  startColor):
        """Does a Discrete Space Hill Climb Algorithm for Gradient Ascent.
           Finds a lokal maximum of evaluateColor Function, ascending from startColor.
           Takes startColor as tuple of ints: (r, g, b).
           View "https://en.wikipedia.org/wiki/Hill_climbing" for infos on Algorithm.
           The pseudocode found there on [11.02.2021] is the basis of this implementation."""
        currentColor = startColor
        topReached = False
        topColor = None
        while not topReached:
            # print(currentColor)#for testing purposes
            listOfAdjacentColors = self.adjacentColors(currentColor)
            nextEvaluation = 0
            nextColor = None
            for adjacentColor in listOfAdjacentColors:
                if (newEvaluation := self.evaluateColor(adjacentColor)) > nextEvaluation:
                    nextColor = adjacentColor
                    nextEvaluation = newEvaluation  # evaluateColor(adjacentColor)
            if nextEvaluation <= self.evaluateColor(currentColor):
                topReached = True
                topColor = currentColor
            currentColor = nextColor
        return topColor

    @classmethod
    def addColor(self,
                 color):
        """Adds given Color to __colorList.
           Takes color as tuple of ints: (r,g,b)."""
        self.__colorList.append(color)

    @classmethod
    def getColorList(self):
        """Returns a copy of the otherwise internal __colorList"""
        return list(self.__colorList)


# Some Test Code that executes if colorAssignclass.py is run instead of imported
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    colAss = ColorAssign()
#   colAss.addColor((255,0,0))  # ein paar farben vordefinieren um zu sehen wie gut optimiert wird
#   colAss.addColor((0,255,0))
#   colAss.addColor((0,0,255))
#   colAss.addColor((255,255,0))
#   colAss.addColor((0,255,255))
#   colAss.addColor((255,0,255))
#   colAss.addColor((0,0,0))
    count = 0
    count += len(colAss.getColorList())
    while True:
        count += 1
        print("NewColor = "+str(colAss.getNewColor()))
        x = input()
        if x == "p":
            plt.figure(figsize=(count,1))
            colorList = colAss.getColorList()
            for n in range(count):
                ax = plt.subplot(1,count,n+1)
                plt.imshow([[colorList[n]]]) #[[[colorList[n][0],colorList[n][0],[colorList[n][1],colorList[n][1]],[colorList[n][2],colorList[n][2]]]])
                plt.gray()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
            plt.show()
        elif x == "x":
            break