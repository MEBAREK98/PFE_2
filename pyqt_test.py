# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:03:16 2018

@author: pc
"""
import sys
from PyQt4 import QtGui
def window():
 app = QtGui.QApplication(sys.argv)
 w = QtGui.QWidget()
 
 b= QtGui.QLabel(w)
 b.setText("Hello World!")
 
 w.setGeometry(100,100,300,50)
 b.move(50,20)
 w.setWindowTitle("METRIC OPEN SCIENCE")
 ##00008B bleu nuit
 w.setStyleSheet("QWidget { background-color: darck }")
 w.show()
 sys.exit(app.exec_())
if __name__ == '__main__':
 window()
