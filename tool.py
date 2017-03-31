# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created: Fri Mar 31 09:57:04 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(642, 518)
        self.radioButton_post = QtGui.QRadioButton(Dialog)
        self.radioButton_post.setGeometry(QtCore.QRect(550, 20, 89, 16))
        self.radioButton_post.setObjectName(_fromUtf8("radioButton_post"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 470, 51, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.radioButton_get = QtGui.QRadioButton(Dialog)
        self.radioButton_get.setGeometry(QtCore.QRect(480, 20, 89, 16))
        self.radioButton_get.setChecked(True)
        self.radioButton_get.setObjectName(_fromUtf8("radioButton_get"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 470, 51, 21))
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_url = QtGui.QLineEdit(Dialog)
        self.lineEdit_url.setGeometry(QtCore.QRect(50, 20, 201, 20))
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 90, 251, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_run = QtGui.QPushButton(Dialog)
        self.pushButton_run.setGeometry(QtCore.QRect(530, 470, 75, 23))
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(170, 470, 21, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 90, 201, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 470, 51, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(310, 470, 21, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_count = QtGui.QLineEdit(Dialog)
        self.lineEdit_count.setGeometry(QtCore.QRect(310, 20, 81, 21))
        self.lineEdit_count.setObjectName(_fromUtf8("lineEdit_count"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 60, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 470, 21, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_select = QtGui.QPushButton(Dialog)
        self.pushButton_select.setGeometry(QtCore.QRect(520, 90, 75, 23))
        self.pushButton_select.setObjectName(_fromUtf8("pushButton_select"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 200, 571, 201))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 20, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.radioButton_post.setText(_translate("Dialog", "POST", None))
        self.radioButton_get.setText(_translate("Dialog", "GET", None))
        self.label_3.setText(_translate("Dialog", "POST DATA", None))
        self.label.setText(_translate("Dialog", "Uri:", None))
        self.lineEdit_url.setText(_translate("Dialog", "http://127.0.0.1:8000/", None))
        self.pushButton_run.setText(_translate("Dialog", "RUN", None))
        self.label_6.setText(_translate("Dialog", "MIN：", None))
        self.label_7.setText(_translate("Dialog", "AVG：", None))
        self.lineEdit_count.setText(_translate("Dialog", "1", None))
        self.label_4.setText(_translate("Dialog", "Image DATA", None))
        self.label_5.setText(_translate("Dialog", "MAX：", None))
        self.pushButton_select.setText(_translate("Dialog", "浏览", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "序号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "开始时间", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "结束时间", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "耗时", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "请求结果", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "返回结果", None))
        self.label_2.setText(_translate("Dialog", "请求数:", None))

