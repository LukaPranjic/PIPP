from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow, File_Dialog
import sys
import cv2

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

fd = File_Dialog()
working_image_path = fd.openFileNameDialog() #image path used for detection/s
if '/' in working_image_path:
    split_ch = '/'
else:
    split_ch = '\\'
working_image_name = working_image_path.split(split_ch)[-1]
img = cv2.imread(working_image_path)
w,h,c = img.shape
status = (working_image_name+" :: "+str(w) + "x" + str(h))

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.statusbar.showMessage(status)
ui.showImage(working_image_path)

MainWindow.show()
sys.exit(app.exec_())

