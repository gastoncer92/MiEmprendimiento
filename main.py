# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication

from gui import *
from database import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.estado.setText("")

        # productos
        self.pushButton_6.clicked.connect(self.ir_a_inicio)
        self.pushButton_17.clicked.connect(self.ir_a_inicio)
        self.pushButton.clicked.connect(self.ir_a_productos)
        self.pushButton_8.clicked.connect(self.ir_a_productoNuevo)
        self.pushButton_27.clicked.connect(self.ir_a_productos)

        # Ajustes
        self.pushButton_7.clicked.connect(self.ir_a_ajustes)
        self.pushButton_20.clicked.connect(self.ir_a_inicio)
        self.pushButton_28.clicked.connect(self.test)


    # metodos productos
    def ir_a_productos(self):
        self.estado.setText("Ir a productos")
        self.stackedWidget.setCurrentIndex(1)
    def ir_a_inicio(self):
        self.stackedWidget.setCurrentIndex(0)
    def ir_a_productoNuevo(self):
        self.estado.setText("Ir a productos")
        self.stackedWidget.setCurrentIndex(2)

    # metodos ajustes
    def ir_a_ajustes(self):
        self.estado.setText("Ir a ventana de ajustes")
        self.stackedWidget.setCurrentIndex(10)
    def test(self):
        conexion()



if __name__ == '__main__':
    # base de datos de ajustes
    ajustes()
    app = QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()
