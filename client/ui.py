
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 120, 40))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)

        self.tableWidget.setGeometry(QtCore.QRect(50, 40, 900, 420))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['文件名','大小','哈希','上传时间'])
        self.tableWidget.setColumnWidth(0, 220)
        self.tableWidget.setColumnWidth(1, 114)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setShowGrid(False) 
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) 
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 470, 150, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 470, 150, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 470, 150, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 200, 40))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

       

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionrefresh = QtWidgets.QAction(MainWindow)
        self.actionrefresh.setObjectName("actionrefresh")
        self.actiondownload = QtWidgets.QAction(MainWindow)
        self.actiondownload.setObjectName("actiondownload")
        self.actionupload = QtWidgets.QAction(MainWindow)
        self.actionupload.setObjectName("actionupload")

        self.menu.addAction(self.actiondownload)
        self.menu_3.addAction(self.actionrefresh)
        self.menu.addAction(self.actionupload)
        self.menu.addAction(self.actionexit)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ipfs-manager"))
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
        self.pushButton_3.setText(_translate("MainWindow", "上传"))

        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "选项"))
        self.menu_3.setTitle(_translate("MainWindow", "查看"))
        self.label.setText(_translate("MainWindow", "未登录..."))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionrefresh.setText(_translate("MainWindow", "刷新"))
        self.actiondownload.setText(_translate("MainWindow", "下载"))
        self.actionupload.setText(_translate("MainWindow", "上传"))
