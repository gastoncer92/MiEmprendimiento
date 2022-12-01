# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication

from database import *
from gui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.estado.setText("")

        # iniciar la base desde configuraciones
        nombreBase = activarBase()
        self.label_13.setText(nombreBase)

        # productos
        self.pushButton_6.clicked.connect(self.ir_a_inicio)
        self.pushButton_17.clicked.connect(self.ir_a_inicio)
        self.pushButton.clicked.connect(self.ir_a_productos)
        self.pushButton_8.clicked.connect(self.ir_a_productoNuevo)
        self.pushButton_27.clicked.connect(self.ir_a_productos)
        self.pushButton_10.clicked.connect(self.cargarProducto)

        # Ajustes
        self.pushButton_7.clicked.connect(self.ir_a_ajustes)
        self.pushButton_20.clicked.connect(self.ir_a_inicio)
        self.pushButton_28.clicked.connect(self.test)

    # metodos productos
    def ir_a_productos(self):
        self.statusbar.showMessage("Ir a productos")

        self.stackedWidget.setCurrentIndex(1)

    def ir_a_inicio(self):
        self.statusbar.showMessage("ir a inicio.")
        self.stackedWidget.setCurrentIndex(0)

    def ir_a_productoNuevo(self):
        self.statusbar.showMessage("Ir a productos")
        self.stackedWidget.setCurrentIndex(2)

    def cargarProducto(self):
        self.statusbar.showMessage("cargarProducto")
        nombre = self.ProductoNuevo1.text()
        detalle = self.ProductoNuevo2.text()
        costoVariable = float(self.ProductoNuevo3.text())
        # costoFijo=self.ProductoNuevo4 # viene de base de datos de ajustes
        costoFijo = float(CostoFijo())
        margenGanancia = int(self.ProductoNuevo5.text().remplace("%", ""))
        # PrecioVenta=self.ProductoNuevo6 # se calcula
        CostoTotal = costoFijo + costoVariable
        PrecioVenta = (CostoTotal / (100 - margenGanancia)) * 100  # (CostoTotal / (100-margenGanancia))*100
        TiempoFabricacion = self.ProductoNuevo7.text()

    # metodos ajustes
    def ir_a_ajustes(self):
        self.estado.setText("Ir a ventana de ajustes")
        self.stackedWidget.setCurrentIndex(10)

    def test(self):
        self.statusbar.showMessage("test inicial")
        conexion()


if __name__ == '__main__':
    # base de datos de ajustes
    ajustes()

    app = QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()
