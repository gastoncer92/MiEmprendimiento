# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication

from basura.gui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accion1)
    def accion1(self):
        print("dddd")
        self.lab


if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()
