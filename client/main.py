import sys
from PyQt5 import QtWidgets
from .ui import Ui_MainWindow


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

        self.actionexit.triggered.connect(quit)
        self.files = [{'hash': 'QmcpFbXkqr9vcSrfLnDiggdBY3PPxBNFrfAtqKhru4nywE', 'name': 'vir.py', 'time': 1586856883.274528, 'size': '163'}, {'hash': 'QmW9DG3Sane1rtYtBtEveFgtVsdcDD8BeV9nHth3LU1BXg', 'name': 'vim.sh', 'time': 1586856863.868105, 'size': '586'}]
        self.refresh()
    def download(self):
        try:
            data = self.tableWidget.selectedItems()
            hash = data[2].text()
        except Exception:
            QtWidgets.QMessageBox.information(self, "info",'未选择文件！')
            return
        print(hash)

    def upload(self):
        print('111')
    def refresh(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.files))
        for k,elem in enumerate(self.files):
            self.tableWidget.setItem(k, 0 ,QtWidgets.QTableWidgetItem(elem['name']))
            self.tableWidget.setItem(k, 1 ,QtWidgets.QTableWidgetItem(elem['size']))
            self.tableWidget.setItem(k, 2 ,QtWidgets.QTableWidgetItem(elem['hash']))
            self.tableWidget.setItem(k, 3 ,QtWidgets.QTableWidgetItem(elem['time']))


if __name__ == '__main__':
    ipfsmanager = QtWidgets.QApplication(sys.argv)
    windows = MyMainWindow()
    windows.show()
    sys.exit(ipfsmanager.exec_())
