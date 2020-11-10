#https://clay-atlas.com/blog/2019/08/26/python-chinese-pyqt5-tutorial-install/
from PyQt5 import QtWidgets, QtGui, QtCore
from UI.AT_main import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
     def __init__(self):
         super(MainWindow, self).__init__()
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
         self.ui.lineEdit_input.setText('Welcom!')
         self.ui.pushButton_go.clicked.connect(self.buttonClicked)

     def buttonClicked(self):
         text = self.ui.lineEdit_input.text()
         self.ui.label_output.setText(text)
         self.ui.lineEdit_input.clear()


if __name__ == '__main__':
     app = QtWidgets.QApplication([])
     window = MainWindow()
     window.show()
     sys.exit(app.exec_())
