# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python Project\软件综合课程设计\QtDesign_File\course_search.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Couorse_Search(object):
    def setupUi(self, Couorse_Search):
        Couorse_Search.setObjectName("Couorse_Search")
        Couorse_Search.resize(920, 449)
        self.gridLayout = QtWidgets.QGridLayout(Couorse_Search)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Couorse_Search)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Couorse_Search)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(213)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(Couorse_Search)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3,QtWidgets.QHeaderView.Stretch)

        self.retranslateUi(Couorse_Search)
        QtCore.QMetaObject.connectSlotsByName(Couorse_Search)

    def retranslateUi(self, Couorse_Search):
        _translate = QtCore.QCoreApplication.translate
        Couorse_Search.setWindowTitle(_translate("Couorse_Search", "Form"))
        self.pushButton.setText(_translate("Couorse_Search", "返回"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Couorse_Search", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Couorse_Search", "课程编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Couorse_Search", "课程名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Couorse_Search", "开课教师"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Couorse_Search", "课程学时"))
        self.pushButton_2.setText(_translate("Couorse_Search", "新建课程"))
