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

    nColor = QtGui.QColor()
    nName = "placeholder"
    h = helper.Helper()
    Dlg = None

    def pickColor(self):
	p = self.frame.palette()
        newColor = QtGui.QColorDialog.getColor()
	p.setColor(self.frame.backgroundRole(), newColor)
	self.frame.setPalette(p)
	self.nColor = newColor

    #because Qt works with QColors, we've got to work with ARGB values.
    #Until someone thinks of a better way to do this, I'm going to make
    #it a 4-tuple.  Noah, you're the one dealing with colors, so if you
    #think of a better way, let me know.  Alpha is first in a QColor
    #then come the RGB values.
    def okClicked(self):
      self.nName = self.textEdit.toPlainText()
      if not(self.nName == ""):
	rgb_vals = [000, 000, 000, 000]
        rgb_vals[0] += self.nColor.alpha()
        rgb_vals[1] += self.nColor.red()
        rgb_vals[2] += self.nColor.blue()
	rgb_vals[3] += self.nColor.green()
	self.h.addEmployee(str(self.nName),str((rgb_vals[0], rgb_vals[1], rgb_vals[2], rgb_vals[3])))
	self.Dlg.accept()
	self.mwD.employees.append([str(self.nName),str((rgb_vals[0], rgb_vals[1], rgb_vals[2], rgb_vals[3]))])
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
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 191, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 341, 21))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 95, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(110, 89, 51, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
	self.frame.setAutoFillBackground(True)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.okClicked)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pickColor)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Employee", None))
        self.label.setText(_translate("Dialog", "Employee to add:", None))
        self.label_2.setText(_translate("Dialog", "Preferred Color:", None))
        self.pushButton.setText(_translate("Dialog", "Select Color", None))

if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  addWindow = QtGui.QDialog()
  ui = Ui_Dialog()
  ui.setupUi(addWindow)
  addWindow.show()
  sys.exit(app.exec_())
