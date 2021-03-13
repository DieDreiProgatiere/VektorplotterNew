from PyQt5.QtWidgets import QApplication, QButtonGroup, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QPushButton, QScrollArea, QSizePolicy, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys
import plotly
import plotly.express as px
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


    def makeWebEngineView(self, fig):
        self.webBox = QWidget()
        self.webBoxLayout = QHBoxLayout()
        self.html = '<html><body>'
        self.html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        self.html += '</body></html>'

        self.plot_widget = QWebEngineView()
        self.plot_widget.setHtml(self.html)
        self.webBoxLayout.addWidget(self.plot_widget)

        self.webBox.setLayout(self.webBoxLayout)
        self.mainLayout.addWidget(self.webBox, 1, 1)

    def makeListView(self):
        self.listBox = QWidget()
        self.listBoxLayout = QGridLayout()
        self.listBox.setMaximumHeight(700)
        self.listBox.setMaximumWidth(500)
        self.listBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.listScroll = QScrollArea()
        self.listScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listScroll.setWidgetResizable(True)
        self.listScroll.setMaximumWidth(500)
        self.listScroll.setWidget(self.listBox)

        self.listLabel = QLabel(self.listBox)
        self.listLabel.setText("List:")
        self.listBoxLayout.addWidget(self.listLabel, 0, 0)
        for element, index in zip(ObjectLists.getObjDict(), range(ObjectLists.getObjDictLen())):
            self.objButton = QPushButton(self.listBox)
            self.objButton.setText(str(element) + ": " + str(ObjectLists.getObjDict()[element]))
            self.objButton.adjustSize()
            self.objButton.clicked.connect(lambda: self.clicked()) # clicked is Placeholder, lambda for future args
            self.objButton.move(0, 25 + index * 25)
            self.objButton.setMinimumSize(QSize(50, 50))
            self.objButton.setMaximumWidth(500)
            self.listBoxLayout.addWidget(self.objButton, index + 1, 0)
            self.listBox.update()

        self.listBox.setLayout(self.listBoxLayout)
        self.mainLayout.addWidget(self.listScroll, 1, 0)

    def makeMenuView(self):
        self.menuBox = QWidget()
        self.menuBoxLayout = QHBoxLayout()
        self.homeButton = QPushButton()
        self.homeButton.setText("Home")
        self.homeButton.adjustSize()
        self.homeButton.clicked.connect(lambda: self.home()) # home is Placeholder, lambda for future args
        self.homeButton.move(0, 0)
        self.menuBoxLayout.addWidget(self.homeButton, 0)

        self.menuBox.setLayout(self.menuBoxLayout)
        self.mainLayout.addWidget(self.menuBox, 0, 0)


    
    def clicked(self):
        pass #Placeholder

    def home(self):
        pass #Placeholder
        


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()