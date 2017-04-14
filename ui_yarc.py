# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yarc_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(340, 100))
        MainWindow.setMaximumSize(QtCore.QSize(340, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 222, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 177, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.howManyPages = QtWidgets.QSpinBox(self.layoutWidget1)
        self.howManyPages.setMinimum(1)
        self.howManyPages.setMaximum(99)
        self.howManyPages.setObjectName("howManyPages")
        self.horizontalLayout_2.addWidget(self.howManyPages)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(240, 10, 91, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.getBut = QtWidgets.QPushButton(self.layoutWidget2)
        self.getBut.setCheckable(False)
        self.getBut.setAutoDefault(False)
        self.getBut.setDefault(False)
        self.getBut.setFlat(False)
        self.getBut.setObjectName("getBut")
        self.verticalLayout.addWidget(self.getBut)
        self.stopBut = QtWidgets.QPushButton(self.layoutWidget2)
        self.stopBut.setObjectName("stopBut")
        self.verticalLayout.addWidget(self.stopBut)
        self.label_wrk = QtWidgets.QLabel(self.centralwidget)
        self.label_wrk.setEnabled(True)
        self.label_wrk.setGeometry(QtCore.QRect(0, 80, 131, 16))
        self.label_wrk.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wrk.setObjectName("label_wrk")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yet Another Reddit Crawler- YARC"))
        self.label.setText(_translate("MainWindow", "Subreddit:"))
        self.label_2.setText(_translate("MainWindow", "How many pages to crawl:"))
        self.getBut.setText(_translate("MainWindow", "Get images"))
        self.stopBut.setText(_translate("MainWindow", "Stop"))
        self.label_wrk.setText(_translate("MainWindow", "Working...Please Wait"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

