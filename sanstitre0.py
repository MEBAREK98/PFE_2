# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:48:24 2018

@author: pc
"""
from PyQt4 import QtGui,QtCore 
from Statistique import getAuthor_nobmbre_de_publication_scholar,\
getAuthor_nobmbre_de_publication_wos,getAuthor_nobmbre_de_publication_scopus,\
getAuthor_nobmbre_de_publication_IET
from Research import Research_step2
from information import information 
import sys
# Classe deﬁnissant un bouton avec le texte Hello World! 
#try:
#    _fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
#    def _fromUtf8(s):
#        return s
#
#try:
#    _encoding = QtGui.QApplication.UnicodeUTF8
#    def _translate(context, text, disambig):
#        return QtGui.QApplication.translate(context, text, disambig, _encoding)
    
#except AttributeError:
#    def _translate(context, text, disambig):
#        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Metricoscience(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Metricoscience, self).__init__()
        
        self.setupUi()
        
#        Metricoscience.label_3.close()
        
        
    def setupUi(self):
        x,y,z,t=350,125,70,20
        
        self.label_1 = QtGui.QLabel(self)
        self.label_1.setGeometry(QtCore.QRect(290, 70, 851, 526))        
        self.label_1.setObjectName("label_4")
        pixmap = QtGui.QPixmap('Background TO USE.png').scaled(1000,800)
        self.label_1.setPixmap(pixmap)
        self.label_1.setGeometry(QtCore.QRect( 0, 0, 1000, 800))
        
        
        self.label_2 = QtGui.QLabel(self)                         
        self.label_2.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.label_2.setObjectName("label_4")
        pixmap = QtGui.QPixmap('O.png').scaled(216,216)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 216, 216))
        
        self.label_3 = QtGui.QLabel()
        self.label_3.setFixedSize(800,200)
        pixmap = QtGui.QPixmap('logo 1.png').scaled(800,200)
        self.label_3.setPixmap(pixmap)
        self.label_3.setGeometry(QtCore.QRect(100, 250, 800, 200)) 
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        
        self.Widget_1 = QtGui.QWidget()
#        self.Widget_2 = QtGui.QWidget()
#        self.stack1.geometry()
        
#        self.layout1=QtGui.QHBoxLayout()        
#        self.Stack = QtGui.QStackedWidget (self)
#        self.Stack.addWidget (self.stack1)
#        self.Stack.addWidget (self.stack2)
        
        self.pushButton_1 = QtGui.QPushButton("HOME",self.Widget_1)
        self.pushButton_1.setGeometry(x,y,z,t)
#        self.pushButton_1.setFixedSize(z,t)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: #07A394;")
#        self.stack1.pushButton_1.clicked.connect(self.display(1))
        
        
        
        self.pushButton_2 = QtGui.QPushButton("STATS",self.Widget_1)
        self.pushButton_2.setGeometry(x+100,y,z,t)
#        self.pushButton_2.setFixedSize(x,y)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #07A394;")
#        self.stack1.pushButton_2.clicked.connect(self.stack2UI)

        self.pushButton_3 = QtGui.QPushButton("ABOUT",self.Widget_1)
        self.pushButton_3.setGeometry(x+200,y,z,t)
#        self.pushButton_3.setFixedSize(x,y)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #07A394;")
        

        self.pushButton_4 = QtGui.QPushButton("SEARCH",self.Widget_1)
        self.pushButton_4.setGeometry(x+300,y,z,t)
#        self.pushButton_4.setFixedSize(x,y)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: #07A394;")

        
        self.pushButton_6 = QtGui.QPushButton("SEARCH")
#        self.pushButton_6.setGeometry(x,y,z,t)    
        self.pushButton_6.setFixedSize(z+10,t)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: #E82B1F;")
            
        self.lineedite_principale=QtGui.QLineEdit()
        self.lineedite_principale.setFixedSize(z+50,t)
        
        self.lineedite_1=QtGui.QLineEdit()
#        self.lineedite_1.setGeometry(x,y+400,z+50,t)
        self.lineedite_1.setFixedSize(z+50,t)
        
        
        self.lineedite_2=QtGui.QLineEdit()
#        self.lineedite_2.setGeometry(x+200,y+400,z+50,t)
        self.lineedite_2.setFixedSize(z+50,t)
        
        
        self.lineedite_3=QtGui.QLineEdit()
        self.lineedite_3.setFixedSize(z+50,t)
        
        
        self.lineedite_4=QtGui.QLineEdit()
        self.lineedite_4.setFixedSize(z+50,t)
        
        
        
        self.lineedite_5=QtGui.QLineEdit()
        self.lineedite_5.setFixedSize(z+50,t)
        
        
        
        self.lineedite_6=QtGui.QLineEdit()
        self.lineedite_6.setFixedSize(z+50,t)
        
        self.lineedite_7=QtGui.QLineEdit()
        self.lineedite_7.setFixedSize(z+50,t)
#        self.label_about
        
        
#        self.lineedite_7.setFixedSize(z+50,t)
        
#        self.lineedite_3.setGeometry(x+400,y+400,z+50,t)
        
        
        self.pushButton_5=QtGui.QPushButton("search")
        self.pushButton_5.setFixedSize(z+10,t)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: #E82B1F;")
        
            
        self.pushButton_7=QtGui.QPushButton("RESET")
        self.pushButton_7.setFixedSize(z+10,t)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: #E82B1F;")
##        
            
            
        self.liste=QtGui.QListWidget()
        self.liste.setFixedSize(500,200)
        
        self.layout_1=QtGui.QHBoxLayout()
        
        
        
        
        self.layout=QtGui.QVBoxLayout()
                
        
            
        
#        self.layout.addWidget(self.pushButton_1)
#        self.layout.addWidget(self.pushButton_2)
#        self.layout.addWidget(self.pushButton_3)
#        self.layout.addWidget(self.pushButton_4)
        self.layout_1.addLayout(self.layout)
        
            
        
        self.Widget_1.setLayout(self.layout_1)
        
        
        self.Stack = QtGui.QStackedWidget(self)
        
        self.Stack.addWidget(self.Widget_1)




        
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL('clicked()'), self.fonction_1)
        
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.fonction_2)
        
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.fonction_3)
        
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.fonction_4)
        
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.fonction_5)
        
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL('clicked()'), self.fonction_6)
        
        self.resize( 1000, 800)
        self.setWindowIcon(QtGui.QIcon("O.png"))
        self.setWindowTitle("Metricoscience")
        self.setCentralWidget(self.Stack)
        self.show()
    
    
    
    def fonction_1(self):
        
        
        
        
        self.lineedite_1.close()
        self.lineedite_2.close()
        self.lineedite_3.close()
        self.lineedite_4.close()
        self.lineedite_5.close()
        self.lineedite_6.close()
        self.lineedite_principale.close()
        self.pushButton_5.close()
        
        
        self.label_3.show()
#        layout=QtGui.QHBoxLayout()
        self.layout.addChildWidget(self.label_3)
        
        self.Widget_1.setLayout(self.layout)
        self.Stack.setCurrentWidget(self.Widget_1)

    def fonction_2(self):
        
        self.label_3.close()
        
        
        
        self.lineedite_1.show()
        self.lineedite_2.show()
        self.lineedite_3.show()
        self.lineedite_4.show()
        self.lineedite_5.show()
        self.lineedite_6.show()
        self.lineedite_principale.show()
        self.pushButton_5.show()
        
        
        
        self.Widget_1=QtGui.QWidget()
        self.layout_2=QtGui.QVBoxLayout()
        self.layout_2.addWidget(self.lineedite_principale)
        self.layout_2.addWidget(self.pushButton_5)
        self.layout_2.addWidget(self.lineedite_1)
        self.layout_2.addWidget(self.lineedite_2)
        self.layout_2.addWidget(self.lineedite_3)
        self.layout_2.addWidget(self.lineedite_4)
        self.layout_2.addWidget(self.lineedite_5)
        self.layout_2.addWidget(self.lineedite_6)
        self.layout.addLayout(self.layout_2)
        self.Widget_1.setLayout(self.layout)
        self.Stack.setCurrentWidget(self.Widget_1)
    
    
    
    def fonction_3(self):
        s=self.lineedite_principale.text()
        
        
#        Abdelkader Hadidi
#        self.setCentralWidget(self.Stack)
#        s=self.lineedite_principale.text()
        a,b,c=getAuthor_nobmbre_de_publication_scholar(s)
        d=getAuthor_nobmbre_de_publication_wos(s)
        e=getAuthor_nobmbre_de_publication_scopus(s)
        f=getAuthor_nobmbre_de_publication_IET(s)
        
        self.lineedite_1.setText(str(a))
        self.lineedite_2.setText(str(b))
        self.lineedite_3.setText(str(c))
        self.lineedite_4.setText(str(d))
        self.lineedite_5.setText(str(e))
        self.lineedite_6.setText(str(f))
        
    def fonction_4(self):
#        print("je suis lAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        
        
        self.Widget_1=QtGui.QWidget()
        self.layout_2=QtGui.QVBoxLayout()

        
        self.layout_2.addWidget(self.lineedite_7)
        self.layout_2.addWidget(self.pushButton_6)
        self.layout_2.addWidget(self.pushButton_7)
        self.layout_2.addWidget(self.liste)
        self.layout.addLayout(self.layout_2)
        self.layout.addLayout(self.layout_2)
        self.Widget_1.setLayout(self.layout)
        self.Stack.setCurrentWidget(self.Widget_1)
    
    def fonction_5(self):
        s=self.lineedite_7.text()
        article=Research_step2("Metricoscience", s)
        print(article)
        for i in article:
            print(i[5])
            self.liste.addItem("Title : "+i[5])
            self.liste.addItem("Date : "+str(i[4]))
            self.liste.addItem("ISSN : "+str(i[3]))
            self.liste.addItem("Authors : "+information(i[5]))
            self.liste.addItem("\n")
    def fonction_6(self):
        self.liste.removeItemWidget()
        
        
        
        
def main():
   app = QtGui.QApplication(sys.argv)
   Metricoscience = Ui_Metricoscience()
   sys.exit(app.exec_())
    
	
if __name__ == '__main__':
   main()
        
        
        

    