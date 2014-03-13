from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.listA = QtGui.QListWidget(self)
        self.listB = QtGui.QListWidget(self)
        self.listA.setStyleSheet("QScrollBar {height:0px}")
        
        layout = QtGui.QHBoxLayout(self)
        layout.addWidget(self.listA)
        layout.addWidget(self.listB)
        for index in range(100):
            self.listA.addItem('Sample text for Item %d' % index)
            self.listB.addItem('Sample text for Item %d' % index)
        self.listA.horizontalScrollBar().valueChanged.connect(
            self.listB.horizontalScrollBar().setValue)
        self.listB.horizontalScrollBar().valueChanged.connect(
            self.listA.horizontalScrollBar().setValue)
        self.listA.verticalScrollBar().valueChanged.connect(
            self.listB.verticalScrollBar().setValue)
        self.listB.verticalScrollBar().valueChanged.connect(
            self.listA.verticalScrollBar().setValue)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
