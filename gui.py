# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.presentacion = QtWidgets.QWidget()
        self.presentacion.setObjectName("presentacion")
        self.label = QtWidgets.QLabel(self.presentacion)
        self.label.setGeometry(QtCore.QRect(250, 30, 131, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.presentacion)
        self.pushButton.setGeometry(QtCore.QRect(170, 100, 84, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.presentacion)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 140, 84, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.presentacion)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 180, 84, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.presentacion)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 220, 84, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.presentacion)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 260, 84, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.presentacion)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 300, 84, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.presentacion)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 330, 84, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.presentacion)
        self.productos = QtWidgets.QWidget()
        self.productos.setObjectName("productos")
        self.widget = QtWidgets.QWidget(self.productos)
        self.widget.setGeometry(QtCore.QRect(20, 100, 621, 80))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 85, 13))
        self.label_2.setObjectName("label_2")
        self.widget_2 = QtWidgets.QWidget(self.productos)
        self.widget_2.setGeometry(QtCore.QRect(19, 190, 621, 341))
        self.widget_2.setObjectName("widget_2")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 551, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_8 = QtWidgets.QPushButton(self.productos)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 50, 85, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.productos)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.productos)
        self.label_3.setGeometry(QtCore.QRect(340, 10, 48, 13))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.productos)
        self.productoNuevo = QtWidgets.QWidget()
        self.productoNuevo.setObjectName("productoNuevo")
        self.label_4 = QtWidgets.QLabel(self.productoNuevo)
        self.label_4.setGeometry(QtCore.QRect(370, 20, 77, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.productoNuevo)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.productoNuevo)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.productoNuevo)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 130, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.productoNuevo)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 160, 113, 20))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.productoNuevo)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 190, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.productoNuevo)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 220, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.productoNuevo)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 260, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_17 = QtWidgets.QPushButton(self.productoNuevo)
        self.pushButton_17.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_27 = QtWidgets.QPushButton(self.productoNuevo)
        self.pushButton_27.setGeometry(QtCore.QRect(130, 30, 75, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.stackedWidget.addWidget(self.productoNuevo)
        self.productoDetalle = QtWidgets.QWidget()
        self.productoDetalle.setObjectName("productoDetalle")
        self.label_5 = QtWidgets.QLabel(self.productoDetalle)
        self.label_5.setGeometry(QtCore.QRect(340, 10, 79, 13))
        self.label_5.setObjectName("label_5")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.productoDetalle)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 180, 113, 20))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.productoDetalle)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 150, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.productoDetalle)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 120, 113, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.productoDetalle)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.productoDetalle)
        self.lineEdit_10.setGeometry(QtCore.QRect(180, 240, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.productoDetalle)
        self.lineEdit_11.setGeometry(QtCore.QRect(180, 210, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.productoDetalle)
        self.lineEdit_12.setGeometry(QtCore.QRect(180, 90, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_12 = QtWidgets.QPushButton(self.productoDetalle)
        self.pushButton_12.setGeometry(QtCore.QRect(30, 40, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.productoDetalle)
        self.pushButton_13.setGeometry(QtCore.QRect(110, 40, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_6 = QtWidgets.QLabel(self.productoDetalle)
        self.label_6.setGeometry(QtCore.QRect(190, 70, 58, 13))
        self.label_6.setObjectName("label_6")
        self.pushButton_14 = QtWidgets.QPushButton(self.productoDetalle)
        self.pushButton_14.setGeometry(QtCore.QRect(200, 40, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.stackedWidget.addWidget(self.productoDetalle)
        self.vender = QtWidgets.QWidget()
        self.vender.setObjectName("vender")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.vender)
        self.tableWidget_2.setGeometry(QtCore.QRect(60, 121, 591, 151))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label_7 = QtWidgets.QLabel(self.vender)
        self.label_7.setGeometry(QtCore.QRect(360, 20, 33, 13))
        self.label_7.setObjectName("label_7")
        self.pushButton_15 = QtWidgets.QPushButton(self.vender)
        self.pushButton_15.setGeometry(QtCore.QRect(60, 390, 75, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_8 = QtWidgets.QLabel(self.vender)
        self.label_8.setGeometry(QtCore.QRect(70, 290, 101, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.vender)
        self.label_9.setGeometry(QtCore.QRect(70, 320, 28, 13))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.vender)
        self.comboBox.setGeometry(QtCore.QRect(180, 290, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_10 = QtWidgets.QLabel(self.vender)
        self.label_10.setGeometry(QtCore.QRect(120, 320, 47, 13))
        self.label_10.setObjectName("label_10")
        self.pushButton_16 = QtWidgets.QPushButton(self.vender)
        self.pushButton_16.setGeometry(QtCore.QRect(190, 320, 75, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.vender)
        self.pushButton_18.setGeometry(QtCore.QRect(50, 20, 75, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.stackedWidget.addWidget(self.vender)
        self.ventas = QtWidgets.QWidget()
        self.ventas.setObjectName("ventas")
        self.pushButton_19 = QtWidgets.QPushButton(self.ventas)
        self.pushButton_19.setGeometry(QtCore.QRect(50, 20, 75, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.stackedWidget.addWidget(self.ventas)
        self.stock = QtWidgets.QWidget()
        self.stock.setObjectName("stock")
        self.pushButton_24 = QtWidgets.QPushButton(self.stock)
        self.pushButton_24.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.stackedWidget.addWidget(self.stock)
        self.gastos = QtWidgets.QWidget()
        self.gastos.setObjectName("gastos")
        self.pushButton_23 = QtWidgets.QPushButton(self.gastos)
        self.pushButton_23.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.stackedWidget.addWidget(self.gastos)
        self.estadisticas = QtWidgets.QWidget()
        self.estadisticas.setObjectName("estadisticas")
        self.pushButton_22 = QtWidgets.QPushButton(self.estadisticas)
        self.pushButton_22.setGeometry(QtCore.QRect(70, 60, 75, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.stackedWidget.addWidget(self.estadisticas)
        self.historial = QtWidgets.QWidget()
        self.historial.setObjectName("historial")
        self.pushButton_21 = QtWidgets.QPushButton(self.historial)
        self.pushButton_21.setGeometry(QtCore.QRect(190, 60, 75, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.stackedWidget.addWidget(self.historial)
        self.ajustes = QtWidgets.QWidget()
        self.ajustes.setObjectName("ajustes")
        self.pushButton_20 = QtWidgets.QPushButton(self.ajustes)
        self.pushButton_20.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_11 = QtWidgets.QLabel(self.ajustes)
        self.label_11.setGeometry(QtCore.QRect(260, 50, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.ajustes)
        self.label_12.setGeometry(QtCore.QRect(100, 110, 104, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.ajustes)
        self.label_13.setGeometry(QtCore.QRect(210, 110, 116, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.ajustes)
        self.label_14.setGeometry(QtCore.QRect(100, 140, 106, 13))
        self.label_14.setObjectName("label_14")
        self.pushButton_25 = QtWidgets.QPushButton(self.ajustes)
        self.pushButton_25.setGeometry(QtCore.QRect(290, 170, 75, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.ajustes)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 140, 113, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_26 = QtWidgets.QPushButton(self.ajustes)
        self.pushButton_26.setGeometry(QtCore.QRect(340, 140, 87, 23))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_15 = QtWidgets.QLabel(self.ajustes)
        self.label_15.setGeometry(QtCore.QRect(110, 180, 167, 13))
        self.label_15.setObjectName("label_15")
        self.pushButton_28 = QtWidgets.QPushButton(self.ajustes)
        self.pushButton_28.setGeometry(QtCore.QRect(170, 310, 75, 23))
        self.pushButton_28.setObjectName("pushButton_28")
        self.stackedWidget.addWidget(self.ajustes)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.estado = QtWidgets.QLabel(self.centralwidget)
        self.estado.setObjectName("estado")
        self.verticalLayout.addWidget(self.estado)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mi Emprendimiento"))
        self.pushButton.setText(_translate("MainWindow", "Productos"))
        self.pushButton_2.setText(_translate("MainWindow", "Vender"))
        self.pushButton_3.setText(_translate("MainWindow", "Stock"))
        self.pushButton_4.setText(_translate("MainWindow", "Gastos"))
        self.pushButton_5.setText(_translate("MainWindow", "Estadisticas"))
        self.pushButton_9.setText(_translate("MainWindow", "Historial"))
        self.pushButton_7.setText(_translate("MainWindow", "Ajustes"))
        self.label_2.setText(_translate("MainWindow", "No hay productos"))
        self.pushButton_8.setText(_translate("MainWindow", "Nuevo Producto"))
        self.pushButton_6.setText(_translate("MainWindow", "Atras"))
        self.label_3.setText(_translate("MainWindow", "Productos"))
        self.label_4.setText(_translate("MainWindow", "Producto Nuevo"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "nombre"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "detalle"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "costo fabricacion"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "tiempo de fabricacion"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Beneficio"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Precio"))
        self.pushButton_10.setText(_translate("MainWindow", "Agregar"))
        self.pushButton_17.setText(_translate("MainWindow", "inicio"))
        self.pushButton_27.setText(_translate("MainWindow", "atras"))
        self.label_5.setText(_translate("MainWindow", "Detalle producto"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "tiempo de fabricacion"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "costo fabricacion"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "detalle"))
        self.pushButton_11.setText(_translate("MainWindow", "Borrar"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "Precio"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Beneficio"))
        self.lineEdit_12.setPlaceholderText(_translate("MainWindow", "nombre"))
        self.pushButton_12.setText(_translate("MainWindow", "Atras"))
        self.pushButton_13.setText(_translate("MainWindow", "Modificar"))
        self.label_6.setText(_translate("MainWindow", "id producto:"))
        self.pushButton_14.setText(_translate("MainWindow", "Restablecer"))
        self.label_7.setText(_translate("MainWindow", "Vender"))
        self.pushButton_15.setText(_translate("MainWindow", "Vender"))
        self.label_8.setText(_translate("MainWindow", "Descuento mayorista"))
        self.label_9.setText(_translate("MainWindow", "Total:"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_16.setText(_translate("MainWindow", "redondear"))
        self.pushButton_18.setText(_translate("MainWindow", "Atras"))
        self.pushButton_19.setText(_translate("MainWindow", "Atras"))
        self.pushButton_24.setText(_translate("MainWindow", "Atras"))
        self.pushButton_23.setText(_translate("MainWindow", "Atras"))
        self.pushButton_22.setText(_translate("MainWindow", "Atras"))
        self.pushButton_21.setText(_translate("MainWindow", "Atras"))
        self.pushButton_20.setText(_translate("MainWindow", "Atras"))
        self.label_11.setText(_translate("MainWindow", "Ajustes"))
        self.label_12.setText(_translate("MainWindow", "Base de datos actual:"))
        self.label_13.setText(_translate("MainWindow", "nombre_base_de_datos"))
        self.label_14.setText(_translate("MainWindow", "Nueva base de datos:"))
        self.pushButton_25.setText(_translate("MainWindow", "Examinar"))
        self.lineEdit_13.setPlaceholderText(_translate("MainWindow", "nombre..."))
        self.pushButton_26.setText(_translate("MainWindow", "crear y conectar"))
        self.label_15.setText(_translate("MainWindow", "Conectar base de datos existente:"))
        self.pushButton_28.setText(_translate("MainWindow", "test"))
        self.estado.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
