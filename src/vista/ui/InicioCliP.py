# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InicioCliPsDaqhI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InicioCliPKHZYvw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1594, 852)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(530, 140, 461, 91))
        font = QFont()
        font.setFamily(u"Bell MT")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.lineDni = QLineEdit(self.centralwidget)
        self.lineDni.setObjectName(u"lineDni")
        self.lineDni.setGeometry(QRect(610, 340, 261, 51))
        self.lineDni.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(620, 300, 181, 31))
        self.lineContrasenna = QLineEdit(self.centralwidget)
        self.lineContrasenna.setObjectName(u"lineContrasenna")
        self.lineContrasenna.setGeometry(QRect(610, 470, 261, 51))
        self.lineContrasenna.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(208, 223, 232);")
        self.lineContrasenna.setEchoMode(QLineEdit.Password)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(620, 425, 181, 41))
        self.enviarBoton = QPushButton(self.centralwidget)
        self.enviarBoton.setObjectName(u"enviarBoton")
        self.enviarBoton.setGeometry(QRect(660, 580, 161, 51))
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
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.enviarBoton.setFont(font1)
        self.enviarBoton.setCursor(QCursor(Qt.PointingHandCursor))
        self.enviarBoton.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.fondo = QLabel(self.centralwidget)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(-260, -230, 2001, 1061))
        self.fondo.setFont(font)
        self.fondo.setPixmap(QPixmap(u"../Imagenes/foto.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.fondo.raise_()
        self.label_3.raise_()
        self.lineDni.raise_()
        self.label_4.raise_()
        self.lineContrasenna.raise_()
        self.label_8.raise_()
        self.enviarBoton.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">\u00a1ENTRA YA!</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">DNI</span></p></body></html>", None))
        self.lineContrasenna.setInputMask("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Contrase\u00f1a</span></p></body></html>", None))
        self.enviarBoton.setText(QCoreApplication.translate("MainWindow", u"ENTRAR", None))
        self.fondo.setText("")
    # retranslateUi


