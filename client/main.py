import sys
from PyQt5 import QtWidgets
from .ui import Ui_MainWindow
from core import Api
import os
import datetime
class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.download)
        self.actiondownload.triggered.connect(self.download)
        self.pushButton_2.clicked.connect(self.refresh)
        self.actionrefresh.triggered.connect(self.refresh)
        self.pushButton_3.clicked.connect(self.upload)
        self.actionupload.triggered.connect(self.upload)
        self.api = Api()
        self.actionexit.triggered.connect(quit)
        #self.files = [{'hash': 'QmcpFbXkqr9vcSrfLnDiggdBY3PPxBNFrfAtqKhru4nywE', 'name': 'vir.py', 'time': 1586856883.274528, 'size': '163'}, {'hash': 'QmW9DG3Sane1rtYtBtEveFgtVsdcDD8BeV9nHth3LU1BXg', 'name': 'vim.sh', 'time': 1586856863.868105, 'size': '586'}]
        self.files = self.api.list_files()

    def isLogin(self):
        return self.api.isLogin()

    def download(self):
        try:
            data = self.tableWidget.selectedItems()
            hash = data[2].text()
        except Exception:
            QtWidgets.QMessageBox.information(self, "info",'未选择文件！')
            return
        print(hash)
        self.api.download(hash)

    def upload(self):
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件")
       
   
        try:
            res = self.api.add(filepath)
            if not res:
                QtWidgets.QMessageBox.information(self, "info",'上传失败！')
            if res == 200:
                QtWidgets.QMessageBox.information(self, "info",'上传成功！')
                self.refresh()
            if res == 409:
                QtWidgets.QMessageBox.information(self, "info",'文件已存在！')
        except Exception:
            raise

    def refresh(self):
        if not self.api.isConnected():
            QtWidgets.QMessageBox.information(self, "info",'未连接服务器！')
            return
        if not self.isLogin():
            QtWidgets.QMessageBox.information(self, "info",'用户未登录！')
            return 
        self.label.setText("%s：已登录"%self.api.client.username)
        self.api.update_files()
        self.tableWidget.clearContents()
        self.files = self.api.list_files()
        self.tableWidget.setRowCount(len(self.files))
        for k,elem in enumerate(self.files):
            self.tableWidget.setItem(k, 0 ,QtWidgets.QTableWidgetItem(elem['name']))
            self.tableWidget.setItem(k, 1 ,QtWidgets.QTableWidgetItem(str(round(int(elem['size'])/1024,2)) +'KB'))
            self.tableWidget.setItem(k, 2 ,QtWidgets.QTableWidgetItem(elem['hash']))
            self.tableWidget.setItem(k, 3 ,QtWidgets.QTableWidgetItem(datetime.datetime.fromtimestamp(elem['time']).strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    ipfsmanager = QtWidgets.QApplication(sys.argv)
    windows = MyMainWindow()
    windows.show()
    sys.exit(ipfsmanager.exec_())
