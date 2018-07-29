# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morita.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("alternate-background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.importar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.importar.setFont(font)
        self.importar.setObjectName("importar")
        self.verticalLayout_3.addWidget(self.importar)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.seleccionar = QtWidgets.QComboBox(self.centralwidget)
        self.seleccionar.setStyleSheet("background-color: rgb(165, 167, 170);")
        self.seleccionar.setObjectName("seleccionar")
        self.verticalLayout_3.addWidget(self.seleccionar)
        self.cargar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cargar.setFont(font)
        self.cargar.setObjectName("cargar")
        self.verticalLayout_3.addWidget(self.cargar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.independiente = QtWidgets.QComboBox(self.centralwidget)
        self.independiente.setStyleSheet("background-color: rgb(165, 167, 170);\n"
"")
        self.independiente.setObjectName("independiente")
        self.verticalLayout_3.addWidget(self.independiente)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.condicion = QtWidgets.QComboBox(self.centralwidget)
        self.condicion.setStyleSheet("background-color: rgb(165, 167, 170);")
        self.condicion.setObjectName("condicion")
        self.verticalLayout_3.addWidget(self.condicion)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.dependiente = QtWidgets.QComboBox(self.centralwidget)
        self.dependiente.setStyleSheet("background-color: rgb(165, 167, 170);")
        self.dependiente.setObjectName("dependiente")
        self.verticalLayout_3.addWidget(self.dependiente)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.analizar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.analizar.setFont(font)
        self.analizar.setObjectName("analizar")
        self.verticalLayout_3.addWidget(self.analizar)
        self.resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.resultado.setStyleSheet("font: 9pt \"Comfortaa\";\n"
"font: 75 italic 9pt \"Arial\";\n"
"color: rgb(0, 170, 255);\n"
"font: 75 9pt \"Mukti Narrow\";\n"
"font: 9pt \"Loma\";\n"
"font: 9pt \"Garuda\";\n"
"font: 9pt \"Gargi\";\n"
"font: 9pt \"Comfortaa\";\n"
"font: 9pt \"Gargi\";")
        self.resultado.setObjectName("resultado")
        self.verticalLayout_3.addWidget(self.resultado)
        self.barra = QtWidgets.QProgressBar(self.centralwidget)
        self.barra.setProperty("value", 0)
        self.barra.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.barra.setObjectName("barra")
        self.verticalLayout_3.addWidget(self.barra)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MORITA "))
        self.importar.setText(_translate("MainWindow", "IMPORTAR"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">SELECCIONAR PÁGINA</p></body></html>"))
        self.cargar.setText(_translate("MainWindow", "CARGAR DATOS"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">VARIABLE INDEPENDIENTE</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CONDICIÓN</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">VARIABLE DEPENDIENTE</p></body></html>"))
        self.analizar.setText(_translate("MainWindow", "ANALIZAR"))

