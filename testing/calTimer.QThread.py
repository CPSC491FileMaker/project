#rewrite of original calTimer to use qthreads as opposed to native python threads
#needed to make UI changes (impossible from native)
#also attempting to alleviate need for sigterm to stop perm loop

from PyQt4 import QtCore
import time,os,ctypes
import sys

class calTimer(QtCore.QThread):

    xml_file = './data/data.xml'
    fileSize = os.stat(xml_file)

    def initFileSize(self):
        fileToCheck = os.stat(self.xml_file)
        self.fileSize = fileToCheck.st_size

    def run(self):
        
