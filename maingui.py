from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QLabel, QMainWindow, QPushButton, QScrollArea, QSizePolicy, QWidget, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
import plotly
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from listclass import ObjectLists
from vector3Dclass import Vector3D
from pointclass import Point
from lineclass import Line
from planeclass import Plane
from nameAssignclass import NameAssign
from colorAssignclass import ColorAssign


x = Vector3D(3, 4, 5)
y = Plane.normalForm(Vector3D(1, 1, 1), Vector3D(2, 2, 2))
z = Plane.parameterForm(Vector3D(3, 4, 5), Vector3D(2, 2, 2), Vector3D(2, 2, 2))
u = Plane.parameterForm(Vector3D(2, 5, 5), Vector3D(1, 4, 2), Vector3D(2, 6, 7))
v = Plane.coordinateForm(Vector3D(3, 2, 1), 2)

class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.title = "Vektorplotter"
        self.setWindowTitle(self.title)
        self.x = 200
        self.y = 100
        self.width = 1000
        self.height = 700
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout()
        self.mainLayout.setColumnStretch(1, 2)
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)
        self.main()

    def main(self):
        ###Testing Purposes
        d = {'x': [0, 1], 'y': [0, 1], 'z': [0, 2]}
        df = pd.DataFrame(data=d)
        lin = px.line_3d(df, x="x", y="y", z="z")
        lin.add_surface(z=np.array([[1,1,1],[1,1,1],[1,1,1]]))
        ###Testing Purposes over
        self.makeWebEngineView(lin)
        self.makeMenuView()
        self.makeListView()
        self.makeNewObjectView()


    def makeWebEngineView(self, fig):
        self.webBox = QWidget()
        self.webBoxLayout = QHBoxLayout()
        self.webBox.setMinimumSize(500, 500)
        self.webBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.webBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.html = '<html><body>'
        self.html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        self.html += '</body></html>'

        self.plot_widget = QWebEngineView()
        self.plot_widget.setHtml(self.html)
        self.webBoxLayout.addWidget(self.plot_widget)

        self.webBox.setLayout(self.webBoxLayout)
        self.mainLayout.addWidget(self.webBox, 1, 1, 2, 1)

    def makeListView(self):
        self.listBox = QWidget()
        self.listBoxLayout = QGridLayout()
        self.listBoxLayout.setSpacing(10)
        self.listBox.setMaximumWidth(450)
        self.listBox.setMinimumWidth(450)
        self.listBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.listBoxLayout.setContentsMargins(0, 10, 0, 0)

        self.listScroll = QScrollArea()
        self.listScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listScroll.setWidgetResizable(True)
        self.listScroll.setMaximumWidth(450)
        self.listScroll.setMinimumWidth(450)
        self.listScroll.setWidget(self.listBox)

        self.listLabel = QLabel(self.listBox)
        self.listLabel.setText("List:")
        self.listLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.listBoxLayout.addWidget(self.listLabel, 0, 0, Qt.AlignmentFlag.AlignTop)

        for element, index in zip(ObjectLists.getObjDict(), range(ObjectLists.getObjDictLen())):
            self.objButton = QPushButton(self.listBox)
            self.objButton.setText(str(element) + ": " + str(ObjectLists.getObjDict()[element]))
            self.objButton.adjustSize()
            self.objButton.clicked.connect(lambda: self.highlightObject(element, index))
            self.objButton.move(0, 25 + index * 25)
            self.objButton.setMinimumSize(QSize(50, 50))
            self.objButton.setMaximumWidth(500)
            self.listBoxLayout.addWidget(self.objButton, index + 1, 0, Qt.AlignmentFlag.AlignTop)

        self.listBox.setLayout(self.listBoxLayout)
        self.mainLayout.addWidget(self.listScroll, 1, 0)

    def makeMenuView(self):
        self.menuBox = QWidget()
        self.menuBoxLayout = QHBoxLayout()
        self.menuBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.menuBoxLayout.setSpacing(10)

        self.homeButton = QPushButton()
        self.homeButton.setText("Home")
        self.homeButton.setMaximumSize(75, 30)
        self.homeButton.setMinimumSize(75, 30)
        self.homeButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.homeButton.clicked.connect(lambda: self.home()) # home is Placeholder, lambda for future args
        self.menuBoxLayout.addWidget(self.homeButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.otherButton = QPushButton()
        self.otherButton.setText("Test")
        self.otherButton.setMaximumSize(75, 30)
        self.otherButton.setMinimumSize(75, 30)
        self.otherButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.otherButton.clicked.connect(lambda: self.home()) # home is Placeholder, lambda for future args
        self.menuBoxLayout.addWidget(self.otherButton, 1, Qt.AlignmentFlag.AlignLeft)

        self.menuBox.setLayout(self.menuBoxLayout)
        self.mainLayout.addWidget(self.menuBox, 0, 0)

    
    def makeNewObjectView(self):
        self.newBox = QWidget()
        self.newBox.setMaximumSize(450, 50)
        self.newBox.setMinimumSize(450, 50)
        self.newBoxLayout = QHBoxLayout()
        self.newBoxLayout.setContentsMargins(0, 0, 0, 10)

        self.newObjectButton = QPushButton()
        self.newObjectButton.setText("Neues Objekt")
        self.newObjectButton.setMaximumSize(220, 50)
        self.newObjectButton.setMinimumSize(220, 50)
        self.newObjectButton.clicked.connect(lambda: self.newObjectButtonClicked())
        self.newBoxLayout.addWidget(self.newObjectButton)
        
        self.newCalcButton = QPushButton()
        self.newCalcButton.setText("Neue Rechnung")
        self.newCalcButton.setMaximumSize(225, 50)
        self.newCalcButton.setMinimumSize(225, 50)
        self.newCalcButton.clicked.connect(lambda: self.newCalcButtonClicked())
        self.newBoxLayout.addWidget(self.newCalcButton)

        self.newBox.setLayout(self.newBoxLayout)
        self.mainLayout.addWidget(self.newBox, 2, 0)


    def highlightObject(self, element, index):
        print(str(element) + "with index" + str(index) + "was clicked")
        # Does not work yet, always printing last element in list 

    def home(self):
        pass #Placeholder

    def newObjectButtonClicked(self):
        # this method is called, if the newObjectButton is clicked
        self.showingNewObjectInputLine = False
        if not(self.showingNewObjectInputLine):
            self.showingNewObjectInputLine = True

            self.newObjectInputLine = QLineEdit()
            self.newObjectInputLine.setFrame(True)
            self.listBoxLayout.addWidget(self.newObjectInputLine)
            self.listBoxLayout.update()
            self.newObjectInputLine.returnPressed.connect(lambda: self.newObjectInput())
        else:
            pass

    def newCalcButtonClicked(self):
        # this method is called, if the newCalcButton is clicked
        self.showingNewCalcInputLine = False
        if not(self.showingNewCalcInputLine):
            self.showingNewCalcInputLine = True

            self.newCalcInputLine = QLineEdit()
            self.newCalcInputLine.setFrame(True)
            self.listBoxLayout.addWidget(self.newCalcInputLine)
            self.listBoxLayout.update()
            self.newCalcInputLine.returnPressed.connect(lambda: self.newCalcInput())
        else:
            pass

    def newObjectInput(self):
        # this method is called if the return key is pressed in the newObjectButtonClicked method
        self.showingNewObjectInputLine = False
        self.newObjectInputLineText = self.newObjectInputLine.text()
        self.listBoxLayout.removeWidget(self.newObjectInputLine)
        self.listBoxLayout.update()

        return self.newObjectInputLineText
        # Has to execute with exec or call another function to add self.newObjectInputLineText (which is the new object) to the ObjDict and ...List
        

    def newCalcInput(self):
        # this method is called, if the return key is pressed in the newCalcButtonClicked method
        self.showingNewCalcInputLine = False
        self.newCalcInputLineText = self.newCalcInputLine.text()
        self.listBoxLayout.removeWidget(self.newCalcInputLine)
        self.listBoxLayout.update()

        return self.newCalcInputLineText
        # Has to be passed to another function, which handles Calculation Input....or handeld in this method 


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
