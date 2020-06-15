# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 09:27:46 2014

@author: danb0b
"""

import decapitalizer.empty_main_widget

import sys
import os
import idealab_tools.setup_tools as st
import traceback
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc
import PyQt5.QtWidgets as qw


excepthook_internal = sys.excepthook

def excepthook(self,exctype,value,tb):
    if exctype is not SystemExit:
        message = '''{}: {}'''.format(str(exctype),str(value))
        print(message)

        tbmessage = traceback.format_tb(tb)
        tbmessage = '  '.join(tbmessage)

#            logger = logging.getLogger('popupCAD')
#        self.logger.error(message)
#        self.logger.debug('\n'+tbmessage)
        
        self.editor.error_log.appendText(message+'\n'+tbmessage)
        excepthook_internal(exctype,value,tb)
        mb = qw.QMessageBox()
        mb.setText(message)
        mb.exec_()
        
sys.excepthook = excepthook          
        
#empty_main_widget.run()