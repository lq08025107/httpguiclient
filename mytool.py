from PyQt4 import QtCore, QtGui
from tool import Ui_Dialog
import urllib2
import base64
from xml.dom import minidom
from threads import WebThread
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
        self.timelength = []

    def openFile(self):
        s = QtGui.QFileDialog.getOpenFileName(self, 'Open file dialog', '/')
        self.lineEdit_4.setText(str(s))

    def goWeb(self):

        method = None
        postdata = ''
        self.timelength = []
        self.tableWidget.setRowCount(0)
        url = str(self.lineEdit_url.text())
        count = int(self.lineEdit_count.text())
        imagepath = str(self.lineEdit_4.text())
        self.tableWidget.setRowCount(count)
        req = urllib2.Request(url)
        if self.radioButton_get.isChecked():
            method = 'GET'
        else:
            method = 'POST'

        if imagepath == '':
            postdata = str(self.plainTextEdit.toPlainText())
        else:
            f = open(imagepath, 'rb')
            ls_f = base64.b64encode(f.read())
            postdata = self.buildxml(str(ls_f))

        self.threads = WebThread(req, method, postdata, count)
        self.threads.finishSignal.connect(self.setView)
        self.threads.start()

    def buildxml(self, postdata):
        impl = minidom.getDOMImplementation()
        dom = impl.createDocument(None, 'Image', None)
        root = dom.documentElement

        msg = dom.createElement('Data')
        data = dom.createTextNode(str(postdata))
        msg.appendChild(data)
        root.appendChild(msg)
        xmlstring = dom.toxml()
        return xmlstring

    def setView(self, listresult):

        i = listresult[0]
        starttime = listresult[1]
        endtime = listresult[2]
        consumetime = listresult[3]
        result = listresult[4]
        content = listresult[5]
        id = QtGui.QTableWidgetItem(str(i))
        self.tableWidget.setItem(i, 0, id)
        starttime = QtGui.QTableWidgetItem(starttime.strftime('%M:%S.%f'))
        self.tableWidget.setItem(i, 1, starttime)
        endtime = QtGui.QTableWidgetItem(endtime.strftime('%M:%S.%f'))
        self.tableWidget.setItem(i, 2, endtime)
        consumetime = QtGui.QTableWidgetItem(str(consumetime))
        self.tableWidget.setItem(i, 3, consumetime)
        content = QtGui.QTableWidgetItem(str(content))
        self.tableWidget.setItem(i, 4, content)
        result = QtGui.QTableWidgetItem(str(result)[0:60])
        self.tableWidget.setItem(i, 5, result)
        self.timelength.append(float(listresult[3]))
        self.lineEdit_5.setText(str(max(self.timelength)))
        self.lineEdit_6.setText(str(min(self.timelength)))
        self.lineEdit_7.setText(str(sum(self.timelength) / len(self.timelength)))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    Dialog = MyDialog()

    Dialog.show()
    sys.exit(app.exec_())
