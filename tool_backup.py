# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created: Thu Mar 30 19:31:06 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import urllib2
import base64
from xml.dom import minidom
import datetime
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
        Dialog.resize(642, 524)
        self.lineEdit_url = QtGui.QLineEdit(Dialog)
        self.lineEdit_url.setGeometry(QtCore.QRect(40, 10, 201, 20))
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.radioButton_get = QtGui.QRadioButton(Dialog)
        self.radioButton_get.setGeometry(QtCore.QRect(470, 10, 89, 16))
        self.radioButton_get.setChecked(True)
        self.radioButton_get.setObjectName(_fromUtf8("radioButton_get"))
        self.radioButton_post = QtGui.QRadioButton(Dialog)
        self.radioButton_post.setGeometry(QtCore.QRect(540, 10, 89, 16))
        self.radioButton_post.setObjectName(_fromUtf8("radioButton_post"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_count = QtGui.QLineEdit(Dialog)
        self.lineEdit_count.setGeometry(QtCore.QRect(300, 10, 81, 21))
        self.lineEdit_count.setObjectName(_fromUtf8("lineEdit_count"))
        self.pushButton_run = QtGui.QPushButton(Dialog)
        self.pushButton_run.setGeometry(QtCore.QRect(540, 480, 75, 23))
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 50, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 80, 201, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_select = QtGui.QPushButton(Dialog)
        self.pushButton_select.setGeometry(QtCore.QRect(510, 80, 75, 23))
        self.pushButton_select.setObjectName(_fromUtf8("pushButton_select"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 460, 21, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 460, 51, 21))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 460, 51, 21))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 460, 21, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(340, 460, 51, 21))
        self.lineEdit_7.setText(_fromUtf8(""))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(300, 460, 21, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 80, 251, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 190, 571, 201))
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

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.pushButton_select, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
        #QtCore.QObject.connect(self.pushButton_run, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def openFile(self):
        s = QtGui.QFileDialog.getOpenFileName(self, 'Open file dialog', '/')
        self.lineEdit_4.setText(str(s))

    def goWeb(self):

        self.tableWidget.setRowCount(0)
        url = str(self.lineEdit_url.text())
        count = int(self.lineEdit_count.text())
        postdata = str(self.plainTextEdit.toPlainText())
        imagepath = str(self.lineEdit_4.text())
        self.tableWidget.setRowCount(count)
        resp = None
        result = None
        time_length = []
        req = urllib2.Request(url)
        for i in range(0, count):
            number = QtGui.QTableWidgetItem(str(i))
            time_start = datetime.datetime.now()
            starttime = QtGui.QTableWidgetItem(time_start.strftime('%M:%S.%f'))

            self.tableWidget.setItem(i, 0, number)
            self.tableWidget.setItem(i, 1, starttime)

            if self.radioButton_get.isChecked():
                try:
                    list = self.http_get(req)
                    resp = list[0]
                    result = list[1]

                except Exception, e:
                    resp = 'ERROR'
                    result = str(e)

            elif self.radioButton_post.isChecked() and imagepath == '':
                try:
                    list = self.http_post(req, postdata)
                    resp = list[0]
                    result = list[1]

                except Exception, e:
                    resp = 'ERROR'
                    result = str(e)
            else:
                f = open(imagepath, 'rb')
                ls_f = base64.b64encode(f.read())
                postdata = self.buildxml(str(ls_f))
                f.close()
                try:
                    list = self.http_post(req, postdata)
                    resp = list[0]
                    result = list[1]
                except Exception, e:
                    resp = 'ERROR'
                    result = str(e)
            time_end = datetime.datetime.now()
            endtime = QtGui.QTableWidgetItem(time_end.strftime('%M:%S.%f'))
            consumetime = QtGui.QTableWidgetItem(str((time_end - time_start).microseconds / 1000))
            requestcontent = QtGui.QTableWidgetItem(str(resp))
            requestresult = QtGui.QTableWidgetItem(str(result))
            time_length.append(float((time_end - time_start).microseconds / 1000))
            self.tableWidget.setItem(i, 2, endtime)
            self.tableWidget.setItem(i, 3, consumetime)
            self.tableWidget.setItem(i, 4, requestcontent)
            self.tableWidget.setItem(i, 5, requestresult)

        self.lineEdit_5.setText(str(max(time_length)))
        self.lineEdit_6.setText(str(min(time_length)))
        self.lineEdit_7.setText(str(sum(time_length) / len(time_length)))

    def http_get(self, req):
        res_data = urllib2.urlopen(req, data=None, timeout=2)
        resp = res_data.read()
        result = res_data.getcode()
        return [resp, result]

    def http_post(self, req, data):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data, timeout=2)
        resp = response.read()
        result = response.getcode()
        return [resp, result]

    def buildxml(self, postdata):
        impl = minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'Image', None)
        root = dom.documentElement

        msg = dom.createElement('Data')
        data = dom.createTextNode(str(postdata))
        msg.appendChild(data)
        root.appendChild(msg)

        xmlstring = dom.toxml();
        return xmlstring

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit_url.setText(_translate("Dialog", "http://127.0.0.1:8000/", None))
        self.label.setText(_translate("Dialog", "Uri:", None))
        self.radioButton_get.setText(_translate("Dialog", "GET", None))
        self.radioButton_post.setText(_translate("Dialog", "POST", None))
        self.label_2.setText(_translate("Dialog", "请求数:", None))
        self.lineEdit_count.setText(_translate("Dialog", "1", None))
        self.pushButton_run.setText(_translate("Dialog", "RUN", None))
        self.label_3.setText(_translate("Dialog", "POST DATA", None))
        self.label_4.setText(_translate("Dialog", "Image DATA", None))
        self.pushButton_select.setText(_translate("Dialog", "浏览", None))
        self.label_5.setText(_translate("Dialog", "MAX：", None))
        self.label_6.setText(_translate("Dialog", "MIN：", None))
        self.label_7.setText(_translate("Dialog", "AVG：", None))
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

