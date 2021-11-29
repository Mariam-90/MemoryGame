import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtCore, QtWidgets, QtMultimedia


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.improvememory.org/wp-content/games/happy-halloween/index.html'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)



app = QApplication(sys.argv)
QApplication.setApplicationName("memory game")
window = MainWindow()
app.exec()
