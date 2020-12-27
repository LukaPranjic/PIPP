from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow, File_Dialog
from objectdetection import objectdetection 
from posedetection import *
import emotion_detection
import os.path
import os,sys
import cv2

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

fd = File_Dialog()
working_image_path = fd.openFileNameDialog() #image path used for detection/s
if '/' in working_image_path:
    split_ch = '/'
else:
    split_ch = '\\'
input_path_head,input_path_tail = os.path.split(working_image_path)

temp = cv2.imread(working_image_path)
w,h,c = temp.shape
status = (input_path_tail+" :: "+str(w) + "x" + str(h))

ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.statusbar.showMessage(status)
ui.showImage(working_image_path)



MainWindow.show()
sys.exit(app.exec_())

