from PyQt4 import QtCore, QtGui
import helper, pycalendar

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def __init__(self, MW_Dlg):
	self.mwD = MW_Dlg

    nName = "placeholder"
    h = helper.Helper()
    Dlg = None

    def okClicked(self):
      self.nName = self.lineEdit.text()
      if not(self.nName == ""):
        self.h.removeStatus(str(self.nName))
      self.Dlg.accept()
      for entry in self.mwD.statuses:
        if entry == str(self.nName):
    	  self.mwD.statuses.remove(str(self.nName))
      self.mwD.refreshCheckboxes()

    def forCallback(self, D):
	return D

    def setupUi(self, Dialog):
	self.Dlg = Dialog
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(366, 133)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 200, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 341, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.okClicked)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Remove status", None))
        self.label.setText(_translate("Dialog", "Status to remove:", None))

if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  addWindow = QtGui.QDialog()
  ui = Ui_Dialog()
  ui.setupUi(addWindow)
  addWindow.show()
  sys.exit(app.exec_())
