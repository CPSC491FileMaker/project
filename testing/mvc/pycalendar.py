from PyQt4 import QtCore, QtGui
import sys
import includes.view
import includes.model


class Controller(object):

    def __init__(self):
        self.model = includes.model.Model()
        self.view = includes.view.start()





if __name__ == "__main__":
    controller = Controller()




