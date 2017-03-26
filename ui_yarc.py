# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yarc_ui.ui'
#
# Created: Sun Mar 26 17:10:55 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 85)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 222, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.subField = QtGui.QLineEdit(self.layoutWidget)
        self.subField.setObjectName("subField")
        self.horizontalLayout.addWidget(self.subField)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 177, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.howManyPages = QtGui.QSpinBox(self.layoutWidget1)
        self.howManyPages.setMinimum(1)
        self.howManyPages.setMaximum(99)
        self.howManyPages.setObjectName("howManyPages")
        self.horizontalLayout_2.addWidget(self.howManyPages)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 10, 91, 54))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getBut = QtGui.QPushButton(self.widget)
        self.getBut.setObjectName("getBut")
        self.verticalLayout.addWidget(self.getBut)
        self.stopBut = QtGui.QPushButton(self.widget)
        self.stopBut.setObjectName("stopBut")
        self.verticalLayout.addWidget(self.stopBut)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Subreddit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "How many pages to crawl:", None, QtGui.QApplication.UnicodeUTF8))
        self.getBut.setText(QtGui.QApplication.translate("MainWindow", "Get images", None, QtGui.QApplication.UnicodeUTF8))
        self.stopBut.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))

