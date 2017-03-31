from PyQt4 import QtCore, QtGui
from tool import Ui_Dialog
import urllib2
import base64
from xml.dom import minidom
import datetime
import sys

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


class MyDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButton_select, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openFile)
        QtCore.QObject.connect(self.pushButton_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goWeb)

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


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    Dialog = MyDialog()

    Dialog.show()
    sys.exit(app.exec_())
