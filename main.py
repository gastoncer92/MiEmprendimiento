# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication

from gui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.productos)
        self.pushButton_2.clicked.connect(self.vender)
        self.pushButton_3.clicked.connect(self.stock)
        self.pushButton_4.clicked.connect(self.gastos)
        self.pushButton_5.clicked.connect(self.estadisticas)
        self.pushButton_9.clicked.connect(self.historial)
        self.pushButton_7.clicked.connect(self.ajustes)

    def productos(self):
        self.stackedWidget.setCurrentIndex(1)
        pass

    def vender(self):
        self.stackedWidget.setCurrentIndex(4)

    def stock(self):
        self.stackedWidget.setCurrentIndex(6)

    def gastos(self):
        self.stackedWidget.setCurrentIndex(7)

    def estadisticas(self):
        self.stackedWidget.setCurrentIndex(8)

    def historial(self):
        self.stackedWidget.setCurrentIndex(9)

    def ajustes(self):
        self.stackedWidget.setCurrentIndex(10)


if __name__ == '__main__':
    app = QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()
