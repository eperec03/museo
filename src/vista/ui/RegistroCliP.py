from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# # import imagenes_rc

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"MainWindow")
#         MainWindow.resize(400, 450)
#         MainWindow.setMinimumSize(QSize(400, 450))
#         MainWindow.setMaximumSize(QSize(400, 450))
#         MainWindow.setStyleSheet(u"#MainWindow {\n"
# " background: qlineargradient(spread:pad, x1:0.498, y1:0.9265, x2:0.482587, y2:0.119, stop:0 rgb(170, 170, 170), stop:1 rgb(240, 240, 240));\n"
# "}\n"
# "\n"
# "/* Entradas de texto */\n"
# "QLineEdit {\n"
# "    background-color: #ffffff;\n"
# "    border: 2px solid #c0c0c0;\n"
# "    padding: 5px;\n"
# "}\n"
# "\n"
# "/* Texto */\n"
# "QLabel {\n"
# "    color: #000000;\n"
# "    font-size: 14px;\n"
# "}\n"
# "\n"
# "/* Bot\u00f3n */\n"
# "QPushButton {\n"
# "    background-color: #4CAF50; /* Color de fondo */\n"
# "    border: none;\n"
# "    color: white;\n"
# "    text-align: center;\n"
# "    text-decoration: none;\n"
# "    font-size: 14px;\n"
# "    margin: 4px 2px;\n"
# "    border-radius: 10px;\n"
# "}\n"
# "\n"
# "/*Bot\u00f3n est\u00e1 presionado */\n"
# "QPushButton:pressed {\n"
# "    background-color: #45a049;\n"
# "}\n"
# "\n"
# "/* Imagen */\n"
# "QLabel#label_6 {\n"
# "    border-image: url(:/src/vista/Imagenes/registro.png);\n"
# "}\n"
# "")
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.frame = QFrame(self.centralwidget)
#         self.frame.setObjectName(u"frame")
#         self.frame.setGeometry(QRect(40, 30, 141, 311))
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         self.frame.setFrameShadow(QFrame.Raised)
#         self.verticalLayout = QVBoxLayout(self.frame)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.label_4 = QLabel(self.frame)
#         self.label_4.setObjectName(u"label_4")
#         self.label_4.setTextFormat(Qt.AutoText)

#         self.verticalLayout.addWidget(self.label_4)

#         self.label_7 = QLabel(self.frame)
#         self.label_7.setObjectName(u"label_7")

#         self.verticalLayout.addWidget(self.label_7)

#         self.label = QLabel(self.frame)
#         self.label.setObjectName(u"label")

#         self.verticalLayout.addWidget(self.label)

#         self.label_2 = QLabel(self.frame)
#         self.label_2.setObjectName(u"label_2")

#         self.verticalLayout.addWidget(self.label_2)

#         self.label_3 = QLabel(self.frame)
#         self.label_3.setObjectName(u"label_3")

#         self.verticalLayout.addWidget(self.label_3)

#         self.label_5 = QLabel(self.frame)
#         self.label_5.setObjectName(u"label_5")

#         self.verticalLayout.addWidget(self.label_5)

#         self.label_8 = QLabel(self.frame)
#         self.label_8.setObjectName(u"label_8")

#         self.verticalLayout.addWidget(self.label_8)

#         self.label_9 = QLabel(self.frame)
#         self.label_9.setObjectName(u"label_9")

#         self.verticalLayout.addWidget(self.label_9)

#         self.label_10 = QLabel(self.frame)
#         self.label_10.setObjectName(u"label_10")

#         self.verticalLayout.addWidget(self.label_10)

#         self.frame_2 = QFrame(self.centralwidget)
#         self.frame_2.setObjectName(u"frame_2")
#         self.frame_2.setGeometry(QRect(11, 11, 31, 442))
#         self.frame_2.setFrameShape(QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QFrame.Raised)
#         self.frame_3 = QFrame(self.centralwidget)
#         self.frame_3.setObjectName(u"frame_3")
#         self.frame_3.setGeometry(QRect(180, 40, 211, 301))
#         self.frame_3.setFrameShape(QFrame.StyledPanel)
#         self.frame_3.setFrameShadow(QFrame.Raised)
#         self.lineNombre = QLineEdit(self.frame_3)
#         self.lineNombre.setObjectName(u"lineNombre")
#         self.lineNombre.setGeometry(QRect(20, 40, 171, 31))
#         self.lineTfno = QLineEdit(self.frame_3)
#         self.lineTfno.setObjectName(u"lineTfno")
#         self.lineTfno.setGeometry(QRect(20, 70, 171, 31))
#         self.lineTitular = QLineEdit(self.frame_3)
#         self.lineTitular.setObjectName(u"lineTitular")
#         self.lineTitular.setGeometry(QRect(20, 130, 171, 31))
#         self.lineNumTarj = QLineEdit(self.frame_3)
#         self.lineNumTarj.setObjectName(u"lineNumTarj")
#         self.lineNumTarj.setGeometry(QRect(20, 160, 171, 31))
#         self.lineCvv = QLineEdit(self.frame_3)
#         self.lineCvv.setObjectName(u"lineCvv")
#         self.lineCvv.setGeometry(QRect(20, 190, 171, 31))
#         self.lineCad = QLineEdit(self.frame_3)
#         self.lineCad.setObjectName(u"lineCad")
#         self.lineCad.setGeometry(QRect(20, 220, 171, 31))
#         self.lineDni = QLineEdit(self.frame_3)
#         self.lineDni.setObjectName(u"lineDni")
#         self.lineDni.setGeometry(QRect(20, 10, 171, 31))
#         self.lineEmail = QLineEdit(self.frame_3)
#         self.lineEmail.setObjectName(u"lineEmail")
#         self.lineEmail.setGeometry(QRect(20, 100, 171, 31))
#         self.lineContrasenna = QLineEdit(self.frame_3)
#         self.lineContrasenna.setObjectName(u"lineContrasenna")
#         self.lineContrasenna.setGeometry(QRect(20, 250, 171, 31))
#         self.frame_4 = QFrame(self.centralwidget)
#         self.frame_4.setObjectName(u"frame_4")
#         self.frame_4.setGeometry(QRect(370, 11, 31, 442))
#         self.frame_4.setFrameShape(QFrame.StyledPanel)
#         self.frame_4.setFrameShadow(QFrame.Raised)
#         self.frame_5 = QFrame(self.centralwidget)
#         self.frame_5.setObjectName(u"frame_5")
#         self.frame_5.setGeometry(QRect(50, 400, 311, 41))
#         self.frame_5.setFrameShape(QFrame.StyledPanel)
#         self.frame_5.setFrameShadow(QFrame.Raised)
#         # self.enviarBoton = QPushButton(self.frame_5)
#         # self.enviarBoton.setObjectName(u"enviarBoton")
#         # self.enviarBoton.setGeometry(QRect(100, 0, 111, 41))
#         # self.enviarBoton.setFont(font)
#         # self.enviarBoton.setCursor(QCursor(Qt.PointingHandCursor))
#         # self.enviarBoton.setMouseTracking(True)
#         # self.enviarBoton.setTabletTracking(True)
#         # self.enviarBoton.setCheckable(False)
#         MainWindow.setCentralWidget(self.centralwidget)

#         self.retranslateUi(MainWindow)
#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi

#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#         self.label_4.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
#         self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nombre Completo", None))
#         self.label.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
#         self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
#         self.label_3.setText(QCoreApplication.translate("MainWindow", u"Titular", None))
#         self.label_5.setText(QCoreApplication.translate("MainWindow", u"NumTarjeta", None))
#         self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cvv", None))
#         self.label_9.setText(QCoreApplication.translate("MainWindow", u"Caducidad", None))
#         self.label_10.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
#         self.lineNombre.setText(QCoreApplication.translate("MainWindow", u"Clara Alejos", None))
#         self.lineTfno.setText(QCoreApplication.translate("MainWindow", u"634597559", None))
#         self.lineTitular.setText(QCoreApplication.translate("MainWindow", u"Clara Alejos", None))
#         self.lineNumTarj.setText(QCoreApplication.translate("MainWindow", u"4545777788889999", None))
#         self.lineCvv.setText(QCoreApplication.translate("MainWindow", u"134", None))
#         self.lineCad.setText(QCoreApplication.translate("MainWindow", u"09/04/2026", None))
#         self.lineDni.setText(QCoreApplication.translate("MainWindow", u"71311695B", None))
#         self.lineEmail.setText(QCoreApplication.translate("MainWindow", u"claraalejos@gmail.com", None))
#         self.lineContrasenna.setText(QCoreApplication.translate("MainWindow", u"changeme", None))
#         self.enviarBoton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
#     # retranslateUi
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerfEFWYy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

