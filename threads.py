from PyQt4 import QtCore
import urllib2
import datetime
class WebThread(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, req, method, postdata, count):
        super(WebThread, self).__init__()
        self.req = req
        self.method = method
        self.postdata = postdata
        self.count = count

    def run(self):

        for i in range(self.count):
            time_start = datetime.datetime.now()
            returnlist = []
            if self.method == 'GET':
                resp, result = self.http_get(self.req)
            else:
                resp, result = self.http_post(self.req, self.postdata)
            time_end = datetime.datetime.now()
            time_consume = float((time_end - time_start).microseconds/1000)
            returnlist.append(i)
            returnlist.append(time_start)
            returnlist.append(time_end)
            returnlist.append(time_consume)
            returnlist.append(resp)
            returnlist.append(result)
            self.finishSignal.emit(returnlist)

    def http_get(self, req):
        try:
            res_data = urllib2.urlopen(req, data=None, timeout=2)
            resp = res_data.read()
            result = res_data.getcode()
        except Exception, e:
            resp = 'Error'
            result = str(e)
        return resp, result

    def http_post(self, req, data):
        try:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
            response = opener.open(req, data, timeout=2)
            resp = response.read()
            result = response.getcode()
            return resp, result
        except Exception, e:
            resp = 'Error'
            result = str(e)
        return resp, result
