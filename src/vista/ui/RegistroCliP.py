# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistroCliPKJfDkl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1687, 854)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.enviarBoton = QPushButton(self.centralwidget)
        self.enviarBoton.setObjectName(u"enviarBoton")
        self.enviarBoton.setGeometry(QRect(760, 710, 161, 51))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(67, 157, 175, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.enviarBoton.setPalette(palette)
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enviarBoton.setFont(font)
        self.enviarBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarBoton.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 20, 701, 91))
        font1 = QFont()
        font1.setFamily(u"Bell MT")
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.lineNombre = QLineEdit(self.centralwidget)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setGeometry(QRect(480, 250, 231, 41))
        self.lineNombre.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 210, 221, 31))
        self.lineDni = QLineEdit(self.centralwidget)
        self.lineDni.setObjectName(u"lineDni")
        self.lineDni.setGeometry(QRect(480, 330, 231, 41))
        self.lineDni.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 300, 181, 31))
        self.lineTfno = QLineEdit(self.centralwidget)
        self.lineTfno.setObjectName(u"lineTfno")
        self.lineTfno.setGeometry(QRect(480, 420, 231, 41))
        self.lineTfno.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 470, 231, 51))
        self.lineEmail = QLineEdit(self.centralwidget)
        self.lineEmail.setObjectName(u"lineEmail")
        self.lineEmail.setGeometry(QRect(480, 510, 231, 41))
        self.lineEmail.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(480, 390, 181, 31))
        self.lineContrasenna = QLineEdit(self.centralwidget)
        self.lineContrasenna.setObjectName(u"lineContrasenna")
        self.lineContrasenna.setGeometry(QRect(480, 600, 231, 41))
        self.lineContrasenna.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.lineContrasenna.setEchoMode(QLineEdit.Password)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(480, 570, 181, 31))
        self.lineTitular = QLineEdit(self.centralwidget)
        self.lineTitular.setObjectName(u"lineTitular")
        self.lineTitular.setGeometry(QRect(970, 280, 241, 41))
        self.lineTitular.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(970, 440, 181, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(970, 350, 221, 31))
        self.lineCvv = QLineEdit(self.centralwidget)
        self.lineCvv.setObjectName(u"lineCvv")
        self.lineCvv.setGeometry(QRect(970, 470, 241, 41))
        self.lineCvv.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.lineCad = QLineEdit(self.centralwidget)
        self.lineCad.setObjectName(u"lineCad")
        self.lineCad.setGeometry(QRect(970, 570, 241, 41))
        self.lineCad.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(970, 530, 231, 41))
        self.lineNumTarj = QLineEdit(self.centralwidget)
        self.lineNumTarj.setObjectName(u"lineNumTarj")
        self.lineNumTarj.setGeometry(QRect(970, 380, 241, 41))
        self.lineNumTarj.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(970, 250, 181, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 150, 381, 41))
        self.label_7.setFont(font1)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(910, 150, 361, 41))
        self.label_14.setFont(font1)
        self.fondo = QLabel(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(-90, -110, 2001, 1061))
        self.fondo.setFont(font1)
        self.fondo.setPixmap(QPixmap(u"../Imagenes/foto.png"))
        self.BotonAtras = QPushButton(self.centralwidget)
        self.BotonAtras.setObjectName(u"BotonAtras")
        self.BotonAtras.setGeometry(QRect(20, 20, 41, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush5 = QBrush(QColor(208, 223, 232, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(67, 157, 175, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        brush7 = QBrush(QColor(67, 157, 175, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        brush8 = QBrush(QColor(67, 157, 175, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.BotonAtras.setPalette(palette1)
        self.BotonAtras.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonAtras.setStyleSheet(u"background-color: rgb(208, 223, 232);\n"
"color:rgb(67, 157, 175);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.fondo.raise_()
        self.enviarBoton.raise_()
        self.label_3.raise_()
        self.lineNombre.raise_()
        self.label.raise_()
        self.lineDni.raise_()
        self.label_4.raise_()
        self.lineTfno.raise_()
        self.label_5.raise_()
        self.lineEmail.raise_()
        self.label_6.raise_()
        self.lineContrasenna.raise_()
        self.label_8.raise_()
        self.lineTitular.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.lineCvv.raise_()
        self.lineCad.raise_()
        self.label_12.raise_()
        self.lineNumTarj.raise_()
        self.label_13.raise_()
        self.label_7.raise_()
        self.label_14.raise_()
        self.BotonAtras.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enviarBoton.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">\u00a1REG\u00cdSTRATE YA!</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Nombre Completo</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">DNI</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Correo electr\u00f3nico</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Tel\u00e9fono</span></p></body></html>", None))
        self.lineContrasenna.setInputMask("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Contrase\u00f1a</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Cvv</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">N\u00famero de Tarjeta</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Fecha de Caducidad</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Titular</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">DATOS PERSONALES</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">DATOS BANCARIOS</span></p></body></html>", None))
        self.fondo.setText("")
        self.BotonAtras.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udc78", None))
    # retranslateUi


