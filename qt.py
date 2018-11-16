# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:44:50 2018

@author: pc
"""

import sys
from PyQt5 import QtGui
def window():
 app = QtGui.QApplication(sys.argv)
 w = QtGui.QWidget()
 b= QtGui.QLabel(w)
 b.setText("Hello World!")
 w.setGeometry(100,100,200,50)
 b.move(50,20)
 w.setWindowTitle("PyQt")
 w.show()
 sys.exit(app.exec_())
if __name__ == '__main__':
 window()
