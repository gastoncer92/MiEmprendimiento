# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QTableView

from database import *
from gui import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # iniciar la base desde configuraciones
        nombreBase = activarBase()
        # self.label_13.setText(nombreBase)

        # productos
        self.pushButton_6.clicked.connect(self.ir_a_inicio)
        self.pushButton_17.clicked.connect(self.ir_a_inicio)
        self.pushButton.clicked.connect(self.ir_a_productos)
        self.pushButton_8.clicked.connect(self.ir_a_productoNuevo)
        self.pushButton_27.clicked.connect(self.ir_a_productos)
        self.pushButton_10.clicked.connect(self.cargarProducto)
        self.pushButton_30.clicked.connect(self.cargarNuevaFilaMateriales)
        self.tableView_3.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        # Ajustes
        self.pushButton_7.clicked.connect(self.ir_a_ajustes)
        self.pushButton_20.clicked.connect(self.ir_a_inicio)
        # self.pushButton_28.clicked.connect(self.cargarNuevaFilaMateriales) #test
        self.pushButton_29.clicked.connect(self.CargarCostoFijo)

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
        costoVariable = self.ProductoNuevo3.text()
        costoFijo = self.ProductoNuevo4.setText()  # viene de base de datos de ajustes
        margenGanancia = int(self.ProductoNuevo5.text().remplace("%", ""))
        # PrecioVenta=self.ProductoNuevo6 # se calcula
        CostoTotal = float(costoFijo) + float(costoVariable)
        PrecioVenta = (CostoTotal / (100 - margenGanancia)) * 100  # (CostoTotal / (100-margenGanancia))*100
        TiempoFabricacion = self.ProductoNuevo7.text()
        materialesCosto = '222'

        producto = [nombre,
                    detalle,
                    materialesCosto,
                    costoVariable,
                    costoFijo,
                    margenGanancia,
                    CostoTotal,
                    PrecioVenta,
                    TiempoFabricacion]
        GuardarProducto(producto)

    def cargarNuevaFilaMateriales(self):
        self.statusbar.showMessage("cargar nueva fila para materiales")
        cantidadDeMateriales = int(self.label_19.text())
        cantidadDeMateriales += 1
        self.label_19.setText(str(cantidadDeMateriales))
        # self.tableView_3.setRowCount(cantidadDeMateriales)
        self.tableView_3.setRo

    # metodos ajustes
    def ir_a_ajustes(self):
        self.stackedWidget.setCurrentIndex(10)

    def test(self):
        self.statusbar.showMessage("test inicial")
        conexion()

    def CargarCostoFijo(self):
        self.statusbar.showMessage("CargarCostoFijo")
        costoFijo = self.lineEdit.text()
        conn = conexionAjustes()
        cursor = conn.cursor()
        consulta = "insert or replace into Ajustes(costoFijo) values((?))"
        cursor.execute(consulta, (costoFijo,))
        conn.commit()
        conn.close()
        self.lineEdit.setText("")


if __name__ == '__main__':
    # base de datos de ajustes
    ajustes()

    app = QApplication([])
    gui = MainWindow()
    gui.show()
    app.exec_()
