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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.enviarBoton = QPushButton(self.centralwidget)
        self.enviarBoton.setObjectName(u"enviarBoton")
        self.enviarBoton.setGeometry(QRect(320, 500, 131, 41))
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
        self.enviarBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarBoton.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 10, 361, 91))
        font = QFont()
        font.setFamily(u"Bell MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.lineNombre = QLineEdit(self.centralwidget)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setGeometry(QRect(120, 170, 211, 31))
        self.lineNombre.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 150, 181, 16))
        self.lineDni = QLineEdit(self.centralwidget)
        self.lineDni.setObjectName(u"lineDni")
        self.lineDni.setGeometry(QRect(120, 230, 211, 31))
        self.lineDni.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 210, 181, 16))
        self.lineTfno = QLineEdit(self.centralwidget)
        self.lineTfno.setObjectName(u"lineTfno")
        self.lineTfno.setGeometry(QRect(120, 290, 211, 31))
        self.lineTfno.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 330, 181, 16))
        self.lineEmail = QLineEdit(self.centralwidget)
        self.lineEmail.setObjectName(u"lineEmail")
        self.lineEmail.setGeometry(QRect(120, 350, 211, 31))
        self.lineEmail.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 270, 181, 16))
        self.lineContrasenna = QLineEdit(self.centralwidget)
        self.lineContrasenna.setObjectName(u"lineContrasenna")
        self.lineContrasenna.setGeometry(QRect(120, 410, 211, 31))
        self.lineContrasenna.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.lineContrasenna.setEchoMode(QLineEdit.Password)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 390, 181, 16))
        self.lineTitular = QLineEdit(self.centralwidget)
        self.lineTitular.setObjectName(u"lineTitular")
        self.lineTitular.setGeometry(QRect(450, 200, 211, 31))
        self.lineTitular.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(460, 300, 181, 16))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(460, 240, 181, 16))
        self.lineCvv = QLineEdit(self.centralwidget)
        self.lineCvv.setObjectName(u"lineCvv")
        self.lineCvv.setGeometry(QRect(450, 320, 211, 31))
        self.lineCvv.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.lineCad = QLineEdit(self.centralwidget)
        self.lineCad.setObjectName(u"lineCad")
        self.lineCad.setGeometry(QRect(450, 380, 211, 31))
        self.lineCad.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(460, 360, 181, 16))
        self.lineNumTarj = QLineEdit(self.centralwidget)
        self.lineNumTarj.setObjectName(u"lineNumTarj")
        self.lineNumTarj.setGeometry(QRect(450, 260, 211, 31))
        self.lineNumTarj.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(460, 180, 181, 16))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 100, 181, 41))
        self.label_7.setFont(font)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(470, 100, 181, 41))
        self.label_14.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enviarBoton.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00a1REGISTRATE YA!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Nombre Completo</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">DNI</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Correo electr\u00f3nico</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Tel\u00e9fono</span></p></body></html>", None))
        self.lineContrasenna.setInputMask("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Contrase\u00f1a</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cvv</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">N\u00famero de Tarjeta</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Fecha de Caducidad</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Titular</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DATOS PERSONALES</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">DATOS BANCARIOS</span></p></body></html>", None))
    # retranslateUi

