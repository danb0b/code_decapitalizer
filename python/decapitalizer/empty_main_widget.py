# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:17:14 2015

@author: danaukes
"""

import os
import sys
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc
import PyQt5.QtWidgets as qw
#import numpy
import re
#import numpy.linalg
#import scipy
#import scipy.optimize
#import scipy.linalg
#import scipy.integrate
#import scipy.integrate.vode
#from scipy.spatial import Delaunay
#import scipy.spatial.ckdtree
#import sympy
#from decapitalizer.matplotlib_widget import GraphView

unimportant_words = ['the','a','an','for']

    
class MainWindow(qw.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.setWindowTitle('Test')
        menu   = self.menuBar().addMenu('File')
        action = menu.addAction('Action')
        action.triggered.connect(self.method)   
        
    def method(self):
#        pass
        d = Dialog()
        if d.exec_():
            print(True)

def test(in1):
    in1 = in1.group()
    out1 = in1[:-1]+in1[-1].upper()
#    print(in1)
#    out1 = 'b'
    return out1

class TextWidget(qw.QWidget):
    def __init__(self,*args,**kwargs):
        super(TextWidget,self).__init__(*args,**kwargs)
        self.t1 = qw.QTextEdit('input')
        self.t1.setAcceptRichText(False)
#        self.t2 = qw.QLineEdit('output')
#        self.t3 = qw.QLineEdit('asdf')
        self.p1 = qw.QPushButton('Capitalize')
        self.p2 = qw.QPushButton('Decapitalize')
        self.p3 = qw.QPushButton('Capitalize Important Words')
        layout = qw.QVBoxLayout()
        layout.addWidget(self.t1)
        layout.addWidget(self.p1)
        layout.addWidget(self.p2)
        layout.addWidget(self.p3)
#        layout.addWidget(self.t2)
#        layout.addWidget(self.t3)
        self.setLayout(layout)
        self.p1.pressed.connect(self.cap)
        self.p2.pressed.connect(self.decap)
        self.p3.pressed.connect(self.wordcap)
    def cap(self):
        self.t1.setPlainText(self.t1.toPlainText().upper())
    def decap(self):
        self.t1.setPlainText(self.t1.toPlainText().lower())
    def wordcap(self):
        t = self.t1.toPlainText()
        t = t.lower()
        result = re.sub('\s[a-z]',test,t)
        result=result[0].upper()+result[1:]
        self.t1.setPlainText(result)
#        print(items)
        
class Widget(qw.QWidget):
    def __init__(self,*args,**kwargs):
        super(Widget,self).__init__(*args,**kwargs)
        self.graph = GraphView()
        self.b1 = qw.QPushButton('ok')
        layout = qw.QVBoxLayout()
        layout.addWidget(qw.QLabel('Main Widget'))
        layout.addWidget(self.graph)
        layout.addWidget(self.b1)
        
        self.setLayout(layout)
        self.b1.clicked.connect(self.method)
        
    def method(self):
#        pass
        d = Dialog()
        if d.exec_():
            print(True)

class Dialog(qw.QDialog):
    def __init__(self,*args,**kwargs):
        super(Dialog,self).__init__(*args,**kwargs)
        self.b1 = qw.QPushButton('ok')
        self.b2 = qw.QPushButton('cancel')
        layout = qw.QHBoxLayout()
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        self.setLayout(layout)
        
        self.b1.clicked.connect(self.accept)
        self.b2.clicked.connect(self.reject)

#def run():


if __name__=='__main__':
    app = qw.QApplication(sys.argv)
    app.setWindowIcon(qg.QIcon('files/logo_4_1_icon.ico'))

    main_window = MainWindow()
    #    widget = Widget()
    tw= TextWidget()
    ##    widget = GraphView()
    #    t = numpy.r_[0:100]
    #    y = numpy.sin(t)
    #    widget.graph.plot(t,y)
    main_window.setCentralWidget(tw)
    main_window.show()
    app.exec_()
    sys.exit()    