# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaServiciosyUJNCE.ui'
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
        MainWindow.resize(1702, 866)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.BotonMapa = QPushButton(self.centralwidget)
        self.BotonMapa.setObjectName(u"BotonMapa")
        self.BotonMapa.setGeometry(QRect(770, 290, 201, 51))
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
        self.BotonMapa.setPalette(palette)
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BotonMapa.setFont(font)
        self.BotonMapa.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonMapa.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.BotonExposicioes = QPushButton(self.centralwidget)
        self.BotonExposicioes.setObjectName(u"BotonExposicioes")
        self.BotonExposicioes.setGeometry(QRect(770, 660, 201, 51))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.BotonExposicioes.setPalette(palette1)
        self.BotonExposicioes.setFont(font)
        self.BotonExposicioes.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonExposicioes.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.Titulo = QLabel(self.centralwidget)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(360, 70, 991, 91))
        font1 = QFont()
        font1.setFamily(u"Bell MT")
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setWeight(50)
        self.Titulo.setFont(font1)
        self.BotonCliP = QPushButton(self.centralwidget)
        self.BotonCliP.setObjectName(u"BotonCliP")
        self.BotonCliP.setGeometry(QRect(770, 540, 201, 51))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.BotonCliP.setPalette(palette2)
        self.BotonCliP.setFont(font)
        self.BotonCliP.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonCliP.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.BotonJuegos = QPushButton(self.centralwidget)
        self.BotonJuegos.setObjectName(u"BotonJuegos")
        self.BotonJuegos.setGeometry(QRect(770, 410, 201, 51))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush13 = QBrush(QColor(255, 255, 255, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.BotonJuegos.setPalette(palette3)
        self.BotonJuegos.setFont(font)
        self.BotonJuegos.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonJuegos.setStyleSheet(u"background-color: rgb(67, 157, 175);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        self.foto = QLabel(self.centralwidget)
        self.foto.setObjectName(u"foto")
        self.foto.setGeometry(QRect(-50, -40, 1751, 971))
        self.foto.setFont(font1)
        self.foto.setPixmap(QPixmap(u"../Imagenes/foto.png"))
        self.BotonAtras = QPushButton(self.centralwidget)
        self.BotonAtras.setObjectName(u"BotonAtras")
        self.BotonAtras.setGeometry(QRect(10, 10, 41, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush14 = QBrush(QColor(208, 223, 232, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush14)
        brush15 = QBrush(QColor(67, 157, 175, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush14)
        brush16 = QBrush(QColor(67, 157, 175, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        brush17 = QBrush(QColor(67, 157, 175, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.BotonAtras.setPalette(palette4)
        self.BotonAtras.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonAtras.setStyleSheet(u"background-color: rgb(208, 223, 232);\n"
"color:rgb(67, 157, 175);\n"
"font-weight: bold;\n"
"font-family: 'Verdana';\n"
"border-radius: 15px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.foto.raise_()
        self.BotonMapa.raise_()
        self.BotonExposicioes.raise_()
        self.Titulo.raise_()
        self.BotonCliP.raise_()
        self.BotonJuegos.raise_()
        self.BotonAtras.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.BotonMapa.setText(QCoreApplication.translate("MainWindow", u"MAPA", None))
        self.BotonExposicioes.setText(QCoreApplication.translate("MainWindow", u"EXPOSICIONES", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">\u00bfA QU\u00c9 DESEA ACCEDER?</span></p></body></html>", None))
        self.BotonCliP.setText(QCoreApplication.translate("MainWindow", u"CAT\u00c1LOGO", None))
        self.BotonJuegos.setText(QCoreApplication.translate("MainWindow", u"JUEGOS", None))
        self.foto.setText("")
        self.BotonAtras.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udc78", None))
    # retranslateUi

