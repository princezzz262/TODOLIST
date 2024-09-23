from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def add(self):
        task = self.TASKEDIT.text()
        if task:
            self.LISTVIEW.addWidget(QtWidgets.QLabel(task))
            self.TASKEDIT.clear()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CONTAINER1 = QtWidgets.QFrame(self.centralwidget)
        self.CONTAINER1.setGeometry(QtCore.QRect(9, 9, 461, 71))
        self.CONTAINER1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CONTAINER1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CONTAINER1.setObjectName("CONTAINER1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CONTAINER1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 9, 461, 52))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.NAV = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.NAV.setContentsMargins(10, 0, 10, 0)
        self.NAV.setObjectName("NAV")
        self.TASKEDIT = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.TASKEDIT.setMinimumSize(QtCore.QSize(0, 30))
        self.TASKEDIT.setObjectName("TASKEDIT")
        self.NAV.addWidget(self.TASKEDIT)
        self.ADDbtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ADDbtn.setMinimumSize(QtCore.QSize(50, 30))
        self.ADDbtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ADDbtn.setObjectName("ADDbtn")
        self.ADDbtn.clicked.connect(self.add)
        self.NAV.addWidget(self.ADDbtn)
        self.CONTAINER = QtWidgets.QFrame(self.centralwidget)
        self.CONTAINER.setGeometry(QtCore.QRect(10, 90, 461, 371))
        self.CONTAINER.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CONTAINER.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CONTAINER.setObjectName("CONTAINER")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.CONTAINER)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 461, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LISTVIEW = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LISTVIEW.setContentsMargins(0, 0, 0, 0)
        self.LISTVIEW.setObjectName("LISTVIEW")
        

        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ADDbtn.setText(_translate("MainWindow", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())