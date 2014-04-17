from PyQt4 import QtCore, QtGui
import helper, pycalendar


#'''
#This class is a simple implementation to bring up a modal dialog window to
#allow the user to remove an existing employee from the list of checkboxes.
#Each removal will remove one name.  If a name is in the list twice, it will
#need removal twice.
#'''


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

    tName = "placeholder"
    nName = "placeholder"
    h = helper.Helper()
    Dlg = None

    #This function runs when the user clicks 'OK' and confirms that they are
    #done with name entry.  It removes the name from the appropriate list
    #on which the checkboxes rely, then refreshes the visible checkboxes.
    def okClicked(self):
      self.nName = self.lineEdit.text()
      #print 'nName : ' + self.nName
      if not(self.nName == ""):
        self.h.removeEmployee(str(self.nName))
      self.Dlg.accept()
      for entry in self.mwD.employees:
        self.tName = entry[0]
        #print 'compared to : ' + self.tName
        if self.tName == self.nName:
          #print 'found'
          self.mwD.employees.remove(entry)
      self.mwD.refreshCheckboxes()

    #Used for debug only
    def forCallback(self, D):
	return D

    #Qt code to set-up the visual modal dialog box
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
        myIcon = QtGui.QIcon()
        myIcon.addPixmap(QtGui.QPixmap(_fromUtf8("./data/bobafett_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(myIcon)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.okClicked)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #Qt code to refresh the visual modal dialog box
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Remove Employee", None))
        self.label.setText(_translate("Dialog", "Employee to remove:", None))

if __name__ == "__main__":
  import sys
  app = QtGui.QApplication(sys.argv)
  addWindow = QtGui.QDialog()
  ui = Ui_Dialog()
  ui.setupUi(addWindow)
  addWindow.show()
  sys.exit(app.exec_())
