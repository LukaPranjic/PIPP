from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow, File_Dialog
import sys


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

fd = File_Dialog()
working_image = fd.openFileNameDialog() #image path used for detection/s

ui = Ui_MainWindow()
ui.setupUi(MainWindow)


MainWindow.show()
sys.exit(app.exec_())
